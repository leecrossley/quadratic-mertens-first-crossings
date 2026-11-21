"""Independent check with finite Fourier special values and prime-power series."""
from math import gcd
from flint import arb, ctx, fmpz


def chi(d, n):
    if gcd(d, n) != 1:
        return 0
    factors = (13, 41) if d == 533 else (5,)
    return (-1)**sum(pow(n, (p-1)//2, p) == p-1 for p in factors)


def l_values(d):
    # The primitive even quadratic Gauss sum equals sqrt(d).
    half_sum = arb(0)
    bernoulli_sum = arb(0)
    for a in range(1, d):
        x = arb(a)/d
        sign = chi(d, a)
        if sign:
            half_sum += sign*(2*x.sin_pi()).log()
            bernoulli_sum += sign*(x*x-x+arb(1)/6)
    return -half_sum/arb(d).sqrt(), arb.pi()**2*bernoulli_sum/arb(d).sqrt()


def check():
    ctx.prec = 160
    modulus, limit = 533, 25_000
    primes = [n for n in range(2, limit+1) if fmpz(n).is_prime()]
    oriented = [(p, chi(modulus, p)) for p in primes
                if chi(modulus, p)*chi(5, p) == -1]
    first = l_values(modulus)
    second = l_values(5)
    constants = []
    for k, (large, small) in enumerate(zip(first, second), 1):
        value = (large/small).log()/2
        for p in (5, 13, 41):
            z = arb(1)/p**k
            value += ((1-chi(modulus, p)*z)/(1-chi(5, p)*z)).log()/2
        # On an oriented prime the excess of atanh(z) over z consists
        # only of z^3/3 + z^5/5 + ... . Enclose the two omitted tails.
        for p, sign in oriented:
            z = arb(1)/p**k
            z2 = z*z
            term = z*z2
            for power in range(3, 50, 2):
                value -= sign*term/power
                term *= z2
        error = arb(4)/limit**(3*k-1) + arb(4)/2**(51*k)
        constants.append(value + arb(0, error))

    def value_at(start):
        v = constants[0]-start*constants[1]
        for p, sign in oriented:
            if p > start:
                break
            v -= arb(sign)*(p-start)/(p*p)
        return arb(start).sqrt()*arb(start).log()*v

    assert arb("-1.033") < value_at(240)-value_at(30) < arb("-1.030")
    assert arb("0.818") < value_at(4096)-value_at(512) < arb("0.822")
    # Average the local jumps directly. The remaining positive contribution
    # is <= 2*y/M from sum_{v>M} 2/(v(v-1)).
    y, mass_limit = 30, 1_000_000
    u = arb(y).log()
    averaged_jumps = {533: arb(0), 5: arb(0)}
    for p in range(2, mass_limit+1):
        if not fmpz(p).is_prime():
            continue
        for d in averaged_jumps:
            sign = chi(d, p)
            norm, count = (p*p, 1) if sign == -1 else (p, 1+sign)
            if norm <= mass_limit:
                averaged_jumps[d] += count*(arb(norm)/(norm-1)).log()*min(1, arb(y)/norm)
    bounded_tail = arb(0).union(arb(2*y)/mass_limit)
    scale = arb(y).sqrt()*u
    comparison = arb.const_euler() + u.log() + y*u.expint(1)
    average = scale*(averaged_jumps[533] + bounded_tail - comparison - first[0].log())
    threshold = scale*(averaged_jumps[5] + bounded_tail - comparison - second[0].log())/2
    assert arb("-0.073") < average < arb("-0.070")
    assert arb("0.293") < threshold < arb("0.295")

    correction = arb(0)
    for p, sig in oriented:
        v = arb(1)/p
        correction += sig*((-(-v).log1p()-v)*max(0,1-y*v)
                           + (-v*v).log1p()*max(0,1-y*v*v)/2)
    for p in (5,13,41):
        v = arb(1)/p
        a, b = chi(533,p), chi(5,p)
        correction -= (a-b)*(-v).log1p()*max(0,1-y*v)/2
        correction -= (a*a-b*b-a+b)*(-v*v).log1p()*max(0,1-y*v*v)/4
    # For p > limit the two correction magnitudes sum to at most 2/p^2.
    lead = value_at(y) + scale*(correction + arb(0, arb(2)/limit))
    assert arb("0.327") < lead < arb("0.333")
    assert lead > threshold
    print("d=533, finite Fourier values and odd-power sums certify both eightfold changes.")
    print("d=533, direct sum over ideal norms certifies -0.073 < sqrt(30) log(30) F(30) < -0.070.")
    print("At y=30, corrected disagreement lead > 0.327 exceeds the reference threshold < 0.295.")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run with assertions enabled.")
    check()
