"""Check independent spectral normalizations and the signed integration formula."""
from flint import acb, acb_series, arb, ctx, dirichlet_char
from bound import ceil_log2, parameters


def spectral_constants(d, label):
    chi = dirichlet_char(d, label)
    assert chi.is_primitive() and chi.parity() == 0 and chi.order() == 2
    s = acb_series([0, 1], prec=3)
    f = s.zeta()*s.dirichlet_l(chi)
    assert f[0].contains(0) and not f[1].contains(0)
    c = -(f[2]/f[1]).real
    a = acb_series([1, 1], prec=2).dirichlet_l(chi)
    slope = (a[1]/a[0]).real
    log_d = arb(d).log()
    v = 2*(1 + log_d/2 - arb.pi().log() - 2*arb(2).log() + slope)
    gap = 2 - 2*arb(2).log() + arb.const_euler() + slope
    assert (v-c).overlaps(gap) and max(gap.rad(), c.rad(), v.rad()) < arb(2)**-110
    ell, m, t, n, q, j = parameters(d)
    delta = arb(2)**-256/ell**2
    u = arb(2, 1)*delta
    b = (-u/2).exp()*(c-u-(-(-2*u).expm1()).log())
    assert u < arb(2).log() and v-b < -80
    assert 7*v/j + 3*(-arb(j)/2).exp()*(abs(c)+j+2) + 48 < 50
    print(f"d={d}: independent constants agree, full seed interval and translated error pass")


def one_mode(u, gamma):
    # Compute the original forward integral directly. Independently evaluate the
    # primitive-side integral using the exponential integral and its recurrence.
    r = acb(arb(1)/2, gamma)
    z = r.conjugate()
    def original(t, analytic):
        return (-z*t).exp()*(u/(u+t) + u/(u+t)**2)
    integral = acb.integral(original, 0, 96, abs_tol=arb(2)**-105)
    lhs = (-1+integral)/r
    i1 = (z*u).exp()*(z*u).expint(1)
    i2 = arb(1)/u - z*i1
    i3 = (arb(1)/u**2 - z*i2)/2
    rhs = 1/z + (arb(1)/u - u*i2 - 2*u*i3)/(r*z)
    # The unevaluated original tail is at most 4 exp(-48)/|r|.
    tail = 4*arb(-48).exp()/abs(r)
    assert abs(lhs-rhs) < tail + arb(2)**-100
    assert abs(rhs-1/z) < 7/(u*abs(r)**2)


def main():
    if not __debug__:
        raise SystemExit("Assertions must be enabled.")
    ctx.prec = 384
    for d, label in ((5,4), (8,5), (12,11), (13,12), (17,16), (29,28), (37,36)):
        spectral_constants(d, label)
    for u in (1, 13, 500):
        for gamma in (0, 1, 7):
            one_mode(u, gamma)
    print("9 complex quadratures agree with the signed primitive formula, including the central mode")
    for d in (5, 8, 9413, 5004173, 10**30, 10**153, 10**2000):
        ell, m, t, n, q, j = parameters(d)
        k = ceil_log2(ell)
        assert m <= 2**(11+k) and 6*ell*t < 2**m
        assert 2*t*(2 + arb(d).log()/2 + arb(t+1).log()) < n
        assert 12*arb.pi()*t*ell/q < 1
        # Compare double binary logarithms without constructing the cutoff.
        log_upper = ceil_log2(4*j) + n*ceil_log2(q)
        assert log_upper.bit_length() < 30000*(d.bit_length()-1)
    print("7 exact parameter checks pass, including sizes on both sides of the conductor threshold")
    for d, counts in ((5, (89, 17273, 20970)), (9413, (90, 44400, 119212))):
        ell, m, t, n, q, j = parameters(d)
        new_upper = ceil_log2(4*j) + n*ceil_log2(q)
        old_h = 512 + 128*ceil_log2(d)
        old_exact = 3 + old_h*(32*old_h + 9)*2**(64*old_h + 9)
        old_simple = d**30000
        assert new_upper < 2**287*d**5 < 2**(64*old_h) < old_exact < old_simple
        for value, digits in zip((new_upper, old_exact, old_simple), counts):
            assert 10**(digits-1) <= value < 10**digits
        print(f"d={d}: decimal digits in new upper estimate, earlier exact integer and simplified exponent: "
              f"{counts[0]:,}, {counts[1]:,}, {counts[2]:,}")


if __name__ == "__main__":
    main()
