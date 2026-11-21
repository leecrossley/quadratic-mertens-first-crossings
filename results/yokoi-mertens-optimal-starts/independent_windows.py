"""Independent window integration with a dense odd sieve and a quadratic-residue table."""
from fractions import Fraction
from heapq import merge
from math import isqrt
from flint import arb, ctx, fmpz


def real(x):
    f = Fraction(x)
    return arb(f.numerator) / f.denominator


def odd_primes(limit):
    # Index i represents the odd number 2*i+1.
    size = (limit+1)//2
    marks = bytearray([1])*size
    marks[0] = 0
    for p in range(3, isqrt(limit)+1, 2):
        if marks[p//2]:
            first = (p*p)//2
            marks[first::p] = bytes((size-1-first)//p+1)
    pos = marks.find(1)
    while pos >= 0:
        yield 2*pos+1
        pos = marks.find(1, pos+1)


def replay(m, end, lo, hi, expected):
    d = m*m+4
    assert d % 8 == 5 and fmpz(d).is_prime()
    squares = bytearray(d)
    for k in range(1, (d+1)//2):
        squares[k*k % d] = 1

    def chi(n):
        k = n % d
        return (2*squares[k]-1) if k else 0

    root = arb(d).sqrt()
    scale = arb.pi()/d
    residue = arb(0)
    for n in range(1, isqrt(25*d)+1):
        a = scale*n*n
        residue += chi(n)*(a.sqrt().erfc()/n+a.expint(1)/root)
    residue += arb(0, 3*(-25*arb.pi()).exp())
    constant = arb.const_euler().exp()*residue
    low, high = Fraction(lo), Fraction(hi)
    squares_inert = [(4,1)] + [(p*p,1) for p in odd_primes(isqrt(end)) if chi(p)<0]
    linear = ((p, chi(p)+1) for p in odd_primes(end) if chi(p)>=0)
    events = merge(sorted(squares_inert), linear, [(low,0),(high,0),(end,0)])
    u = arb(2).log()
    product = arb(1)
    area = arb(0)
    probes = {}
    first = None
    minimum_area, minimum_q = None, None
    norms = 0
    for q, mult in events:
        v = real(q).log()
        old_error = (product/(constant*u)).log()
        area += (v-u)*(1+old_error) - v*((v-u)/u).log1p()
        if first is None:
            right = product-constant*v
            if right < 0:
                first = (product/constant).exp()
                assert first > real(high)
            else:
                assert right > 0
        if first is not None:
            if minimum_area is None or area < minimum_area:
                minimum_area, minimum_q = area,q
            else:
                assert area > minimum_area
        if q == low or q == high:
            probes[q] = area
        if mult:
            norms += 1
            product *= (arb(q)/(q-1))**mult
        u = v
    assert minimum_q == expected
    assert probes[low] < minimum_area < probes[high]
    loss = 2*(9+3*arb(d).log())/(arb(end).sqrt()*u)
    assert area-minimum_area > loss
    print(f'd={d}, {norms} norms, first crossing {first.str(16)}, least post-crossing area at {minimum_q}.')
    print(f'Earliest start in ({lo}, {hi}); direct window integrals leave {(area-minimum_area-loss).str(10)} beyond the tail allowance.')


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Enable assertions')
    ctx.prec = 182
    replay(97, 4000000, '337.87434', '337.87436', 2017)
    replay(1543, 125000000, '137123.79815', '137123.79818', 154877)
