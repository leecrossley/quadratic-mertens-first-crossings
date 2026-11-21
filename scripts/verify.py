"""Interval evaluation of the entire oriented tail and the log-product average."""
from math import isqrt
from flint import arb, ctx, dirichlet_char, fmpz

D, LIMIT = 533, 100_000


def primes():
    sieve = bytearray([1]) * (LIMIT + 1)
    for p in range(2, isqrt(LIMIT) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((LIMIT-p*p)//p + 1)
    return [p for p in range(2, LIMIT + 1) if sieve[p]]


def character(d, p):
    return -1 if p == 2 else int(fmpz(d).jacobi(p))


def contain(value, low, high):
    assert arb(low) < value < arb(high), (value, low, high)


def calculate():
    ctx.prec = 160
    assert D == 23**2 + 4 == 13*41
    field, reference = dirichlet_char(D, D-1), dirichlet_char(5, 4)
    prime_list = primes()
    rows = [(p, character(D, p), character(5, p)) for p in prime_list]
    # Check the Conrey labellings on a full residue system.
    for d, chi in ((D, field), (5, reference)):
        assert all(chi(n) == int(fmpz(n).jacobi(d)) for n in range(d))

    constants = []
    for k in (1, 2):
        value = (field.l(k).real / reference.l(k).real).log()
        for p, a, b in rows:
            if a == b:
                continue
            x = arb(1) / (p**k)
            value += (-a*x).log1p() - (-b*x).log1p()
            if a and b:
                value += (a-b)*x
        # Beyond LIMIT all primes are unramified. Even powers cancel;
        # the absolute tail of the unhalved correction is <= 2/M^(3k-1).
        constants.append(value/2 + arb(0, arb(2)/LIMIT**(3*k-1)))

    def weighted(y):
        linear, square = constants
        for p, a, b in rows:
            if p > y:
                break
            if a*b == -1:
                linear -= arb(a)/p
                square -= arb(a)/p**2
        return arb(y).sqrt()*arb(y).log()*(linear-y*square)

    def product_average(y, function, column):
        tail = (arb(2).zeta()*function.l(2).real).log()
        prefix = prefix_slope = arb(0)
        for row in rows:
            p, a = row[0], row[column]
            q, multiplicity = (p*p, 1) if a == -1 else (p, 1+a)
            if q > LIMIT:
                continue
            z = arb(1)/q
            local = -(-z).log1p()
            tail += multiplicity*(z*local + (-z*z).log1p())
            if q <= y:
                prefix += multiplicity*local
                prefix_slope += multiplicity*z*local
        tail += arb(0, arb(4)/LIMIT**2)
        logy = arb(y).log()
        f = (prefix - arb.const_euler() - function.l(1).real.log() - logy.log()
             + y*(tail-prefix_slope-logy.expint(1)))
        return arb(y).sqrt()*logy*f

    down = weighted(240) - weighted(30)
    up = weighted(4096) - weighted(512)
    average = product_average(30, field, 1)
    threshold = product_average(30, reference, 2)/2
    contain(weighted(30), "0.5142549", "0.5142550")
    contain(threshold, "0.293944", "0.293946")
    contain(threshold-average/2, "0.329780", "0.329783")
    band = ((arb(699)*arb(8).log()/2000).sin()
            / (((arb(701)/1000)**2 + arb(1)/4)
               * ((arb(701)/1000)**2 + arb(9)/4)).sqrt())
    contain(band, "0.4660719", "0.4660720")
    contain(down, "-1.033", "-1.030")
    contain(up, "0.818", "0.822")
    print("spectral interval: 0.4660719 < endpoint lower bound < 0.4660720")
    print("d=533, W(log 240)-W(log 30) in (-1.033,-1.030)")
    print("d=533, W(log 4096)-W(log 512) in (0.818,0.822)")
    contain(average, "-0.071674", "-0.071672")
    print("d=533, -0.071674 < sqrt(30) log(30) F(30) < -0.071672")
    print("y=30, oriented W in (0.5142549,0.5142550), corrected lead in (0.329780,0.329783)")
    print("y=30, reference crossing threshold in (0.293944,0.293946)")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run with assertions enabled.")
    calculate()
