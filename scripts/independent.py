"""Integer and rational interval verification. Uses Python's standard library."""
from fractions import Fraction as F
from math import isqrt

X, WIDTH, SCALE = 2**24, 2**18, 10**22


def primes():
    end = X + WIDTH
    flags = bytearray([1])*(end+1)
    for p in range(2, isqrt(end)+1):
        if flags[p]:
            flags[p*p::p] = bytes((end-p*p)//p+1)
    return [p for p in range(X, end+1) if flags[p]]


def sign(n, p):
    v = pow(n, (p-1)//2, p)
    return -1 if v == p-1 else v


def log_bounds(z):
    x = F(z-1, z+1)
    total = 2*sum(x**(2*k+1)/(2*k+1) for k in range(30))
    return total, total + 2*x**61/(61*(1-x*x))


def multiply(a, b):
    endpoints = [x*y for x in a for y in b]
    return min(endpoints), max(endpoints)


def step(first, classes, quotas):
    table = [(p, old) for key, n in quotas.items() for p, old in classes[key][:n]]
    assert len(table) == sum(quotas.values())
    l2, l3 = log_bounds(2), log_bounds(3)
    root3 = isqrt(3*SCALE**2)
    values = []
    for denominator in (3, 1):
        # Quantise each signed rational term outwards to bound the sum.
        lower = sum((-old*(denominator*p-X)*SCALE)//(denominator*p*p) for p, old in table)
        rational_sum = (F(lower, SCALE), F(lower+len(table), SCALE))
        if denominator == 1:
            norm = (isqrt(X)*24*l2[0], isqrt(X)*24*l2[1])
        else:
            sq = F(isqrt(X)*SCALE, root3+1), F(isqrt(X)*SCALE, root3)
            norm = multiply(sq, (24*l2[0]-l3[1], 24*l2[1]-l3[0]))
        values.append(multiply(norm, rational_sum))
    low, high = values[1][0]-values[0][1], values[1][1]-values[0][0]
    expected = ("5.9010","5.9012") if first else ("3.5134","3.5136")
    assert F(expected[0]) < low <= high < F(expected[1])


def central_value():
    # Whole-period truncation and Abel summation give tail <= B/sqrt(N).
    period = [sign(n,5)*sign(n,13) for n in range(1,66)]
    s = bound = 0
    for value in period:
        s += value
        bound = max(bound, abs(s))
    assert s == 0
    nmax = 65*256
    lower = 0
    for n in range(1, nmax+1):
        c = period[(n-1)%65]
        root = isqrt(SCALE*SCALE//n)
        lower += c*(root if c >= 0 else root+1)
    assert F(lower,SCALE)-F(bound,isqrt(nmax)) > F(6,5)


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run with assertions enabled.")
    buckets = {(e,s): [] for e in (-1,1) for s in (-1,1)}
    for p in primes():
        e, s = sign(p,5), sign(p,13)
        buckets[(e,s)].append((p,s))
    step(True, buckets, {(1,1):2048, (-1,1):2048})
    step(False, buckets, {(1,-1):409, (-1,1):2867})
    central_value()
    print("Independent integer sieve and rational intervals certify both first-packet rises.")
    print("Direct periodic Dirichlet series gives L(1/2,chi_65) > 6/5.")
