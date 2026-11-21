# What the exceptional traces require of actual primes

Use the hypotheses and notation of the [real-axis test](REAL-AXIS.md). Let $\phi$ be real, smooth and supported in a fixed $[\alpha,\beta]\subset(0,\infty)$. Put

```math
 S_d(\phi)=\frac1L\sum_p \frac{\chi_d(p)\log p}{\sqrt p}\,
       \phi\!\left(\frac{\log p}{L}\right).
```

Only primes in $[(3d)^\alpha,(3d)^\beta]$ occur. Split primes enter positively, inert primes negatively, and ramified primes contribute zero.

**Local identity.** Uniformly over positive fundamental discriminants tending to infinity,

```math
 \int \phi(v) f_d(Lv)\,dv=-\frac43 S_d(\phi)
                 +O_\phi\!\left(\frac1{\log L}\right),\qquad L=\log(3d).
 \tag{1}
```

In particular, for a fixed nonnegative $\phi$, a positive split-prime excess larger than $C_\phi/\log L$ forces $F_d(y)<0$ at some starting point **inside the same interval of powers**. The constant is independent of central zeros. The opposite sign gives a positive start. A finite set of weights admitting such a positive excess in every large Yokoi field would give one exponent for the family. The calculation below establishes the identity without prescribing the signs of the prime sums.

## Proof of the error bound

First $P_d(1)\ll L/\log L$. In the centered square-sinc explicit formula take $H=\log L$. The conductor term is $O(L/H)$, the gamma term is $O(1/H)$ and the absolute contribution of the prime powers is $O(e^{H/2})$, by bounding $\Lambda(n)\le\log n$ through $e^H$. Each zero with $|\gamma|\le1/H$ contributes at least $1/2$ to the square-sinc sum. At the remaining zeros,
$(1+L^2\gamma^2)^{-1}\ll H^2 L^{-2}(1+\gamma^2)^{-1}$. The sum of the latter unscaled weights is $O(L)$ by the completed derivative at 2. This proves the assertion independently of any sign assumption. [Centered explicit formula (2)](PRIME-TEST.md) · [Unscaled mass](PROOF.md#the-future-integral-of-the-prime-power-error)

Write $\widehat\phi_+(t)=\int\phi(v)e^{itv}dv$, $c_0=4/3$, and
$W_d(\phi)=\sum_{\gamma\in\chi_d}\Re\widehat\phi_+(L\gamma)$. For the coefficient $c_\gamma$ in the fixed zero sum one has $|c_\gamma-c_0|\ll|\gamma|$ by differentiating its rational formula. The transform of $\phi$ decays faster than any power. Thus replacing every quadratic $c_\gamma$ by $c_0$ after integration costs $O_\phi(P_d(1)/L)$, using $|t\widehat\phi_+(t)|\ll_\phi(1+t^2)^{-1}$.

In the actual $f_d$ the coefficient is $h_\gamma(Lv)$. For $v\in[\alpha,\beta]$, its difference from $c_\gamma$ and the first two $v$-derivatives of that difference are $O_{\alpha,\beta}(|c_\gamma|/L)$. To see this, put $D_\gamma(s)=[(1/2-i\gamma+s)(3/2-i\gamma+s)]^{-1}$. Each of its first two derivatives on $s\ge0$ is bounded by an absolute constant times $|c_\gamma|$. The coefficient is $\int_0^\infty e^{-t}D_\gamma(t/(Lv))dt$. The mean value bound and the chain rule give the assertion, since the first two moments of $e^{-t}$ are finite. Two integrations by parts, or the direct bound at small frequency, now bound each integrated difference by $O_\phi(|c_\gamma|/(L(1+(L\gamma)^2)))$. The ordinary zeros contribute $O_\phi(L^{-2})$ after the same estimates, using their fixed gap and summability. The arithmetic remainder on the support is $2/3+O_\phi(1/L)$. Pairing signs gives

$$
 \int\phi(v)f_d(Lv)dv
     =\frac23\int\phi(v)dv+\frac43W_d(\phi)+O_\phi(1/\log L).
 \tag{2}
$$

Apply the even primitive quadratic explicit formula with zero test $h(t)=\int\phi(v)\cos(Ltv)dv$. Its inverse angular Fourier transform is $\phi(|u|/L)/(2L)$, with $\phi$ extended by zero outside its support. The conductor term vanishes since the support avoids zero. The gamma integral is $O_\phi(1/L)$ by rapid decay of $h(t)$ in $Lt$ and the digamma bound $O(\log(2+|t|))$. The prime-power contribution, with both sides of the even test, gives

```math
 W_d(\phi)=-\frac1L\sum_{p,k\ge1}
     \frac{\chi_d(p)^k\log p}{p^{k/2}}\,\phi(k\log p/L)+O_\phi(1/L),
```

where $p$ ranges over primes. The terms with $k\ge3$ cost $O_\phi(1/L)$ by absolute convergence. At $k=2$, partial summation of $\sum_{p\le t}\log p/p=\log t+O(1)$ gives $\tfrac12\int\phi+O_\phi(1/L)$ before the minus sign. Removing the ramified primes costs $O_\phi(e^{-\alpha L/2})$ since their logarithms sum to at most $\log d$. Substitution in (2) cancels the square contribution and proves (1). [Carneiro, Chandee and Milinovich, explicit formula (4.6)](https://arxiv.org/pdf/1503.00955#page=8) · [Mertens prime sum](https://doi.org/10.1215/ijm/1255631807)

## Two explicit requirements on genuine quadratic characters

Suppose a bounded-crowding sequence with arbitrarily long polynomial delays has limiting zero measure $2\sum_{k\in\mathbb Z}\delta_{4\pi k}$. Then for each $\phi$ as above,

```math
 S_d(\phi)\longrightarrow -\frac12\int\phi(v)\,dv-\sum_{k\ge1}\phi(k/2).
 \tag{3}
```

In fact $P_d(1)$ is bounded on this subsequence by the earlier counting theorem. The rapid decay of $\widehat\phi_+$ therefore controls its tails uniformly in $W_d$. Vague convergence deals with the compact part. Poisson summation gives $2\sum_{j\in\mathbb Z}\widehat\phi_+(4\pi j)=\sum_{k\in\mathbb Z}\phi(k/2)$. Only positive $k$ occur on this support. This proves (3) by the prime-power formula. The half-integers identify where that lattice would require additional inert-prime excess. [Bounded-count limit](NEAR-CENTRAL.md#a-test-using-values-on-the-real-axis)

For the crowded example just **two** measurement scales identify its normalized limit. Suppose $P_d(1)\to\infty$ and $P_d(2)/P_d(1)\to1/2$. Put $t=L\gamma$. The probability measure with masses $(1+t^2)^{-1}/P_d(1)$ has mean of $3t^2/(4+t^2)$ equal to $2P_d(2)/P_d(1)-1$. This nonnegative quantity tends to zero. The mass outside every fixed neighbourhood of zero therefore tends to zero. Testing against the bounded continuous function $(1+t^2)\Re\widehat\phi_+(t)$ gives $W_d(\phi)/P_d(1)\to\int\phi$. In particular

```math
 \frac{S_d(\phi)}{P_d(1)}\longrightarrow-\int\phi(v)\,dv .
 \tag{4}
```

This last implication does not require a delay assumption. Equations (3) and (4) are necessary arithmetic signatures of the specified patterns. Other progression or crowding limits may have different signatures. Current estimates do not give a violating weight in every large Yokoi field.
