"""Check the four finite margins from real-values.json using the Python standard library."""
import argparse
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from fractions import Fraction
import json
from pathlib import Path


DOWN = Context(prec=105, rounding=ROUND_FLOOR)
UP = Context(prec=105, rounding=ROUND_CEILING)
NEAR = Context(prec=105, rounding=ROUND_HALF_EVEN)
D = 2380853


def require(condition, message):
    if not condition:
        raise ValueError(message)


class Interval:
    def __init__(self, lower, upper):
        self.lo, self.hi = Decimal(lower), Decimal(upper)
        require(self.lo.is_finite() and self.hi.is_finite() and self.lo <= self.hi,
                "Invalid interval endpoints")

    @staticmethod
    def of(value):
        if isinstance(value, Interval):
            return value
        if isinstance(value, Fraction):
            n, d = Decimal(value.numerator), Decimal(value.denominator)
            return Interval(DOWN.divide(n, d), UP.divide(n, d))
        return Interval(value, value)

    def __add__(self, other):
        other = self.of(other)
        return Interval(DOWN.add(self.lo, other.lo), UP.add(self.hi, other.hi))

    __radd__ = __add__

    def __neg__(self):
        return Interval(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + (-self.of(other))

    def __rsub__(self, other):
        return self.of(other) + (-self)

    def __mul__(self, other):
        other = self.of(other)
        pairs = [(x, y) for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return Interval(min(DOWN.multiply(x, y) for x, y in pairs),
                        max(UP.multiply(x, y) for x, y in pairs))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.of(other)
        require(other.hi < 0 or other.lo > 0, "Denominator contains zero")
        return self * Interval(DOWN.divide(1, other.hi), UP.divide(1, other.lo))

    def ln(self):
        require(self.lo > 0, "Logarithm requires a positive interval")
        return Interval(NEAR.next_minus(NEAR.ln(self.lo)), NEAR.next_plus(NEAR.ln(self.hi)))

    def exp(self):
        # Decimal's exp and ln are correctly rounded to nearest. Widen by
        # one representable number on each side, using their monotonicity.
        return Interval(NEAR.next_minus(NEAR.exp(self.lo)), NEAR.next_plus(NEAR.exp(self.hi)))


def multiply_polynomials(a, b):
    product = [Fraction(0)]*(len(a)+len(b)-1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            product[j+k] += x*y
    return product


def evaluate(coefficients, x):
    total = 0
    for coefficient in reversed(coefficients):
        total = x*total + coefficient
    return total


def weight(centre):
    # Shifted Chebyshev polynomials T_j(2z-1), in ascending powers of z.
    previous, current = [1], [-1, 2]
    series = [Fraction(1)] + [Fraction(0)]*12
    for j in range(1, 13):
        factor = 2*evaluate(current, centre)
        for k, coefficient in enumerate(current):
            series[k] += factor*coefficient
        if j < 12:
            following = multiply_polynomials([-2, 4], current)
            for k, coefficient in enumerate(previous):
                following[k] -= coefficient
            previous, current = current, following
    squared = multiply_polynomials(series, series)
    result = multiply_polynomials(squared, squared)
    require(len(result) == 49 and result[-1] != 0, "Unexpected weight degree")
    return result


def read_table(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    require(data["discriminant"] == D and D == 1543**2+4, "Unexpected discriminant")
    require(data["decimal_places"] == 42, "Unexpected decimal scale")
    rows = data["rows"]
    expected = [f"j={j}" for j in range(1, 50)] + ["s=1", "s=2"]
    require([row["point"] for row in rows] == expected, "Missing or mislabelled measurement")
    values = [Interval(row["lower"], row["upper"]) for row in rows]
    for value in values:
        require(DOWN.subtract(value.hi, value.lo) == Decimal("3e-42"),
                "Unexpected measurement width")
    return values


def transfer_constants(log_d):
    # Euler's constant is less than H_n - log n. Use pi > 3.14.
    harmonic = sum((Fraction(1, j) for j in range(1, 1025)), Fraction(0))
    ordinary_upper = 2 + Interval.of(harmonic) - Interval.of(1024).ln() - Interval.of("12.56").ln()
    require(ordinary_upper.hi < Decimal("0.05"), "Ordinary coefficient bound failed")
    # u >= 4 log d > 58, w = u/2 >= 29 and log d < 15. The terms w^k exp(-w/2)
    # decrease for w>=29 and k<=2. Use pi>3 and 2 tanh(u)>1.
    require((4*log_d).lo > 58 and log_d.hi < 15, "Transfer range failed")
    w = Interval.of(29)
    poly = (w/6 + 2)*15 + 2*(w*w/24 + 2)
    excess = 2*poly*(-w/2).exp() + (-w).exp() + 8*(-2*w/6).exp()
    require(excess.hi < Decimal("0.001"), "Prime-power and archimedean error bound failed")


def check(table):
    values = read_table(table)
    at_one, at_two = values[-2:]
    scale, log_d = Interval.of(3*D).ln(), Interval.of(D).ln()
    a, b = Fraction(1, 2), Fraction(3, 2)
    bias = Fraction(2, 3)
    mass = Interval.of("8.423")
    require(at_one.lo > 0 and at_two.lo > 0, "Nonpositive endpoint")
    require((scale*scale*at_one*at_two/(a*b)).hi < (mass*mass).lo,
            "Quadratic coefficient mass bound failed")
    transfer_constants(log_d)
    moments = []
    for j, value in enumerate(values[:-2], start=1):
        x = Interval.of(Fraction(j, 16))
        q = x/scale
        integral = (Interval.of(bias)/x + value/((a-q)*(b-q))
                    - at_one/(a-q) + at_two/(b-q))
        moments.append(integral/16)
    tests = [(4, 10, Fraction(2, 3), -1, "1.3"), (11, 18, Fraction(5, 12), 1, "1.8"),
             (19, 27, Fraction(1, 4), -1, "0.5"), (28, 36, Fraction(1, 6), 1, "0.25")]
    for lo, hi, centre, sign, target in tests:
        coefficients = weight(centre)
        primitive = [0]+[c/(k+1) for k, c in enumerate(coefficients)]
        total = sum(primitive)
        require(total > 0, "Kernel normalization failed")
        left = (-hi*log_d/(16*scale)).exp()
        right = (-lo*log_d/(16*scale)).exp()
        inside = (evaluate(primitive, right) - evaluate(primitive, left))/total
        require(inside.lo > 0 and inside.hi < 1, "Window probability failed")
        mean = sum(m*c for m, c in zip(moments, coefficients))/total
        error = 8*mass/(3*lo*log_d) + Interval.of("0.05")
        error += bias if sign > 0 else Interval.of("0.001")
        margin = sign*mean - inside*error - (1-inside)*(mass+sign*bias)
        require(margin.lo > Decimal(target), f"Unresolved margin on [{lo},{hi}]")
        shown = DOWN.quantize(margin.lo, Decimal("0.000001"))
        print(f"[d^{lo}, d^{hi}] sign {sign:+d}  lower bound {shown} > {target}")
    print("All four strict signs follow from the table and the stated analytic transfer bounds.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--table", type=Path, default=Path(__file__).with_name("real-values.json"))
    check(parser.parse_args().table)
