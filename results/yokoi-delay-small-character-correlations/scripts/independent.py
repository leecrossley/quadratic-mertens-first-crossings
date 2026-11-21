"""Separate check with trial division, Euler's criterion and incomplete gamma integrals."""

if not __debug__:
    raise SystemExit("Run with assertions enabled.")

from decimal import Decimal, localcontext
from math import isqrt
from flint import arb, ctx

ctx.prec = 136
d = 1543**2+4
def prime(n):
    return n >= 2 and all(n % j for j in range(2, isqrt(n)+1))
assert prime(d)

def symbol(a,p):
    v = pow(a % p, (p-1)//2, p)
    return -1 if v==p-1 else v

refs = (-31,-24,-23,-20,-19,-15,-11,-8,-7,-4,-3,5,8,12,13,17,21,24,28,29)
raw = {}
for k in (1,*refs):
    num = den = 1
    for p in range(33699,67397,2):
        if prime(p):
            s = symbol(d*k,p)
            if s == 1:
                num *= p
            elif s == -1:
                den *= p
    # Decimal.ln is correctly rounded. Each input is an exact integer;
    # here both logarithms are < 100000, so 40 significant digits
    # give an error below 1e-32 in their difference.
    with localcontext() as ctxd:
        ctxd.prec = 40
        raw[k] = Decimal(num).ln() - Decimal(den).ln()
assert max(refs,key=lambda k:abs(raw[k])) == -11
for k,n in ((1,-174081),(5,-58202),(13,79015),(-11,87994)):
    assert n+Decimal("1e-25") < 100*raw[k] < n+1-Decimal("1e-25")
print("Exact prime products reproduce all four window intervals and the maximising character.")

def l_values(q, other):
    half = arb(1)/2
    pi = arb.pi()
    rate = pi/q
    vals = [arb(0), arb(0)]
    stop = 10*(1+isqrt(q))
    for n in range(1,stop+1):
        chi = symbol(n,d)*(symbol(n,other) if other != 1 else 1)
        if not chi:
            continue
        x = rate*n*n
        for j,s in enumerate((half,arb(1))):
            t = half-s
            # Integrate the original theta sum from 2 to infinity
            # and its transformed sum from 1/2 to infinity.
            vals[j] += chi*((2*x).gamma_upper(s)*x**(-s)
                            +(x/2).gamma_upper(t)*x**(-t))
    err = 6*q/(pi*stop)*(-rate*stop**2/2).exp()
    assert err < arb("1e-50")
    return [(v+arb(0,"1e-50"))*rate**s/s.gamma()
            for v,s in zip(vals,(half,arb(1)))]

end = 3*d
# Odd-only sieve, then a different Euler-product subtraction.
odd = bytearray([1])*(end//2+1)
for i in range(3,isqrt(end)+1,2):
    if odd[i//2]:
        j = i*i//2
        odd[j::i] = bytes((len(odd)-1-j)//i+1)
ps = [2]+[2*i+1 for i in range(1,len(odd)) if 2*i+1 <= end and odd[i]]
ys = (163,d,end)
bounds = {1:((-176,-175),(-115,-112),(-301,-298)),
          5:((24,25),(166,169),(103,106)),
          13:((-2,-1),(-170,-167),(-93,-90))}
for k in (1,5,13):
    ls = l_values(k*d,k)
    prefix = {}
    corrections = [arb(0), arb(0)]
    sums = [arb(0), arb(0)]
    j = 0
    for p in ps:
        while j < len(ys) and ys[j] < p:
            prefix[ys[j]] = tuple(sums)
            j += 1
        chi = symbol(p,d)*(symbol(p,k) if k != 1 else 1)
        for i in range(2):
            z = arb(chi)/p**(i+1)
            sums[i] += z
            corrections[i] += (-z).log1p()+z
    while j < len(ys):
        prefix[ys[j]] = tuple(sums)
        j += 1
    tails = [ls[i].log()+corrections[i]+arb(0,arb(1)/((2*i+1)*end**(2*i+1)))
             for i in range(2)]
    for y,(lo,hi) in zip(ys,bounds[k]):
        w = arb(y).sqrt()*arb(y).log()*(tails[0]-prefix[y][0]-y*(tails[1]-prefix[y][1]))
        assert lo < 100*w < hi,(k,y,w)
print("Three infinite tails at three starts pass a separate theta split and direct Euler remainder.")

