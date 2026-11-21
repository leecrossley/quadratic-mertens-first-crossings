"""Residue enumeration and a split incomplete-gamma transform for the late field."""
from array import array
from math import isqrt

from flint import acb, arb, ctx

if not __debug__:
    raise SystemExit("Run with assertions enabled.")


def main():
    ctx.prec = 128
    d = 1543 * 1543 + 4
    assert all(d % p for p in range(2, isqrt(d) + 1))
    squares = bytearray(d)
    for n in range(1, (d + 1) // 2):
        squares[n * n % d] = 1
    running = maximum = 0
    prefix = array("h", [0])
    for value in squares[1:]:
        running += 2 * value - 1
        prefix.append(running)
        maximum = max(maximum, abs(running))
    assert running == 0 and maximum == 1068
    cutoff = int((arb(d).log() ** 2).floor().unique_fmpz())
    primes = [n for n in range(2, cutoff + 1) if all(n % k for k in range(2, isqrt(n) + 1))]
    inert = [p for p in primes if squares[p] == 0]
    assert len(inert) == 31 and len(primes) == 47
    for deleted, first, return_at in [(inert, 49937, 49943), (primes, 331, 367)]:
        keep = bytearray([1]) * (return_at + 1)
        for p in deleted:
            keep[p::p] = bytes(return_at // p)
        sums = [0]
        for n in range(1, return_at + 1):
            sums.append(sums[-1] + keep[n] * (2 * squares[n] - 1))
        assert min(sums[:first]) == 0 and sums[first] == -1
        assert max(sums[first:return_at]) == 0 and sums[return_at] == 1
    print("Enumeration of nonzero squares separately verifies both first crossings and the period maximum.")

    # Each deleted inert prime contributes 1+p^(-s). Sum the primitive
    # prefixes at all squarefree divisors, using their exact period.
    deleted = [p for p in inert if p != 43]
    def dilates(bound, first_prime=0):
        answer = prefix[bound % d]
        for i in range(first_prime, len(deleted)):
            p = deleted[i]
            if p > bound:
                break
            answer += dilates(bound // p, i + 1)
        return answer
    for n, expected in [(48220, 0), (48221, -1), (137705720538, 0),
                        (137705720539, 1), (137705727786, 18), (137705727787, 19)]:
        assert dilates(n) == expected
    print("Squarefree divisor sums reproduce the six endpoints of the long recovery.")

    pi = arb.pi()
    z = pi / d
    count = 8000
    u = z * count ** 2
    tail = u ** (-arb(3) / 4) * (-u).exp() / (pi ** (arb(1) / 4) * arb(count).sqrt() * 2 * z * count)
    assert tail < arb("1e-35")
    for t, sign in [("0.02849001", 1), ("0.02849002", -1)]:
        s = acb(arb(1) / 2, arb(t))
        total = acb(0)
        for n in range(1, count + 1):
            term = acb(z * n * n).gamma_upper(s / 2) * acb(n) ** (-s)
            total += term if squares[n] else -term
        phase = acb(0, arb(t) * arb(d).log() / 2).exp()
        real_transform = (phase * acb(pi) ** (-s / 2) * total).real
        assert sign * real_transform > tail
    print("An independent incomplete-gamma sum certifies a zero between 0.02849001 and 0.02849002.")


if __name__ == "__main__":
    main()
