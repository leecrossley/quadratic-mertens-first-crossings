"""Exact finite checks for the near-central zero tests. Uses the standard library."""
from fractions import Fraction
from itertools import product


def check_six_moments():
    signs = (1, -1, 1, -1, 1, -1)
    size = len(signs)
    coefficients = [
        sum(signs[i] * signs[j] for i in range(size) for j in range(size)
            if abs(i-j) == k)
        for k in range(size)
    ]
    assert coefficients == [6, -10, 8, -6, 4, -2]
    error = Fraction(1, 100)
    upper = [Fraction(5, 2) + error, 1-error, error, 1-error, error, -error]
    via_square = sum(signs[i] * signs[j] * upper[abs(i-j)]
                     for i in range(size) for j in range(size))
    assert via_square == sum(c*m for c, m in zip(coefficients, upper)) == Fraction(-16, 25)
    assert via_square < Fraction(-1, 2)
    print("Six Fourier coefficients:", *coefficients)
    print("Worst permitted square with errors of 1/100:", via_square)


def check_conflict_graphs():
    points = tuple(range(0, 32, 4))
    centers = (3, 4, 5, 8, 11, 16, 23, 29)
    cardinalities = [bin(mask).count("1") for mask in range(1 << len(points))]
    checks = 0
    for flags in product((False, True), repeat=len(centers)):
        forbidden = [c for c, active in zip(centers, flags) if active]
        # Radius one. Three centers can cover the same unsigned difference.
        rows = []
        for x in points:
            row = sum(1 << j for j, y in enumerate(points)
                      if x != y and any(abs(abs(x-y)-c) <= 1 for c in forbidden))
            rows.append(row)
        largest_independent = [0] * (1 << len(points))
        for vertices in range(1, 1 << len(points)):
            first = (vertices & -vertices).bit_length() - 1
            others = vertices ^ (1 << first)
            largest_independent[vertices] = max(
                largest_independent[others],
                1 + largest_independent[others & ~rows[first]],
            )
            degree = max(cardinalities[vertices & row] for j, row in enumerate(rows)
                         if vertices & (1 << j))
            assert degree <= 2 * len(forbidden)
            assert cardinalities[vertices] <= (degree+1) * largest_independent[vertices]
            checks += 1
    print(f"Checked degree and independent-set bounds for {checks:,} finite graphs with inclusive endpoints.")


def check_grid_at_the_center():
    # Coordinates in half-units, with a repeated coordinate. The grid is Z.
    points = (0, 0, 1, 2, 3, 4, 5)
    pairs = [[4 * int((x-y) % 2 == 0) + int(x == y) for y in points]
             for x in points]  # twice the kernel
    count = 0
    for signs in product((-1, 0, 1), repeat=len(points)):
        form = sum(c*d*pairs[i][j] for i, c in enumerate(signs) for j, d in enumerate(signs))
        coset_mass = sum(sum(c for x, c in zip(points, signs) if x % 2 == r)**2
                         for r in (0, 1))
        atom_mass = sum(sum(c for x, c in zip(points, signs) if x == r)**2 for r in set(points))
        assert form == 4*coset_mass + atom_mass and form >= 0
        count += 1
    print(f"Checked the double lattice and its half-unit central bias on {count:,} signed vectors.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run with assertions enabled.")
    check_six_moments()
    check_conflict_graphs()
    check_grid_at_the_center()
