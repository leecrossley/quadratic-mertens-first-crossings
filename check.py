"""Exact arithmetic checks for truncation, prime-rank maxima and power kernels."""
from fractions import Fraction as F
from itertools import combinations, product
from math import prod


def check_moments():
    # Test independent, asymmetric, signed tilts rather than symmetric fair coins.
    primes = (5,7,11,13,17)
    coeff = [F(-2,31),F(-1,19),F(-1,32),F(1,24),F(1,40)]
    laws = []
    for p in primes:
        b = 2 if p%4 == 1 else 0
        law = {s:F(p*(p-b-s),2*(p*p-b)) for s in (-1,1)}
        law[0] = 1-sum(law.values())
        laws.append(law)
    mu = [sum(t*w for t,w in law.items()) for law in laws]
    v = [sum((t-m)**2*w for t,w in law.items()) for law,m in zip(laws,mu)]
    norm = prod(1+a*a*z for a,z in zip(coeff,v))
    # Tilted variance need not equal the original variance.
    tilted = [{x:p*(1+a*(x-m))**2/(1+a*a*z) for x,p in law.items()}
              for law,a,m,z in zip(laws,coeff,mu,v)]
    nu = [sum(t*w for t,w in law.items()) for law in tilted]
    for law in tilted:
        assert sum(law.values()) == 1
    for index in range(len(primes)):
        assert (nu[index]-mu[index])/coeff[index] > F(1,2)
    terms = [(indices,prod(primes[j] for j in indices),prod(coeff[j] for j in indices))
             for k in range(6) for indices in combinations(range(5),k)]
    for limit in (15,100,500):
        retained = [(indices,a) for indices,n,a in terms if n <= limit]
        prob = F(0)
        for chosen,n,a in terms:
            inclusion = [coeff[j]**2*v[j]/(1+coeff[j]**2*v[j]) for j in range(5)]
            if n > limit:
                prob += prod(t if j in chosen else 1-t for j,t in enumerate(inclusion))
        exact = F(0)
        for outcome in product((-1,0,1), repeat=5):
            weight = prod(law[t] for law,t in zip(laws,outcome))
            centered = [t-m for t,m in zip(outcome,mu)]
            truncated = sum(a*prod(centered[j] for j in idx) for idx,a in retained)
            full = prod(1+a*z for a,z in zip(coeff,centered))
            exact += weight*(full-truncated)**2
        assert exact == prob*norm
    print('Three cutoffs for an asymmetric signed tilt: discarded squared norm equals the exact random-product tail.')


def check_rank_and_abel():
    primes = (5,7,11,13,17,19,23)
    count = 0
    for signs in product((-1,0,1),repeat=len(primes)):
        increments = [F(s,p) for s,p in zip(signs,primes)]
        prefix = [F(0)]
        for v in increments:
            prefix.append(prefix[-1]+v)
        bound = max(map(abs,prefix))
        for start in (3,5,8,12):
            for exponent in (1,2,4):
                for cap in (2,None):
                    def weight(p):
                        if p <= start:
                            return F(0)
                        ratio = F(p,start) if cap is None else min(F(p,start),F(cap))
                        return 1-ratio**(-exponent)
                    weights = [weight(p) for p in primes]
                    total = sum(w*z for w,z in zip(weights,increments))
                    by_parts = weights[-1]*prefix[-1] - sum(prefix[k]*(weights[k]-weights[k-1]) for k in range(1,len(weights)))
                    assert total == by_parts and abs(total) <= 2*bound
                    count += 1
        # A prime-rank prefix has a disjoint binary subdivision even for a
        # non-power-of-two prime count.
        padded = increments+[0]
        for stop in range(1,len(primes)+1):
            used = 0
            total = F(0)
            for power in (4,2,1):
                if stop & power:
                    assert used % power == 0
                    total += sum(padded[used:used+power])
                    used += power
            assert total == prefix[stop]
    print(f'{count} exact full and capped power sums satisfy the Abel bound over all tested sign patterns.')


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Enable assertions')
    check_moments()
    check_rank_and_abel()
