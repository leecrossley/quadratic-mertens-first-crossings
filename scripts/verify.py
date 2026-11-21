"""Prime windows and complete ordered tails for one late Yokoi field."""
from math import isqrt
from flint import arb, ctx, fmpz
from weighted import primes, prime_constants

ctx.prec = 144
d = 2380853
assert d == 1543**2 + 4 and fmpz(d).is_prime()
plist = primes(3*d)
window = [p for p in plist if 33698 < p <= 67396]
refs = []
for delta in range(-31, 32):
    v = delta if delta % 4 == 1 else (
        delta//4 if delta % 4 == 0 and delta//4 % 4 in (2,3) else 0)
    if delta != 1 and v and all(v % (j*j) for j in range(2, isqrt(abs(v))+1)):
        refs.append(delta)
assert len(refs) == 20 and len(window) == 3103
logs = {delta: sum(int(fmpz(d*delta).jacobi(p))*arb(p).log() for p in window)
        for delta in [1, *refs]}
assert all(abs(logs[delta]) < logs[-11] for delta in refs if delta != -11)
for delta, lo in [(1,-174081), (5,-58202), (13,79015), (-11,87994)]:
    value = 100*logs[delta]
    assert lo < value < lo+1
    print(f"Window character {delta:3}: weighted log sum in ({lo}/100, {lo+1}/100).")
print("3103 primes. Strongest of the 20 secondary characters: discriminant -11.")

starts = (163, d, 3*d)
ranges = (
    ((-1755,-1754), (-1139,-1138), (-2997,-2996)),
    ((249,250), (1677,1678), (1046,1047)),
    ((-13,-12), (-1683,-1682), (-912,-911)),
)
early = [p for p in plist if p <= 200000]
for (q, factors), targets in zip(((d,[d]),(5*d,[5,d]),(13*d,[13,d])), ranges):
    c1,c2 = prime_constants(q, factors, early, 1)
    j = 0
    for y,(lower,upper) in zip(starts, targets):
        while j < len(plist) and plist[j] <= y:
            p = plist[j]
            sign = int(fmpz(p).jacobi(q))
            c1 -= arb(sign)/p
            c2 -= arb(sign)/(p*p)
            j += 1
        v = arb(y).sqrt()*arb(y).log()*(c1-y*c2)
        assert lower < v*1000 < upper, (q,y,v)
        print(f"y={y}, character {q//d}: normalised full tail in ({lower}/1000, {upper}/1000).")

