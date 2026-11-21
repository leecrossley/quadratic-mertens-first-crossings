"""Interval checks of two first packets, their signed prime sums, and the twist."""
from fractions import Fraction
from math import isqrt
from flint import arb, ctx, dirichlet_char

X = 2**24
WIDTH = 2**18


def packet_primes():
    end = X+WIDTH
    flags = bytearray([1])*(WIDTH+1)
    small = bytearray([1])*(isqrt(end)+1)
    for p in range(2, len(small)):
        if not small[p]:
            continue
        small[p*p::p] = bytes(len(small[p*p::p]))
        first = (-X) % p
        flags[first::p] = bytes(len(flags[first::p]))
    return [X+i for i, flag in enumerate(flags) if flag]


def old_sign(p):
    return 1 if p % 13 in (1, 3, 4, 9, 10, 12) else -1


def reference_sign(p):
    return 1 if p % 5 in (1, 4) else -1


def packet(name, c, b, primes):
    signed = []
    for eta in (1, -1):
        allocation = (c+eta*b)/2
        count = int(abs(allocation)*isqrt(X))
        sign = 1 if allocation > 0 else -1
        eligible = [p for p in primes if old_sign(p) == sign and reference_sign(p) == eta]
        assert len(eligible) >= count
        signed.extend((p, sign, eta) for p in eligible[:count])
    assert len(signed) <= isqrt(X)
    assert abs(sum(s for p, s, e in signed)-isqrt(X)*c) < 2
    assert abs(sum(s*e for p, s, e in signed)-isqrt(X)*b) < 2
    changes, average_changes = [], []
    for y in (arb(X)/3, arb(X)):
        d_race, d_product = arb(0), arb(0)
        for p, s, _ in signed:
            v = arb(1)/p
            d_race -= s*v*(1-y*v)
            d_product += s*(-2*(-v).log1p()*(1-y*v)
                            + (-v*v).log1p()*(1-y*v*v))
        norm = y.sqrt()*y.log()
        changes.append(norm*d_race)
        average_changes.append(norm*d_product)
    assert all(abs(x + 2*w) < arb("0.001") for x, w in zip(average_changes, changes))
    rise = changes[1]-changes[0]
    print(name, "flips", len(signed), "old signed mass", sum(s for p,s,e in signed),
          "twisted mass", sum(s*e for p,s,e in signed))
    bounds = ("5.9010", "5.9012") if name == "central" else ("3.5134", "3.5136")
    assert arb(bounds[0]) < rise < arb(bounds[1])
    print(name, "first-packet rise between", *bounds)


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run with assertions enabled.")
    ctx.prec = 160
    values = packet_primes()
    packet("central", Fraction(1), Fraction(0), values)
    packet("mixed", Fraction(3,5), Fraction(-4,5), values)
    twist = dirichlet_char(65, 64)
    assert all(twist(n) == (0 if n%5 == 0 or n%13 == 0 else old_sign(n)*reference_sign(n))
               for n in range(65))
    assert arb("1.2815") < twist.l(arb(1)/2).real < arb("1.2816")
    print("1.2815 < L(1/2,chi_65) < 1.2816")
