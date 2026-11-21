"""Exact checks on the shared block, polynomial and overlapping tails."""
from fractions import Fraction as F
from itertools import product
from math import comb


def kernel_mass(y,p,end):
    upper = p if end is None else min(p,end)
    return 0 if upper <= y else 1-F(y,upper)


def shared_block():
    for y in (5,19,53):
        for k in (4,7,16):
            for p in range(2,2*k*y):
                full, finite = kernel_mass(y,p,None), kernel_mass(y,p,k*y)
                if y < p <= k*y:
                    assert full == finite == 1-F(y,p)
                elif p > k*y:
                    assert 1 >= full >= finite == 1-F(1,k)
                else:
                    assert full == finite == 0


def polynomial_check():
    # Sixteen equiprobable sign bits. The standardized sum has variance one.
    law = [(F(2*j-16,4),F(comb(16,j),2**16)) for j in range(17)]
    def g(x):
        return (x-F(1,4))*(x+1)**2
    m = sum(w*g(x) for x,w in law)
    v = sum(w*g(x)**2 for x,w in law)
    assert m == F(3,2) and v >= 1
    lam = 1/v
    values = [((1-lam*g(x))**2,w,x) for x,w in law]
    assert all(p >= 0 and (x > F(1,4) or p >= 1) for p,_,x in values)
    assert sum(p*w for p,w,x in values) <= 1-lam
    print('Exact 16-sign model: cubic mean',m,'and squared moment',v)


def overlap_check():
    # On a finite independent sign space, second moments of sums of overlapping
    # tails must equal the squared norm of the combined coefficient vector.
    ps = (5,7,11,13,17,19,23,29)
    for kind in ('full','finite'):
        rows = [[kernel_mass(y,p,None if kind=='full' else 2*y)/p
                 if p > 2*y else F(0) for p in ps] for y in (2,4,8)]
        coefficients = list(map(sum,zip(*rows)))
        expected = sum(b*b for b in coefficients)
        direct = F(0)
        for signs in product((-1,1),repeat=len(ps)):
            t = sum(sum(b*z for b,z in zip(row,signs)) for row in rows)
            direct += F(t*t,2**len(ps))
        assert expected == direct
    print('Exact prime-window coefficients and both overlapping-tail variance identities agree.')


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Enable assertions')
    shared_block()
    polynomial_check()
    overlap_check()
