"""Bound the lowest quadratic pair from real logarithmic derivatives alone."""
from pathlib import Path
import sys

from flint import arb, ctx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "fixed-weight-delay-2380853"))
from theta import DISCRIMINANT, ERROR, theta_nodes


def real_trace(x, scale, nodes):
    v = x/(2*scale)
    assert 0 < v < arb(1)/4
    value = sum((w*(v*t).cosh() for t, w in nodes), arb(0)) + arb(0, ERROR)
    derivative = sum((w*(t/2)*(v*t).sinh() for t, w in nodes), arb(0)) + arb(0, ERROR)
    assert value > 0 and derivative > 0
    return derivative/(scale*value)


def main():
    if not __debug__:
        raise SystemExit("Run with assertions enabled.")
    ctx.prec = 192
    nodes = theta_nodes()
    scale = arb(3*DISCRIMINANT).log()
    x, y = arb(1)/4, arb(1)/2
    small = real_trace(x, scale, nodes)
    medium = real_trace(y, scale, nodes)
    unit = real_trace(arb(1), scale, nodes)
    ratio = (small/x)/(medium/y)
    assert ratio > 1
    lower = (2*x/small-x*x).sqrt()
    upper = ((y*y-ratio*x*x)/(ratio-1)).sqrt()
    assert arb("0.4480") < lower < upper < arb("0.4524") and 2*unit < 4
    for value, target in zip((small, medium, unit),
                             ("1.899512107795", "2.232132467629", "1.704476593310")):
        assert abs(value-arb(target)) < arb("1e-11")
    print("Quadratic real-axis traces at 1/4, 1/2 and 1:")
    for value in (small, medium, unit):
        print(value.str(13))
    print("Scaled first height exceeds", lower.lower().str(12), "and lies below", upper.upper().str(12))
    print("Exactly two ordinates in |gamma| log(3d) <= 1, counted with multiplicity.")


if __name__ == "__main__":
    main()
