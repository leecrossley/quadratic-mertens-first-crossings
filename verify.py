"""Certified future Mertens averages for the fields of discriminants 5 and 13."""
from math import isqrt

from flint import arb, ctx


LIMIT = 10**6


def character(d, n):
    v = pow(n, (d-1)//2, d)
    return -1 if v == d-1 else v


def prime_ideal_norms(d):
    sieve = bytearray([1]) * (LIMIT + 1)
    for p in range(2, isqrt(LIMIT) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((LIMIT - p*p)//p + 1)
    norms = []
    for p in range(2, LIMIT + 1):
        if not sieve[p]:
            continue
        chi = character(d, p)
        q, multiplicity = (p*p, 1) if chi < 0 else (p, 1 + chi)
        if q <= LIMIT:
            norms.append((q, multiplicity))
    return sorted(norms)


def finite_averages(d, norms):
    root = arb(d).sqrt()
    residue = 2*((isqrt(d-4) + root)/2).log()/root
    l2 = arb.pi()**2*sum(character(d,a)*a*a for a in range(1,d+1))/(root*d*d)
    constant = arb.const_euler() + residue.log()
    total = (arb.pi()**2*l2/6).log()
    jumps = []
    for q, count in norms:
        x = 1/arb(q)
        jump = -count*(-x).log1p()
        total += x*jump + count*(-x*x).log1p()
        jumps.append((q, jump))
    total += arb(0, 4/arb(LIMIT)**2)
    prefix = slope = arb(0)
    index = 0

    def endpoint(y):
        nonlocal prefix, slope, index
        while index < len(jumps) and jumps[index][0] <= y:
            norm, jump = jumps[index]
            prefix += jump
            slope += jump/norm
            index += 1
        u = arb(y).log()
        return prefix - constant - u.log() + y*(total - slope - u.expint(1))

    def on_first_gap(y):
        u = y.log()
        benchmark = constant + u.log()
        moving = y*(total - u.expint(1))
        normalised = y.sqrt()*u*(moving-benchmark)
        derivative = (1+3*u/2)*moving - (1+u/2)*benchmark
        return normalised, derivative

    if d == 5:
        assert on_first_gap(arb(2))[1] < 0
        left_root, right_root = arb("2.64281618"), arb("2.64281620")
        assert on_first_gap(left_root)[1] < 0 < on_first_gap(right_root)[1]
        for n in range(128, 256):
            a, b = arb(n)/64, arb(n+1)/64
            y = a.union(b)
            u = y.log()
            e1 = b.log().expint(1).union(a.log().expint(1))
            second = 2/u + arb(3)/2 + (4+3*u/2)*y*(total-e1)
            assert second > 0, (a,b)
        root_value = on_first_gap(left_root.union(right_root))[0]
        assert arb("0.183894") < root_value < arb("0.183896")
        print("d=5, unique minimum on [2,4]: 2.64281618 < y < 2.64281620, 0.183894 < normalised value < 0.183896.")
    start, margin = (4, arb(1)/5) if d == 5 else (2, arb(1)/40)
    a = start
    left = endpoint(a)
    intervals = 0
    while a < LIMIT:
        b = min(LIMIT, a + max(1, a//200))
        right = endpoint(b)
        u = arb(a).log()
        defect = (b-a)**2 / (8*arb(a)**2*u)
        normalisation = arb(a).sqrt()*u
        for end in (left, right):
            assert normalisation*(end-defect) > margin, (d, a, b, end, defect)
        a, left = b, right
        intervals += 1
    print(f"d={d}, chord certificate: {intervals} intervals cover [{start},{LIMIT}].")


def check_psi(d, norms):
    start = 1000
    jumps = []
    for q, count in norms:
        power = q
        size = count*arb(q).log()
        while power <= LIMIT:
            jumps.append((power, size))
            power *= q
    jumps.sort(key=lambda item: item[0])
    psi = arb(0)

    allowance = 50 if d == 5 else 37

    def check(x, value):
        assert (1000-allowance)*x < 1000*value < (1000+allowance)*x, (x, value)

    for q, size in jumps:
        if q <= start:
            psi += size
        else:
            check(q, psi)
            psi += size
            check(q, psi)
    initial = sum((v for n, v in jumps if n <= start), arb(0))
    check(start, initial)
    check(LIMIT, psi)
    u = arb(LIMIT).log()
    delta = ((u/(2*arb.pi()) + 2)*arb(d).log() + 2*(u*u/(8*arb.pi()) + 2))/arb(LIMIT).sqrt()
    assert u > 4 and delta < arb(allowance)/1000
    print(f"d={d}, |psi(x)-x| < ({allowance}/1000)x for x >= {start}.")


def tail(d):
    cutoff = 65000
    value = derivative = arb(0)
    partial = largest = 0
    for n in range(1,d+1):
        partial += character(d,n)
        largest = max(largest,abs(partial))
    assert cutoff % d == 0 and partial == 0
    for n in range(1, cutoff + 1):
        chi = character(d,n)
        value += arb(chi)/n
        derivative -= chi*arb(n).log()/n
    value += arb(0, largest/arb(cutoff))
    derivative += arb(0, largest*arb(cutoff).log()/cutoff)
    mass = 2 + arb(d).log() - 2*arb.pi().log() - 4*arb(2).log() + 2*derivative/value
    cap = arb(11)/50 if d == 5 else arb(445)/1000
    assert 0 < mass < cap
    u = arb(LIMIT).log()
    delta = arb(1)/20 if d == 5 else arb(37)/1000
    lower = 2*u/(3*u+8) - 2*delta - u/arb(LIMIT).sqrt() - cap
    denominator = 5 if d == 5 else 40
    assert lower > 1/arb(denominator)
    print(f"d={d}, analytic lower bound > 1/{denominator} from y = {LIMIT} onwards.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Enable Python assertions.")
    ctx.prec = 160
    for discriminant in (5,13):
        data = prime_ideal_norms(discriminant)
        finite_averages(discriminant, data)
        check_psi(discriminant, data)
        tail(discriminant)
