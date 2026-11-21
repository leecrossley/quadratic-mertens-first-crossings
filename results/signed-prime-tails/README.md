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

## Near-central zeros on the conductor scale

Assume RH and quadratic Dirichlet GRH as above. For every sufficiently large $`d`$, one fixed exponent covers a pair arbitrarily close to the centre, including a double zero there, if the next pair is sufficiently far away on the scale $`1/\log(3d)`$. With at most two ordinates within $`1/(4\log(3d))`$ of the centre, a second criterion uses zeros near $`t`$ and $`3t`$ and gaps near $`2t`$ and $`4t`$. The theorem gives the allowed widths. For a sequence that misses every fixed power, bounded crowding at the centre forces the limiting rescaled zero heights to lie in finitely many arithmetic progressions up to finitely many exceptions, with the same conclusion for each multiplicity. The same restriction gives a test using real values of the completed quadratic function. A common exponent for the full Yokoi family remains open. [Theorems and proof](NEAR-CENTRAL.md) · [Earlier work](PRIOR-WORK.md#near-central-zeros-on-the-conductor-scale)

Run the following from this result directory to replay the six Fourier coefficients, the margin with errors, the finite conflict graphs and the double-lattice check.

~~~sh
python3 -B central_patterns.py
~~~

For the three real-axis measurements in discriminant 2,380,853, run the next command with python-flint 0.9.0. It uses the adjacent field result’s theta quadrature. [Interval output](evidence/near-central-trace.txt)

~~~sh
python3 -B central_trace.py
~~~

From the Mathlib revision listed above run the following with Lean 4.33.1.

~~~sh
lake env lean /absolute/path/to/NearCentralZeros.lean
~~~

The five checked lemmas cover the cost of moving a pair to zero before integration, the signed Fourier margin, uniqueness of a neighbor per signed ordinate, the graph's independent-set bound, and passage to the limit in a finite quadratic form. The explicit formula, extraction of limits of zeros, the harmonic-analysis application and the resulting number-theoretic theorems are written proofs. [Exact replay output](evidence/near-central-checks.txt) · [Lean output](evidence/near-central-lean.txt)

## Testing the prime average on the real axis

Under RH and quadratic Dirichlet GRH, finitely many real values of the completed quadratic logarithmic derivative can certify a negative starting point inside a polynomial deadline. The test allows arbitrary central multiplicity. Limiting progressions must have density at least $1/(2\pi)$ counted with multiplicity. A double lattice attains that density in a model, and a crowded model also passes every limiting test. [Theorem and proof](REAL-AXIS.md) · [What genuine primes would have to do](REAL-AXIS-PRIMES.md) · [Approximation away from the centre](REAL-AXIS-OUTER.md)

For discriminant 2,380,853, 51 real derivatives certify four successive signs of the average. Two programs check the signs by different theta quadratures and different computations of the polynomial weights. Neither takes a zero location as input. Run them here with python-flint 0.9.0. [Four intervals and proof](REAL-AXIS-FIELD.md) · [First replay](evidence/real-axis-signs.txt) · [Second replay](evidence/real-axis-gauss.txt)

~~~sh
python3 -B real_axis.py
python3 -B real_axis_gauss.py
~~~

With Lean 4.33.1 and the Mathlib revision listed above, run the following from that Mathlib checkout.

~~~sh
lake env lean /absolute/path/to/RealAxisCrossings.lean
~~~

The six checked identities and inequalities cover the resolvents, conductor offset, transfer of a strict margin into an interval, double lattice, two-sample concentration identity and prime-square cancellation. The number-theoretic arguments and limiting theorems are written proofs. [Lean output](evidence/real-axis-lean.txt) · [Prior work and novelty](PRIOR-WORK.md#real-values-and-the-sign-of-the-future-average)
