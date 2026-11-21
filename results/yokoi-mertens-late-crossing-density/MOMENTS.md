# A tail estimate uniform in the discriminant shells

Use the notation of the [frequency theorem](PROOF.md). Let $R=X\exp(a\sqrt u)$ with fixed $a>0$, $u=\log X$. For the estimate on moving shells assume $u\to\infty$, $L=\log\log D$, and

$$
 R\le(\log D)\exp(-c_0\sqrt L)
 \tag{5}
$$

for some fixed $c_0>0$. Every use of this estimate in the main proof or the conditional shape satisfies (5). The model estimate holds for all large $u$.

In the independent model subtract $\mu_p=\mathbb E T_p=O(1/p)$ from each sign. A centred sign obeys $\mathbb E\exp(v(T_p-\mu_p))\le \exp(v^2/2)$ for real $v$. Indeed the second derivative of its log moment-generating function is the variance under exponential tilting, at most 1 for a variable in $[-1,1]$. Integrate twice from zero. By independence, exponential Markov and optimisation over $v$, a sum over $t<p\le V$ with coefficients $1/p$ has two-sided tail at level $z$ at most $2\exp(-z^2/(2\sum p^{-2}))$. Integrate this probability against $2k z^{2k-1}\thinspace dz$ and use $k!\le k^k$. For $k\ge1$

$$
 \left\Vert\sum_{t < p\le V}T_p/p\right\Vert_{2k}\le C\sqrt{k/t}+C/t.
 \tag{6}
$$

All constants in the moment estimates are absolute. The mean has been restored. The bound passes to $V=\infty$ by convergence in probability and Fatou.

In the model the norm factorisation gives $B(t)=-\sum_{p>t}T_p/p+O(e^{-c\sqrt{\log t}}+t^{-1/2})$, by the effective ordinary prime number theorem, the inert-square correction and the quadratic remainder in the log factors. Thus by Minkowski's inequality both $|B(R)|$ and $\int_R^\infty|B(t)|dt/t$ have $L^{2k}$ norms at most

$$
 C_1\big(\sqrt{k/R}+e^{-c_1\sqrt{\log R}}\big).
 \tag{7}
$$

In the integral one uses $\int_R^\infty t^{-1/2}\thinspace dt/t=2/\sqrt R$ and absorbs the polynomial factor in the integral of the exponential term by reducing $c_1$. Taking $k=\lfloor c_2R/u^2\rfloor$ with $c_2$ small makes the right side at most $1/(2u)$. Markov's inequality and a union bound show that the probability that either quantity exceeds $1/u$ is $O(\exp(-c_3 R/u^2))$.

For actual fields set $V=(\log D)^{128}$ and $Z_t=\sum_{t<p\le V}\chi_d(p)/p$. The normalised shell expectation of $Z_t^{2k}$ differs from the model moment by at most

$$
 E_{D,k}\ll D^{-1/6}\log D\thinspace V^{4k/3}
        \left(\sum_{p\le V}1/p\right)^{2k}.
 \tag{8}
$$

Expand the power. The largest character index is $V^{2k}$, and the displayed coefficient sum bounds the total absolute expansion. Dahl and Kala's count and moment comparison apply after subtracting the two endpoints of the shell. [Proposition 14](https://arxiv.org/pdf/1611.02424#page=11)

For $k=\lfloor c_2R/u^2\rfloor$ in (5), $kL=o(\log D)$. To see this, if $u\ge\sqrt L$ then $kL\ll R=o(\log D)$. If $u<\sqrt L$, then $R\le\exp(O(\sqrt L))$. Thus $E_{D,k}\le D^{-1/8}$ for all sufficiently large $D$. The actual $L^{2k}$ norm in (6) incurs at most $D^{-1/(16k)}$ extra. Apart from $O(D^{1/4})$ primitive characters, for $R\le t\le V$ the field error satisfies

$$
 |B_d(t)|\le |Z_t|+C\big(e^{-c\sqrt{\log t}}+t^{-1/2}+(\log D)^{-3}\big).
$$

This is obtained by truncating the quadratic Euler product via Granville and Soundararajan and using the rational norm factorisation. Beyond $V$, the quadratic pointwise bound gives $\int_V^\infty |B_d(t)|\thinspace dt/t\ll(\log D+\log V+1)/\sqrt V$ for every field. [Euler products, Proposition 2.2](https://arxiv.org/pdf/math/0206031#page=7) · [Details of both error estimates](https://github.com/leecrossley/yokoi-mertens-crossing-lookahead/blob/v1.0.0/FAMILY.md)

Multiply either controlled quantity by the indicator of the nonexceptional set. Applying Minkowski over $R\le t\le V$ gives (7) with the additional error

$$
 O\big((1+\log V)(D^{-1/(16k)}+(\log D)^{-3})
        +(\log D+\log V+1)/\sqrt V\big)=o(1/u).
$$

Here $\log D/k$ grows faster than $L$ and $u=O(L)$. The nonexceptional indicator can be used inside the integral and discarded on the nonnegative $|Z_t|$ bound. Choose $c_2$ smaller if necessary and apply Markov. The exceptional set has proportion $O(D^{-1/4})$ in the shell, since the discriminants give distinct primitive characters and their shell count is $\asymp\sqrt D$. This proves the asserted probability bound including that error.

For the fixed-$`R`$ tightness step, repeat the calculation with $k=1$ and let $D\to\infty$. Equation (8) tends to zero even after taking a square root and multiplying by $\log V$. The remaining norms are bounded by $C_1(R^{-1/2}+\exp(-c_1\sqrt{\log R}))$ on the nonexceptional set. Its complement has vanishing proportion. This gives exactly the uniform-in-probability tail statement used to pass from a finite prime prefix to the whole primitive.
