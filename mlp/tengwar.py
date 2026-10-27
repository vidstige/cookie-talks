"""Tengwar drawn from stems, bows and hooks, simplified for 16 by 16.
Twelve letters chosen to look unlike each other, plus one held out."""
import numpy as np

from raster import Shape, arc, capsule, ring

PEN = 0.1
BOW = 0.45       # half height of a bow
HALF = 0.42      # bow box half width; a double bow has two halves
TOP, BASE = BOW, -BOW
ASCENT, DESCENT = 1.0, -1.0

STEM = {'down': (DESCENT, TOP), 'up': (BASE, ASCENT),
        'short': (BASE, TOP)}


def stem(x, kind):
    y0, y1 = STEM[kind]
    return capsule(x, y0, x, y1, PEN)


def arch(cx, rx):
    """Open to the bottom, hanging from the stem: tinco's bow."""
    return arc(cx, 0, rx, BOW, -np.pi / 3, np.pi, PEN)


def cup(cx, rx):
    """Open to the top, standing on the baseline: calma's bow."""
    return arc(cx, 0, rx, BOW, 2 * np.pi / 3, 2 * np.pi, PEN)


def tengwa(kind, bows, closed, side) -> Shape:
    """A regular tengwa: stem length, one or two bows, closed or
    open, bows to the right ('n') or left ('u') of the stem."""
    rx = HALF / bows
    x = -side * HALF
    centres = [x + side * (2 * i + 1) * rx for i in range(bows)]
    curve = arch if side > 0 else cup
    bow = [ring(c, 0, rx, BOW, PEN) if closed else curve(c, rx)
           for c in centres]
    return [stem(x, kind)] + bow


def romen() -> Shape:
    return [cup(0, HALF), capsule(HALF, 0, HALF, DESCENT, PEN),
            capsule(-HALF, 0, -HALF, TOP, PEN)]


def yanta() -> Shape:
    return [cup(0, HALF), capsule(-HALF, 0, -HALF, DESCENT, PEN),
            capsule(HALF, 0, HALF, TOP, PEN)]


def lambe() -> Shape:
    return [capsule(-HALF, TOP, HALF, TOP, PEN),
            arc(0, 0, HALF, BOW, np.pi, 1.9 * np.pi, PEN)]


def hyarmen() -> Shape:
    return [capsule(-HALF, BASE, HALF * 0.6, ASCENT, PEN),
            capsule(-0.1, 0.2, HALF, BASE, PEN)]


def silme() -> Shape:
    return [arc(0.1, 0.45, 0.35, 0.4, 0.3 * np.pi, 1.3 * np.pi, PEN),
            arc(-0.1, -0.45, 0.35, 0.4, 1.3 * np.pi, 2.3 * np.pi, PEN)]


def osse() -> Shape:
    return [arc(0.05, 0, HALF, BOW, np.pi / 4, 7 * np.pi / 4, PEN)]


def long_carrier() -> Shape:
    return [stem(0.2, 'down'),
            arc(-0.05, DESCENT + 0.25, 0.25, 0.25, np.pi, 2 * np.pi, PEN)]


# Sound to shape, in the mode of Beleriand where the sound is on the
# doors: m is vala and n is óre there.
GLYPHS: dict[str, Shape] = {
    'm': tengwa('short', 1, True, +1),    # vala
    'e': yanta(),
    'l': lambe(),
    'o': tengwa('short', 1, False, -1),   # anna
    'n': tengwa('short', 1, False, +1),   # óre
    'h': hyarmen(),
    'v': tengwa('up', 2, True, +1),       # ampa
    'g': tengwa('down', 2, False, -1),    # anga
    'th': tengwa('up', 1, False, +1),     # thúle
    's': silme(),
    'a': osse(),
    'y': long_carrier(),
    'r': romen(),
}

UNSEEN = 'r'

PARMA = tengwa('down', 1, True, +1)  # the p of pedo, drawn on the door

WORD = ['m', 'e', 'l', 'l', 'o', 'n']  # mellon, friend
