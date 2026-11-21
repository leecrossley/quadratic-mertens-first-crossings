"""Interval certificate for the fixed power-one average and signed prime tail."""
from math import factorial
from pathlib import Path

from flint import acb, arb, ctx

from early import check_early, primes, square_residues
from theta import DISCRIMINANT, completed, curvature_sum, sign, theta_nodes, total_mass


ORDER = 6
STEPS = 160


def span(a, b):
    return (a+b)/2 + arb(0, (b-a)/2)


def certified_ordinates(nodes):
    path = Path(__file__).with_name("brackets.txt")
    quadratic = []
    previous = 0
    for line in path.read_text().splitlines():
        lo, hi = map(int, line.split())
        assert previous < lo < hi <= 60*10**8
        a, b = arb(lo)/10**8, arb(hi)/10**8
        assert sign(completed(a,nodes))*sign(completed(b,nodes)) == -1
        quadratic.append(span(a,b))
        previous = hi
    rational = [acb.zeta_zero(k).imag for k in range(1,21)]
    print(f"Certified {len(quadratic)} disjoint positive quadratic zero brackets; the first is {quadratic[0].str(9)}.")
    return quadratic, rational


class ZeroSum:
    def __init__(self, ordinates, mass):
        self.terms = []
        self.remainder = arb(0)
        represented = arb(0)
        for gamma in ordinates:
            a = acb(arb(1)/2,-gamma)
            b = 1+a
            coeffs = [(-1)**j*factorial(j)*(a**(-j-1)-b**(-j-1)) for j in range(ORDER)]
            self.terms.append((gamma, coeffs))
            self.remainder += 2*factorial(ORDER)*(abs(a)**(-ORDER-1)+abs(b)**(-ORDER-1))
            represented += 2/(arb(1)/4+gamma**2)
        self.missing = mass-represented
        assert self.missing > 0

    def bound(self, u):
        # Partial fractions and a finite geometric expansion of the Laplace kernel.
        inverse = 1/u
        total = arb(0)
        for gamma, coeffs in self.terms:
            z = coeffs[-1]
            for coefficient in reversed(coeffs[:-1]):
                z = z*inverse+coefficient
            phase = gamma*u
            sn,cs = phase.sin_cos()
            total += 2*(cs*z.real-sn*z.imag)
        return total+arb(0,self.missing+self.remainder*inverse**ORDER)


def square_lower_bounds(requests, residues):
    bits = 1 << 144
    endpoints = set()
    windows = []
    for a,b,lower in requests:
        start = int((b/2).exp().upper().ceil().unique_fmpz())
        finish = min(int(a.exp().lower().floor().unique_fmpz()),
                     int((64*(a/2).exp()).lower().floor().unique_fmpz()))
        assert start < finish and arb(start) >= (b/2).exp() and arb(finish) <= a.exp()
        endpoints.update((start,finish))
        windows.append((a,b,lower,start,finish))
    if not windows:
        return
    bounds = iter(sorted(endpoints))
    endpoint = next(bounds)
    sums = {}
    s2 = s4 = 0
    for p in primes(max(endpoints)):
        while endpoint < p:
            sums[endpoint] = (s2,s4)
            endpoint = next(bounds)
        if residues[p % DISCRIMINANT]:
            s2 += bits//p**2
            s4 += (bits+p**4-1)//p**4
    for k in (endpoint,*bounds):
        sums[k] = (s2,s4)
    minimum = arb(1000)
    for a,b,lower,start,finish in windows:
        s2 = sums[finish][0]-sums[start][0]
        s4 = sums[finish][1]-sums[start][1]
        squares = a*(a/2).exp()*(s2-b.exp()*s4)/bits
        assert lower+squares > 0, (a,b,lower,squares)
        minimum = minimum.min(lower+squares)
    print(f"Split-prime squares certify the remaining {len(windows)} intervals, using primes through {max(endpoints)}.")
    print(f"Smallest lower endpoint bound in those intervals exceeds {minimum.lower().str(6)} (normalised units).")


def lower_halfline(part, residues):
    upper = 9*arb(DISCRIMINANT).log()/4
    n = int((upper*STEPS).upper().ceil().unique_fmpz())
    remaining = []
    for j in range(14*STEPS,n):
        a,b = arb(j)/STEPS,arb(j+1)/STEPS
        low = part.bound(span(a,b)).lower()
        if not low > 0:
            remaining.append((a,b,low))
    square_lower_bounds(remaining,residues)
    print(f"All {n-14*STEPS} spectral intervals from log(y)=14 through log(y)={n}/{STEPS} are covered.")


def prime_power_upper(u, degree, conductor):
    # Relative Chebyshev bound at sqrt(y), decreasing beyond that point.
    w = u/2
    delta = ((w/(2*arb.pi())+2)*arb(conductor).log() +
             (w*w/(8*arb.pi())+2)*degree)*(-w/2).exp()
    assert w > 4
    return (1+3*delta)*2/3 + arb(39)/5*(-u/6).exp()


def check_local_sums(zeros, unseen):
    # One unaccounted zero this low would already exceed the full residual mass.
    cutoff = arb(29)/10
    assert unseen < 1/(arb(1)/4+cutoff**2)
    tau = zeros[0]
    p0 = unseen/cutoff**2
    pt = unseen/(cutoff-tau)**2
    for index,g in enumerate(zeros):
        c = 1/((arb(1)/4+g*g)*(arb(9)/4+g*g)).sqrt()
        p0 += 2*c/g**2
        pt += c/(g+tau)**2
        if index:
            pt += c/(g-tau)**2
    bound = (p0+pt)/(3*arb(DISCRIMINANT)).log()**2
    assert bound < arb("14.859")
    print(f"The two quadratic local zero sums divided by log(3d)^2 are together below {bound.upper().str(8)}.")


def main():
    if not __debug__:
        raise SystemExit("Enable Python assertions.")
    ctx.prec = 190
    nodes = theta_nodes()
    residues = square_residues()
    check_early(nodes,residues)
    quadratic,rational = certified_ordinates(nodes)
    mass = total_mass(nodes)
    ordinary = 2+arb.const_euler()-(4*arb.pi()).log()
    full = ZeroSum(quadratic+rational,mass)
    print(f"Total inverse-square zero mass {mass.str(13)}; omitted mass {full.missing.str(10)}.")
    lower_halfline(full,residues)
    u = 7*arb(DISCRIMINANT).log()/3
    gamma_term = (-u/2).exp()/(2*u.tanh())
    upper = (full.bound(u)+gamma_term+prime_power_upper(u,2,DISCRIMINANT)).upper()
    assert upper < -arb("0.22"), upper
    character = ZeroSum(quadratic,mass-ordinary)
    check_local_sums(quadratic,character.missing)
    derivatives = curvature_sum(nodes,quadratic[0])/(3*arb(DISCRIMINANT)).log()**2
    assert derivatives > 0 and derivatives < 16
    print(f"Two Taylor expansions independently put the unweighted local sums at {derivatives.str(8)} times log(3d)^2.")
    signed = -(character.bound(u)+gamma_term+prime_power_upper(u,1,1)).upper()
    assert signed > arb("0.26"), signed
    print(f"At y=d^(7/3), sqrt(y) log(y) F(y) < {upper.str(8)}.")
    print(f"At the same start the normalised signed split-minus-inert tail exceeds {signed.str(8)}.")
    # Subtract the continuous square contribution before bounding the two errors.
    z = u/2
    def delta(n,disc):
        return ((z/(2*arb.pi())+2)*arb(disc).log()+n*(z*z/(8*arb.pi())+2))*(-z/2).exp()
    allowance = (ordinary+gamma_term+2*(delta(2,DISCRIMINANT)+delta(1,1))+
                 arb(78)/5*(-u/6).exp()+3*u/2*(-u/2).exp())
    stop = arb(10)**26
    truncation = 4*u*(u/2).exp()*((3*arb(DISCRIMINANT)).log()+stop.log()+2)/stop.sqrt()
    assert allowance < arb("0.15") and truncation < arb("0.03")
    assert signed-truncation > arb("0.23") and arb("0.23") > allowance+truncation
    print(f"Through 10^26 the normalised finite prime sum exceeds 0.23; truncation costs < {truncation.upper().str(7)}, field correction < {allowance.upper().str(7)}.")


if __name__ == "__main__":
    main()
