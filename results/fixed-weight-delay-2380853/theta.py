"""Completed quadratic L-function on the critical line by a theta integral."""
from math import ceil, sqrt

from flint import arb, ctx, fmpz


DISCRIMINANT = 2380853
STEP = 32
TRUNCATION = 22
ERROR = arb("1e-48")


def theta_nodes():
    d = DISCRIMINANT
    assert fmpz(d).is_prime() and d == 1543**2 + 4
    character = [int(fmpz(n).jacobi(d)) for n in range(8*ceil(sqrt(d)) + 1)]
    data = []
    for j in range(STEP*TRUNCATION + 1):
        x = arb(j)/STEP
        c = arb.pi()*x.exp()/d
        nmax = max(1, ceil(sqrt(152/float(c))))
        assert c*nmax**2 > 150 and nmax < len(character)
        # exp(-c*n^2) is updated using the successive odd differences.
        base = (-c).exp()
        ratio_step = base*base
        term, ratio = base, base*ratio_step
        total = arb(0)
        for n in range(1, nmax+1):
            total += character[n]*term
            term *= ratio
            ratio *= ratio_step
        tail = (-c*nmax**2).exp()/(2*c*nmax)
        total += arb(0, tail)
        weight = total*(x/4).exp()*(1 if j == 0 else 2)/STEP
        data.append((x, weight))
    return data


def completed(t, nodes):
    assert abs(t) <= 64
    return sum((w*(x*t/2).cos() for x, w in nodes), arb(0)) + arb(0, ERROR)


def total_mass(nodes):
    # The quotient is 2 Lambda'(1)/Lambda(1) for the quadratic factor.
    numerator = sum((w*x*(x/4).sinh() for x,w in nodes), arb(0)) + arb(0, ERROR)
    denominator = sum((w*(x/4).cosh() for x,w in nodes), arb(0)) + arb(0, ERROR)
    assert denominator > 0
    return numerator/denominator + 2 + arb.const_euler() - (4*arb.pi()).log()


def curvature_sum(nodes,tau):
    # Derivatives in the ordinate, with the minus sign for two vertical derivatives.
    z = completed(arb(0),nodes)
    d2_at_zero = -sum((w*(x/2)**2 for x,w in nodes),arb(0))+arb(0,ERROR)
    d1 = d2 = d3 = arb(0)
    for x,w in nodes:
        v = x/2
        sn,cs = (v*tau).sin_cos()
        d1 -= w*v*sn
        d2 -= w*v**2*cs
        d3 += w*v**3*sn
    d1 += arb(0,ERROR)
    d2 += arb(0,ERROR)
    d3 += arb(0,ERROR)
    assert not d1.contains(0) and not z.contains(0)
    return -d2_at_zero/z-d3/(3*d1)+(d2/(2*d1))**2


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    raise ArithmeticError("Unresolved sign")
