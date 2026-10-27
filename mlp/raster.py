"""Rasterise shapes of strokes and arcs with random shift,
scale, rotation and smudge."""
import numpy as np

SUPERSAMPLE = 8
SCALE = (0.75, 0.95)
SHIFT = 0.3
ROTATION = np.radians(10)
NOISE = 0.06

Shape = list[tuple]


def capsule(x0, y0, x1, y1, r):
    return ('capsule', x0, y0, x1, y1, r)


def arc(cx, cy, rx, ry, a0, a1, r):
    """Elliptical arc from angle a0 to a1 counter-clockwise, stroke
    radius r. Angles are the ellipse parameter, in radians."""
    return ('arc', cx, cy, rx, ry, a0, a1, r)


def ring(cx, cy, rx, ry, r):
    return arc(cx, cy, rx, ry, 0, 2 * np.pi, r)


def inside_capsule(p, x, y):
    _, x0, y0, x1, y1, r = p
    dx, dy = x1 - x0, y1 - y0
    t = ((x - x0) * dx + (y - y0) * dy) / (dx * dx + dy * dy)
    t = np.clip(t, 0, 1)
    return (x - x0 - t * dx) ** 2 + (y - y0 - t * dy) ** 2 <= r * r


def inside_arc(p, x, y):
    _, cx, cy, rx, ry, a0, a1, r = p
    u, v = (x - cx) / rx, (y - cy) / ry
    rho = np.sqrt(u * u + v * v)
    # First-order distance to the ellipse: (rho - 1) / |grad rho|.
    grad = np.sqrt((u / rx) ** 2 + (v / ry) ** 2) / rho
    on_curve = np.abs(rho - 1) / grad <= r
    angle = (np.arctan2(v, u) - a0) % (2 * np.pi)
    return on_curve & (angle <= a1 - a0)


def inside(p, x, y):
    if p[0] == 'capsule':
        return inside_capsule(p, x, y)
    return inside_arc(p, x, y)


def mask(shape: Shape, x, y) -> np.ndarray:
    return np.any([inside(p, x, y) for p in shape], axis=0)


def blur(image):
    padded = np.pad(image, 1, mode='edge')
    n, m = image.shape
    return sum(padded[i:i + n, j:j + m]
               for i in range(3) for j in range(3)) / 9


def render(shape: Shape, n: int, rng, shift=SHIFT,
           scale=SCALE) -> np.ndarray:
    """One smudged n by n image, 1 where inked."""
    fine = n * SUPERSAMPLE
    c = (np.arange(fine) + 0.5) / fine * 2 - 1
    x, y = np.meshgrid(c, -c)
    s = rng.uniform(*scale)
    a = rng.uniform(-ROTATION, ROTATION)
    x = x - rng.uniform(-shift, shift)
    y = y - rng.uniform(-shift, shift)
    u = (np.cos(a) * x + np.sin(a) * y) / s
    v = (-np.sin(a) * x + np.cos(a) * y) / s
    inked = mask(shape, u, v)
    image = inked.reshape(n, SUPERSAMPLE, n, SUPERSAMPLE).mean((1, 3))
    image = rng.uniform(0.7, 1.0) * image
    image += rng.uniform(0, 0.6) * (blur(image) - image)
    return np.clip(image + rng.normal(0, NOISE, image.shape), 0, 1)
