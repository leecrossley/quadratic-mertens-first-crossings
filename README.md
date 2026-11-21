# How early can an average detect a late prime-product dip?

Let $S$ be the first time the prime-ideal Mertens product in a Yokoi field falls below its expected value. Let $Y$ be the earliest possible start for a negative average of its logarithmic error, allowing any bounded nonnegative decreasing weight and any observation length.

Among fields with a very late first dip, almost all satisfy
$$
 a\,S/(\log S)^8 \ <\ Y\ \le S
$$
for an absolute $a>0$, in the discriminant ranges of the theorem. Thus the first successful start and the first dip have the same exponent on the logarithmic scale. Exceptional fields exist. The asserted exponent 8 is an upper bound on the logarithmic loss. [Theorem and proof](PROOF.md)

More precisely, in each sufficiently large shell $D/2<d\le D$ condition on a finite $S\ge X$. The exceptional fraction is at most $\exp[-b(\log X)^4]$ through $\log X\le c(\log D)^{1/20}$ as $X\to\infty$. A separate estimate at a specified cutoff $X$ holds farther, through $\log X\le c'(\log D)^{1/5}$. The proof counts late fields in the denominator as well as early successful starts in the numerator. [Late-field count](SURVIVAL.md) · [Future-error estimate](TAIL.md)

The argument uses the jumps on just one earlier prime interval. Divide it into blocks and compare the first and second half of each. If the product stays positive and a faraway negative interval can repay all that positive area, most of these differences must be exceptionally small. A fourth-degree polynomial bounds the number of fields in which this happens. The comparison also gives a certificate for a specified discriminant once a successful start is known. The sign of a suitable start in **every** sufficiently large field remains open. [Individual certificate, §5](PROOF.md) · [Earlier results and scope](PRIOR-WORK.md)

## Reproducing the finite checks

Run the following from the release directory with Python 3.10 or later. Two calculations of each contrast use its weighted jumps and direct integration over prime-ideal norm windows. Class numbers and zeta residues cancel from both calculations.

~~~sh
python3 -m pip install -r requirements.txt
shasum -a 256 -c SHA256SUMS
python3 -B contrast.py
~~~

[Certified local contrasts and deadlines](evidence/contrasts.txt) · [Verifier](contrast.py)

The distribution theorems have written proofs. Three supporting inequalities were checked in Lean 4.33.1. Set NOTE to the absolute release directory and run the command from the [pinned Mathlib checkout](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).

~~~sh
lake env lean -R "$NOTE" "$NOTE/LateStarts.lean"
~~~

[Lean source](LateStarts.lean) · [Kernel output](evidence/lean.txt)
