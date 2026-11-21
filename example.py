"""Certify one long wait by two residue and prime-ideal calculations."""
from collections import Counter
from fractions import Fraction
from math import isqrt
from flint import arb, ctx, dirichlet_char, fmpz

M = 2237
D = 5004173
CAP = 201500
PLACES = 6


def interval(q):
    return arb(q.numerator)/q.denominator


def class_formula():
    primes = (41, 122053)
    assert M*M + 4 == D == primes[0]*primes[1] and D % 8 == 5
    tables = []
    for p in primes:
        assert all(p % j for j in range(2, isqrt(p)+1))
        signs = [-1]*p
        signs[0] = 0
        for j in range(1, (p+1)//2):
            signs[j*j % p] = 1
        tables.append(signs)
    total = partial = maximum = 0
    scale = 10**22
    a, b = tables
    for j in range(1, D+1):
        value = a[j%primes[0]]*b[j%primes[1]]
        partial += value
        maximum = max(maximum, abs(partial))
        total += (scale*value)//j
    assert partial == 0
    tail = Fraction(maximum, D+1)
    lo = interval(Fraction(total, scale)-tail)
    hi = interval(Fraction(total+D, scale)+tail)
    step = 2*((M+arb(D).sqrt())/2).log()/arb(D).sqrt()
    h = (lo/step).ceil().unique_fmpz()
    assert h is not None and h == (hi/step).floor().unique_fmpz()
    return step*int(h), int(h), maximum


def sieve_primes(limit):
    sieve = bytearray([1])*(limit+1)
    for p in range(2, isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p::p] = bytes((limit-p*p)//p+1)
    return [p for p in range(2, limit+1) if sieve[p]]


def euler_norms():
    norms = Counter()
    for p in sieve_primes(CAP):
        if D % p == 0:
            norms[p] += 1
        elif p != 2 and pow(D, (p-1)//2, p) == 1:
            norms[p] += 2
        elif p*p <= CAP:
            norms[p*p] += 1
    return norms


def conrey_norms():
    norms = Counter()
    for p in range(2, CAP+1):
        if not fmpz(p).is_prime():
            continue
        s = int(fmpz(p).jacobi(D))
        if s >= 0:
            norms[p] += 1+s
        elif p*p <= CAP:
            norms[p*p] += 1
    return norms


def first_window(residue, norms, logarithmic):
    c = arb.const_euler().exp()*residue
    value = arb(0 if logarithmic else 1)
    previous = 2
    for k, (q, multiplicity) in enumerate(sorted(norms.items()), start=1):
        benchmark = c*arb(q).log()
        target = benchmark.log() if logarithmic else benchmark
        if value < target:
            product = value.exp() if logarithmic else value
            assert product > c*arb(previous).log()
            root = (product/c).exp()
            n = (root*10**PLACES).floor().unique_fmpz()
            assert n is not None and root > arb(n)/10**PLACES and root < arb(n+1)/10**PLACES
            return previous, q, int(n), k
        assert value > target
        factor = arb(q)/(q-1)
        if logarithmic:
            value += multiplicity*factor.log()
        else:
            value *= factor**multiplicity
        previous = q
    raise ArithmeticError("Increase CAP to reach a certified crossing.")


def fixed(n):
    z, r = divmod(n, 10**PLACES)
    return f"{z}.{r:0{PLACES}d}"


def main():
    if not __debug__:
        raise SystemExit("Assertions must be enabled.")
    ctx.prec = 180
    resid1, h, maximum = class_formula()
    character = dirichlet_char(D, D-1)
    assert character.order() == 2 and character.is_primitive() and character.parity() == 0
    lval = character.l(1)
    assert lval.imag.is_zero() and lval.real.overlaps(resid1)
    first = first_window(resid1, euler_norms(), False)
    second = first_window(lval.real, conrey_norms(), True)
    assert first == second
    a, b, n, windows = first
    print(f"d={D}={M}^2+4; class number {h}; maximum absolute character partial sum {maximum}")
    print(f"{windows} norm windows checked in each calculation; final window [{a}, {b})")
    print(f"{fixed(n)} < S_d < {fixed(n+1)}")


if __name__ == "__main__":
    main()
