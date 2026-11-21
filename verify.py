"""Enclose the two real crossings and exhaust all earlier integer and norm samples."""

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from math import isqrt


def transcend(value, operation, upper):
    """Rational one-sided bound for an increasing, correctly rounded Decimal operation."""
    value = Fraction(value)
    with localcontext() as context:
        context.prec = 55
        context.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        endpoint = Decimal(value.numerator) / Decimal(value.denominator)
        rounded = getattr(endpoint, operation)()
        outward = rounded.next_plus() if upper else rounded.next_minus()
        return Fraction(outward)


def euler_constant():
    # Digamma expansion at n, with remainder between zero and the next term.
    n = 128
    subtotal = sum(Fraction(1, j) for j in range(1, n + 1))
    subtotal -= Fraction(1, 2 * n)
    subtotal += Fraction(1, 12 * n**2) - Fraction(1, 120 * n**4)
    subtotal += Fraction(1, 252 * n**6) - Fraction(1, 240 * n**8)
    lower = subtotal - transcend(n, "ln", True)
    upper = subtotal - transcend(n, "ln", False) + Fraction(1, 132 * n**10)
    return lower, upper


def main_term_constant(discriminant, unit_trace):
    scale = 10**55
    root = isqrt(discriminant * scale**2)
    root_lo, root_hi = Fraction(root, scale), Fraction(root + 1, scale)
    log_unit_lo = transcend((unit_trace + root_lo) / 2, "ln", False)
    log_unit_hi = transcend((unit_trace + root_hi) / 2, "ln", True)
    gamma_lo, gamma_hi = euler_constant()
    return (transcend(gamma_lo, "exp", False) * 2 * log_unit_lo / root_hi,
            transcend(gamma_hi, "exp", True) * 2 * log_unit_hi / root_lo)


def primes_to(limit):
    sieve = bytearray([1]) * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((limit - p*p) // p + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def prime_norms(discriminant, limit):
    norms = {}
    for p in primes_to(limit):
        symbol = pow(p, (discriminant - 1) // 2, discriminant)
        if symbol == 0:
            norms[p] = 1
        elif symbol == 1:
            norms[p] = 2
        elif p * p <= limit:
            norms[p * p] = 1
    return norms


def sign_at(product, constant, n):
    lower, upper = constant
    if product > upper * transcend(n, "ln", True):
        return 1
    if product < lower * transcend(n, "ln", False):
        return -1
    raise ArithmeticError(f"Unseparated sign at {n}")


def check(discriminant, trace, first_norm, digits, expected_integer, expected_norm):
    constant = main_term_constant(discriminant, trace)
    crossing_lo = transcend(1 / constant[1], "exp", False)
    crossing_hi = transcend(1 / constant[0], "exp", True)
    left = Fraction(digits)
    right = left + Fraction(1, 10**12)
    if not 2 < left < crossing_lo <= crossing_hi < right < first_norm:
        raise ArithmeticError("Real crossing enclosure failed")

    norms = prime_norms(discriminant, expected_norm)
    if min(norms) != first_norm:
        raise ArithmeticError("Unexpected initial prime-ideal norm")
    post_digits = {5: "8.794547206823", 13: "12.699403270702"}[discriminant]
    post_lo = Fraction(post_digits)
    post_hi = post_lo + Fraction(1, 10**12)
    preceding = Fraction(1)
    jumps = sorted(norms)
    for start, stop in zip(jumps, jumps[1:]):
        preceding *= Fraction(start, start - 1) ** norms[start]
        if sign_at(preceding, constant, start) < 0:
            raise ArithmeticError("Unexpected negative error at an ideal norm")
        if sign_at(preceding, constant, stop) < 0:
            if not (start < post_lo < post_hi < stop
                    and sign_at(preceding, constant, post_lo) > 0
                    and sign_at(preceding, constant, post_hi) < 0):
                raise ArithmeticError("Post-entry boundary enclosure failed")
            break
    else:
        raise ArithmeticError("Missing post-entry boundary")
    print(f"D={discriminant}: {post_digits} < first boundary after entry < {Decimal(post_hi.numerator)/Decimal(post_hi.denominator):.12f}")
    product = Fraction(1)
    first_integer = first_at_norm = None
    norms_checked = 0
    for n in range(2, expected_norm + 1):
        if n in norms:
            product *= Fraction(n, n - 1) ** norms[n]
            norms_checked += 1
        elif first_integer is not None:
            continue
        sign = sign_at(product, constant, n)
        if n == first_norm and sign != 1:
            raise ArithmeticError("Unexpected sign after the first jump")
        if sign < 0:
            if first_integer is None:
                first_integer = n
            if n in norms and first_at_norm is None:
                first_at_norm = n
    if (first_integer, first_at_norm) != (expected_integer, expected_norm):
        raise ArithmeticError("First negative sample mismatch")
    hi_text = format(Decimal(digits) + Decimal("0.000000000001"), "f")
    print(f"D={discriminant}: {digits} < first real boundary < {hi_text}")
    print(f"  first negative integer {first_integer}; first negative at a norm "
          f"{first_at_norm}; distinct norms checked {norms_checked}")


if __name__ == "__main__":
    check(5, 1, 4, "3.685768810485", 28, 8581)
    check(13, 3, 3, "2.333070011801", 16, 101)
