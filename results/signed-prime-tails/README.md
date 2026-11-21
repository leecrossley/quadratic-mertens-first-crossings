# A signed-prime test for a negative Mertens average

Assume the critical-line property for the Riemann zeta function and $L(s,\chi_d)$ for the quadratic discriminants concerned (field GRH). Alpöge's announced Dirichlet GRH theorem supplies this input. The analytic proofs use it throughout. [Announcement](https://alpo.ge/remark.pdf) [Independent formal checks](https://math.mit.edu/~drew/grh/)

In a real quadratic field, an ordinary prime can split into two prime ideals or stay inert. Count a split prime positively, an inert prime negatively, and weight each prime above $y$ by $(1-y/p)/p$. At polynomial scales this balance determines the sign of the full $y/t$ average of the Mertens log error up to a correction from ordinary primes. After multiplying by $\sqrt y\log y$, the correction has absolute value at most $0.046192$ plus a term that tends to zero as $d\to\infty$. For an individual field the proof gives a larger explicit allowance, about 0.14 for $d=2{,}380{,}853$ at $y=d^{7/3}$.

The proof yields a polynomial starting point for every field satisfying one quantitative condition on two sums over zeros of its quadratic Dirichlet function. The condition can be tested from derivatives at just two points, the centre and one low zero. For any sufficiently large individual discriminant with a nonzero central value, the argument also proves the existence of arbitrarily late negative averages. A common exponent for every sufficiently large Yokoi field remains open. [Theorems, hypotheses and proofs](PROOF.md) · [Earlier work](PRIOR-WORK.md)

## Replay

From this directory, run the exact rational checks with the Python standard library.

~~~sh
python3 -B check.py
~~~

For the measure-theoretic implication that forces a negative value, use Lean 4.33.1 with Mathlib revision 0df444a360eaa60ab8c11dca51a86af692955474. From a checkout of that Mathlib revision run the following command, replacing the path with the path to this file.

~~~sh
lake env lean /absolute/path/to/FrequencyTest.lean
~~~

Lean checks the Fourier coefficient inequality for a nonnegative weight and the resulting negative-set criterion. The explicit formula, the conductor estimates and their application are given in the written proof. [Factor checks](evidence/factors.txt) · [Lean kernel output](evidence/lean.txt) · [Reproduction hashes](SHA256SUMS)

## Central zeros and close pairs

For the first negative start, the two local inverse-square bounds can be replaced by one quantity. If $g_d$ is the height of the nearest quadratic zero and $g_d>0$, then some negative average starts by $\exp(C(\log(3d)+1/g_d))$ for every sufficiently large $d$. Zeros away from the centre can be arbitrarily close. A second test allows a double zero at the centre when seven low ordinates have the specified 21 differences. One exponent for every sufficiently large Yokoi field remains open. [Theorems and proof](NEAREST-ZERO.md) · [Test using split and inert primes](PRIME-TEST.md) · [Limit of zero-count arguments](GRID.md)

For $d=2{,}380{,}853$ the interval calculation withholds **all** quadratic ordinates of height at most $1/2$. Even allowing enough unobserved mass for a double central zero, the normalized average is below $-0.05$ at $\log y=1454.36$. The same certificate puts the normalized signed prime tail above $0.10$. [Certificate and input](WITHHELD.md) · [Earlier work and novelty search](PRIOR-WORK.md#the-nearest-zero-and-central-multiplicity)

From this directory, run the following with Python and python-flint 0.9.0. The verifier imports the earlier field's arithmetic routines from the adjacent result directory.

~~~sh
python3 -B packets.py
~~~

With the same Lean and Mathlib versions as above, run the following from the Mathlib checkout.

~~~sh
lake env lean /absolute/path/to/CentralPackets.lean
~~~

The four kernel-checked lemmas establish the exact integral identity, a lower bound on a signed square test, absorption of the central mass, and the numerical margin for seven frequencies. The written proof derives the analytic theorems and states the hypotheses on the zero differences. [Interval output](evidence/packets.txt) · [Lean output](evidence/central-lean.txt)
