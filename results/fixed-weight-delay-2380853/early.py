"""Direct certificate covering every real start from 2 through exp(14)."""
from math import isqrt

from flint import arb

from theta import DISCRIMINANT, ERROR


def primes(limit):
    sieve = bytearray(b"\1")*(limit+1)
    sieve[:2] = b"\0\0"
    for p in range(2, isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p::p] = bytes((limit-p*p)//p+1)
    return (p for p in range(2, limit+1) if sieve[p])


def square_residues():
    d = DISCRIMINANT
    result = bytearray(d)
    for n in range(1, (d+1)//2):
        result[n*n % d] = 1
    return result


def check_early(nodes, residues):
    d = DISCRIMINANT
    limit = 1203000
    assert arb(14).exp() < limit
    L1 = (sum((w*(x/4).cosh() for x,w in nodes), arb(0)) + arb(0, ERROR))/arb(d).sqrt()
    L2 = (sum((w*(3*x/4).cosh() for x,w in nodes), arb(0)) + arb(0, ERROR))*arb.pi()/d
    logc = arb.const_euler()+L1.log()
    assert L1 > 0 and L2 > 0
    D = (arb.pi()**2*L2/6).log()
    jumps = []
    for p in primes(limit):
        if p == d or residues[p % d]:
            q, k = p, 1 if p == d else 2
        else:
            q, k = p*p, 1
        if q <= limit:
            inv = 1/arb(q)
            ell = -(-inv).log1p()
            jumps.append((q, k*ell))
            D += k*(inv*ell+(-inv**2).log1p())
    # At most two prime ideals have a given integer norm.
    D += arb(0, 1/arb(limit)**2)
    jumps.sort(key=lambda e:e[0])
    j, a, windows = 0, 2, 0
    prefix = slope = arb(0)
    last_y = last_f = None
    while True:
        while j < len(jumps) and jumps[j][0] <= a:
            q, term = jumps[j]
            prefix += term
            slope += term/q
            j += 1
        loga = arb(a).log()
        f = prefix-logc-loga.log()+a*(D-slope-loga.expint(1))
        if last_y is not None:
            curvature = 1/(arb(last_y)**2*arb(last_y).log())
            defect = curvature*(a-last_y)**2/8
            assert last_f > defect and f > defect, (last_y,a,f)
            windows += 1
        last_y, last_f = a, f
        if a == limit:
            break
        a = min(limit, a+max(1,a//200))
    print(f"Direct product and chord bounds cover [2,{limit}] in {windows} intervals.")
    print(f"L(1) = {L1.str(17)}, D = {D.str(16)}.")
