"""Enclose the 51 normalized real derivatives with both tagged theta rules."""
import argparse
import json
from pathlib import Path
import sys

from flint import arb, ctx, fmpq


HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "source" / "results"
if (HERE.parent / "REAL-AXIS.md").is_file():
    RESULTS = HERE.parents[1]  # Inside results/signed-prime-tails/review.
sys.path.insert(0, str(RESULTS / "fixed-weight-delay-2380853"))
sys.path.insert(0, str(RESULTS / "signed-prime-tails"))
from theta import DISCRIMINANT, ERROR, theta_nodes
from real_axis_gauss import theta_rule


DIGITS = 42
UNIT = 10**DIGITS
FILE = HERE / "real-values.json"


def trapezoidal_ratio(q, nodes, scale):
    den, num = arb(0), arb(0)
    for t, weight in nodes:
        argument = q*t/2
        den += weight*argument.cosh()
        num += weight*t*argument.sinh()/2
    den += arb(0, ERROR)
    num += arb(0, ERROR)
    if not den > 0:
        raise ArithmeticError("Trapezoidal denominator enclosure contains zero")
    return num/(scale*den)


def gaussian_ratio(q, nodes, allowance, scale):
    den, num = arb(0), arb(0)
    for half_t, weight in nodes:
        exponential = (q*half_t).exp()
        reciprocal = 1/exponential
        den += weight*(exponential+reciprocal)/2
        num += weight*half_t*(exponential-reciprocal)/2
    den += allowance
    num += allowance
    if not den > 0:
        raise ArithmeticError("Gaussian denominator enclosure contains zero")
    return num/(scale*den)


def decimal_string(n):
    sign = "-" if n < 0 else ""
    whole, remainder = divmod(abs(n), UNIT)
    return f"{sign}{whole}.{remainder:0{DIGITS}d}"


def measurements():
    ctx.prec = 320
    d = DISCRIMINANT
    scale = arb(3*d).log()
    trap = theta_nodes()
    gauss, allowance = theta_rule(d)
    arguments = [(f"j={j}", arb(j)/(16*scale)) for j in range(1, 50)]
    arguments += [("s=1", arb(1)/2), ("s=2", arb(3)/2)]
    for label, q in arguments:
        first = trapezoidal_ratio(q, trap, scale)
        second = gaussian_ratio(q, gauss, allowance, scale)
        if not first.overlaps(second):
            raise ArithmeticError(f"{label}: the two independently computed balls are disjoint")
        yield label, first, second


def main():
    if not __debug__:
        raise SystemExit("Run with assertions enabled for the two tagged rules.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", type=Path, metavar="NEW_FILE",
                        help="write newly constructed enclosures to a new file")
    args = parser.parse_args()
    rows = []
    for label, first, second in measurements():
        # The midpoint chooses decimal endpoints. The strict enclosure tests
        # below are the proof that these rounded endpoints are valid.
        n = int((first.mid()*UNIT).floor().unique_fmpz())
        low, high = n-1, n+2
        low_ball = arb(fmpq(low, UNIT))
        high_ball = arb(fmpq(high, UNIT))
        if not all(val > low_ball and val < high_ball for val in (first, second)):
            raise ArithmeticError(f"{label}: decimal endpoints do not enclose both balls")
        rows.append(dict(point=label, lower=decimal_string(low), upper=decimal_string(high)))
    data = dict(discriminant=DISCRIMINANT, scale="L = log(3*d)",
                value="Lambda_d'(s) / (L * Lambda_d(s))",
                grid="j=1..49: s = 1/2 + j/(16*L); the final rows use s=1,2",
                decimal_places=DIGITS, rows=rows)
    if args.write:
        with args.write.open("x", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2)
            handle.write("\n")
    elif data != json.loads(FILE.read_text(encoding="utf-8")):
        raise SystemExit("The supplied table differs from the recomputation.")
    print("51 normalized derivatives: two overlapping enclosures at every point.")
    print("All 51 decimal intervals contain both full Arb balls; width = 3e-42.")
    if not args.write:
        print("The recomputed table agrees with real-values.json.")


if __name__ == "__main__":
    main()
