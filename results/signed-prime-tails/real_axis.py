"""Four signs of the future Mertens average from real logarithmic derivatives."""
from pathlib import Path
import sys

from flint import arb, ctx, fmpq, fmpq_poly

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "fixed-weight-delay-2380853"))
from theta import DISCRIMINANT, ERROR, theta_nodes


def polynomial(centre):
    """Chebyshev kernel on [0,1], raised to the fourth power."""
    variable = fmpq_poly([-1, 2])
    prev, curr = fmpq_poly([1]), variable
    result = prev + 2*curr(centre)*curr
    for _ in range(2, 13):
        prev, curr = curr, 2*variable*curr-prev
        result += 2*curr(centre)*curr
    return result**4


def evaluate(poly, point):
    value = arb(0)
    for coeff in reversed(list(poly)):
        value = value*point + arb(coeff)
    return value


def main():
    if not __debug__:
        raise SystemExit("Enable Python assertions.")
    ctx.prec = 320
    d = DISCRIMINANT
    scale = arb(3*d).log()
    log_d = arb(d).log()
    nodes = theta_nodes()
    half, bias = arb(1)/2, arb(2)/3

    def trace(q):
        assert 0 < q <= 3*half
        den = sum((w*(q*t/2).cosh() for t, w in nodes), arb(0)) + arb(0, ERROR)
        num = sum((w*(t/2)*(q*t/2).sinh() for t, w in nodes), arb(0)) + arb(0, ERROR)
        assert den > 0
        return num/(scale*den)

    at_one, at_two = trace(half), trace(3*half)
    mass = scale*(at_one*at_two/(3*half**2)).sqrt()
    assert mass < arb("8.423")
    ordinary = 2 + arb.const_euler() - (4*arb.pi()).log()
    assert ordinary < arb("0.046192")
    moments = []
    for j in range(1, 50):
        x = arb(j)/16
        q = x/scale
        # z = exp(-v/16): the j-th Laplace integral divided by 16
        # is the moment against z^(j-1) dz on the unit interval.
        integral = (bias/x + trace(q)/((half-q)*(3*half-q))
                    - at_one/(half-q) + at_two/(3*half-q))
        moments.append(integral/16)

    print("51 real logarithmic derivatives. No zero ordinates used.")
    print("Quadratic coefficient mass <", mass.upper().str(10))
    for lo, hi, centre, sign, target in [
        (4, 10, fmpq(2, 3), -1, "1.3"),
        (11, 18, fmpq(5, 12), 1, "1.8"),
        (19, 27, fmpq(1, 4), -1, "0.5"),
        (28, 36, fmpq(1, 6), 1, "0.25"),
    ]:
        weight = polynomial(centre)
        assert weight.degree() == 48
        primitive = weight.integral()
        total = arb(primitive(1))
        mean = sum((arb(c)*v for c, v in zip(weight, moments)), arb(0))/total
        u = lo*log_d
        left, right = (-hi*log_d/(16*scale)).exp(), (-u/(16*scale)).exp()
        inside = (evaluate(primitive, right)-evaluate(primitive, left))/total
        assert 0 < inside < 1
        error = 8*mass/(3*u) + ordinary
        if sign > 0:
            error += bias
        else:
            w = u/2
            delta = ((w/(2*arb.pi())+2)*log_d + 2*(w*w/(8*arb.pi())+2))*(-w/2).exp()
            error += (-u/2).exp()/(2*u.tanh()) + 2*delta + arb(39)/5*(-u/6).exp()
        cost = inside*error + (1-inside)*(mass+sign*bias)
        margin = sign*mean-cost
        assert margin > arb(target)
        print(f"[d^{lo}, d^{hi}] sign {sign:+d}  mean {mean.str(7)}  "
              f"outside {(1-inside).str(7)}  margin {margin.str(7)}")


if __name__ == "__main__":
    main()
