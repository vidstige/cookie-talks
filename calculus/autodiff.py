"""Forward-mode automatic differentiation with dual numbers.

Every number carries a pair (v, d): its value and its slope dv/dx. An
operation f(a, b) computes its value from the values, and its slope by
the chain rule:

    d/dx f(a, b) = df/da * da/dx + df/db * db/dx

where df/da and df/db are the operation's own partial derivatives,
evaluated at the input values. That rule, once per operator, is all of it.
"""
import math
from typing import Callable


def as_dual(a: "Dual | float") -> "Dual":
    """A plain number is a constant: its slope is 0."""
    return a if isinstance(a, Dual) else Dual(a, 0.0)


class Dual:
    def __init__(self, v: float, d: float):
        self.v = v
        self.d = d

    def __repr__(self) -> str:
        return f"({self.v:g}, {self.d:g})"

    # f = a + b:  df/da = 1,  df/db = 1
    def __add__(a, b):
        b = as_dual(b)
        return Dual(a.v + b.v, 1 * a.d + 1 * b.d)

    # f = a - b:  df/da = 1,  df/db = -1
    def __sub__(a, b):
        b = as_dual(b)
        return Dual(a.v - b.v, 1 * a.d - 1 * b.d)

    # f = a * b:  df/da = b,  df/db = a
    def __mul__(a, b):
        b = as_dual(b)
        return Dual(a.v * b.v, b.v * a.d + a.v * b.d)

    # f = a / b:  df/da = 1/b,  df/db = -a/b^2
    def __truediv__(a, b):
        b = as_dual(b)
        return Dual(a.v / b.v, a.d / b.v - a.v / b.v**2 * b.d)

    # f = a^b:  df/da = b a^(b-1),  df/db = a^b ln a
    def __pow__(a, b):
        b = as_dual(b)
        z = a.v**b.v
        # ln a is undefined for a <= 0, but a constant exponent
        # (b.d == 0) never needs it: that is how x**2 works at x < 0.
        dfdb = z * math.log(a.v) if b.d else 0.0
        return Dual(z, b.v * a.v ** (b.v - 1) * a.d + dfdb * b.d)

    # Constant on the left, as in 3 * x: swap and reuse the rules above.
    def __radd__(a, b):
        return as_dual(b) + a

    def __rsub__(a, b):
        return as_dual(b) - a

    def __rmul__(a, b):
        return as_dual(b) * a

    def __rtruediv__(a, b):
        return as_dual(b) / a

    def __rpow__(a, b):
        return as_dual(b) ** a


def derivative(f: Callable, x: float) -> float:
    """Seed x with slope dx/dx = 1 and read the slope off the result."""
    return f(Dual(x, 1.0)).d


def central(f: Callable, x: float, h: float = 1e-5) -> float:
    return (f(x + h) - f(x - h)) / (2 * h)


def g(x):
    return x**2 + 3 * x


def h(x):
    return (x**x - 1 / x) / (2**x + x * 3 - 1)


if __name__ == "__main__":
    x = Dual(2.0, 1.0)
    print("x       =", x)
    print("x**2    =", x**2)
    print("3 * x   =", 3 * x)
    print("g(x)    =", g(x), " (2x + 3 = 7)")
    for x in [0.5, 1.0, 2.0, 3.0]:
        print(f"h'({x}) = {derivative(h, x):.8f}"
              f"  central difference {central(h, x):.8f}")
