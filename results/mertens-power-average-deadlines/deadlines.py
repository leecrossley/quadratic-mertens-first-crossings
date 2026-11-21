"""Certify optimal comparison deadlines for two possible sets of jump locations."""
import argparse
from fractions import Fraction
from math import isqrt
from flint import arb, ctx


def num(value):
    q=Fraction(value)
    return arb(q.numerator)/q.denominator


def jumps(kind, y, limit):
    if kind == 'integers':
        return range(y+1, limit+1)
    marks = bytearray([1])*(limit+1)
    for p in range(2,isqrt(limit)+1):
        if marks[p]:
            marks[p*p::p]=bytes(1+(limit-p*p)//p)
    powers=set()
    for p in range(2,limit+1):
        if marks[p]:
            q=p
            while q<=limit:
                if q>y:
                    powers.add(q)
                q*=p
    return sorted(powers)


def certified_root(y,s,kind,limit):
    ell=num(y).log()
    start=s*ell
    deficit=start.exp()*start.expint(1)
    previous=y
    for q in jumps(kind,y,limit):
        hi=num(q).log()
        weight=(num(y)/previous)**s
        gain=weight*(hi/ell).log()
        if gain>deficit:
            root=(ell*(deficit/weight).exp()).exp()
            assert root>previous and root<q
            return root, previous,q
        assert gain<deficit
        deficit-=gain
        previous,ell=q,hi
    raise ArithmeticError('Increase the search limit')


def digits(val,places=8):
    mult=10**places
    k=int((val*mult).floor().unique_fmpz())
    assert num(Fraction(k,mult))<val<num(Fraction(k+1,mult))
    def form(n):
        i,j=divmod(n,mult)
        return f'{i}.{j:0{places}d}'
    return form(k),form(k+1)


if __name__=='__main__':
    if not __debug__:
        raise SystemExit('Enable assertions')
    ctx.prec=192
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start',type=int)
    parser.add_argument('--power',type=int)
    parser.add_argument('--limit',type=int,default=100000)
    args=parser.parse_args()
    if (args.start is None)!=(args.power is None):
        parser.error('Supply both the start and the power')
    cases=[(args.start,args.power)] if args.start is not None else [(2,1),(10,1),(10,2),(100,1),(100,2)]
    print('y s jump_set previous_jump next_jump root_lower root_upper')
    for y,s in cases:
        if y<2 or s<1 or args.limit<=y:
            parser.error('Use start >=2, positive integral power and limit > start')
        for kind in ('integers','prime_powers'):
            val,left,right=certified_root(y,s,kind,args.limit)
            print(y,s,kind,left,right,*digits(val))
