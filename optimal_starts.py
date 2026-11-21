"""Rigorous comparisons for optimal decreasing-weight starting points in Yokoi fields."""
import argparse
from dataclasses import dataclass
from fractions import Fraction
from heapq import merge
from math import isqrt
from pathlib import Path

from flint import arb, ctx, fmpz


@dataclass(frozen=True)
class Field:
    m: int
    class_number: int
    first_left: int
    first_right: int
    minimum_norm: int
    horizon: int
    start_lower: str
    start_upper: str

    @property
    def d(self):
        return self.m * self.m + 4


FIELDS = (
    Field(97, 3, 509, 547, 2017, 4_000_000, '337.87434', '337.87436'),
    Field(1543, 29, 142993, 143063, 154877, 125_000_000, '137123.79815', '137123.79818'),
)


def rational(value):
    f = Fraction(value)
    return arb(f.numerator) / f.denominator


def small_primes(limit):
    marks = bytearray([1]) * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if marks[p]:
            marks[p*p::p] = bytes((limit - p*p)//p + 1)
    return [p for p in range(2, limit+1) if marks[p]]


def primes(limit):
    small = small_primes(isqrt(limit))
    block = 1 << 19
    for start in range(2, limit+1, block):
        stop = min(limit+1, start+block)
        marks = bytearray([1]) * (stop-start)
        for p in small:
            if p*p >= stop:
                break
            first = max(p*p, ((start+p-1)//p)*p)
            if first < stop:
                marks[first-start::p] = bytes((stop-1-first)//p + 1)
        for i, flag in enumerate(marks):
            if flag:
                yield start+i


def norm_jumps(d, limit):
    def degree_one():
        for p in primes(limit):
            sign = int(fmpz(p).jacobi(d))
            if sign >= 0:
                yield p, 1+sign
    inert = ((p*p, 1) for p in small_primes(isqrt(limit)) if int(fmpz(p).jacobi(d)) == -1)
    return merge(degree_one(), inert)


def residue_from_class(m, h):
    root = arb(m*m+4).sqrt()
    return 2 * h * ((m+root)/2).log() / root


def theta_check(m, h):
    d = m*m+4
    assert all(a == 1 for _, a in fmpz(d).factor())
    root = arb(d).sqrt()
    pi_over_d = arb.pi()/d
    total = arb(0)
    for n in range(1, isqrt(25*d)+1):
        sign = int(fmpz(n).jacobi(d))
        if sign:
            a = pi_over_d*(n*n)
            total += sign * (a.sqrt().erfc()/n + a.expint(1)/root)
    enclosed = total + arb(0, 3*(-25*arb.pi()).exp())
    assert (enclosed/residue_from_class(m,1)).unique_fmpz() == h
    assert enclosed.contains(residue_from_class(m,h))


class Primitive:
    def __init__(self, residue):
        self.constant = 1 - arb.const_euler() - residue.log()
        self.product = arb(0)
        self.moment = arb(0)

    def at_log(self, u):
        return u*(self.constant + self.product - u.log()) - self.moment

    def jump(self, q, count, u):
        delta = count * (arb(1)/(q-1)).log1p()
        self.product += delta
        self.moment += u*delta


def values_at(d, residue, points):
    points = sorted(set(Fraction(x) for x in points))
    itr = iter(norm_jumps(d, int(points[-1])))
    jump = next(itr, None)
    cumulative = Primitive(residue)
    results = {}
    for point in points:
        while jump and jump[0] <= point:
            q, count = jump
            cumulative.jump(q, count, arb(q).log())
            jump = next(itr, None)
        results[point] = cumulative.at_log(rational(point).log())
    return results


def certify_threshold(field):
    d = field.d
    theta_check(field.m, field.class_number)
    residue = residue_from_class(field.m, field.class_number)
    q_star = field.minimum_norm
    upper = Fraction(field.start_upper)
    lower = Fraction(field.start_lower)
    vals = values_at(d, residue, [lower, upper, q_star])
    minimum = vals[q_star]
    assert vals[lower] < minimum < vals[upper]
    cumulative = Primitive(residue)
    previous = 2
    found_crossing = False
    visits = 0
    for q, count in norm_jumps(d, field.horizon):
        visits += 1
        u = arb(q).log()
        if not found_crossing:
            error_before = cumulative.constant - 1 + cumulative.product - u.log()
            if q == field.first_right:
                assert previous == field.first_left and error_before < 0
                log_crossing = (cumulative.constant - 1 + cumulative.product).exp()
                crossing = log_crossing.exp()
                assert crossing > previous and crossing < q and crossing > rational(upper)
                assert cumulative.at_log(log_crossing) > minimum
                found_crossing = True
            else:
                assert error_before > 0
        if found_crossing:
            value = cumulative.at_log(u)
            if q == q_star:
                assert value.overlaps(minimum)
            else:
                assert value > minimum
        cumulative.jump(q, count, u)
        previous = q
    assert found_crossing
    end = arb(field.horizon)
    margin = cumulative.at_log(end.log()) - minimum
    zero_bound = 9 + 3*arb(d).log()
    tail_loss = 2*zero_bound/(end.sqrt()*end.log())
    assert margin > tail_loss
    print(f'd={d}, h={field.class_number}, {visits} norm jumps through {field.horizon}; minimising endpoint {q_star}.')
    print(f'First crossing in ({field.first_left},{field.first_right}); {field.start_lower} < earliest-start infimum < {field.start_upper}.')
    print(f'Area above the minimum at cutoff {margin.str(10)}; certified maximum future loss {tail_loss.str(10)}.')
    if field.m == 1543:
        exponent_low = rational(lower).log()/arb(d).log()
        exponent_high = rational(upper).log()/arb(d).log()
        assert exponent_low > rational('0.80560267') and exponent_high < rational('0.80560269')
        assert arb(d)**4 < rational(lower)**5
        print('Every start through d^(4/5) fails for every decreasing weight. Worst exponent lies in (0.80560267,0.80560269).')


def census_record(path):
    rows = [line.split() for line in path.read_text().splitlines()[1:]]
    assert len(rows) == 8950 and int(rows[-1][1]) == 400040005
    exceptions = [int(d) for _,d,*_,hi in rows if Fraction(hi)**5 >= int(d)**4]
    assert exceptions == [5, 2380853]
    y = Fraction(18,5)
    assert y**5 < 5**4
    vals = values_at(5, residue_from_class(1,1), [y,4])
    assert vals[4] < vals[y]
    print('8,948 certified first crossings before d^(4/5); d=5 has a negative average from 18/5 to 4.')
    print('The unique largest optimal-start exponent in this finite census belongs to d=2380853.')


def largest_absolute():
    d, m, h = 98346893, 9917, 196
    start, end = 1105000, 20886007
    theta_check(m,h)
    vals = values_at(d, residue_from_class(m,h), [start,end])
    result = vals[end] - vals[start]
    assert result < 0
    print(f'd={d}, start {start}, end {end}: signed log area {result.str(12)}.')


def main():
    if not __debug__:
        raise SystemExit('Enable Python assertions')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--census', type=Path, default=Path(__file__).with_name('crossings.txt'))
    parser.add_argument('--check', choices=['all','small','worst','largest','census'], default='all')
    args = parser.parse_args()
    ctx.prec = 160
    if args.check in ('all','small'):
        certify_threshold(FIELDS[0])
    if args.check in ('all','worst'):
        certify_threshold(FIELDS[1])
    if args.check in ('all','largest'):
        largest_absolute()
    if args.check in ('all','census'):
        census_record(args.census)


if __name__ == '__main__':
    main()
