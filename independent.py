"""Second interval check using primality tests, tangents and Dirichlet L series."""
from flint import acb_series, arb, ctx, dirichlet_char, fmpz


END = 1_000_000


def prime_data(d):
    by_norm = {}
    psi_jumps = {}
    for p in range(2, END + 1):
        if not fmpz(p).is_prime():
            continue
        chi = -1 if p == 2 else int(fmpz(d).jacobi(p))
        if chi < 0:
            if p*p <= END:
                by_norm[p*p] = 1
        else:
            by_norm[p] = 1 + chi
        power = p
        character_power = chi
        logp = arb(p).log()
        while power <= END:
            psi_jumps[power] = (1 + character_power)*logp
            power *= p
            character_power *= chi
    return by_norm, psi_jumps


def check(d):
    chi = dirichlet_char(d, d-1)
    assert chi(2) == -1 and chi.is_real() and not chi.is_principal()
    series = acb_series([1, 1], prec=2).dirichlet_l(chi)
    l1, lp = series[0].real, series[1].real
    l2 = chi.l(2).real
    mass = 2 + (arb(d)/(16*arb.pi()**2)).log() + 2*lp/l1
    lo, hi = ("0.202","0.204") if d == 5 else ("0.442","0.444")
    assert arb(lo) < mass < arb(hi)
    norms, jumps = prime_data(d)

    psi = arb(0)
    for n in range(2, END + 1):
        if n in jumps:
            psi += jumps[n]
        if n >= 1000:
            delta = 50 if d == 5 else 37
            assert (1000-delta)*(n+1) < 1000*psi < (1000+delta)*n
    constant = arb.const_euler() + l1.log()
    total = (arb(2).zeta()*l2).log()
    terms = {}
    for q, multiplicity in norms.items():
        v = arb(q)
        term = multiplicity*(v/(v-1)).log()
        terms[q] = term
        total += term/v - multiplicity*(v**2/(v**2-1)).log()
    total += arb(0, 4/arb(END)**2)

    def first_gap(a, b):
        y = a.union(b)
        u = y.log()
        moving = y*(total - a.log().expint(1).union(b.log().expint(1)))
        main = constant + u.log()
        w = (1+3*u/2)*moving - (1+u/2)*main
        dw = 1-main/2 + (5+3*u)*moving/2
        return w, dw, y.sqrt()*u*(moving-main)

    if d == 5:
        for k in range(2000, 4000):
            w, dw, _ = first_gap(arb(k)/1000, arb(k+1)/1000)
            if k < 2400:
                assert w < 0
            else:
                assert dw > 0
        left, right = arb(264281618)/10**8, arb(264281620)/10**8
        assert first_gap(left,left)[0] < 0 < first_gap(right,right)[0]
        value = first_gap(left,right)[2]
        assert arb(183894)/10**6 < value < arb(183896)/10**6
        print("d=5, derivative sign and monotonicity isolate the same unique minimiser on [2,4].")

    # The benchmark is concave. On a gap between norms its tangent
    # gives an affine lower bound for F, valid up to both endpoints.
    prefix = used_slope = arb(0)
    count = 0
    margin = arb(1)/5 if d == 5 else arb(1)/40

    def on_gap(a, b):
        u = a.log()
        slope = total - used_slope - u.expint(1)
        left = prefix - constant - u.log() + a*slope
        n = a.sqrt()*u
        if n*left > margin and n*(left + (b-a)*slope) > margin:
            return 1
        middle = (a+b)/2
        assert b-a > arb(1)/1024, (a, b, left)
        return on_gap(a, middle) + on_gap(middle, b)

    a = 4 if d == 5 else 2
    for b in sorted(set(terms) | {END}):
        if b > a:
            count += on_gap(arb(a), arb(b))
        if b in terms:
            prefix += terms[b]
            used_slope += terms[b]/b
        a = b
    # Check the infinite endpoint constants independently as rational targets.
    u = arb(END).log()
    delta = 50 if d == 5 else 37
    assert ((u/(2*arb.pi())+2)*arb(d).log() + u*u/(4*arb.pi())+4) < delta
    assert (arb(2)/3)/(1+8/(3*u)) - arb(delta)/500 - u/1000 - mass > margin
    print(f"d={d}, prime tests and supporting tangents certify all {count} subintervals.")
    print(f"d={d}, Dirichlet L evaluation gives {lo} < inverse-square mass < {hi}.")
    print(f"d={d}, independent Chebyshev and infinite tail inequalities pass.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Enable Python assertions.")
    ctx.prec = 192
    for discriminant in (5,13):
        check(discriminant)
