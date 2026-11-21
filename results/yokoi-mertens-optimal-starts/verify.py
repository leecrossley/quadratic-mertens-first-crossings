"""Verify all the real first crossings using the supplied class-cycle file."""
import argparse
from collections import deque
from functools import lru_cache
from math import isqrt
from pathlib import Path

from flint import arb, ctx, fmpz


def primes_up_to(limit):
    marks = bytearray([1]) * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if marks[p]:
            marks[p*p::p] = bytes(1 + (limit-p*p)//p)
    return [p for p in range(2, limit + 1) if marks[p]]


@lru_cache(maxsize=None)
def log_norm(norm):
    return arb(norm).log()


@lru_cache(maxsize=None)
def log_factor(norm):
    return (arb(1)/(norm-1)).log1p()


def first_crossing(d, m, h, primes):
    root_d = arb(d).sqrt()
    residue = 2*h*((m + root_d)/2).log()/root_d
    log_c = arb.const_euler() + residue.log()
    value = arb(0)
    if value < log_c + log_norm(2).log():
        return arb(2), 2, 2, 0
    assert value > log_c + log_norm(2).log()
    inert = deque()
    previous, visited = 2, 0

    # The product is constant up to the limit from below at the next norm.
    def inspect(norm):
        nonlocal previous, visited
        visited += 1
        benchmark = log_c + log_norm(norm).log()
        if value < benchmark:
            crossing = (value-log_c).exp().exp()
            assert crossing > previous and crossing < norm
            return crossing, previous, norm, visited
        assert value > benchmark
        previous = norm
        return None

    for p in primes:
        while inert and inert[0] < p:
            n = inert.popleft()
            result = inspect(n)
            if result:
                return result
            value += log_factor(n)
        sign = int(fmpz(p).jacobi(d))
        if sign == -1:
            if p*p <= primes[-1]:
                inert.append(p*p)
            continue
        assert sign in (0, 1)
        result = inspect(p)
        if result:
            return result
        value += (1+sign)*log_factor(p)
    raise ArithmeticError(f'Prime table exhausted for discriminant {d}')


def digits(x, places):
    scale = 10**places
    n = (x*scale).floor().unique_fmpz()
    assert n is not None and x > arb(n)/scale and x < arb(n+1)/scale
    def fixed(k):
        a,b = divmod(int(k),scale)
        return f'{a}.{b:0{places}d}'
    return fixed(n), fixed(n+1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('classes', type=Path, help='output of class_numbers')
    parser.add_argument('--limit', type=int, default=20001)
    parser.add_argument('--crossings', type=Path, help='save certified endpoints for every field')
    args = parser.parse_args()
    if not __debug__:
        raise SystemExit('Enable Python assertions')
    ctx.prec = 176
    assert 1 <= args.limit <= 20001
    eligible = []
    for m in range(1, args.limit+1, 2):
        d = m*m+4
        if all(e == 1 for _, e in fmpz(d).factor()):
            eligible.append((m,d))
    lines = args.classes.read_text().splitlines()
    assert lines[0] == 'm d h reduced'
    rows = [tuple(map(int, line.split())) for line in lines[1:]]
    assert [(m,d) for m,d,_,_ in rows] == eligible
    primes = primes_up_to(2500000)
    worst = longest = None
    total = boundary = 0
    table = ['m d h window_start window_end windows_examined crossing_lower crossing_upper']
    for m,d,h,count in rows:
        assert 1 <= h <= count
        hit, left, right, windows = first_crossing(d, m, h, primes)
        total += windows
        boundary += int(left == right == 2)
        if args.crossings:
            lo, hi = ('2', '2') if left == right == 2 else digits(hit, 8)
            table.append(f'{m} {d} {h} {left} {right} {windows} {lo} {hi}')
        ratio = hit.log()/arb(d).log()
        if d == 5:
            worst = (ratio, d)
            assert ratio > arb(81)/100
        else:
            assert ratio < arb(81)/100
        if longest is None or hit > longest[0]:
            longest = (hit,d,m,h,left,right,windows)
        elif not hit.is_exact() or not longest[0].is_exact():
            assert hit < longest[0]
    print(f'{len(rows)} squarefree Yokoi discriminants checked from 5 through {rows[-1][1]}')
    print(f'{total} successive norm windows checked; {boundary} fields already strictly below at 2')
    hit,d,m,h,left,right,windows = longest
    lo,hi=digits(hit,8)
    print(f'Largest absolute wait: d={d}={m}^2+4, h={h}, window {windows} [{left}, {right})')
    print(f'{lo} < first crossing < {hi}')
    ratio,d=worst
    lo,hi=digits(ratio,10)
    print(f'Largest log(first crossing)/log(d) occurs at d={d}: {lo} < exponent < {hi}')
    print('Every other field in this finite range has first crossing strictly before d^(81/100)')
    if args.crossings:
        args.crossings.write_text('\n'.join(table) + '\n')


if __name__ == '__main__':
    main()
