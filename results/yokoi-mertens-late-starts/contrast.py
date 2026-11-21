"""Compute a local certificate for an individual field without using its zeta residue."""
from bisect import bisect_right
from flint import arb, ctx, fmpz


def certificate(d, z, blocks):
    assert all(e == 1 for _, e in fmpz(d).factor()) and d % 8 == 5
    half_steps = [z**(2*blocks) * (2**j) for j in range(2*blocks+1)]
    edges = [arb(z).log()+arb(j)*arb(2).log()/(2*blocks) for j in range(2*blocks+1)]
    events = [[] for _ in range(2*blocks)]
    for p in range(2, 2*z+1):
        if not fmpz(p).is_prime():
            continue
        symbol = fmpz(p).jacobi(d)
        norm = p*p if symbol == -1 else p
        if z < norm < 2*z:
            multiplicity = 2 if symbol == 1 else 1
            i = bisect_right(half_steps, norm**(2*blocks))-1
            events[i].append((norm, multiplicity*(arb(norm)/(norm-1)).log()))
    primitive = lambda v: v*(v.log()-1)
    reserve = arb(0)
    height = arb(0)
    for i in range(blocks):
        left, middle, right = edges[2*i:2*i+3]
        by_jumps = 2*primitive(middle)-primitive(left)-primitive(right)
        by_windows = arb(0)
        for j in (2*i,2*i+1):
            direction = -1 if j % 2 == 0 else 1
            previous = edges[j]
            for q, gain in sorted(events[j]):
                v = arb(q).log()
                h = v-left if direction == -1 else right-v
                by_jumps += gain*h
                by_windows += direction*((v-previous)*height-primitive(v)+primitive(previous))
                height += gain
                previous = v
            v = edges[j+1]
            by_windows += direction*((v-previous)*height-primitive(v)+primitive(previous))
        assert by_jumps.overlaps(by_windows)
        reserve += abs(by_jumps)
    threshold = 2*(9+3*arb(d).log())
    def deadline(amount):
        lo, hi = 2*z-1, 2*z
        def test(n):
            lhs = arb(n).sqrt()*arb(n).log()*amount
            if lhs > threshold:
                return True
            assert lhs < threshold
            return False
        while not test(hi):
            hi *= 2
        while hi-lo > 1:
            mid = (lo+hi)//2
            if test(mid):
                hi = mid
            else:
                lo = mid
        return hi
    old = deadline(arb(1)/(64*z))
    new = deadline(reserve)
    assert 2*z <= new < old
    print(f'd={d}, z={z}, {blocks} contrasts, sum of absolute contrasts {reserve.str(12)}.')
    print(f'Conditional crossing deadline {new}, compared with {old} from the uniform norm-gap reserve.')


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Enable assertions')
    ctx.prec = 176
    certificate(2380853,1000,8)
    certificate(82864613,4096,16)
