"""Integer per-bin interpolation and rounding; periodic central-value enclosure."""
from fractions import Fraction
from math import isqrt
from decimal import Decimal, localcontext

def prime(n):
    return n>1 and all(n % j for j in range(2,isqrt(n)+1))
def sign(p,q):
    r = p%q
    return 0 if not r else 1 if r in {i*i%q for i in range(1,q)} else -1
# Characters on classes are indexed by bit masks, with chi_5 first.
def walsh(c,j):
    return (-1)**bin(c & j).count('1')
def char(p,j):
    return (1,sign(p,5),sign(p,13),sign(p,5)*sign(p,13))[j]
def dest(p,j):
    return (sign(p,13),sign(p,5)*sign(p,13),sign(p,17),sign(p,5))[j]

round_carry = [Fraction(0) for _ in range(4)]
for left in (20000,30000):
    pts = [p for p in range(left+1,left+10001) if prime(p)]
    accum = [[0,0] for _ in range(4)]
    for c in range(4):
        part = [p for p in pts if all(char(p,j)==walsh(c,j) for j in (1,2))]
        count = len(part)
        first = sum(p-left for p in part)
        second = sum((p-left)**2 for p in part)
        a = sum(walsh(c,j)*dest(p,j) for p in pts for j in range(4))
        b = sum(walsh(c,j)*dest(p,j)*(p-left) for p in pts for j in range(4))
        den = 4*(count*second-first**2)
        intercept = second*a-first*b
        slope = count*b-first*a
        assert den>0 and 2*(abs(intercept)+10000*abs(slope)) < den
        for p in part:
            val = Fraction(intercept+(p-left)*slope,den)
            round_carry[c] += (1+val)/2
            bit = int(round_carry[c])
            round_carry[c] -= bit
            assert bit in (0,1) and 0<=round_carry[c]<1
            for j in range(4):
                v = walsh(c,j)*val
                accum[j][0] += v
                accum[j][1] += (p-left)*v
    for j in range(4):
        assert accum[j] == [sum(dest(p,j) for p in pts),sum(dest(p,j)*(p-left) for p in pts)]
print("Integer normal equations, residue-square tables and in-place rounding reproduce all sixteen moments.")

periods = [p for p in range(222,555) if prime(p)][:32]
bound = min(periods)**2
for n in range(1,bound):
    inds=[p for p in periods if not n%p]
    assert len(inds)<=1
    b=sum(p*((-1)**(n//(2*p))) for p in inds if n%(2*p)==0)
    assert abs(b)<=max(periods)
    special=[p for p in [periods[0]-1,*periods[1:]] if n%p==0]
    assert len(special)<=2
    e=sum(p*((-1)**(n//(2*p))) for p in special if n%(2*p)==0)
    assert abs(e)<=2*max(periods)
print("Direct divisibility search confirms both shorter-period envelopes.")
# General term chi(n)/sqrt(n). Its partial period sums after a whole
# period have absolute value <= 2, by direct enumeration. Abel summation
# bounds the infinite remainder by 2/sqrt(N) at a period boundary.
partial = []
total=0
for n in range(1,18):
    total+=sign(n,17)
    partial.append(total)
assert total==0
with localcontext() as ctx:
    ctx.prec=42
    N=17*2000
    v=sum(Decimal(sign(n,17))/Decimal(n).sqrt() for n in range(1,N+1))
    err=Decimal(max(map(abs,partial)))/Decimal(N).sqrt()+Decimal("1e-30")
    assert v-err>Decimal("0.70") and v+err<Decimal("0.75")
print("Elementary period summation without special functions puts the central value between 0.70 and 0.75.")

