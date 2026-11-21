"""Certify each first crossing for squarefree d=m^2+4 through 10000.

The class number is isolated using one or more periods of the Dirichlet series.
The class number formula then gives a tight enclosure of L(1, chi_d).
"""

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from math import isqrt


def bound(x, operation, upper):
    # Both the rational input and the correctly rounded transcendental operation
    # are enclosed. Decimal ln and exp round to nearest, irrespective of context.
    x = Fraction(x)
    with localcontext() as context:
        context.prec = 56
        context.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        endpoint = Decimal(x.numerator) / Decimal(x.denominator)
        result = getattr(endpoint, operation)()
        return Fraction(result.next_plus() if upper else result.next_minus())


def exp_gamma():
    n = 128
    h = sum(Fraction(1, k) for k in range(1, n + 1))
    a = h - Fraction(1, 2*n) + Fraction(1, 12*n**2) - Fraction(1, 120*n**4)
    a += Fraction(1, 252*n**6) - Fraction(1, 240*n**8)
    return (bound(a - bound(n, "ln", True), "exp", False),
            bound(a - bound(n, "ln", False) + Fraction(1, 132*n**10), "exp", True))


def jacobi(a, n):
    value = 1
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                value = -value
        if a % 4 == n % 4 == 3:
            value = -value
        a, n = n % a, a
    return value if n == 1 else 0


def unit_step(m, d):
    scale = 10**50
    lower = isqrt(d * scale**2)
    r, s = Fraction(lower, scale), Fraction(lower + 1, scale)
    return (2 * bound((m+r)/2, "ln", False) / s,
            2 * bound((m+s)/2, "ln", True) / r)


def zeta_residue(m, d):
    step_lo, step_hi = unit_step(m, d)
    period = [jacobi(j, d) for j in range(1, d + 1)]
    cumul = largest = 0
    for c in period:
        cumul += c
        largest = max(largest, abs(cumul))
    if cumul:
        raise ArithmeticError("Character does not have mean zero")

    scale = 10**18
    lo = hi = terms = 0
    while True:
        for c in period:
            terms += 1
            lo += (c * scale) // terms
            hi -= (-c * scale) // terms
        # Partial summation after an exact period.
        tail = Fraction(largest, terms + 1)
        first = (Fraction(lo, scale) - tail) / step_hi
        last = (Fraction(hi, scale) + tail) / step_lo
        h = max(1, -(-first.numerator // first.denominator))
        if h > last:
            raise ArithmeticError("Class number interval is empty")
        if h + 1 > last:
            return h * step_lo, h * step_hi


def primes_to(limit):
    sieve = bytearray([1]) * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((limit-p*p)//p+1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def text_at_precision(n):
    q, r = divmod(n, 10**12)
    return f"{q}.{r:012d}"


def first_window(d, coefficient, primes):
    c_lo, c_hi = coefficient
    norms = {}
    for p in primes:
        sign = jacobi(p, d)
        if sign >= 0:
            norms[p] = 1 + sign
        elif p*p <= 600:
            norms[p*p] = 1
    value = Fraction(1)
    left = 2
    first = None
    first_norm = min(norms)
    for right, multiplicity in sorted(norms.items()):
        if value < c_lo * bound(right, "ln", False):
            if value < c_lo * bound(left, "ln", False):
                row = (left, right, str(left), str(left))
            else:
                if value <= c_hi * bound(left, "ln", True):
                    raise ArithmeticError("Unseparated sign at the start of a window")
                low_root = bound(value/c_hi, "exp", False)
                high_root = bound(value/c_lo, "exp", True)
                k = int(10**12 * low_root)
                if not Fraction(k, 10**12) < low_root <= high_root < Fraction(k+1, 10**12):
                    raise ArithmeticError("Unseparated decimal enclosure")
                row = (left, right, text_at_precision(k), text_at_precision(k+1))
            if first is None:
                first = row
            if left >= first_norm:
                return (*first, first_norm, *row)
        elif value <= c_hi * bound(right, "ln", True):
            raise ArithmeticError("Unseparated sign immediately before a norm")
        value *= Fraction(right, right-1)**multiplicity
        left = right
    raise ArithmeticError(f"No certified crossing through the last norm for {d}")


def main():
    primes = primes_to(600)
    gamma_lo, gamma_hi = exp_gamma()
    print("m\td\twindow_left\twindow_right\tboundary_lower\tboundary_upper\tfirst_ideal_norm\tpost_window_left\tpost_window_right\tpost_lower\tpost_upper")
    for m in range(1, isqrt(10000-4) + 1, 2):
        d = m*m + 4
        if any(d % (p*p) == 0 for p in primes if p*p <= d):
            continue
        lo, hi = zeta_residue(m, d)
        row = first_window(d, (lo*gamma_lo, hi*gamma_hi), primes)
        print(m, d, *row, sep="\t")


if __name__ == "__main__":
    main()
