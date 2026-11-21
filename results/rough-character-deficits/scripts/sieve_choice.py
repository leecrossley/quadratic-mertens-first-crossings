"""All small-prime deletions for the quadratic character of conductor 2380853."""
from math import gcd, prod

from flint import arb, fmpz

from verify import D, LOG_D, ROOT, base_value, central_mass

if not __debug__:
    raise SystemExit("Run with assertions enabled.")

STEP = 2048
UNIT = 1 << 46


def bounded_integer(value):
    """An integer multiple of 1/UNIT with certified absolute error."""
    chosen = round(float(value) * UNIT)
    assert abs(value - arb(chosen) / UNIT) < arb(2) / UNIT
    return chosen


def primes_and_counts():
    assert D == 1543 ** 2 + 4 and fmpz(D).is_prime()
    z = int((LOG_D ** 2).floor().unique_fmpz())
    primes = [p for p in range(2, z + 1) if fmpz(p).is_prime()]
    inert = [p for p in primes if fmpz(p).jacobi(D) == -1]
    assert (z, len(primes), len(inert)) == (215, 47, 31)
    for deleted, expected in [(inert, (49937, 49943)), (primes, (331, 367))]:
        modulus = prod(deleted)
        total = 0
        first = None
        for n in range(1, expected[1] + 1):
            if gcd(n, modulus) == 1:
                total += int(fmpz(n).jacobi(D))
            if total < 0 and first is None:
                first = n
            if first is not None and total > 0:
                break
        assert (first, n, total) == (*expected, 1)
    running = maximum = 0
    for n in range(1, D):
        running += int(fmpz(n).jacobi(D))
        maximum = max(maximum, abs(running))
    assert running == 0 and maximum == 1068
    print("47 eligible primes, 31 inert. The latest first negative is 49937. This sieve first recovers at 49943.")
    print("Maximum absolute primitive partial sum over one period: 1068.")
    return inert


def primitive_grid():
    low = -2 * STEP
    high = int(((LOG_D + 2) * STEP).ceil().unique_fmpz())
    data = []
    for k in range(low, high + 1):
        t = arb(k) / STEP
        u = LOG_D - t if 2 * t > LOG_D else t
        assert u <= LOG_D / 2
        value = base_value(u)
        if k in (low, high):
            assert abs(value) < arb(1) / UNIT
            data.append(0)
        else:
            data.append(bounded_integer(value))
    return low, data


def zero_and_recovery(low, grid):
    # Reciprocity makes the centred cosine transform real. The bounds below
    # cover trapezoidal error, outward-rounded samples and both Gaussian tails.
    err = 42 * ROOT.sqrt() / (8 * STEP ** 2) + arb(100) / UNIT + arb("1e-60")
    for height, sign in [("0.028", 1), ("0.030", -1)]:
        t = arb(height)
        area = sum((v * (t * (arb(low + i) / STEP - LOG_D / 2)).cos()
                    for i, v in enumerate(grid)), arb(0)) / (STEP * UNIT)
        assert sign * area > err
    tau_min = arb(3).log()
    h = 6 * LOG_D
    assert arb(".030") * h < arb.pi()
    assert arb(".030") * arb(49937).log() < arb(1) / 3
    # sin(t)/t >= 1-t^2/6 > .98 on the initial interval.
    v = arb(2).log()
    # Exact integral of (tau-u) exp(-u/2) from 0 to log 2, divided by tau;
    # it is smallest at tau = log 3.
    initial = arb(".98") * (2 * (1 - (-v / 2).exp())
              - (4 - (2 * v + 4) * (-v / 2).exp()) / tau_min)
    bad = arb(1) / 1000 * h ** 2 / (2 * LOG_D ** 2)
    # The full deletion is already checked. Every proper subset has <=46 primes.
    tail = 2 * 1068 * (1 << 46) / (arb(".028") * D ** 3)
    assert initial > arb(".40") and bad < arb(".019")
    assert tail < arb(".401") and (initial - bad) * tau_min > tail
    assert arb(49937).sqrt() < 1000 * LOG_D
    assert arb(331).log() * arb(367).sqrt() < 1000 * LOG_D ** 2
    scale = arb(48221).log() / (1000 * LOG_D ** 2)
    assert 18 < scale * arb(137705720539).sqrt() and scale * arb(137705727787).sqrt() < 19
    print("Opposite signs of the real completed transform at 0.028 and 0.030.")
    print("Every one of 140737488355328 sieves meets both 1/1000 thresholds in order by d^6.")


def apply_prime(data, p):
    shift = arb(p).log() * STEP
    jump = int(shift.floor().unique_fmpz())
    part = shift - jump
    chance = 1 / (1 + arb(p).sqrt())
    near = bounded_integer(chance * (1 - part))
    far = bounded_integer(chance * part)
    stay = UNIT - near - far
    assert min(near, far, stay) >= 0
    result = [0] * (len(data) + jump + 1)
    for i, value in enumerate(data):
        result[i] += stay * value
        result[i + jump] += near * value
        result[i + jump + 1] += far * value
    result = [(v + UNIT // 2) // UNIT for v in result]
    assert max(map(abs, result)) < 21 * UNIT
    return result


def optimal_gaussian_mass(grid, inert):
    assert max(map(abs, grid)) < 21 * UNIT
    values = grid
    for p in inert:
        values = apply_prime(values, p)
    assert values[0] == values[-1] == 0 and len(values) < 250 * STEP
    # Lower and upper integrals of the positive part on each affine cell.
    lower = arb(sum(max(0, a + b) for a, b in zip(values, values[1:]))) / (2 * STEP * UNIT)
    upper = arb(sum(max(0, v) for v in values)) / (STEP * UNIT)
    chance_sum = sum(1 / (1 + arb(p).sqrt()) for p in inert)
    error = 40 * ROOT.sqrt() * (1 + chance_sum) / (8 * STEP ** 2)
    error += arb(250) * (3 + len(inert) * 169) / UNIT + arb("1e-60")
    positive = (lower - error).union(upper + error)
    signed = central_mass()
    assert positive > 0 and signed > 0
    ratio = 1 - signed / positive
    assert arb(".912") < ratio and ratio < arb(".913"), ratio
    print("The minimum full Gaussian negative/positive mass ratio lies strictly between 0.912 and 0.913.")


def main():
    inert = primes_and_counts()
    low, grid = primitive_grid()
    zero_and_recovery(low, grid)
    optimal_gaussian_mass(grid, inert)


if __name__ == "__main__":
    main()
