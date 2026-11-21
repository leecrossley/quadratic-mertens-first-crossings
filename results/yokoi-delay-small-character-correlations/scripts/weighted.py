"""Enclose the two complete prime tails using a split theta integral."""
from math import isqrt
from flint import arb, ctx, fmpz


def primes(limit):
    flags = bytearray([1]) * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p * p :: p] = bytes((limit - p * p) // p + 1)
    return [p for p in range(2, limit + 1) if flags[p]]


def even_l_values(q, split):
    r = arb(split)
    root = arb(q).sqrt()
    pi = arb.pi()
    step = pi / q
    nmax = 9 * (1 + isqrt(q))
    total1 = arb(0)
    total2 = arb(0)
    for n in range(1, nmax + 1):
        sgn = int(fmpz(n).jacobi(q))
        if not sgn:
            continue
        x = step * (n * n)
        a, b = x * r, x / r
        erfc_a = a.sqrt().erfc()
        erfc_b = erfc_a if split == 1 else b.sqrt().erfc()
        total1 += sgn * ((pi / x).sqrt() * erfc_a + b.expint(1))
        total2 += sgn * ((-a).exp() / x + 2 * r.sqrt() * (-b).exp()
                         - 2 * (pi * x).sqrt() * erfc_b)
    # Each positive defining integral on t >= 1/2 has integrand at
    # most 3 exp(-xt) for these four powers of t. Here x > 1.
    err = 6 * q / (pi * nmax) * (-step * nmax**2 / 2).exp()
    assert err < arb("1e-40")
    return ((total1 + arb(0, "1e-40")) / root,
            (total2 + arb(0, "1e-40")) * step)


def prime_constants(q, factors, plist, split):
    vals = even_l_values(q, split)
    bound = plist[-1]
    constants = []
    for k, value in enumerate(vals, 1):
        even = arb(2 * k).zeta()
        for p in factors:
            even *= 1 - arb(p) ** (-2 * k)
        odd = arb(0)
        for p in plist:
            sign = int(fmpz(p).jacobi(q))
            if sign:
                v = arb(1) / (p**k)
                odd += sign * (v.atanh() - v)
        rem = arb(2) / (bound ** (3*k-1))
        constants.append(value.log() - even.log()/2 - odd + arb(0, rem))
    return constants


def weighted_value(q, start, constants, plist):
    c1, c2 = constants
    for p in plist:
        if p > start:
            break
        sgn = int(fmpz(p).jacobi(q))
        c1 -= arb(sgn) / p
        c2 -= arb(sgn) / (p*p)
    return arb(start).sqrt() * arb(start).log() * (c1 - start*c2)

