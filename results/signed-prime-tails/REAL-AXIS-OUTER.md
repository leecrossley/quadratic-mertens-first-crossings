# What genuine Yokoi fields can do away from the centre

Assume RH and the critical-line property for the primitive quadratic characters considered. Write $`H_d=L'/L(\,\cdot\,,\chi_d)`$ for the Dirichlet factor with its conductor and gamma factor removed. Let $\mathcal D(D)$ be the squarefree $d=n^2+4\le D$ with $n$ positive and odd.

**Proposition.** Fix a compact set $C$ in $\Re s>1/2$, a tolerance $\epsilon>0$ and a finite set of primes. A positive lower proportion of the fields in $\mathcal D(D)$ have the same values of the character as $\chi_5$ at the specified primes and satisfy

$$
 \sup_{s\in C}|H_d(s)-H_5(s)|\lt\epsilon.
$$

There is consequently a sequence $d_j\to\infty$ on which $H_{d_j}\to H_5$ locally uniformly throughout this half-plane and $F_{d_j}\to F_5$ uniformly on every compact interval of real starts $y\ge2$. For each fixed $Y$, eventually $F_{d_j}$ is positive on $[2,Y]$. The order of quantifiers matters. The proof gives no positivity through $d_j^a$ for a fixed $a>0$.

## Proof

Choose a bounded region containing a fixed neighbourhood of $C$ with $\Re s\ge1/2+\delta$, $\delta>0$. By partial summation of the field GRH bound
$|\sum_{p\le u}\chi_d(p)\log p|\ll\sqrt u(1+\log u)(\log(3d)+\log u)$, the prime terms of $-H_d(s)$ beyond $Y$ on this region cost

$$
 O_C\big(Y^{-\delta}(1+\log Y)(\log(3d)+\log Y+1)\big).
$$

The implicit constant also depends on the chosen region and $\delta$. The expansion in increasing prime order, with the higher powers absolutely convergent, holds by analytic continuation from $\Re s>1$. Take $Y=(\log(3D))^{4/\delta}$ so the error tends uniformly to zero for $d\le D$. For $H_5$ the same bound with fixed conductor makes the prime tail beyond $B$ tend to zero with $B$. For either character the terms with prime base $p>B$ and exponent at least two are $O_\delta(\sum_{m>B}(\log m)m^{-1-2\delta})=o_\delta(1)$. [Prime-sum estimate and derivation](PROOF.md#the-future-integral-of-the-prime-power-error)

Take $B\ge5$ larger than the specified primes and condition on $E_B$, agreement with $\chi_5$ at every prime through $B$. Dahl and Kala's independent local variables $X_p$ for $(2k+1)^2+4$ have $X_2=-1$, $|\mathbb E X_p|\ll1/p$ for odd $p$, and positive probability for each prescribed local value. In particular $X_5=0$ has positive probability. This also follows from the allowed squarefree local class $n=1$ at every prime. For fixed $B$ let $c_B>0$ be the product of these probabilities. The indicator of each prescribed value is a polynomial of degree at most two on $`\{-1,0,1\}`$, so the indicator of $E_B$ is a finite linear combination of $\chi_d(m)$ with $m$ depending only on $B$. [Dahl and Kala, Proposition 14](https://arxiv.org/pdf/1611.02424#page=11) [Local laws in this family](../yokoi-mertens-long-positive-intervals/PROOF.md#2-biasing-many-primes-a-little)

For uniform counting measure on $\mathcal D(D)$ the proposition of Dahl and Kala compares the mean of $\chi_d(m)$ to that of the completely multiplicative model $X(m)$ with error $O(m^{2/3}D^{-1/6}\log D)$. In particular $\Pr(E_B)\to c_B$. For
$T_d(s)=\sum_{B<p\le Y}\chi_d(p)\log(p)p^{-s}$, expand $\mathbf1_{E_B}|T_d(s)|^2$. Each character argument is at most $C_B Y^2$ and the sum of the absolute coefficient sizes is at most $C_B Y^2(\log Y)^2$. The total comparison error tends to zero for fixed $B$, uniformly on the region. Independence of the model above $B$, with $\sigma_0=1/2+\delta$, gives

$$
 \limsup_{D\to\infty}\ \sup_s\ \mathbb E_D(|T_d(s)|^2\mid E_B)
 \le \sum_{p>B}\frac{(\log p)^2}{p^{2\sigma_0}}
       +O\left(\left(\sum_{p>B}\frac{\log p}{p^{1+\sigma_0}}\right)^2\right).
$$

Indeed diagonal variances are at most one and the remaining term is the squared mean. The $c_B$ from the model numerator cancels with the conditional denominator **before** increasing $B$. The right side tends to zero. A fixed small disk around any point of $C$ lies in the chosen region. The area mean inequality for $|T_d|^2$ bounds its supremum on $C$ by a constant times its integral over the region. The same small bound therefore applies to the conditional mean of the squared supremum. Choose $B$ large enough, then $D$ large enough. Markov's inequality leaves at least half the conditioned fields with small enough $T_d$ on $C$. The prime powers at bases through $B$ match exactly. Together with the tail bounds this proves the positive-lower-proportion assertion.

Exhaust the half-plane by compact rectangles and prescribe all primes through successive integers with tolerances tending to zero. Choose increasing $d_j$ from the sets just obtained. Then $L(2,\chi_{d_j})\to L(2,\chi_5)$ by absolute convergence of the Euler product and local matching. Integrating $H_{d_j}$ along $[1,2]$ gives convergence of the logarithms of $L(1)$ as well. For each fixed $T$ the prime-ideal products through every $t\le T$ match for large $j$, since all rational primes through $T$ match. Uniformly along the sequence $|B_{d_j}(t)|\ll 1+\log t$ on $t\ge2$ by bounding the prime product by two ordinary prime products and using boundedness of $\log L(1,\chi_{d_j})$. For $y$ in a fixed compact interval the integrated tail beyond $T$ is then $O((1+\log T)/T)$ with a compact-dependent constant. This proves compact convergence to $F_5$. The continuous function $F_5$ has a strictly positive minimum on each such interval. [Positivity for all starts in discriminant five](../yokoi-mertens-positive-averages-5-13/PROOF.md)

The conductor-matched models in the [real-axis test](REAL-AXIS.md#two-patterns-that-pass-the-test) have this same limit for their uncompleted logarithmic derivatives on fixed compact sets. Establishing either model's microscopic zero pattern for an actual field is a separate open step.
