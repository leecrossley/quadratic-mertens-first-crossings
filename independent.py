"""Independent census using Arb L-values and factorization in the ring of integers."""

from flint import arb, ctx, dirichlet_char, fmpz


def norm_factors(d, cap):
    factors = []
    constant = (1 - d) // 4
    for p in range(2, cap + 1):
        if not fmpz(p).is_prime():
            continue
        roots = sum((j*j - j + constant) % p == 0 for j in range(p))
        if roots:
            factors.extend([p] * roots)
        elif p*p <= cap:
            factors.append(p*p)
    return sorted(factors)


def check(d):
    char = dirichlet_char(d, d-1)
    if not (char.is_primitive() and char.order() == 2 and char.parity() == 0):
        raise ArithmeticError("Unexpected quadratic character")
    residue = char.l(1)
    if not residue.imag.is_zero():
        raise ArithmeticError("Non-real residue")
    log_c = arb.const_euler() + residue.real.log()

    factors = norm_factors(d, 600)
    previous, i = 2, 0
    acc = arb(0)
    initial = None
    while i < len(factors):
        n = factors[i]
        # Use logarithms on both sides. All prime ideals at the same norm jump together.
        gap = acc - log_c - arb(n).log().log()
        if gap < 0:
            at_left = acc - log_c - arb(previous).log().log()
            if at_left < 0:
                row = (previous, n, str(previous), str(previous))
            else:
                if not at_left > 0:
                    raise ArithmeticError("Unresolved left endpoint")
                root = (acc - log_c).exp().exp()
                k = (root * 10**12).floor().unique_fmpz()
                if k is None or not (root > arb(k)/10**12 and root < arb(k+1)/10**12):
                    raise ArithmeticError("Unresolved rounding")
                def endpoint(j):
                    w, f = divmod(int(j), 10**12)
                    return f"{w}.{f:012d}"
                row = (previous, n, endpoint(k), endpoint(k+1))
            if initial is None:
                initial = row
            if i > 0:
                return (*initial, factors[0], *row)
        elif not gap > 0:
            raise ArithmeticError("Unresolved right limit")
        while i < len(factors) and factors[i] == n:
            acc += (arb(n)/(n-1)).log()
            i += 1
        previous = n
    raise ArithmeticError(f"No crossing verified for {d}")


def main():
    ctx.prec = 180
    print("m\td\twindow_left\twindow_right\tboundary_lower\tboundary_upper\tfirst_ideal_norm\tpost_window_left\tpost_window_right\tpost_lower\tpost_upper")
    m = 1
    while m*m + 4 <= 10000:
        d = m*m + 4
        if all(e == 1 for _, e in fmpz(d).factor()):
            print(m, d, *check(d), sep="\t")
        m += 2


if __name__ == "__main__":
    main()
