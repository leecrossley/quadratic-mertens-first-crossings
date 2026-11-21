# Verification

The extension to all small-prime selections, its two full integer sweeps, its two new supporting Lean lemmas and the optimum Gaussian mass are covered in [the sieve-choice checks](SIEVE-CHECKS.md).

The proof specifies its hypotheses on the Riemann zeta function and the primitive quadratic Dirichlet function. The bounds on the ordinary sums, including the exponent 8, are analytic. The finite calculations below use character values and Gaussian sums directly and have no zero-location input.

## A late field

The prime $`d=1543^2+4=2{,}380{,}853`$ has $`\lfloor(\log d)^2\rfloor=215`$. Removing all 47 primes through 215 leaves 1 and the primes above 215 throughout the range checked below. The signed count first reaches $`-1`$ at 331. It stays nonpositive until it first returns to $`+1`$ at 367. One program uses Jacobi symbols. A second program generates the quadratic residues by squaring every representative through $`(d-1)/2`$.

For the Gaussian profile the full ratio of negative to positive mass lies in $`(0.9918,0.9927)`$ before any deletions, and in $`(0.9845,0.9859)`$ after deleting multiples of 2, 3 and 5. At the single scale $`x=10`$ the corresponding Gaussian values lie in $`(-0.145,-0.144)`$ and $`(0.229,0.231)`$. The mass assertions here use two deletion choices, $`q=1,30`$. The 47-prime calculation concerns sharp integer counts.

## A finite family check

All 444 squarefree $`d=m^2+4`$ with odd $`1\le m\le999`$ were included. Set $`z=\lfloor(\log d)^2\rfloor`$ separately for each field and remove every prime through $`z`$. Up to $`z^2`$ each survivor is 1 or prime. Count an occurrence only when the total is strictly negative and a subsequent total is strictly positive.

| Outcome through $`z^2`$ | Fields |
| --- | ---: |
| No negative value | 7 |
| Negative value, no subsequent positive value in the interval | 12 |
| Negative value followed by a positive value | 425 |

The Jacobi-symbol program uses interval logarithms and a certified floor. A second program checks squarefreeness by trial division, computes the cutoff using 48-digit decimal arithmetic and uses Euler's criterion modulo each surviving prime. Both reproduce the three totals. This checks signs on the stated short interval. The analytic theorem concerns sufficiently large fields, quantitative thresholds and a longer interval.

## Gaussian enclosures

[The Arb verifier](scripts/verify.py) uses 112-bit ball arithmetic. All truncation and interpolation errors enter the final intervals. The signed integral of the primitive sum over the whole line in $`\log x`$ is computed on the primitive half-range and doubled. Substituting $`u=\pi n^2/x^2`$ gives

```math
 \int_0^\infty G(x)\frac{dx}{x}
 =\pi^{-1/4}\sum_{n\ge1}\frac{\chi_d(n)}{\sqrt n}\,
          \Gamma(1/4,\pi n^2/d).
```

The upper incomplete gamma tail uses $`\Gamma(1/4,u)\le u^{-3/4}e^{-u}`$. Its contribution is less than $`10^{-18}`$. The deletion factor at the centre multiplies this whole-line integral.

For the positive mass, interpolate $`G`$ on a mesh in $`\log x`$ of step $`1/512`$. Differentiate a single Gaussian twice in that variable. Its multiplier is $`4u^2-6u+1/4`$. Since $`(4u^2+6u+1/4)e^{-u/2}<14`$ and $`\sum_{n\ge1}e^{-\pi n^2/(2x^2)}\le x/\sqrt2`$, the primitive second derivative has absolute value at most $`10d^{1/4}`$ after reflection. The same bound times $`\sum_{j\mid q}j^{-1/2}`$ covers $`H_q`$. Linear interpolation with curvature $`M`$ costs at most $`Mh^2/8`$ per value. The verifier uses $`Mh^2/7`$ for each of the two interpolations, allowing for ball overlaps at mesh knots. On each cell, the positive part of the endpoint mean bounds the integrated positive part of its chord from below after multiplication by the step. The mean of the positive endpoint parts bounds it from above. The discarded log tails have total absolute mass below $`10^{-55}`$ for $`q=1,30`$ by the Gaussian estimate at $`x\le e^{-2}`$ and reflection.

The signed integral and the positive-mass enclosure give $`N/P=1-(P-N)/P`$. The verifier also integrates the negative part and checks compatibility with the independent incomplete-gamma evaluation. The [standard-library verifier](scripts/independent.py) checks the integer examples and the two pointwise Gaussian signs. [Recorded output](evidence/check.txt)

## Lean and replay

[Balance.lean](Balance.lean) checks six supporting lemmas. The original four cover the signed cosine integral, a finite weighted witness, the budget in the ordered recovery proof and the numerical margins for the exponent 8. `negative_prefix_of_dilates` and `mass_ratio_order` support the sieve-choice theorem. The functional equation, the use of Chandee's bound, the microscopic zero implication, the ordered recovery and the number-theoretic theorem are proved in [PROOF.md](PROOF.md).

Run the following from this result's directory. The optional second command uses a built Mathlib checkout at the linked revision, with its Lean toolchain on the path.

```sh
python3 -m pip install -r requirements.txt
sh verify-release.sh
sh check-lean.sh /path/to/mathlib4
```

[Compiler and Mathlib revision](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474) · [Lean output](evidence/lean.txt) · [Contents and hashes](SHA256SUMS)
