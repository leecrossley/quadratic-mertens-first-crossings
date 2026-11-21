"""Exact finite checks on the sign model, its changes and the concentration argument."""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial, isqrt


def distribution(p):
    if p == 2:
        return {-1: F(1)}
    b = 1 + (1 if p % 4 == 1 else -1)
    law = {s: F(p*(p-b-s), 2*(p*p-b)) for s in (-1, 1)}
    law[0] = 1 - sum(law.values())
    return {s: q for s, q in law.items() if q}


def local_switch(p):
    split = F(p, p-1)**2
    inert = F(p*p, p*p-1)
    benchmark_ratio = F(p+1, p-1)
    assert split / inert == benchmark_ratio
    assert split / benchmark_ratio == inert
    # For p >= 5, log(p/2) >= log(p)/2 and
    # log((p+1)/(p-1)) > 1/p, while log(p^2/(p^2-1)) < 1/(p^2-1).
    assert p*p >= 4*p and F(1, 2*p) > F(1, p*p-1)


def moments():
    primes = (3, 5, 7, 11, 13, 17, 19)
    laws = [distribution(p) for p in primes]
    means = [sum(s*q for s, q in law.items()) for law in laws]
    exact_variance = sum((sum(s*s*q for s, q in law.items()) - m*m) / (p*p)
                         for p, law, m in zip(primes, laws, means))
    m2 = m4 = total = F(0)
    for signs in product(*laws):
        weight = F(1)
        value = F(0)
        for p, s, law, mean in zip(primes, signs, laws, means):
            weight *= law[s]
            value += (s-mean)/p
        total += weight
        m2 += weight*value**2
        m4 += weight*value**4
    v = sum(F(1,p*p) for p in primes)
    assert total == 1 and m2 == exact_variance and m4 <= 16*v*v


def antichains():
    for k in range(1,11):
        # Equal subset sums with strictly positive increments form an antichain.
        levels = {}
        for j in range(k+1):
            for subset in combinations(range(1,k+1), j):
                level = sum(x*(x+1)//2 for x in subset)
                levels.setdefault(level, []).append(j)
        for sizes in levels.values():
            assert sum(factorial(j)*factorial(k-j) for j in sizes) <= factorial(k)
            assert len(sizes) <= comb(k,k//2)


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Enable assertions')
    for p in range(5, 2000):
        if all(p % j for j in range(2,isqrt(p)+1)):
            local_switch(p)
            assert sum(distribution(p).values()) == 1
    moments()
    antichains()
    print('Euler-factor switches and their signs checked at all primes from 5 through 1999.')
    print('Exact second and fourth moment checks on the independent seven-prime splitting model passed.')
    print('Maximal-chain and middle-layer bounds passed on all equal-sum classes through dimension ten.')
