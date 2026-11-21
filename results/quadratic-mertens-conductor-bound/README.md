# A smaller deadline for a prime product to cross its curve

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24410800.svg)](https://doi.org/10.5281/zenodo.24410800)

Daniel R. Johnston asked how far a number field's prime-ideal product can run ahead of the curve predicted by Mertens' theorem. For each real quadratic field of discriminant $d$, the smaller deadline assumes that the nontrivial zeros of $\zeta(s)L(s,\chi_d)$ have real part $1/2$. Alpöge's announced Dirichlet GRH theorem supplies this hypothesis for both factors. [Announcement](https://alpo.ge/remark.pdf) [Formal verification](https://math.mit.edu/~drew/grh/)

Let $d$ be the fundamental discriminant. Write $S_d$ for the first crossing, the infimum of the points $x\ge2$ at which the prime-ideal product falls strictly below $e^\gamma L(1,\chi_d)\log x$. There is a fully specified integer $U(d)$ with $S_d<U(d)$ and

$$
\log\log U(d)\ll(\log d)^3(\log\log d)^2.
$$

The earlier proof gave a sharper cutoff as well as the simplified double exponent $d^{30000}$. At $d=5$ the earlier exact double binary logarithm has 17,273 decimal digits, the simplified exponent has 20,970, and the new upper estimate has 89. The proof compares the exact cutoffs for every $d\ge5$. Here it grows at most like the cube of the digit count times the square of its logarithm. The deadline is still far too large for a direct prime search. Whether a fixed power of $d$ always suffices remains open in these bounds. [Full proof and integer formula](PROOF.md) [Earlier cutoff](https://github.com/leecrossley/yokoi-mertens-explicit-upper-bound/releases/tag/v1.0.0) [Problem 8, pp. 4–5](https://arxiv.org/pdf/2407.03530#page=4)

## Where the improvement comes from

The proof starts with an interval close to 1 on which an expression built from the zeta zeros has a definite negative sign. Smoothing and simultaneous approximation move that sign to a much later interval where it forces an actual crossing. The length of the starting interval largely determines how expensive the move is.

Two terms in the signed expression each grow on the scale of $\log d$. Their difference depends on $L'(1,\chi_d)/L(1,\chi_d)$ and is only $O(\log\log d)$. Keeping the cancellation permits a starting interval of length comparable to $1/(\log d)^2$. The final calculation uses a bound on how many zeros must be brought back into phase. [Proof, §§1–4](PROOF.md) · [Chirre, Valås Hagen and Simonič, Theorem 1](https://arxiv.org/pdf/2206.00819#page=1) · [Literature and scope](PRIOR-WORK.md)

## Checking the result

The argument uses the critical-line theorem for the Riemann zeta function and the primitive quadratic Dirichlet function of conductor $d$. The source and independent kernel checks for that input are public. The new proof is written out. Four subsidiary lemmas have Lean proofs. Finite numerical tests use Arb enclosures to compare independent formulas for the residues, the signed integral, and the parameter bounds. [Formal zero-location verification](https://math.mit.edu/~drew/grh/) · [Lean source](ConductorBound.lean) · [Lean output](evidence/lean.txt) · [Numerical output](evidence/check.txt)

~~~sh
python3 bound.py 5004173
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
./verify-release.sh
~~~

The calculator takes a real quadratic fundamental discriminant, assumed as input, and prints the cutoff without expanding its exponent. The verification script checks the file manifest and reproduces the numerical output.

To compile the local Lean lemmas, pass a built Mathlib checkout to the same script. It checks the Mathlib and compiler commits, treats compiler warnings as errors, compares the printed axioms with the recorded sets and replays the compiled module through the kernel. [Pinned Mathlib revision](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474)

~~~sh
./verify-release.sh /path/to/mathlib4
~~~
