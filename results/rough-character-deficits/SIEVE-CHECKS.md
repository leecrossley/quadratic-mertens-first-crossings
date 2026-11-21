# Verifying the sieve comparison

The theorem and the two exact recovery examples are in [SIEVE-CHOICE.md](SIEVE-CHOICE.md). Run the following from this directory with Python 3.11 or later and a C++20 compiler.

~~~sh
python3 -m pip install -r requirements.txt
sh verify-release.sh
~~~

The long Python sweep processes every block through 137,705,727,787. It takes several minutes on a single core. The separate C++ sweep uses 64 integers to a word. The analytic certificate for all choices uses one period of the primitive character and two transform signs. It avoids enumerating the $`2^{47}`$ subsets. [Recorded results](evidence/sieve-choice.txt)

## Integer counts

The first verifier enumerates primes through $`\lfloor(\log d)^2\rfloor`$ with Arb and FLINT, evaluates Jacobi symbols, checks the first deficits and recoveries of the two reference sieves, and measures the largest absolute primitive prefix over its whole period. A second program constructs the full table of nonzero squares directly. For the choice that keeps 43 it checks the six integers bordering the three crossings by summing $`S_1(\lfloor n/j\rfloor)`$ over squarefree divisors $`j`$ of the deleted product. Every sign in this divisor expansion is positive because all the deleted primes are inert. Periodicity reduces every primitive prefix to one table lookup. [Jacobi and interval verifier](scripts/sieve_choice.py) · [Divisor and incomplete-gamma verifier](scripts/sieve_independent.py)

The two long sweeps follow the integer count in order. The Python version constructs the squares as the orbit of the square of a generator modulo $`d`$ and builds independent periodic bitsets for groups of deleted primes. It excludes every multiple of $`d`$. In a block with $`U`$ positive scores and $`D'`$ negative scores, every prefix stays between the incoming count minus $`D'`$ and the incoming count plus $`U`$. When these bounds permit a first crossing it bisects the block until the position is certified. The C++ version generates the squares by squaring each representative through $`(d-1)/2`$, groups the primes in reverse order and examines individual set bits in any 64-integer word that can cross. Both find the same first $`-1`$, subsequent $`+1`$ and subsequent $`+19`$. [Python sweep](scripts/long_recovery.py) · [C++ sweep](scripts/long_recovery.cc)

## Gaussian integral for a zero

Write $`G(u)=H_1(e^u)`$ in this note, so $`G(u)=G(L-u)`$ with $`L=\log d`$. With $`w=\pi n^2 e^{-2u}`$ the first two derivatives of each primitive term with respect to $`u`$ have multipliers $`2w-1/2`$ and $`4w^2-6w+1/4`$. For $`j=0,1,2`$ the bounds on $`|G^{(j)}(u)|`$ for $`u\le L/2`$ are respectively $`(1/2)e^{u/2}`$, $`4e^{u/2}`$ and $`10e^{u/2}`$. The last follows from $`(4w^2+6w+1/4)e^{-w/2}<14`$ and $`\sum_{n\ge1}e^{-\pi n^2/(2x^2)}\le x/\sqrt2`$. The first derivative bound follows from $`(2w+1/2)e^{-w/2}<3`$. Reflect for $`u>L/2`$. Thus the three integral norms are at most $`2d^{1/4},16d^{1/4},40d^{1/4}`$.

For $`0\le t\le0.030`$ the real transform is

```math
 C(t)=\int_{\mathbb R}G(u)\cos(t(u-L/2))\,du .
```

Symmetry makes the corresponding sine integral vanish. The Mellin identity in [the original proof](PROOF.md#the-reciprocal-transform) expresses this centred transform as the completed quadratic function times a nonzero factor. Its integrand has second-derivative integral norm below $`42d^{1/4}`$. On any mesh of width $`h`$, the integral of the absolute error of piecewise linear interpolation is at most $`h^2\|f''\|_1/8`$. Indeed the absolute interpolation error on each interval is bounded by the integral of its Dirichlet Green kernel against $`|f''|`$. Integrating the kernel in its first variable gives $`(v-a)(b-v)/2\le h^2/8`$ on $`[a,b]`$.

Use $`h=1/2048`$ and nodes from $`-2`$ through the first mesh point at or beyond $`L+2`$. On the left discarded tail, putting $`w=\pi e^{-2u}`$ bounds the integral of $`|G|`$ by $`\pi^{-1/4}\int_{\pi e^4}^\infty w^{-3/4}e^{-w}\,dw<10^{-65}`$. Here the absolute Gaussian series is at most $`2e^{-w}`$ before its normalising factor. Reflection gives the same right-tail estimate. The node values come from the truncated Gaussian with an Arb enclosure, as in [the earlier checks](CHECKS.md#gaussian-enclosures). Each is replaced by a multiple of $`1/B`$ with verified error below $`2/B`$, where $`B=2^{46}`$. The two endpoints are set to zero with error below $`1/B`$. The signed trapezoid areas at $`t=0.028`$ and $`0.030`$ exceed the total error $`42d^{1/4}h^2/8+100/B+10^{-60}`$ in opposite directions.

A separate calculation uses the split incomplete-gamma series for the very same integral. With $`s=1/2+it`$ it is

```math
 C(t)=\Re\left(e^{itL/2}\pi^{-s/2}
 \sum_{n\ge1}\chi(n)n^{-s}\Gamma(s/2,\pi n^2/d)\right).
```

This is twice the real part of the integral on $`u\le L/2`$, after the substitution $`w=\pi n^2 e^{-2u}`$. For $`z=\pi/d`$ and $`M=8000`$ the absolute omitted tail is at most

```math
 \frac{(zM^2)^{-3/4}e^{-zM^2}}{\pi^{1/4}\sqrt M\,2zM}<10^{-35}.
```

Indeed $`|\Gamma(s/2,w)|\le w^{-3/4}e^{-w}`$, and the remaining Gaussian sum is bounded by its decreasing integral. Arb certifies opposite signs at 0.02849001 and 0.02849002. The narrower bracket was already known in this field. The new computation rechecks the input to the all-sieve recovery bound. [Earlier bracket and evaluations](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/cae0113ded2504f0f29857045ca2a3028ddaab55/results/fixed-weight-delay-2380853/QUADRATURE.md)

## The optimum Gaussian mass without expanding two billion terms

For each of the 31 inert primes put $`r_p=1/(1+\sqrt p)`$. In $`\log x`$, the normalised Gaussian profile $`H_*/E_*(1/2)`$ is the expectation of $`G`$ translated by the sum of independent shifts. The shift for $`p`$ is $`\log p`$ with probability $`r_p`$ and zero otherwise. Its signed integral is exactly the primitive signed integral $`C(0)`$, which the [incomplete-gamma verifier for the primitive mass](scripts/verify.py) encloses directly.

To enclose the positive mass, condition on which primes shift. For each selected prime round $`\log p`$ independently to one of its two neighbouring mesh points, with the probabilities that preserve its mean. The total rounding error $`\Delta`$ has conditional mean zero and unconditional second moment at most $`h^2\sum r_p/4`$. Taylor's formula with integral remainder, integrated over all translates of $`G`$, bounds the resulting integral-norm error by $`\|G''\|_1\mathbb E(\Delta^2)/2`$. Replacing $`G`$ itself by its continuous piecewise linear interpolant costs at most $`h^2\|G''\|_1/8`$, apart from the discarded tails and rounding of samples. Translations and probability mixtures preserve or decrease the integral norm.

The rounded translations are now exact mesh shifts. Each prime uses three nonnegative integer weights with sum $`B`$. For the two nonzero shifts each weight divided by $`B`$ differs from its true probability by less than $`2/B`$. The total absolute error across all three weights is at most $`8/B`$. Every stored ordinate has absolute value below 21. Thus a stage costs at most $`(8\cdot21+1)/B`$ in supremum norm, allowing also for rounding the new ordinate. The initial sample error is below $`3/B`$ and the entire rounded support has length below 250. Combining the errors gives

```math
 \frac{40d^{1/4}h^2}{8}\left(1+\sum_{p\mid Q_*}r_p\right)
 +\frac{250(3+31\cdot169)}B+10^{-60}.
```

On each final affine cell, the positive part of the endpoint mean bounds the mean positive part from below. The mean of the positive endpoint parts bounds it from above. Widen the resulting areas by the displayed error to enclose the positive mass $`P`$ of the normalised profile. Then $`1-C(0)/P`$ lies in $`(0.912,0.913)`$. The comparison theorem proves this is an enclosure for the minimum over every prime selection. [Mass certificate](scripts/sieve_choice.py)

## Formal checks and scope

The two added Lean lemmas check the earlier negative-prefix implication for nonnegative dilations and the inequality between mass ratios. The Euler-factor argument, the use of the zero, the recovery deadline and the interpolation estimates are written proofs. The full replay checks the numerical hypotheses for this field. [Lean source](Balance.lean) · [Lean output](evidence/lean.txt) · [Prior work](PRIOR-WORK.md)
