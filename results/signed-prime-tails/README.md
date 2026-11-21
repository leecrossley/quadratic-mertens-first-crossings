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
