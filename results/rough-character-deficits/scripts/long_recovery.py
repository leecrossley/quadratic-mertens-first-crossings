"""Check every prefix of the count with 43 retained, using packed periodic sets."""
from math import gcd, isqrt, prod

if not __debug__:
    raise SystemExit("Run with assertions enabled.")

D = 2_380_853
BLOCK = 1 << 18
FIRST = 48221
POSITIVE = 137_705_720_539
LEVEL_19 = 137_705_727_787


def prime_factors(n):
    factors = []
    k = 2
    while k * k <= n:
        if n % k == 0:
            factors.append(k)
            while n % k == 0:
                n //= k
        k += 1
    if n > 1:
        factors.append(n)
    return factors


class Cycle:
    """A byte-aligned period with enough repeated padding for one block."""

    def __init__(self, flags):
        period = len(flags)
        self.period = period // gcd(8, period)
        packed = bytearray(self.period)
        for i in range(self.period * 8):
            if flags[i % period]:
                packed[i // 8] |= 1 << (i % 8)
        repeats = (BLOCK // 8 + self.period - 1) // self.period
        self.padded = memoryview(packed * (1 + repeats))

    def block(self, start):
        byte = (start // 8) % self.period
        return int.from_bytes(self.padded[byte:byte + BLOCK // 8], "little")


def squares_by_generator():
    assert all(D % i for i in range(2, isqrt(D) + 1))
    factors = prime_factors(D - 1)
    generator = next(a for a in range(2, D) if all(pow(a, (D - 1) // p, D) != 1 for p in factors))
    step = pow(generator, 2, D)
    flags = bytearray(D)
    value = 1
    for _ in range((D - 1) // 2):
        flags[value] = 1
        value = value * step % D
    assert value == 1 and sum(flags) == (D - 1) // 2
    return flags


def wheels(deleted):
    groups = [[]]
    period = 1
    for p in deleted:
        if period * p > 800_000:
            groups.append([])
            period = 1
        groups[-1].append(p)
        period *= p
    cycles = []
    for group in groups:
        size = prod(group)
        flags = bytearray([1]) * size
        for p in group:
            flags[::p] = bytes(size // p)
        cycles.append(Cycle(flags))
    return cycles


def sweep():
    square = squares_by_generator()
    eligible = [p for p in range(2, 216) if all(p % i for i in range(2, isqrt(p) + 1))]
    deleted = [p for p in eligible if not square[p] and p != 43]
    assert len(deleted) == 30 and not square[43]
    filters = wheels(deleted)
    residues = Cycle(square)
    events = []
    total = 0

    def visit(start, width, up, down):
        nonlocal total
        rises, falls = up.bit_count(), down.bit_count()
        # These bounds hold for every prefix, regardless of bit order.
        if len(events) == 0:
            can_skip = total - falls >= 0
        else:
            target = 1 if len(events) == 1 else 19
            can_skip = total + rises < target
        if can_skip:
            total += rises - falls
            return
        if width == 1:
            total += rises - falls
            events.append((start, total))
            return
        half = width // 2
        mask = (1 << half) - 1
        visit(start, half, up & mask, down & mask)
        if len(events) < 3:
            visit(start + half, half, up >> half, down >> half)

    whole = (1 << BLOCK) - 1
    for start in range(0, LEVEL_19 + 1, BLOCK):
        alive = whole
        for wheel in filters:
            alive &= wheel.block(start)
        # The primitive character vanishes at every multiple of D.
        for n in range((-start) % D, BLOCK, D):
            alive &= ~(1 << n)
        if start + BLOCK > LEVEL_19 + 1:
            alive &= (1 << (LEVEL_19 + 1 - start)) - 1
        up = alive & residues.block(start)
        visit(start, BLOCK, up, alive ^ up)
        if len(events) == 3:
            break
    assert events == [(FIRST, -1), (POSITIVE, 1), (LEVEL_19, 19)], events
    print("With 43 retained: first -1 at 48221, next +1 at 137705720539, first subsequent +19 at 137705727787.")


if __name__ == "__main__":
    sweep()
