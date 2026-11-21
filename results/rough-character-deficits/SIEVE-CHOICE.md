# Which small primes delay the first negative count?

Lee Crossley

In the field of discriminant $`d=1543^2+4=2{,}380{,}853`$, every choice among the 47 primes through $`(\log d)^2`$ gives a negative count by 49,937 and a subsequent positive count by $`d^6`$. Both changes meet the quantitative test in [the preceding theorem](PROOF.md). This statement about integers is unconditional.

| Multiples removed | First negative | First positive after it |
| --- | ---: | ---: |
| All 47 eligible primes | 331 | 367 |
| All 31 eligible inert primes | 49,937 | 49,943 |
| The same inert primes except 43 | 48,221 | 137,705,720,539 |

The middle row attains the latest possible first negative among all $`2^{47}`$ choices. The return takes six integers in that row. Keeping 43 stretches the wait to 137,705,672,318 integers. The maximum possible first recovery is still unknown.

## Comparing every choice with one sieve

Let $`\chi`$ be a nonprincipal real primitive quadratic character of positive fundamental discriminant $`d`$. Let $`\mathcal P`$ be any finite set of primes. A choice $`Q`$ is the squarefree product of a subset of $`\mathcal P`$, with the empty product allowed. Write

```math
 S_Q(n)=\sum_{\substack{j\le n\\(j,Q)=1}}\chi(j),\qquad
 E_Q(s)=\prod_{p\mid Q}(1-\chi(p)p^{-s}).
```

Put $`S_Q(0)=0`$. Let $`Q_*`$ remove the multiples of exactly those eligible primes for which $`\chi(p)=-1`$. A ramified prime has no effect. Define $`I`$ to be the eligible inert primes kept by $`Q`$ and $`R`$ the eligible split primes removed by $`Q`$. Then

```math
 \frac{E_*(s)}{E_Q(s)}
 =\prod_{p\in I}(1+p^{-s})\prod_{p\in R}(1-p^{-s})^{-1}
 =\sum_{a\ge1}k(a)a^{-s}.
```

Here $`k(a)=1`$ if all prime factors of $`a`$ belong to $`I\cup R`$ and each factor in $`I`$ occurs to exponent at most one. All other coefficients are zero. This finite-prime Euler product converges absolutely for $`\Re s>0`$. Coefficient comparison on $`\Re s>1`$ and summation to $`n`$ give the exact identity

```math
 S_*(n)=\sum_{a\le n}k(a)S_Q(\lfloor n/a\rfloor).
 \tag{1}
```

If the left side is negative, one of the prefixes on the right is negative. Thus $`Q_*`$ attains the largest first strictly negative index, with infinity permitted. Equivalently, there exists a choice keeping every prefix nonnegative through $`X`$ precisely when $`Q_*`$ does so. Equation (1) can average positive prefixes from before a first deficit. It gives no ordering of recovery times, as the last two rows illustrate.

There is also an exact optimum for the relative amount of negative mass. Let $`J_Q`$ be either the sharp profile $`S_Q(\lfloor x\rfloor)/\sqrt x`$ or the Gaussian profile $`x^{-1/2}\sum_{(n,Q)=1}\chi(n)e^{-\pi(n/x)^2}`$, with $`n\ge1`$. Write $`P_Q,N_Q`$ for the integrals of its positive and negative parts against $`dx/x`$. Multiplying the coefficient identity by the sharp or Gaussian weight gives

```math
 J_*(x)=\sum_a k(a)a^{-1/2}J_Q(x/a),\qquad
 K=\sum_a k(a)a^{-1/2}=\frac{E_*(1/2)}{E_Q(1/2)}.
 \tag{2}
```

The sharp primitive profile is integrable by periodicity and zero mean. The Gaussian primitive profile is integrable by quadratic theta reciprocity. Finite deletion preserves integrability, and (2) is absolutely convergent in the integral norm since $`K<\infty`$. Translation in $`\log x`$ preserves the measure. Taking positive parts and then integrating gives $`P_*\le KP_Q`$, whereas $`P_*-N_*=K(P_Q-N_Q)`$. All positive masses are nonzero, as the integer 1 supplies the leading term at the small end. If $`P_Q-N_Q\ge0`$, division gives

```math
 \frac{N_*}{P_*}\le\frac{N_Q}{P_Q}.
 \tag{3}
```

For each profile the sign of the signed mass is the sign of $`L(1/2,\chi)`$ by its Mellin transform. The inequality holds whenever that central value is nonnegative, in particular under quadratic GRH. If it vanishes, all the ratios equal 1. In the field of the table the signed mass is certified positive directly. The exact minimum of the full Gaussian ratio there lies strictly between **0.912 and 0.913**. Thus every choice retains more than 91.2% as much negative mass as positive mass. This ratio concerns areas under the Gaussian profile. The first two columns of counts concern integer prefixes.

## Both quantitative swings for all 140,737,488,355,328 choices

Take $`d=2{,}380{,}853`$, $`L=\log d`$, $`X=d^6`$ and $`c=1/1000`$. For each allowable $`Q`$, let $`m`$ be its first strictly negative index and put $`\tau=\log m`$. Then some integer $`n`$ satisfies

```math
 3\le m\le49{,}937,\quad m\lt n\le X,\quad
 S_Q(m)<-c\sqrt m/L,\qquad S_Q(n)>c\tau\sqrt n/L^2.
 \tag{4}
```

The exact computation for $`Q_*`$, followed by (1), proves the first deadline. Since $`c\sqrt{49937}<L`$, the first strict negative is also the first crossing of the quantitative threshold. When all 47 primes are removed, the positive count at 367 satisfies (4). Consider a proper subset from here on.

The primitive period computation gives $`\max_{0\le j<d}|S_1(j)|=1068`$. Inclusion-exclusion and periodicity give $`|S_Q(j)|\le1068\cdot2^{46}`$ for every $`j`$ and every proper subset. The real completed quadratic function has a zero at $`s=1/2+ig`$ with $`0.028<g<0.030`$. Only this single sign bracket is needed. Its existence follows by continuity from two certified evaluations. [Numerical details](SIEVE-CHECKS.md)

Write $`u=\log x`$, $`H=6L`$ and $`V(u)=e^{-u/2}S_Q(\lfloor e^u\rfloor)`$. The sharp Mellin transform gives

```math
 \int_0^\infty V(u)e^{-igu}\,du
 =\frac{L(1/2+ig,\chi)}{1/2+ig} E_Q(1/2+ig)=0.
```

Consequently the integral against $`W(u)=\sin(g(\tau-u))/g`$ is zero. On $`[0,H]`$ the weight has the sign of $`\tau-u`$ since $`0.030H<\pi`$. Before $`\tau`$ the count is nonnegative. On $`[0,\log 2)`$ it equals 1. There $`g\tau<1/3`$, giving $`W(u)\ge0.98(\tau-u)`$. The initial contribution is greater than $`0.40\tau`$, since

```math
 0.98\int_0^{\log 2} e^{-u/2}(1-u/\log 3)\,du>0.40,\qquad \tau\ge\log3.
```

If the required positive count were absent, then $`V(u)\le c\tau/L^2`$ on $`[\tau,H]`$. This uses $`\sqrt{\lfloor e^u\rfloor}\le e^{u/2}`$. As $`|W(u)|\le u-\tau`$ there, the negative contribution costs at most $`c\tau H^2/(2L^2)=0.018\tau`$. The remainder beyond $`H`$ has absolute value at most

```math
 \frac{2\cdot1068\cdot2^{46}}{0.028\,d^3}<0.401.
```

But $`(0.40-0.018)\log3>0.401`$. The full integral would be positive, proving (4).

The constants in (4) also fit the sufficiently-large-field argument with endpoint $`d^8`$ in the preceding theorem. For the sharp profile, the positive mass from $`1\le x<2`$ alone exceeds $`0.58`$. The cost of suppressing the first deficit is $`8c=0.008`$. The initial constant $`c_3`$ in the ordered recovery proof exceeds $`0.13`$ by restricting to $`1\le x\le3/2`$. Its combined cost is $`8c/2+64c/2=0.036<c_3/2`$. The earlier proof absorbs the vanishing tails by increasing its absolute delay threshold. This fixes specific sizes for the two swings in the comparison. [Ordered deficit and recovery](PROOF.md#an-ordered-deficit-and-recovery)

## The choice that keeps 43

For $`Q=Q_*/43`$, the count takes value $`-1`$ at 48,221. It then takes only nonpositive values through 137,705,720,538 and first reaches $`+1`$ at the next integer. The first crossing of the positive threshold in (4) is **137,705,727,787**, where the count reaches 19. That threshold lies strictly between 18 and 19 throughout the interval between these last two witnesses. The full integer sweeps check each prefix or rule it out by bounding all prefixes of its block. A third computation evaluates the six endpoint counts by summing primitive prefixes at the squarefree divisors of $`Q`$. [Checks and replay](SIEVE-CHECKS.md)

## Consequence for the family

For the future prime-ideal Mertens average $`F_d(y)=\int_y^\infty B_d(t)y\,dt/t^2`$, the question is whether one absolute $`a`$ supplies a negative value at some $`2\le y\le d^a`$ in every sufficiently large Yokoi field. The extremal sieve answers the first strict-sign selection question in every field. For the mass criterion a fixed gap below 1 for its ratio in every sufficiently large field would suffice, by (3) and the earlier theorem.

There is a structural restriction on the proposed arithmetic route. Under the critical-line hypotheses of the earlier theorem, if the nearest quadratic zero has ordinate $`g`$ with $`g\log d`$ sufficiently small, its transform forces **both quantitative swings for every choice** by $`d^8`$. This includes a zero at the centre, where the signed mass also vanishes for every choice. The proof only needs the small ordinate at this step, irrespective of how long the prime average stays positive. A family-wide proof that works by choosing a missing swing would therefore have to rule out such fields at large discriminant. [Earlier transform argument](PROOF.md#cancellation-on-reciprocal-scales)

Conversely, if $`g\ge\kappa/\log d`$ with one $`\kappa>0`$ throughout these sufficiently large fields, the earlier bound $`\exp(C(\log(3d)+1/g))`$ already gives a negative prime average by $`d^{O(1+1/\kappa)}`$. Thus the gap a universally successful missing-swing sieve would imply is itself sufficient for the prime-average target. Its existence and the fixed-exponent crossing remain open. [Nearest-zero theorem](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/cae0113ded2504f0f29857045ca2a3028ddaab55/results/signed-prime-tails/NEAREST-ZERO.md)
