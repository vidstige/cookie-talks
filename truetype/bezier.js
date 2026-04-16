const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const info = document.getElementById('info');
const removeBtn = document.getElementById('removeBtn');

const POINT_RADIUS = 7;
const HIT_RADIUS = 14;
const CURVE_STEPS = 300;

const DEGREE_NAMES = ['', 'Linear', 'Quadratic', 'Cubic', 'Quartic', 'Quintic'];

let points = [
  { x: 150, y: 400 },
  { x: 250, y: 150 },
  { x: 450, y: 150 },
  { x: 550, y: 400 },
];

let dragging = null;

// De Casteljau's algorithm
function bezierAt(pts, t) {
  let p = pts.map(pt => ({ x: pt.x, y: pt.y }));
  while (p.length > 1) {
    p = p.slice(0, -1).map((pt, i) => ({
      x: (1 - t) * pt.x + t * p[i + 1].x,
      y: (1 - t) * pt.y + t * p[i + 1].y,
    }));
  }
  return p[0];
}

function degreeName(n) {
  return n < DEGREE_NAMES.length ? DEGREE_NAMES[n] : `degree ${n}`;
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const n = points.length - 1;

  // Control polygon
  ctx.beginPath();
  ctx.setLineDash([6, 6]);
  ctx.strokeStyle = '#555';
  ctx.lineWidth = 1;
  points.forEach((p, i) => i === 0 ? ctx.moveTo(p.x, p.y) : ctx.lineTo(p.x, p.y));
  ctx.stroke();
  ctx.setLineDash([]);

  // Bezier curve
  if (points.length >= 2) {
    ctx.beginPath();
    ctx.strokeStyle = '#5bc8f5';
    ctx.lineWidth = 2.5;
    for (let i = 0; i <= CURVE_STEPS; i++) {
      const pt = bezierAt(points, i / CURVE_STEPS);
      i === 0 ? ctx.moveTo(pt.x, pt.y) : ctx.lineTo(pt.x, pt.y);
    }
    ctx.stroke();
  }

  // Points
  points.forEach((p, i) => {
    const isEndpoint = i === 0 || i === points.length - 1;
    ctx.beginPath();
    ctx.arc(p.x, p.y, POINT_RADIUS, 0, Math.PI * 2);
    if (isEndpoint) {
      ctx.fillStyle = '#5bc8f5';
      ctx.fill();
    } else {
      ctx.strokeStyle = '#5bc8f5';
      ctx.lineWidth = 2;
      ctx.stroke();
    }
  });

  // Info
  info.textContent = `n = ${n}  (${degreeName(n)},  ${points.length} points)`;
  removeBtn.disabled = points.length <= 2;
}

function hitTest(mx, my) {
  for (let i = points.length - 1; i >= 0; i--) {
    const dx = mx - points[i].x;
    const dy = my - points[i].y;
    if (dx * dx + dy * dy <= HIT_RADIUS * HIT_RADIUS) return i;
  }
  return null;
}

function clientToCanvas(e) {
  const rect = canvas.getBoundingClientRect();
  const src = e.touches ? e.touches[0] : e;
  return { x: src.clientX - rect.left, y: src.clientY - rect.top };
}

canvas.addEventListener('mousedown', e => {
  const { x, y } = clientToCanvas(e);
  dragging = hitTest(x, y);
});

canvas.addEventListener('mousemove', e => {
  if (dragging === null) return;
  const { x, y } = clientToCanvas(e);
  points[dragging].x = x;
  points[dragging].y = y;
  draw();
});

canvas.addEventListener('mouseup', () => { dragging = null; });
canvas.addEventListener('mouseleave', () => { dragging = null; });

// Touch support
canvas.addEventListener('touchstart', e => {
  e.preventDefault();
  const { x, y } = clientToCanvas(e);
  dragging = hitTest(x, y);
}, { passive: false });

canvas.addEventListener('touchmove', e => {
  e.preventDefault();
  if (dragging === null) return;
  const { x, y } = clientToCanvas(e);
  points[dragging].x = x;
  points[dragging].y = y;
  draw();
}, { passive: false });

canvas.addEventListener('touchend', () => { dragging = null; });

document.getElementById('addBtn').addEventListener('click', () => {
  // Insert a new control point before the last endpoint
  const a = points[points.length - 2];
  const b = points[points.length - 1];
  points.splice(points.length - 1, 0, {
    x: (a.x + b.x) / 2 + (Math.random() - 0.5) * 30,
    y: (a.y + b.y) / 2 + (Math.random() - 0.5) * 30,
  });
  draw();
});

document.getElementById('removeBtn').addEventListener('click', () => {
  if (points.length <= 2) return;
  // Remove last control point (keep both endpoints)
  points.splice(points.length - 2, 1);
  draw();
});

function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight - document.getElementById('toolbar').offsetHeight;
  draw();
}

window.addEventListener('resize', resize);
resize();
