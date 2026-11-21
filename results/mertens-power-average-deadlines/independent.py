"""Second arithmetic implementation, including a quadrature independent of expint."""
from fractions import Fraction
from math import isqrt
from pathlib import Path
from flint import arb, ctx, fmpz


def qnum(x):
    v=Fraction(x)
    return arb(v.numerator)/v.denominator


def baseline(a):
    # Integral of exp(-v)/(a+v), using a Taylor expansion on unit panels.
    half=arb(1)/2
    em=(-arb(1)).exp()
    moments=[1-em]
    for k in range(1,57):
        moments.append((-half)**k-half**k*em+k*moments[-1])
    total=arb(0)
    for j in range(60):
        midpoint=a+j+half
        poly=arb(0)
        for moment in reversed(moments):
            poly=moment-poly/midpoint
        remainder=(half/midpoint)**len(moments)/(a+j)
        total+=(-arb(j)).exp()*(poly/midpoint+arb(0,remainder))
    return total+arb(0,(-arb(60)).exp()/(a+60))


def endpoint_value(y,s,kind,N,base):
    # Average the log height of each constant window directly.
    n=Fraction(N)
    last=y
    total=arb(0)
    def mass(t):
        return (arb(y)/qnum(t))**s
    for k in range(y+1,int(n)+1):
        if kind=='prime_powers' and len(fmpz(k).factor())!=1:
            continue
        total+=(mass(last)-mass(k))*(arb(k).log()/arb(y).log()).log()
        last=k
    total+=mass(last)*(qnum(n).log()/arb(y).log()).log()
    return total-base


def yokoi_supremum():
    root_y=arb(2)
    a=root_y.log()
    avgloglog=a.log()+baseline(a)
    cutoff=20000
    ell=lambda q:(1/(arb(q)-1)).log1p()
    avg=sum(2*ell(p*p)/(p*p) for p in range(2,cutoff+1) if fmpz(p).is_prime())
    # 2*ell(p^2)/p^2 <= 4/p^4 and sum_{n>Q} 1/n^4 <= 1/(3Q^3).
    tail=arb(4)/(3*cutoff**3)
    avg+=arb(tail/2,tail/2)
    benchmark=(avg-avgloglog).exp()
    boundary=(1/benchmark).exp()
    assert boundary>qnum('3.46133211') and boundary<qnum('3.46133212')
    split=(avg+4*ell(3)/3-2*ell(9)/9-avgloglog).exp()
    assert split*arb(3).log()>1
    print('Yokoi supremum at y=2, s=1 in (3.46133211, 3.46133212).')
    print('A split at 3 forces the first crossing below 3. The all-inert limit crosses between 3 and 4.')


def independent_deadlines():
    file=Path(__file__).resolve().parent/'evidence'/'deadlines.txt'
    for row in file.read_text().splitlines()[1:]:
        y,s,kind,_,_,lower,upper=row.split()
        y,s=int(y),int(s)
        a=s*arb(y).log()
        ref=baseline(a)
        assert ref.overlaps(a.exp()*a.expint(1))
        assert endpoint_value(y,s,kind,lower,ref)<0
        assert endpoint_value(y,s,kind,upper,ref)>0
    print('All ten deadline brackets passed using direct window masses, integer factorisation and a separate quadrature.')


if __name__=='__main__':
    if not __debug__:
        raise SystemExit('Enable Python assertions')
    ctx.prec=416
    independent_deadlines()
    yokoi_supremum()
