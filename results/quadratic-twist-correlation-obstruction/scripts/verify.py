"""On ordinary primes, interpolate four quadratic twists in two adjacent bins."""

if not __debug__:
    raise SystemExit("Run with assertions enabled.")

from fractions import Fraction as F
from itertools import product
from math import isqrt, log
from flint import arb, ctx, dirichlet_char, fmpz

ctx.prec = 112
def chi(e,p):
    return int(fmpz(e).jacobi(p))

classes = list(product((1,-1), repeat=2))
def row(c):
    a,b=c
    return (1,a,b,a*b)
def targets(p):
    return tuple(chi(e,p) for e in (13,65,17,5))

# Carry the rounding prefix over the common boundary.
mass = dict.fromkeys(classes,F(0))
error = dict.fromkeys(classes,F(0))
num = 0
for left,right in ((20000,30000),(30000,40000)):
    ps = [p for p in range(left+1,right+1,2) if fmpz(p).is_prime()]
    norm = {p:F(p-left,right-left) for p in ps}
    groups = {c:[p for p in ps if (chi(5,p),chi(13,p)) == c] for c in classes}
    moment = [[sum(targets(p)[i]*norm[p]**j for p in ps) for j in (0,1)]
              for i in range(4)]
    f = {}
    for c,group in groups.items():
        a,b = [sum(row(c)[i]*moment[i][j] for i in range(4))/4 for j in (0,1)]
        n = len(group)
        u = sum(norm[p] for p in group)
        v = sum(norm[p]**2 for p in group)
        det = n*v-u*u
        assert det > 0
        A, B = (a*v-b*u)/det, (b*n-a*u)/det
        assert abs(A)+abs(B) < F(1,2)
        for p in group:
            f[p] = A+B*norm[p]
            old = mass[c]
            mass[c] += (1+f[p])/2
            sign = 2*(int(mass[c])-int(old))-1
            error[c] += sign-f[p]
            assert sign in (-1,1) and abs(error[c]) < 2
    for i in range(4):
        for j in (0,1):
            got = sum(f[p]*row((chi(5,p),chi(13,p)))[i]*norm[p]**j for p in ps)
            assert got == moment[i][j]
    num += len(ps)
    print(f"Bin ({left},{right}]: {len(ps)} primes, eight target moments exactly matched.")
print(f"{num} ordinary primes, both bins share the same four rounding accumulators; every class prefix has error below two.")

# Grids use cos(j*pi/2), an exact integer cycle.
k=32
periods = [p for p in range(int(2*k*log(k))+1,int(5*k*log(k))+1)
           if fmpz(p).is_prime()][:k]
assert len(periods)==k
cut = min(periods)**2
coefs = [0]*cut
hits = [0]*cut
for p in periods:
    for j in range(1,(cut-1)//p+1):
        coefs[j*p] += p*(1,0,-1,0)[j%4]
        hits[j*p] += 1
assert max(hits)==1 and max(map(abs,coefs))==max(periods)
S = sum(periods)
assert S > 22*max(periods)
special = [periods[0]-1, *periods[1:]]
assert sum(special) == S-1
extra = [0]*cut
for v in special:
    for j in range(1,(cut-1)//v+1):
        extra[j*v] += v*(1,0,-1,0)[j%4]
assert max(map(abs,extra)) <= 2*max(periods)
assert 17*17**sum(special) == 17**S
for n in (2*special[0],2*periods[0],S,2*S):
    A = S if n%S == 0 else 0
    for B,E in ((coefs[n],extra[n]),(0,0)):
        weights = [F(A-B,4)+B*(c==(1,1))+F(E-B,4)*c[1] for c in classes]
        assert [sum(w*row(c)[i] for w,c in zip(weights,classes)) for i in range(4)] == [A,B,E,B]
print(f"{k} periods, S={S}, largest integer period={max(periods)}. Both sequences checked through index {cut-1}.")
print("Special and ordinary conductor factors agree with the twist rule. Immediate and postponed class quotas reproduce all four coefficients.")
central = dirichlet_char(17,16).l(arb(1)/2)
assert central.imag == 0 or central.imag.contains(0)
assert arb("0.7216") < central.real < arb("0.7218")
print("L(1/2, chi_17) lies in (0.7216, 0.7218).")

