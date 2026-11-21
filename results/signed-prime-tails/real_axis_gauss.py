"""Independent sign replay with Gaussian theta quadrature and polynomial interpolation."""
from math import ceil, comb, sqrt

from flint import arb, ctx, fmpq, fmpq_poly


def theta_rule(d):
    n = 64
    residues = bytearray(d)
    for base in range(1, (d+1)//2):
        residues[(base*base) % d] = 1
    rule = [arb.legendre_p_root(n, i, weight=True) for i in range(n)]
    nodes = []
    for interval in range(22):
        for root, weight in rule:
            t = interval+(1+root)/2
            c = arb.pi()*t.exp()/d
            last = max(1, ceil(sqrt(160/float(c))))
            assert last < d and c*last**2 > 150
            value = sum(((2*residues[j]-1)*(-c*j*j).exp() for j in range(1, last+1)), arb(0))
            value += arb(0, (-c*last**2).exp()/(2*c*last))
            nodes.append((t/2, weight*(t/4).exp()*value))
    bound = 22*8*d*d*arb(32).exp()/((2*n+1)*arb(comb(2*n, n))**2) + arb("1e-100")
    assert bound < arb("1e-46")
    return nodes, arb(0, bound)


def kernel(z, centre):
    def chebyshev(t):
        terms = [1, t]
        for _ in range(2, 13):
            terms.append(2*t*terms[-1]-terms[-2])
        return terms

    coeff = chebyshev(2*centre-1)
    values = chebyshev(2*z-1)
    return (1+2*sum(a*b for a, b in zip(coeff[1:], values[1:])))**4


def interpolate(centre):
    degree = 48
    differences = [kernel(fmpq(j, degree), centre) for j in range(degree+1)]
    result, term = fmpq_poly([]), fmpq_poly([1])
    for j in range(degree+1):
        result += term*differences[0]
        differences = [v-u for u, v in zip(differences, differences[1:])]
        term = term*fmpq_poly([-j, degree])/(j+1)
    assert result.degree() == degree and result(fmpq(1, 7)) == kernel(fmpq(1, 7), centre)
    return result


def main():
    if not __debug__:
        raise SystemExit("Enable Python assertions.")
    ctx.prec = 320
    d = 1543**2+4
    assert d == 2380853
    ld, scale = arb(d).log(), arb(3*d).log()
    nodes, enclosure = theta_rule(d)
    a, b = arb(1)/2, arb(3)/2

    def derivative(q):
        assert 0 < q <= b
        den, num = arb(0), arb(0)
        for t, w in nodes:
            ex = (q*t).exp()
            inv = 1/ex
            den += w*(ex+inv)/2
            num += w*t*(ex-inv)/2
        assert den+enclosure > 0
        return (num+enclosure)/(den+enclosure)

    one, two = derivative(a), derivative(b)
    mass = arb("8.423")
    assert one*two < a*b*mass**2
    field_moments = []
    for k in range(1, 50):
        x = arb(k)/16
        q = x/scale
        measured = derivative(q)
        diff = (measured-one)/(a-q) - (measured-two)/(b-q)
        field_moments.append((diff/scale + 2/(3*x))/16)

    # Positive quadrature integrates a degree-48 polynomial exactly.
    rule = [arb.legendre_p_root(25, j, weight=True) for j in range(25)]

    def weight_mass(left, right, centre):
        width = (right-left)/2
        return width*sum((wt*kernel(left+width*(1+r), centre) for r, wt in rule), arb(0))

    ordinary = arb("0.046192")
    assert 2+arb.const_euler()-(4*arb.pi()).log() < ordinary
    min_u = 4*ld
    w = min_u/2
    delta = ((w/(2*arb.pi())+2)*ld + 2*(w*w/(8*arb.pi())+2))*(-w/2).exp()
    excess = (-min_u/2).exp()/min_u.tanh() + 2*delta + 8*(-min_u/6).exp()
    assert excess < arb("0.001")
    for lo, hi, c, sign, target in [
        (4, 10, fmpq(2, 3), -1, "1.3"), (11, 18, fmpq(5, 12), 1, "1.8"),
        (19, 27, fmpq(1, 4), -1, "0.5"), (28, 36, fmpq(1, 6), 1, "0.25"),
    ]:
        coeffs = interpolate(c)
        total = weight_mass(arb(0), arb(1), arb(c))
        assert total > 0 and total.contains(arb(coeffs.integral()(1)))
        mean = sum((arb(v)*t for v, t in zip(coeffs, field_moments)), arb(0))/total
        left, right = (-hi*ld/(16*scale)).exp(), (-lo*ld/(16*scale)).exp()
        outside = (weight_mass(arb(0), left, arb(c)) + weight_mass(right, arb(1), arb(c)))/total
        assert 0 < outside < 1
        bias = arb(2)/3
        err = 8*mass/(3*lo*ld) + ordinary + (bias if sign > 0 else arb("0.001"))
        deficit = sign*mean - (mass+sign*bias)*outside - err*(1-outside)
        assert deficit > arb(target)
        print(f"Gaussian replay [d^{lo}, d^{hi}] sign {sign:+d}, margin > {target}.")


if __name__ == "__main__":
    main()
