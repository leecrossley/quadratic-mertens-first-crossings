"""Check a negative prime average from 151 off-centre zero brackets."""
from math import comb, factorial
from pathlib import Path
import sys

from flint import acb, arb, ctx

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "fixed-weight-delay-2380853"))
from early import primes
from theta import DISCRIMINANT, ERROR, completed, theta_nodes
from verify import prime_power_upper


def brackets(nodes):
    zeros = []
    previous = 50_000_000
    for line in (HERE / "brackets-above-half.txt").read_text().splitlines():
        lo, hi = map(int, line.split())
        assert previous < lo < hi <= 60 * 10**8
        left = arb(lo) / 10**8
        right = arb(hi) / 10**8
        assert completed(left, nodes) * completed(right, nodes) < 0
        zeros.append(arb(lo + hi) / (2 * 10**8) + arb(0, arb(hi - lo) / (2 * 10**8)))
        previous = hi
    assert len(zeros) == 151
    return zeros


def theta_trace(nodes):
    denominator = sum((w * (3*x/4).cosh() for x, w in nodes), arb(0)) + arb(0, ERROR)
    numerator = sum((w * x * (3*x/4).sinh() for x, w in nodes), arb(0)) + arb(0, ERROR)
    assert denominator > 0
    return numerator / (3 * denominator)


def euler_trace(d, limit=300_000):
    logarithmic_derivative = arb(0)
    for p in primes(limit):
        residue = pow(p, (d - 1) // 2, d)
        chi = -1 if residue == d - 1 else residue
        assert chi in (-1, 0, 1)
        logarithmic_derivative -= arb(p).log() * chi / (p*p - chi)
    tail = 2 * (arb(limit).log() + 1) / limit
    return ((arb(d)/arb.pi()).log() - arb.const_euler()
            + 2*(logarithmic_derivative + arb(0, tail))) / 3


def taylor_terms(zeros, u):
    total = arb(0)
    for g in zeros:
        a = acb(arb(1)/2, -g)
        b = 1 + a
        coefficient = sum(((-1)**j * factorial(j) / u**j *
                           (a**(-j-1) - b**(-j-1)) for j in range(3)), acb(0))
        error = 6 / u**3 * (abs(a)**-4 + abs(b)**-4)
        total += 2 * ((acb(0, g*u).exp() * coefficient).real + arb(0, error))
    return total


def integrated_terms(zeros, u):
    # Integrate exp(-t)/[(a+t/u)(1+a+t/u)] on the positive half-line.
    order = 8
    intervals = 24
    rule = [arb.legendre_p_root(order, k, weight=True) for k in range(order)]
    nodes = []
    for j in range(intervals):
        for x, w in rule:
            t = j + (1 + x)/2
            nodes.append((t/u, (-t).exp() * w/2))
    component_error = (arb(5 * intervals) / ((2*order+1) * comb(2*order, order)**2)
                       + 4 * arb(-intervals).exp())
    error = acb(arb(0, component_error), arb(0, component_error))
    total = arb(0)
    for g in zeros:
        a = acb(arb(1)/2, -g)
        kernel = sum((w/((a+t)*(1+a+t)) for t, w in nodes), acb(0)) + error
        total += 2 * (acb(0, g*u).exp() * kernel).real
    return total


def check_model_base():
    # Complete periods of chi_5 leave the partial sums of the tail in [-1, 1].
    cutoff = 5000
    value = arb(0)
    derivative = arb(0)
    for n in range(1, cutoff+1):
        chi = (0, 1, -1, -1, 1)[n % 5]
        value += arb(chi)/n
        derivative -= chi*arb(n).log()/n
    value += arb(0, 1/arb(cutoff))
    derivative += arb(0, arb(cutoff).log()/cutoff)
    assert value > 0
    mass = 2 + arb(5).log() - 2*arb.pi().log() - 4*arb(2).log() + 2*derivative/value
    assert 0 < mass < arb(1)/4
    print("The combined ordinary and conductor-five inverse-square mass is below 1/4.")


def check_shifted_grid():
    period, angle, cutoff = 8, arb(1)/8, 512
    # The negative ordinates are the reflections of the retained positive list.
    grid = [(2*arb.pi()*k + sign*angle)/period
            for k in range(0, cutoff+1) for sign in (-1, 1) if k or sign == 1]
    frequency_tail = 4*period**2/(arb.pi()**2 * cutoff)
    for start, expected in ((47, 1), (48, 1), (191, -1)):
        u = arb(start)
        constant_sum = arb(0)
        for g in grid:
            a = acb(arb(1)/2, -g)
            constant_sum += 2*(acb(0, g*u).exp()/(a*(1+a))).real
        varying_sum = taylor_terms(grid, u)
        j0 = (start+period-1)//period
        constant_images = varying_images = arb(0)
        for j in range(j0, j0+25):
            v = j*period-u
            image = 2*period*(j*angle).cos()*(-v/2).exp()*(1-(-v).exp())
            constant_images += image
            varying_images += image*u/(j*period)
        image_tail = 2*period*((u-(j0+25)*period)/2).exp()/(1-arb(-period/2).exp())
        for frequencies, images in ((constant_sum, constant_images), (varying_sum, varying_images)):
            lhs = frequencies + arb(0, frequency_tail)
            rhs = images + arb(0, image_tail)
            assert lhs.overlaps(rhs) and expected*lhs > 0 and expected*rhs > 0
    print("Both grid kernels agree with periodization before, at and beyond a lattice point, including a negative case.")


def main():
    if not __debug__:
        raise SystemExit("Enable Python assertions.")
    ctx.prec = 192
    d = DISCRIMINANT
    u = arb(36359) / 25
    assert u < 100 * arb(d).log()
    nodes = theta_nodes()
    zeros = brackets(nodes)
    print("151 disjoint quadratic brackets above height 1/2 have opposite endpoint signs.")
    represented = sum((2/(arb(9)/4 + g*g) for g in zeros), arb(0))
    traces = (theta_trace(nodes), euler_trace(d))
    pieces = (taylor_terms(zeros, u), integrated_terms(zeros, u))
    assert traces[0].overlaps(traces[1]) and pieces[0].overlaps(pieces[1])
    ordinary = 2 + arb.const_euler() - (4 * arb.pi()).log()
    archimedean = (-u/2).exp() / (2*u.tanh())
    for label, trace, terms in zip(("Theta and Taylor", "Euler product and Gaussian quadrature"),
                                   traces, pieces):
        unresolved = trace - represented
        assert arb(8)/9 < unresolved < arb("0.984")
        upper = (terms + 3*unresolved + ordinary + archimedean + prime_power_upper(u, 2, d)).upper()
        signed = -(terms + 3*unresolved + archimedean + prime_power_upper(u, 1, 1)).upper()
        assert upper < -arb(1)/20 and signed > arb(1)/10, (label, upper, signed)
        print(f"{label} give 8/9 < unresolved trace < 0.984. "
              f"Normalised average < {upper.str(10)}, signed prime tail > {signed.str(10)}.")
    check_model_base()
    check_shifted_grid()


if __name__ == "__main__":
    main()
