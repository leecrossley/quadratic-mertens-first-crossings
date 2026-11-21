"""Verify the first dip and the first negative average from 2 in one field."""
from fractions import Fraction
from math import isqrt

from flint import arb, ctx, fmpz


def as_ball(q):
    q = Fraction(q)
    return arb(q.numerator) / q.denominator


def calc_residue(d, m):
    root = arb(d).sqrt()
    scale = arb.pi() / d
    total = arb(0)
    for n in range(1, isqrt(25 * d) + 1):
        symbol = fmpz(n).jacobi(d)
        if symbol:
            v = scale * n * n
            total += symbol * (v.sqrt().erfc() / n + v.expint(1) / root)
    total += arb(0, 3 * (-25 * arb.pi()).exp())
    class_unit = 2 * ((m + root) / 2).log() / root
    classes = (total / class_unit).unique_fmpz()
    assert classes == 192 and total.contains(classes * class_unit)
    return classes * class_unit


def norm_events(d, limit):
    result = []
    for p in range(2, limit + 1):
        if not fmpz(p).is_prime():
            continue
        symbol = fmpz(p).jacobi(d)
        if symbol >= 0:
            result.append((p, 1 + int(symbol)))
        elif p*p <= limit:
            result.append((p*p, 1))
    return sorted(result)


def certificate():
    d, m = 82864613, 9103
    assert d == m*m+4 and all(power == 1 for _, power in fmpz(d).factor())
    c = calc_residue(d, m) * arb.const_euler().exp()
    events = norm_events(d, 1021)
    left = arb(2).log()
    product, area = arb(1), arb(0)
    first = None
    weights = []
    def direct(q):
        right = as_ball(q).log()
        base = arb(2).log()
        smooth = (right-base)*(1-c.log()) - right*right.log() + base*base.log()
        return smooth + sum(w*(right-u) for u,w in weights)
    for q, multiplicity in events:
        right = arb(q).log()
        error = (product / (c * left)).log()
        gain = (right-left)*(1+error) - right*(right/left).log()
        assert (area+gain).overlaps(direct(q))
        if first is None:
            if product < c*right:
                first = (product / c).exp()
                assert first > as_ball('7.00521788') and first < as_ball('7.00521789')
            else:
                assert product > c*right
        if q == 1021:
            assert area+gain < 0 and prev == 977
            break
        assert area+gain > 0
        weights.append((right, multiplicity*(arb(q)/(q-1)).log()))
        product *= (arb(q)/(q-1))**multiplicity
        area += gain
        left, prev = right, q
    # The primitive is concave in log t on every gap. The first negative
    # endpoint closes a gap with positive left value and a unique zero.
    low, high = Fraction(977), Fraction(1021)
    while high-low > Fraction(1, 10**10):
        mid = (low+high) / 2
        v = direct(mid)
        if v > 0:
            low = mid
        else:
            assert v < 0
            high = mid
    unit = 10**8
    lower = (unit*low).__floor__()
    assert lower < unit*low < unit*high < lower+1
    assert direct(Fraction(lower,unit)) > 0 > direct(Fraction(lower+1,unit))
    print('d = 82864613 = 9103^2+4, class number 192, independently enclosed by the quadratic theta integral.')
    print('First product dip in (7.00521788, 7.00521789).')
    print(f'First negative cumulative area has infimum in ({lower//unit}.{lower%unit:08}, {(lower+1)//unit}.{(lower+1)%unit:08}).')
    print('Primitive checked at all preceding norm endpoints and on both sides of its zero.')


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Enable assertions')
    ctx.prec = 144
    certificate()
