"""Independent sign check at d^(7/3) by direct Gaussian quadrature."""
from math import ceil, comb, sqrt
from pathlib import Path

from flint import acb, arb, ctx


def main():
    if not __debug__:
        raise SystemExit("Enable Python assertions.")
    ctx.prec = 192
    d = 2380853
    n = 64
    # Twice the even critical-line theta integrand on the positive half-axis.
    rule = [arb.legendre_p_root(n,k,weight=True) for k in range(n)]
    residues = bytearray(d)
    for i in range(1,(d+1)//2):
        residues[i*i%d] = 1
    points = []
    for j in range(22):
        for root,weight in rule:
            x = j+(1+root)/2
            c = arb.pi()*x.exp()/d
            last = max(1,ceil(sqrt(160/float(c))))
            assert last < d and c*last**2 > 150
            value = sum(((1 if residues[k] else -1)*(-c*k*k).exp() for k in range(1,last+1)),arb(0))
            value += arb(0,(-c*last**2).exp()/(2*c*last))
            points.append((x,weight*value*(x/4).exp()))
    # Cauchy's inequality on radius-one disks in each unit interval.
    quadrature_error = 22*8*d*d*arb(32).exp()/((2*n+1)*arb(comb(2*n,n))**2)
    quadrature_error += arb("1e-100")
    assert quadrature_error < arb("1e-46")
    enclosure = arb(0,quadrature_error)
    def integral(fn):
        return sum((w*fn(x) for x,w in points),arb(0))+enclosure
    L = integral(lambda x:(x/4).cosh())
    V = integral(lambda x:x*(x/4).sinh())/L
    u = 7*arb(d).log()/3
    assert u > 30
    order = 16
    kernel_rule = [arb.legendre_p_root(order,k,weight=True) for k in range(order)]
    kernel_nodes = []
    for j in range(40):
        for root,weight in kernel_rule:
            t = j+(1+root)/2
            kernel_nodes.append((t/u,weight*(-t).exp()/2))
    kernel_error = arb(200)/((2*order+1)*arb(comb(2*order,order))**2)+4*arb(-40).exp()
    def zero_term(gamma):
        a = acb(arb(1)/2,-gamma)
        kernel = sum((weight/((a+t)*(a+1+t)) for t,weight in kernel_nodes),acb(0))
        kernel += acb(arb(0,kernel_error),arb(0,kernel_error))
        return 2*((acb(0,gamma*u)).exp()*kernel).real
    Q = arb(0)
    for line in Path(__file__).with_name("brackets.txt").read_text().splitlines():
        l,r = map(int,line.split())
        assert 0<l<r<=60*10**8
        a,b = arb(l)/10**8,arb(r)/10**8
        left = integral(lambda x:(a*x/2).cos())
        right = integral(lambda x:(b*x/2).cos())
        assert left*right < 0
        # Use a point value and a derivative bound throughout the bracket.
        g = (a+b)/2
        dg = (b-a)/2
        Q += zero_term(g) + arb(0,2*dg*(u+3)/(arb(1)/4+a*a))
        V -= 2/(arb(1)/4+b*b)
    assert 0 < V < arb("0.11")
    Q += arb(0,V)
    rational = arb(0)
    mass = 2+arb.const_euler()-(4*arb.pi()).log()
    for k in range(1,21):
        g = acb.zeta_zero(k).imag
        rational += zero_term(g)
        mass -= 2/(arb(1)/4+g*g)
    rational += arb(0,mass)
    t = u/2
    # Rounded-up bounds for the square and higher-power terms.
    def correction(degree,discriminant):
        delta=((t/(2*arb.pi())+2)*arb(discriminant).log()+degree*(t*t/(8*arb.pi())+2))*(-t/2).exp()
        return (1+3*delta)*2/3+8*(-u/6).exp()+1/((u/2).exp()*u.tanh())
    signed_lower = -(Q+correction(1,1)).upper()
    field_upper = (Q+rational+correction(2,d)).upper()
    assert signed_lower > arb("0.26") and field_upper < -arb("0.22"), (signed_lower,field_upper,Q,rational)
    print("Gaussian quadrature independently confirms every quadratic bracket.")
    print(f"Direct Laplace integrals give signed tail > {signed_lower.str(8)}, field average < {field_upper.str(8)} (normalised).")


if __name__ == "__main__":
    main()
