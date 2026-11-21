"""Exact finite checks on the signed tilt, truncation, fourth moment and profile budgets."""
from fractions import Fraction as F
from itertools import combinations, product
from math import prod


def local_law(p):
    roots = 2 if p % 4 == 1 else 0
    probabilities = {s:F(p*(p-roots-s), 2*(p*p-roots)) for s in (-1,1)}
    probabilities[0] = 1-sum(probabilities.values())
    return probabilities


def moments():
    primes = (5, 7, 11, 13, 17)
    slopes = tuple(F(x,64) for x in (1,-2,3,-1,2))
    laws = list(map(local_law, primes))
    means = [sum(t*w for t,w in law.items()) for law in laws]
    variances = []
    fourth_bound = F(1)
    for a, law, mu in zip(slopes, laws, means):
        assert all(w >= 0 for w in law.values()) and sum(law.values()) == 1
        v = sum(w*(t-mu)**2 for t,w in law.items())
        m3 = sum(w*(t-mu)**3 for t,w in law.items())
        variances.append(v)
        norm = sum(w*(1+a*(t-mu))**2 for t,w in law.items())
        shifted = sum(w*t*(1+a*(t-mu))**2 for t,w in law.items())/norm
        assert shifted-mu == (2*a*v+a*a*m3)/(1+a*a*v)
        assert (shifted-mu)/a >= F(1,2)
        fourth_bound *= 1+6*a*a*v+4*abs(a)**3*sum(w*abs(t-mu)**3 for t,w in law.items())+a**4*sum(w*(t-mu)**4 for t,w in law.items())

    factors = [(idx,prod(primes[j] for j in idx),prod(slopes[j] for j in idx))
               for k in range(len(primes)+1) for idx in combinations(range(len(primes)),k)]
    full_norm = prod(1+a*a*v for a,v in zip(slopes,variances))
    for cutoff in (1,11,70,200,5000,100000):
        retained = [(idx,a) for idx,n,a in factors if n <= cutoff]
        joint2 = joint4 = dropped = F(0)
        for outcome in product((-1,0,1), repeat=len(primes)):
            probability = prod(law[t] for law,t in zip(laws,outcome))
            z = [t-mu for t,mu in zip(outcome,means)]
            truncated = sum(a*prod(z[j] for j in idx) for idx,a in retained)
            full = prod(1+a*v for a,v in zip(slopes,z))
            joint2 += probability*truncated**2
            joint4 += probability*truncated**4
            dropped += probability*(full-truncated)**2
        target_norm = sum(a*a*prod(variances[j] for j in idx) for idx,a in retained)
        assert joint2 == target_norm and joint2+dropped == full_norm
        assert joint4 <= fourth_bound
    print('Five signed local tilts and six truncations: exact normalization, discarded mass and fourth-moment envelope.')


def profile(r, eta):
    k = 16/(r*eta)
    high = 16*k
    vertices = [(r/2,high),(r-eta/2,high),(r,1),(1,1),
                (1+eta/4,-k),(1+eta,-k),(1+2*eta,0),(2,0)]
    # Refine at the lower restriction before forming rectangular enclosures.
    vertices.insert(1,(r-eta,high))
    unweighted = power = reserve = loss = F(0)
    steps = 32
    for (left,fleft),(right,fright) in zip(vertices,vertices[1:]):
        if left == right:
            continue
        for j in range(steps):
            a = left+(right-left)*F(j, steps)
            b = left+(right-left)*F(j+1, steps)
            fa = fleft+(fright-fleft)*F(j, steps)
            fb = fleft+(fright-fleft)*F(j+1, steps)
            high_value, low_value = max(fa,fb), min(fa,fb)
            if a >= r:
                if b <= 1+eta:
                    unweighted += (b-a)*max(high_value/a,high_value/b)
                power += (b-a)*max(r*high_value/a**2,r*high_value/b**2)
            if a >= r-eta and b <= r:
                reserve += (b-a)*min(low_value/a,low_value/b)
            if a >= 1:
                loss += (b-a)*max(0,-low_value/a)
    assert power < -1 and unweighted < -1 and reserve-loss > 1


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Enable assertions')
    moments()
    for ratio in map(F,('1','3/4','1/2','1/8','1/32')):
        for divisor in (4, 8, 32, 256):
            profile(ratio, ratio/divisor)
    print('Twenty exact profile enclosures: both prescribed averages are negative and the earlier area covers the entire negative part.')
