"""Check the local laws, truncated weight and fourth moments with exact rationals."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import prod


def local_law(p):
    squares = {i*i % p for i in range(1, p)}
    counts = Counter()
    for m in range(p*p):
        d = m*m+4
        if d % (p*p):
            sign = 0 if d % p == 0 else 1 if d % p in squares else -1
            counts[sign] += 1
    c = 2 if p % 4 == 1 else 0
    law = {s: F(n, sum(counts.values())) for s, n in counts.items()}
    for s in (-1, 1):
        assert law[s] == F(p*(p-c-s), 2*(p*p-c))
    assert law.get(0, 0) == F(c*(p-1), p*p-c)
    return law


def expectation(law, f):
    return sum(prob*f(s) for s, prob in law.items())


def check_weights():
    primes = (3, 5, 7, 11, 13)
    laws = [local_law(p) for p in primes]
    mu = [expectation(law, lambda s: s) for law in laws]
    var = [expectation(law, lambda s: (s-m)**2) for law, m in zip(laws, mu)]
    a = [F(1, p+17) for p in primes]
    tilted = []
    for law, m, v, k in zip(laws, mu, var, a):
        new = {s: w*(1-k*(s-m))**2/(1+k*k*v) for s, w in law.items()}
        assert sum(new.values()) == 1
        skew = expectation(law, lambda s: (s-m)**3)
        mean = expectation(new, lambda s: s)
        assert mean == m+(-2*k*v+k*k*skew)/(1+k*k*v) and mean <= -k/2
        tilted.append(new)
    nu = [expectation(law, lambda s: s) for law in tilted]
    indices = range(len(primes))
    sets = [subset for length in range(len(primes)+1) for subset in combinations(indices, length)]
    norms = [prod(primes[i] for i in subset) for subset in sets]
    masses = [prod(a[i]**2*var[i] for i in subset) for subset in sets]
    norm = prod(1+k*k*v for k, v in zip(a, var))
    assert sum(masses) == norm
    cuts = (1, 35, 75, 1000, prod(primes))
    lost = [F(0) for _ in cuts]
    blocks = [(lo, hi) for lo in indices for hi in range(lo+1, len(primes)+1)]
    moments = Counter()
    cases = 0
    for signs in product(*laws):
        cases += 1
        prob = prod(law[s] for law, s in zip(laws, signs))
        z = [s-m for s, m in zip(signs, mu)]
        full = prod(1-k*x for k, x in zip(a, z))
        tilted_prob = prod(law[s] for law, s in zip(tilted, signs))
        assert prob*full**2/norm == tilted_prob
        terms = [prod(-a[i]*z[i] for i in subset) for subset in sets]
        assert sum(terms) == full
        for j, cut in enumerate(cuts):
            truncated = sum(t for t, n in zip(terms, norms) if n <= cut)
            lost[j] += prob*(full-truncated)**2
        for lo, hi in blocks:
            centered = sum((signs[i]-nu[i])/primes[i] for i in range(lo, hi))
            moments[lo, hi] += tilted_prob*centered**4
    for cut, actual in zip(cuts, lost):
        assert actual == sum(mass for mass, n in zip(masses, norms) if n > cut)
    for lo, hi in blocks:
        vv, fourth = [], []
        for i in range(lo, hi):
            vv.append(expectation(tilted[i], lambda s: ((s-nu[i])/primes[i])**2))
            fourth.append(expectation(tilted[i], lambda s: ((s-nu[i])/primes[i])**4))
        assert moments[lo, hi] == sum(fourth)+6*sum(x*y for x, y in combinations(vv, 2))
    print(f"5 local laws from residue counts, {cases} joint assignments, 5 length cutoffs")
    print(f"All tilted means, discarded squared norms and {len(blocks)} centered fourth moments agree exactly")


def check_prefixes():
    count = 0
    for log_size in range(8):
        size = 1 << log_size
        for length in range(size+1):
            start = 0
            covered = []
            for level in range(log_size+1):
                width = size >> level
                if length & width:
                    assert start % width == 0
                    covered.extend(range(start, start+width))
                    start += width
            assert covered == list(range(length))
            count += 1
    print(f"{count} prefixes partition into aligned dyadic intervals on blocks of size 1 through 128")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Assertions must be enabled.")
    check_weights()
    check_prefixes()
