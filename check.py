"""Independent ball-arithmetic checks of the normalization, sign and a worked field."""
from fractions import Fraction
from math import isqrt
from flint import acb_series, arb, ctx, dirichlet_char

from bound import parameters


def check_constants(d, label):
    chi = dirichlet_char(d, label)
    assert chi.is_primitive() and chi.order() == 2 and chi.parity() == 0
    s0 = acb_series([0, 1], prec=3)
    zeta_k = s0.zeta() * s0.dirichlet_l(chi)
    assert zeta_k[0].contains(0) and not zeta_k[1].contains(0)
    c_zero = -(zeta_k[2] / zeta_k[1]).real

    # At 1, remove the pole of zeta. Gamma'(1/2)/Gamma(1/2) = -gamma - 2 log 2.
    slope = acb_series([1, 1], prec=2).dirichlet_l(chi)
    ld = arb(d).log()
    lp = arb.pi().log()
    v = 2 * (1 + ld/2 - lp - 2*arb(2).log() + (slope[1]/slope[0]).real)
    c_one = v/2 - 1 + ld/2 - lp - arb.const_euler()
    assert c_zero.overlaps(c_one) and max(c_zero.rad(), c_one.rad()) < arb(2)**-120
    assert v > 0 and v < 9 + 3*ld and abs(c_zero) < 8 + 2*ld

    h, log_t, log_q, log_n_over_h = parameters(d)
    delta = arb(2)**(-16*h)
    u = arb(2, 1)*delta   # the entire interval [delta, 3 delta]
    assert u > 0 and u < arb(2).log()
    b = (-u/2).exp() * (c_zero - u - (-(-2*u).expm1()).log())
    assert b > 4*h
    assert 16*(2*v + abs(c_one) + 2) + 48 < h

    # Evaluate log₂ log₂ U_* directly as one exact integer.
    e = 3 + h * log_q * (1 << log_n_over_h)
    assert e == 3 + (log_t+5) * (2*h * (1 << (2*log_t)))
    assert e <= (1 << (65*h)) <= d**30000
    print(f"d={d}: constants at 0 and 1 agree, early interval and cutoff pass")


def prime_norms(d, limit):
    # Count the distinct roots of the integral-basis polynomial at each rational prime.
    linear, constant = (-1, (1-d)//4) if d % 4 == 1 else (0, -d//4)
    factors = []
    for p in range(2, limit+1):
        if any(p % j == 0 for j in range(2, isqrt(p)+1)):
            continue
        roots = sum((r*r + linear*r + constant) % p == 0 for r in range(p))
        if roots:
            factors.extend([p]*roots)
        elif p*p <= limit:
            factors.append(p*p)
    return sorted(factors)


def exact_product(norms, x):
    value = Fraction(1)
    for q in norms:
        if q <= x:
            value *= Fraction(q, q-1)
    return arb(value.numerator)/value.denominator


def check_transfer(d, label):
    norms = prime_norms(d, 526)
    residue = dirichlet_char(d, label).l(1).real
    for twice_x in (7, 27, 129, 257, 1053):
        x = arb(twice_x)/2
        cap = twice_x//2
        psi = arb(0)
        a = Fraction(0)
        for q in norms:
            power, j = q, 1
            while power <= cap:
                psi += arb(q).log()
                a += Fraction(1, j*power)
                power, j = power*q, j+1
        lp = exact_product(norms, cap).log()
        scale = x.sqrt()*x.log()
        correction = lp - arb(a.numerator)/a.denominator
        assert correction >= 0 and correction*scale < 48
        e = scale*(lp - arb.const_euler() - residue.log() - x.log().log())
        phi = (psi-x)/x.sqrt()
        assert abs(e-phi) < 496 + 128*arb(d).log()


def worked_field():
    d = 9413
    chi = dirichlet_char(d, d-1)
    assert chi.is_primitive() and chi.order() == 2 and chi.parity() == 0
    c = arb.const_euler().exp() * chi.l(1).real
    norms = prime_norms(d, 526)
    # Before each jump, the left limit is the least product-minus-curve value
    # on the preceding gap. At the jump the product increases.
    for q in sorted(set(norms)):
        assert exact_product(norms, q-1) > c*arb(q).log()
    assert exact_product(norms, 525) > c*arb(525).log()
    product = exact_product(norms, 526)
    assert product < c*arb(526).log()
    root = (product/c).exp()
    assert root > arb(525474356978253)/10**12
    assert root < arb(525474356978254)/10**12
    print("d=9413: 525.474356978253 < first crossing < 525.474356978254")


def main():
    if not __debug__:
        raise SystemExit("Use normal Python mode so that assertions execute.")
    ctx.prec = 192
    for d, label in ((5, 4), (8, 5), (12, 11), (13, 12), (17, 16), (29, 28), (37, 36)):
        check_constants(d, label)
        check_transfer(d, label)
    print("35 nonintegral arguments: prime-power correction and signed transfer pass")
    worked_field()


if __name__ == "__main__":
    main()
