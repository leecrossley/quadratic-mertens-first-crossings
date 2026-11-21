"""Certify the minimum positive logarithmic area on finite Yokoi patterns."""
from itertools import product
from math import isqrt

from flint import arb, ctx


def primes_below(limit):
    return [p for p in range(2, limit)
            if all(p % k for k in range(2, isqrt(p) + 1))]


def options(p):
    if p == 2:
        return (-1,)
    return (-1, 0, 1) if p % 4 == 1 else (-1, 1)


def local_events(p, signs, limit):
    events = []
    for sign in signs:
        q = p * p if sign == -1 else p
        multiplicity = 2 if sign == 1 else 1
        if q < limit:
            events.append((q, multiplicity * (arb(q) / (q - 1)).log()))
        else:
            events.append(None)
    return events


def minimum_area(limit, direct_check):
    primes = primes_below(limit)
    choices = [local_events(p, options(p), limit) for p in primes]
    log_t = {t: arb(t).log() for t in range(2, limit + 1)}
    log_log = {t: u.log() for t, u in log_t.items()}
    left, right = log_t[2], log_t[limit]
    integral_log_log = right * (log_log[limit] - 1) - left * (log_log[2] - 1)
    best = None
    count = 0
    for pattern in product(*choices):
        jumps = sorted(event for event in pattern if event is not None)
        height = arb(0)
        log_c = None
        integral_jumps = arb(0)
        for q, increment in jumps:
            cap = height - log_log[q]
            log_c = cap if log_c is None else log_c.min(cap)
            integral_jumps += increment * (right - log_t[q])
            height += increment
        cap = height - log_log[limit]
        log_c = cap if log_c is None else log_c.min(cap)
        area = integral_jumps - (right - left) * log_c - integral_log_log
        if direct_check:
            # A separate integration uses the product on each actual window.
            prev, height, total = 2, arb(0), arb(0)
            for q, increment in jumps + [(limit, arb(0))]:
                a, b = log_t[prev], log_t[q]
                total += (b-a)*(height-log_c+1) - b*log_log[q] + a*log_log[prev]
                height += increment
                prev = q
            assert total.overlaps(area)
        best = area if best is None else best.min(area)
        count += 1
    return best, count


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Enable assertions')
    ctx.prec = 176
    previous = arb(0)
    print('L patterns lower upper (certified minimum A_L)')
    for L in (3, 7, 13, 23, 37, 43):
        value, count = minimum_area(L, direct_check=L <= 37)
        assert value > previous
        previous = value
        unit = 10**10
        floor = int((value * unit).floor().unique_fmpz())
        assert arb(floor)/unit < value < arb(floor+1)/unit
        print(L, count, f'{floor//unit}.{floor%unit:010}', f'{(floor+1)//unit}.{(floor+1)%unit:010}')
