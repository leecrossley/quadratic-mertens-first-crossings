"""Independent integer and direct-Gaussian checks using the standard library."""
from decimal import Decimal, localcontext
from math import gcd, isqrt, prod


def prime(n):
    return n >= 2 and all(n % p for p in range(2, isqrt(n) + 1))


def independent():
    d = 1543 ** 2 + 4
    assert prime(d)
    # Build the residues by squaring. No character symbol or Euler test is used.
    residues = {k * k % d for k in range(1, (d + 1) // 2)}
    signs = [0] + [1 if n in residues else -1 for n in range(1, 500)]
    primes = [p for p in range(2, 216) if prime(p)]
    q = prod(primes)
    survivors = [n for n in range(1, 368) if gcd(n, q) == 1]
    assert survivors == [1] + [p for p in range(216, 368) if prime(p)]
    prefixes = [sum(signs[n] for n in survivors if n <= limit) for limit in range(368)]
    assert min(prefixes[1:331]) == 0 and prefixes[331] == -1
    assert max(prefixes[331:367]) == 0 and prefixes[367] == 1
    # Direct integer convolution against the divisors of 30.
    for n in range(1, 500):
        assert sum(signs[n // j] for j in (1, 2, 3, 5, 6, 10, 15, 30) if n % j == 0) == (
            signs[n] if gcd(n, 30) == 1 else 0)
    with localcontext() as ctx:
        ctx.prec = 48
        assert int(Decimal(d).ln() ** 2) == 215
        pi = Decimal("3.141592653589793238462643383279502884197169399375")
        # Duplicated from the definition at a single scale. For n>128 and
        # x=10 the integral tail after normalisation is less than 10^-68.
        def value(q):
            x = Decimal(10)
            return sum(signs[n] * (-pi * (Decimal(n) / x) ** 2).exp()
                       for n in range(1, 129) if gcd(n, q) == 1) / x.sqrt()
        assert Decimal("-0.145") < value(1) < Decimal("-0.144")
        assert Decimal("0.229") < value(30) < Decimal("0.231")
    print("Square-residue enumeration independently finds the ordered signs at 331 and 367.")
    print("Direct Gaussian sums at x=10: negative before removal, positive after removing 2, 3 and 5.")


def audit_census():
    primes = [p for p in range(2, 40001) if prime(p)]
    counts = [0, 0, 0]
    with localcontext() as ctx:
        ctx.prec = 48
        for m in range(1, 1000, 2):
            d = m*m + 4
            if any(d % (p*p) == 0 for p in primes if p <= isqrt(d)):
                continue
            z = int(Decimal(d).ln() ** 2)
            assert 2 <= z and z*z < 40000
            walk = [1]
            for p in primes:
                if p <= z:
                    continue
                if p > z*z:
                    break
                symbol = pow(d, (p-1)//2, p)
                walk.append(walk[-1] + (-1 if symbol == p-1 else symbol))
            first = next((i for i, s in enumerate(walk) if s < 0), len(walk))
            counts[0 if first == len(walk) else 1 + int(max(walk[first:]) > 0)] += 1
    assert counts == [7, 12, 425]
    print("Independent prime-residue walk reproduces all three census counts.")


if __name__ == "__main__":
    independent()
    audit_census()
