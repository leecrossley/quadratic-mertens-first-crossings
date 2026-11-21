"""Exact finite checks of the local laws, the cutoff identity and the census summary."""

import csv
from collections import Counter
from fractions import Fraction
from math import isqrt


def check_identity(p, sign, twice_x):
    # Work at half-integers so both sides of each jump are checked exactly.
    ideal = Fraction(1)
    if sign == -1:
        if 2*p*p <= twice_x:
            ideal = Fraction(p*p, p*p-1)
    elif 2*p <= twice_x:
        ideal = Fraction(p, p-1)**(1+sign)
    decomposed = Fraction(1)
    if 2*p <= twice_x:
        decomposed = Fraction(p, p-1) * Fraction(p, p-sign)
        if sign == -1 and 2*p*p > twice_x:
            decomposed *= Fraction(p*p-1, p*p)
    mandatory = Fraction(p*p, p*p-1) if 2*p*p <= twice_x else Fraction(1)
    if ideal != decomposed or ideal < mandatory:
        raise ArithmeticError("Local product identity or lower bound failed")


def local_checks():
    comparisons = classes = 0
    for p in range(2, 48):
        if any(p % j == 0 for j in range(2, isqrt(p)+1)):
            continue
        for sign in (-1, 0, 1):
            for twice_x in (2*p-1, 2*p, 2*p+1, 2*p*p-1, 2*p*p, 2*p*p+1):
                check_identity(p, sign, twice_x)
                comparisons += 1
        if p == 2:
            continue
        squares = {t*t % p for t in range(1, p)}
        counts = Counter()
        for m in range(p*p):
            d = m*m + 4
            if d % (p*p):
                sign = 0 if d % p == 0 else (1 if d % p in squares else -1)
                counts[sign] += 1
        roots = 2 if p % 4 == 1 else 0
        if sum(counts.values()) != p*p-roots or counts[0] != roots*(p-1):
            raise ArithmeticError("Unexpected squarefree local count")
        for sign in (-1, 1):
            if 2*counts[sign] != p*(p-roots-sign):
                raise ArithmeticError("Unexpected split or inert count")
        classes += sum(counts.values())
    print(f"Exact cutoff identities and quadratic lower factors: {comparisons} comparisons.")
    print(f"Local laws: {classes} admissible residue classes counted at odd primes through 47.")


def census_summary():
    with open("evidence/census.tsv", newline="") as table:
        rows = list(csv.DictReader(table, delimiter="\t"))
    if len(rows) != 45 or len({r["d"] for r in rows}) != 45:
        raise ArithmeticError("Unexpected census count")
    top = max(rows, key=lambda r: Fraction(r["boundary_upper"]))
    if top["d"] != "9413" or any(Fraction(r["boundary_upper"]) >= 37 for r in rows if r != top):
        raise ArithmeticError("Unexpected extremal field")
    if not 525 < Fraction(top["boundary_lower"]) < Fraction(top["boundary_upper"]) < 526:
        raise ArithmeticError("Extremal enclosure does not separate the entire census")
    print("All 45 squarefree Yokoi discriminants through 10000 have a first crossing below 526.")
    print(f'The largest is d={top["d"]}: {top["boundary_lower"]} < S < {top["boundary_upper"]}.')


if __name__ == "__main__":
    local_checks()
    census_summary()
