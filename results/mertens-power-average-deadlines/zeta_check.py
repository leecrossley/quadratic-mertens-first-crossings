"""Independent evaluation of the extremal inert product using zeta values."""
from flint import arb, ctx, fmpz


def mobius(n):
    factors=fmpz(n).factor()
    return 0 if any(k>1 for _,k in factors) else (-1)**len(factors)


def check():
    terms=32
    inversions=20
    result=arb(0)
    for k in range(1,terms+1):
        u=2*k+2
        prime_zeta=sum(mobius(m)*arb(m*u).zeta().log()/m for m in range(1,inversions+1))
        result+=2*prime_zeta/k
    error=arb(4)**(-terms)+8*terms*arb(2)**(-4*(inversions+1))
    result+=arb(0,error)
    a=arb(2).log()
    benchmark=(result-a.log()-a.exp()*a.expint(1)).exp()
    value=(1/benchmark).exp()
    assert value>arb(346133211)/10**8 and value<arb(346133212)/10**8
    print('Integer-zeta inversion gives sharp Yokoi deadline',value.str(17))
    print('32 prime-zeta terms, 20 Moebius terms and explicit bounds on both remainders.')


if __name__=='__main__':
    if not __debug__:
        raise SystemExit('Enable assertions')
    ctx.prec=192
    check()
