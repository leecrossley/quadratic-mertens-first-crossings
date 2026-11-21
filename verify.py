"""Check the prime identities on finite packets and the scalar constants."""
from fractions import Fraction
from math import isqrt

from flint import arb, ctx, fmpz


def cosine_multiple(first, j):
    previous, current = Fraction(1), first
    for _ in range(1, j):
        previous, current = current, 2*first*current - previous
    return current


def select_packet(j, c):
    x = 256**j
    limit = x + isqrt(isqrt(x**3))
    wanted = int(abs(c)*isqrt(x)/j)
    direction = 1 if c > 0 else -1
    selected = []
    for p in range(x+1, limit+1, 2):
        if (0,1,-1,-1,1)[p % 5] == direction and fmpz(p).is_prime():
            selected.append(p)
            if len(selected) == wanted:
                break
    assert len(selected) == wanted > 0
    return x, direction, selected


def check_packet(j, c):
    x, sign, primes = select_packet(j,c)
    values = []
    normalisation = arb(0)
    for p in primes:
        norm = arb(p)
        first = -(-1/norm).log1p()
        second = -(-1/(norm*norm)).log1p()
        normalisation += ((norm-sign)/(norm+sign)).log()
        values.append((p,first,second))
    assert (primes[-1]-x)**4 <= x**3
    one = arb(1)
    for y in (x//2, x, primes[len(primes)//2], primes[-1]+1, x*x, primes[-1]**2+1):
        direct, tail = -normalisation, arb(0)
        for p, first, second in values:
            small = arb(y)/p
            large = small/p
            direct += sign*(-2*first*min(one,small) + second*min(one,large))
            tail += sign*(2*first*max(0,1-small) - second*max(0,1-large))
        assert direct.overlaps(tail)
        assert abs(direct-tail) < arb("1e-28")

    # A power cutoff that includes the whole packet and separates equal even powers.
    H = arb(x).log()*arb(7)/2
    for t in (arb(0),arb(1)/5):
        before, after = arb(0), arb(0)
        for p in primes:
            v = arb(p).log()
            for k in (1,2,3):
                z = k*v
                assert z < H
                w = v*(-z/2).exp()*(1-z/H)*(t*z).cos()
                before += sign**k*w
                after += (-sign)**k*w
        direct = -2*(after-before)/H
        # The floor, displacement and odd powers dominate the difference.
        u = arb(x).log()
        ideal = 4*arb(256).log()/H*(1-u/H)*(t*u).cos()*arb(c.numerator)/c.denominator
        allowance = (12*arb(256).log()/arb(x).sqrt().sqrt()+8*u/arb(x).sqrt())/H
        assert abs(direct-ideal) < allowance
    return len(primes)


def check():
    pi = arb.pi()
    assert -arb(1)/8-4/pi**2 < -arb(53)/100
    assert arb(1)/2*((pi/2).sin()/(pi/2))**2*2 > arb(4)/10
    for first in (Fraction(1),Fraction(3,5)):
        counts = [check_packet(j,cosine_multiple(first,j)) for j in (2,3,4)]
        print(f"cos(theta)={first}, selected {counts} ordinary primes in packets 2, 3 and 4.")
    print("Direct local product changes equal the signed tails at six cutoffs per packet.")
    print("Weighted prime powers at two frequencies meet the computed packet error bounds.")
    print("The uniform limiting scalar bound is below -0.53.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Enable Python assertions.")
    ctx.prec = 192
    check()
