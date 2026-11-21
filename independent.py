"""Cross-check with Gauss sums, polynomial factorization and Arb ball arithmetic."""

from math import isqrt
from fractions import Fraction
from flint import arb, ctx


def residue_at_one(d):
    squares = {k * k % d for k in range(1, d)}
    total = arb(0)
    for a in range(1, d):
        character = 1 if a in squares else -1
        chord = 2 * (arb.pi() * a / d).sin()
        total -= character * chord.log()
    return total / arb(d).sqrt()


def prime_ideals(d, limit):
    # Modulo p the roots of t^2-t+(1-d)/4 count the degree-one prime ideals.
    constant = (1 - d) // 4
    norms = []
    for p in range(2, limit + 1):
        if any(p % a == 0 for a in range(2, isqrt(p) + 1)):
            continue
        roots = sum((t*t - t + constant) % p == 0 for t in range(p))
        if roots:
            norms.extend([p] * roots)
        elif p*p <= limit:
            norms.append(p*p)
    return sorted(norms)


def check(d, digits, expected_integer, expected_norm):
    c = arb.const_euler().exp() * residue_at_one(d)
    boundary = (1 / c).exp()
    lo = arb(digits)
    if not (boundary > lo and boundary < lo + arb(1)/10**12):
        raise ArithmeticError("Independent real crossing enclosure failed")
    norms = prime_ideals(d, expected_norm)
    if not (boundary > 2 and boundary < norms[0]):
        raise ArithmeticError("First crossing is outside the empty-product interval")

    # Use logarithms of Euler factors here, independently of the exact products.
    log_product = arb(0)
    first_integer = first_at_norm = None
    pos = 0
    for n in range(2, expected_norm + 1):
        before = pos
        while pos < len(norms) and norms[pos] == n:
            log_product += (arb(n)/(n - 1)).log()
            pos += 1
        if before == pos and first_integer is not None:
            continue
        error = log_product - (c * arb(n).log()).log()
        if error < 0:
            if first_integer is None:
                first_integer = n
            if before < pos and first_at_norm is None:
                first_at_norm = n
        elif not error > 0:
            raise ArithmeticError(f"Independent check cannot separate the sign at {n}")
    if (first_integer, first_at_norm) != (expected_integer, expected_norm):
        raise ArithmeticError("Independent first negative sample mismatch")
    print(f"D={d}: Gauss-sum enclosure and norm-factorization check agree "
          f"at {ctx.prec} bits; first negative integer {first_integer}, norm {first_at_norm}.")


def check_family():
    # Count all admissible residue classes mod p^2, avoiding the character-sum formula.
    choices = []
    primes = [n for n in range(3, 4001, 2)
              if all(n % a != 0 for a in range(2, isqrt(n) + 1))]
    for p in primes:
        if p > 31:
            break
        squares = {a*a % p for a in range(1, p)}
        levels = {-1: 0, 0: 0, 1: 0}
        for m in range(p*p):
            d = m*m + 4
            if d % (p*p) == 0:
                continue
            residue = d % p
            s = 0 if residue == 0 else (1 if residue in squares else -1)
            levels[s] += 1
        total = sum(levels.values())
        choices.append([(Fraction(p, p-s), Fraction(n, total))
                        for s, n in levels.items() if n])

    def subtree(k, product):
        if k == len(choices):
            return int(Fraction(59, 100) <= product <= Fraction(7, 10))
        return sum(weight * subtree(k + 1, product * factor)
                   for factor, weight in choices[k])

    mass = subtree(0, Fraction(2, 3))
    if mass != Fraction(116900317682048, 964766068682647):
        raise ArithmeticError("Independent residue-class count failed")
    variance = sum(1 / arb(p-1)**2 for p in primes if p > 31) + 1/arb(3999)
    radius = arb(7)/50
    if not (variance < arb(1)/150 and radius > 2*variance):
        raise ArithmeticError("Independent tail preparation failed")
    probability = 1 - variance / (radius - 2*variance)**2
    if not arb(mass.numerator)/mass.denominator * probability > arb(7)/100:
        raise ArithmeticError("Independent probability inequality failed")
    eg = (-arb.const_euler()).exp()
    left_limit = eg / (arb(299)/100).log()
    right_limit = eg / (arb(401)/200).log()
    if not (left_limit < arb(59)/100 * (-radius).exp()
            and arb(7)/10 * radius.exp() < right_limit):
        raise ArithmeticError("Independent real-interval inclusion failed")
    print("Yokoi family: direct local counts modulo p^2 and Arb interval checks "
          "confirm relative proportion > 7/100.")


if __name__ == "__main__":
    ctx.prec = 180
    check(5, "3.685768810485", 28, 8581)
    check(13, "2.333070011801", 16, 101)
    check_family()
