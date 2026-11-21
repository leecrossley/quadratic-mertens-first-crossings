# Can split and inert primes expose a zero near the centre?

A proposed route to a negative Mertens average uses two inequalities for signed prime sums. If the average stays nonnegative through a long interval, both inequalities must hold. Reversing either one with enough margin would give a negative start. [Original tests](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/ef3e53c/results/signed-prime-tails/PRIME-TEST.md)

For a genuine positive quadratic discriminant $d$, a zero at the centre or a conjugate pair of height at most $\pi/H$ forces the first sum **below $-0.52$** when $H\ge4\log(3d)$ and $d$ is sufficiently large. The proposed contradiction would require that sum to exceed a threshold near $-0.5$.

For the second test, there is an explicit assignment of split and inert signs to ordinary primes with a double central zero. Its weighted average stays positive for every real start and every finite matrix of the tested frequencies satisfies the necessary bound. Moving the zeros to a close pair preserves positivity beyond any chosen power of the reference parameter, with a suitable choice of the pair. Each prime has the allowed local Euler factor and the assignment extends completely multiplicatively. Its construction gives a model. A bound for all sufficiently large actual Yokoi fields remains open. The last part of the proof gives a concrete arithmetic distinction, using prime counts twisted by the conductor-five character. [Theorem and proof](PROOF.md) · [Prior work and scope](PRIOR-WORK.md)

## Reproduce the checks

~~~sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
sh verify-release.sh
~~~

The program selects ordinary primes of the prescribed signs and checks two independent evaluations of the local product changes. It also checks the finite prime-power sums at two frequencies. A second program sums the actual grid ordinates and compares them with the triangular Fourier polynomial, including a cut at a grid frequency. The estimates uniform in the parameter and starting point are proved analytically. [Finite check output](evidence/check.txt)

Two Lean lemmas verify positivity of cosine difference matrices and preservation of any positive kernel under multiplication by such a cosine. Use Lean 4.33.1 and Mathlib revision 0df444a360eaa60ab8c11dca51a86af692955474. From that Mathlib checkout run the following, replacing the path with the local file. [Lean source](PrimeSigns.lean) · [Kernel output](evidence/lean.txt)

~~~sh
lake env lean /absolute/path/to/PrimeSigns.lean
~~~
