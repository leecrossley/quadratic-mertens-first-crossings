"""Certify an explicit lower proportion in the squarefree Yokoi family."""

from fractions import Fraction
from verify import euler_constant, primes_to, transcend


def good_prefix_mass():
    # Each pair gives the Euler product so far and its probability.
    states = [(Fraction(2, 3), Fraction(1))]
    for p in primes_to(31):
        if p == 2:
            continue
        roots = 2 if p % 4 == 1 else 0
        allowed = p*p - roots
        factors = []
        for s in (-1, 1):
            probability = Fraction(p * (p - roots - s), 2 * allowed)
            factors.append((Fraction(p, p - s), probability))
        if roots:
            factors.append((Fraction(1), Fraction(roots * (p - 1), allowed)))
        states = [(value * factor, mass * probability)
                  for value, mass in states for factor, probability in factors]
    if sum(mass for _, mass in states) != 1:
        raise ArithmeticError("Finite model has incorrect total mass")
    low, high = Fraction(59, 100), Fraction(7, 10)
    return len(states), sum(mass for value, mass in states if low <= value <= high)


def check():
    count, mass = good_prefix_mass()
    if count != 5184 or mass != Fraction(116900317682048, 964766068682647):
        raise ArithmeticError("Prefix probability disagrees with the exact value")
    if not mass > Fraction(3, 25):
        raise ArithmeticError("Prefix probability bound failed")
    variance_bound = sum(Fraction(1, (p - 1)**2) for p in primes_to(4000) if p > 31)
    variance_bound += Fraction(1, 3999)  # Integral majorant for all integers above 4000.
    if not variance_bound < Fraction(1, 150):
        raise ArithmeticError("Tail variance comparison failed")

    radius = Fraction(7, 50)
    gamma_lo, gamma_hi = euler_constant()
    u, v = Fraction(401, 200), Fraction(299, 100)
    g_upper_at_v = transcend(-gamma_lo, "exp", True) / transcend(v, "ln", False)
    g_lower_at_u = transcend(-gamma_hi, "exp", False) / transcend(u, "ln", True)
    if not g_upper_at_v < Fraction(59, 100) * transcend(-radius, "exp", False):
        raise ArithmeticError("Lower L-value inclusion failed")
    if not Fraction(7, 10) * transcend(radius, "exp", True) < g_lower_at_u:
        raise ArithmeticError("Upper L-value inclusion failed")

    nu = Fraction(1, 150)
    tail_probability = 1 - nu / (radius - 2 * nu)**2
    if tail_probability != Fraction(211, 361) or not mass * tail_probability > Fraction(7, 100):
        raise ArithmeticError("Lower density comparison failed")
    print(f"Yokoi family: {count} finite Euler-factor configurations; "
          "good prefix mass > 3/25; tail variance < 1/150.")
    print("Relative proportion with 2.005 < first boundary <= 2.99 exceeds 7/100.")


if __name__ == "__main__":
    check()
