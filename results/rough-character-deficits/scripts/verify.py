"""Certified signed Gaussian masses and exact sieve data in one Yokoi field."""
from itertools import combinations
from math import ceil, prod
from flint import arb, ctx, fmpz

ctx.prec = 112
D = 2_380_853
PI = arb.pi()
STEP = 512
RADIUS = arb("1e-18")
LOW = -2
LOG_D = arb(D).log()
ROOT = arb(D).sqrt()
MAX_INDEX = ceil(float(LOG_D / 2) * STEP) + 2
CHARACTER = [int(fmpz(n).jacobi(D)) for n in range(ceil(5 * float(ROOT)) + 16)]


def base_value(log_x):
    x = log_x.exp()
    cut = max(1, ceil(4.25 * float(x)))
    # The integral test gives x^2 exp(-pi cut^2/x^2)/(2 pi cut sqrt(x)).
    tail = x ** 2 * (-PI * (cut / x) ** 2).exp() / (2 * PI * cut * x.sqrt())
    assert tail < RADIUS
    ratio = (-PI / x ** 2).exp()
    term = ratio
    increment = ratio ** 3
    increment_ratio = ratio ** 2
    total = arb(0)
    for n in range(1, cut + 1):
        if CHARACTER[n] == 1:
            total += term
        elif CHARACTER[n] == -1:
            total -= term
        term *= increment
        increment *= increment_ratio
    return total / x.sqrt() + arb(0, RADIUS)


def build_mesh():
    return [base_value(arb(k) / STEP) for k in range(LOW * STEP, MAX_INDEX + 1)]


def interpolate(mesh, v):
    # The identity holds on either side of the chosen reflection point.
    if float(v) > float(LOG_D / 2):
        v = LOG_D - v
    if v < LOW:
        # For x <= exp(-2) the entire absolute Gaussian is below 10^-65.
        return arb(0, "1e-65")
    k = round(float(v) * STEP)
    if v < arb(k) / STEP:
        k -= 1
    # At a grid boundary either adjacent affine extension has the stated error.
    t = v * STEP - k
    assert t > arb("-1e-25") and t < arb("1.0000000000000000000000001")
    i = k - LOW * STEP
    assert 0 <= i < len(mesh) - 1
    return (1 - t) * mesh[i] + t * mesh[i + 1]


def central_mass():
    # Twice the primitive half integral. Monotonic upper bound for the tail.
    end = ceil(4.25 * float(ROOT))
    z = PI / D
    total = arb(0)
    for n in range(1, end + 1):
        if CHARACTER[n]:
            total += CHARACTER[n] * (z * n * n).gamma_upper(arb(1) / 4) / arb(n).sqrt()
    total /= PI ** (arb(1) / 4)
    # Gamma(1/4,u) <= u^(-3/4) exp(-u) for u>0. Bound n>=end by
    # its value in the polynomial factors, then integrate the Gaussian.
    u = z * end ** 2
    tail = u ** (-arb(3) / 4) * (-u).exp() / (
        PI ** (arb(1) / 4) * arb(end).sqrt() * 2 * z * end)
    assert tail < RADIUS
    return total + arb(0, RADIUS)


def factors(primes):
    terms = []
    for k in range(len(primes) + 1):
        for subset in combinations(primes, k):
            j = prod(subset)
            a = (-1) ** k * CHARACTER[j]
            terms.append((arb(j).log(), a / arb(j).sqrt()))
    return terms


def enclose(mesh, mass, primes):
    q = prod(primes)
    terms = factors(primes)
    norm = sum(abs(a) for _, a in terms)
    upper = ceil(float(LOG_D + arb(q).log())) + 2
    # Outside [exp(-2),exp(upper)] every primitive term has a small
    # argument <= exp(-2), on the right after reflection.
    assert arb(upper) >= LOG_D + arb(q).log() + 2
    assert norm < 5
    # For the derivative with respect to log x, |G''| <= 10 d^(1/4).
    # This bounds both mesh interpolation errors (including roundoff at
    # knots) and interpolation of H between integration points.
    curvature = 10 * ROOT.sqrt() * norm
    cell_error = curvature / (7 * STEP ** 2)
    pos_lower = pos_upper = neg_lower = neg_upper = arb(0)
    previous = None
    zero = arb(0)
    for k in range(LOW * STEP, upper * STEP + 1):
        v = arb(k) / STEP
        current = sum(a * interpolate(mesh, v - shift) for shift, a in terms)
        if previous is not None:
            mean = (previous + current) / 2
            pos_lower += mean.max(zero)
            pos_upper += (previous.max(zero) + current.max(zero)) / 2
            neg_lower += (-mean).max(zero)
            neg_upper += ((-previous).max(zero) + (-current).max(zero)) / 2
        previous = current
    error = 2 * (upper - LOW) * cell_error + arb("1e-55")
    positive = (pos_lower / STEP - error).union(pos_upper / STEP + error)
    negative = (neg_lower / STEP - error).union(neg_upper / STEP + error)
    signed = sum(a for _, a in terms) * mass
    assert (positive - negative).overlaps(signed)
    assert positive > 0 and signed > 0
    return 1 - signed / positive


def rough_sum():
    z = int((LOG_D ** 2).floor().unique_fmpz())
    primes = [n for n in range(2, z + 1) if fmpz(n).is_prime()]
    q = fmpz(prod(primes))
    total = 0
    for n in range(1, 368):
        if q.gcd(n) == 1:
            total += CHARACTER[n]
        if n < 331:
            assert total >= 0
        if n == 331:
            assert total == -1
        if 331 <= n < 367:
            assert total <= 0
    assert z == 215 and len(primes) == 47 and total == 1
    print("All 47 primes up to 215 removed: first deficit 331 (-1), first recovery 367 (+1).")


def census():
    primes = [p for p in range(2, 40001) if fmpz(p).is_prime()]
    outcomes = [0, 0, 0]
    for m in range(1, 1000, 2):
        d = fmpz(m*m + 4)
        if d.moebius_mu() == 0:
            continue
        z = int((arb(d).log() ** 2).floor().unique_fmpz())
        assert z*z < 40000
        total = 1
        state = 0
        for p in primes:
            if p <= z:
                continue
            if p > z*z:
                break
            total += int(fmpz(p).jacobi(d))
            if total < 0:
                state = 1
            if state == 1 and total > 0:
                state = 2
                break
        outcomes[state] += 1
    assert outcomes == [7, 12, 425]
    print("444 squarefree fields, odd m <= 999, through z^2: 7 no deficit, 12 deficit only, 425 both signs in order.")


def main():
    assert D == 1543 ** 2 + 4 and fmpz(D).is_prime()
    mesh = build_mesh()
    mass = central_mass()
    assert arb("0.00594") < mass and mass < arb("0.00596")
    for q, lo, hi in [(1, "-0.145", "-0.144"), (30, "0.229", "0.231")]:
        value = sum(CHARACTER[n] * (-PI * (arb(n) / 10) ** 2).exp()
                    for n in range(1, 129) if fmpz(n).gcd(q) == 1) / arb(10).sqrt()
        value += arb(0, RADIUS)
        assert arb(lo) < value and value < arb(hi)
    for primes, lo, hi in [
        ((), "0.9918", "0.9927"),
        ((2, 3, 5), "0.9845", "0.9859"),
    ]:
        ratio = enclose(mesh, mass, primes)
        assert arb(lo) < ratio and ratio < arb(hi), ratio
        print(f"q={prod(primes)}: full negative/positive mass in ({lo}, {hi}).")
    rough_sum()
    census()


if __name__ == "__main__":
    main()
