# Negative averages on a fixed geometric grid

For odd $m\ge1$ with $d=m^2+4$ squarefree, let $K_d=\mathbb Q(\sqrt d)$, $\chi_d=(d/\cdot)$ and $\kappa_d=L(1,\chi_d)$. Put

$$
 B_d(t)=\sum_{N\mathfrak p\le t}-\log(1-1/N\mathfrak p)-\gamma-\log\kappa_d-\log\log t.
$$

Let $S_d=\inf\lbrace t\ge2:B_d(t)<0\rbrace$. For a start $y$ consider the two integrals

$$
 F_d(y)=\int_y^\infty B_d(t)\frac{y}{t}\frac{dt}{t},\qquad
 G_d(y)=\int_y^{Ky}B_d(t)\frac{y}{t}\frac{dt}{t}.
$$

The finite upper endpoint uses the grid ratio $K$ in the theorem. The infinite integral is absolutely convergent, for instance by the bound $1\le P_d(t)\le P_{\mathbb Q}(t)^2$ for the corresponding products.

**Theorem.** Assume the critical-line property for the Riemann zeta function (RH). There are absolute $y_0\ge 3$, integer $K\ge 4$ and constants $c,a,\beta,C>0$ with the following property. Let $D$ be sufficiently large, $b\ge y_0$, $J\ge1$ an integer and $R=bK^J$. Suppose

$$
 J(\log R+\log\log D)\le a\log D.
 \tag{1}
$$

Apart from a proportion at most $C e^{-cJ}$ of the squarefree Yokoi discriminants in $(D/2,D]$, at least $\beta J$ of the starts $y_j=bK^j$, $0\le j<J$, have **both** $F_d(y_j)<0$ and $G_d(y_j)<0$. At each such start the prime product lies below its main term at some point of $[y_j,Ky_j)$. The starting points are the same for every field in the shell.

**Corollary.** Assume RH. For absolute $\theta,c_1>0$, uniformly for $2\le X\le \exp(c_1\sqrt{\log D})$, the proportion of fields for which **none** of the grid windows with $b=y_0$ and $K y_j\le X$ succeeds is $O(X^{-\theta})$. This bounds the proportion with $S_d\ge X$ as well. Choose $J=\lfloor\log(X/y_0)/\log K\rfloor$ and reduce $c_1$ if necessary to obtain (1). The bounded initial range is absorbed into the implied constant. At the top of this range there are $O(\sqrt D\thinspace e^{-c_2\sqrt{\log D}})$ possible exceptions, for some $c_2>0$. They include every field that could fail a given fixed positive polynomial starting-point bound for sufficiently large $D$. The theorem leaves open whether any such failures occur.

## 1. A deterministic bound for the rational average

Write $B_{\mathbb Q}$ for the ordinary Mertens log error. We need

$$
 \int_y^\infty |B_{\mathbb Q}(t)|\thinspace y\thinspace dt/t^2\ll 1/(\sqrt y\log y).
 \tag{2}
$$

Writing $E(t)=\psi(t)-t$, Cramér's bound on the ordinary Riemann hypothesis gives $\int_x^{2x}|E(t)|dt\ll x^{3/2}$. Partial summation from $t$ to infinity gives the log error of $\sum_{p^k\le t}1/(kp^k)$ as $E(t)/(t\log t)-\int_t^\infty E(v)(1+\log v)/(v^2\log^2v)\thinspace dv$. Dyadic summation of Cramér's estimate bounds the latter integral absolutely by $O(1/(\sqrt t\log t))$. Averaging the boundary term with weight $y/t^2$ and again summing dyadically gives (2) for the prime-power sum. The omitted powers for $p\le\sqrt t$ sum to at most $2/t$ per prime, and for $p>\sqrt t$ to at most $2/p^2$ per prime. The prime number theorem makes their total $O(1/(\sqrt t\log t))$. This proves (2), also bounding the rational contribution on a truncated window. [Diamond and Pintz, (4.3)](https://www.numdam.org/item/10.5802/jtnb.687.pdf#page=7) · [Independent formal checks](https://math.mit.edu/~drew/grh/)

Set $V=R^{128}(\log D)^{128}$. Choose $a$ small enough that $V\le D/2$. The short Euler product through $V$ for $\log\kappa_d$ has additive error $O((\log D)V^{-1/32})$ outside at most $D^{1/4}$ primitive characters, by Granville and Soundararajan with $A=8$. Rational-prime factorisation gives exactly the ordinary product times $\prod_{p\le t}(1-\chi_d(p)/p)^{-1}$ times an inert correction $\prod_{\sqrt t<p\le t,\ \chi_d(p)=-1}(1-p^{-2})\le1$. In both averages write $k_p$ for the integral of the averaging measure from $y$ up to $p$ (capped at the finite endpoint when present). It vanishes for $p\le y$. For $y<p\le Ky$, **both** weights give $k_p=1-y/p$. For $p>Ky$ the two values are $1-y/p$ and $1-1/K$ respectively. This identity is the reason that both tests can be made to succeed at the same start.

In either integral, subtract the short Euler product multiplied by the mass of that integral. Each logarithmic factor for $y<p\le V$ then contributes $-k_p[-\log(1-\chi_d(p)/p)]\le-k_p\chi_d(p)/p$. Above $V$ the finite window has no terms. For the infinite window the extra terms have total absolute size $O(y\sum_{p>V}p^{-2})=O(y/V)$, permitting termwise integration. The inert correction has favourable sign. [Granville and Soundararajan, Proposition 2.2](https://arxiv.org/pdf/math/0206031#page=7)

Use the independent Dahl–Kala variables $T_p$ with their Yokoi splitting laws. For odd $p$ set $b_p=1+(-1/p)$, with the Legendre symbol. Then $\Pr(T_p=s)=p(p-b_p-s)/(2(p^2-b_p))$ for $s=\pm1$, and the remaining mass is at zero. The mean $\mu_p=-p/(p^2-b_p)$ and variance $v_p=1+O(1/p)$. Set $z_p=T_p-\mu_p$ in the model and $z_p=\chi_d(p)-\mu_p$ for actual fields. The mean correction costs $O(1/y)$. Thus for either average $A_d(y)$ and each nonexceptional field,

$$
 A_d(y)\le \frac{C_0}{\sqrt y\log y}
  +O(1/y+y/V+(\log D)V^{-1/32})-\sum_{y < p\le V}\frac{k_p z_p}{p}.
 \tag{3}
$$

All constants so far are uniform in $K\ge4$. [Dahl and Kala, §3 and Proposition 14](https://arxiv.org/pdf/1611.02424#page=11)

## 2. A shared contribution from each block

For $y=y_j$ write

$$
 \sigma_j^2=\sum_{y < p\le Ky}v_p(1-y/p)^2/p^2,\qquad
 U_j=\frac1{\sigma_j}\sum_{y < p\le Ky}(1-y/p)z_p/p.
$$

Uniformly in $K\ge4$ we have $\sigma_j^2\asymp1/(y\log y)$. For the lower bound use $2y<p\le4y$, where $1-y/p\ge1/2$. For the upper bound sum $p^{-2}$ beyond $y$. Both follow by the prime number theorem. Thus the error in (3) is at most $\sigma_j/8$ by taking $y_0,D$ large, using $y\le R$ and the choice of $V$ for the uniform short-product error. Let $T_{j,h}$ denote the remaining centered sum on $Ky<p\le V$, divided by $\sigma_j$, for either choice $h$ of kernel. Its coefficients are nonnegative and at most $1/(p\sigma_j)$. Hence

$$
 A_d(y_j)/\sigma_j\le 1/8-U_j-T_{j,h}.
 \tag{4}
$$

A window with $U_j>1/4$ that fails either strict inequality in the theorem therefore has $T_{j,h}<-1/8$ for at least one of the two kernels.

The $U_j$ are independent in the model, centered, and have variance one. For $u_0=1/4$ let $g(x)=(x-u_0)(x+1)^2$. There exist absolute $\lambda,\alpha>0$, independent of $K$, such that the nonnegative polynomial

$$
 P(x)=(1-\lambda g(x))^2
$$

is at least one for $x\le1/4$ and $\mathbb E P(U_j)\le1-\alpha$. Indeed $\mathbb E g(U_j)=3/2+\mathbb E U_j^3$. The absolute third moment of each centered summand, summed over the block, is at most its largest absolute bound times the sum of its variances. The resulting bound on $|\mathbb E U_j^3|$ is $O(\sqrt{\log y/y})$, by independence; thus $\mathbb E g(U_j)\ge1$. Also $\mathbb E g(U_j)^2\le C_1$ for an absolute $C_1\ge1$. One proof uses the elementary bounded-variable estimate $\mathbb E e^{sZ}\le e^{s^2 L^2/8}$ for centered $Z$ in an interval of length $L$. This follows because the second derivative of its log moment generating function is a tilted variance at most $L^2/4$. For $U_j$, the sum of squared interval lengths is bounded by $8$, using $v_p\ge1/2$, so all sixth moments are bounded uniformly. Set $\lambda=1/C_1$ and $\alpha=\lambda$, decreasing $\lambda$ if necessary so $\alpha<1$. Expansion of $P$ gives the required strict contraction. [Hoeffding, bounded independent variables](https://doi.org/10.1080/01621459.1963.10500830)

## 3. The cost of many bad remainders

For a fixed set $I$ of $n$ indices and one kernel $h$, write $T_I=\sum_{j\in I}T_{j,h}=\sum_{p\le V}b(p)z_p$. Uniformly in the set,

$$
 \sum_p b(p)^2\le C_2 n/K. \tag{5}
$$

For $i\le j$ the inner product of the two coefficient vectors is at most

$$
 (\sigma_i\sigma_j)^{-1}\sum_{p>Ky_j}p^{-2}
 \ll \frac1K\sqrt{\frac{y_i\log y_i}{y_j\log y_j}}
 \le \frac{C}{K} K^{-(j-i)/2}.
$$

Summing the geometric bound proves (5) with an absolute constant. By the same bounded-variable estimate,
$\mathbb E e^{sT_I}\le\exp(C_2s^2 n/(2K))$. A Chernoff bound and integration of the two-sided tail give

$$
 \mathbb E |8T_I/n|^{2n}\le 2(C_3/K)^n. \tag{6}
$$

Explicitly, use $\Pr(|T_I|>u)\le2\exp(-K u^2/(2C_2 n))$ and integrate $2n u^{2n-1}$, giving at most $2(2C_2 n/K)^n n!$ before multiplying by $(8/n)^{2n}$. This estimate allows overlaps between the far tails of different blocks.

## 4. Transferring the tests and counting the exceptions

Dahl and Kala's Proposition 14, subtracted at $D/2$ and $D$ and divided by the shell cardinality $\asymp\sqrt D$, gives

$$
 \mathbb E_{\rm shell}\chi_d(m)=\mathbb E T(m)+O(m^{2/3}D^{-1/6}\log D).
 \tag{7}
$$

Here $T(m)$ is extended completely multiplicatively. Products of the polynomials $P(U_j)$ over any subset and $(8T_I/n)^{2n}$ have expectations differing from their model values by at most $D^{-1/10}$ for sufficiently small absolute $a$ in (1). To see this, in the raw character expansion each single block or normalized tail sum has sum of absolute coefficients at most $O(V^2)$ and only indices at most $V$, since $\sigma_j^{-1}\ll\sqrt{R\log R}$ and $|\mu_p|\le1$. The sum $(8/n)T_I$ retains the same bound up to an absolute factor. The index bound for the required polynomials is $V^{6J}$ and their coefficient norm is at most $V^{C_4 J}$, with an absolute $C_4$. Apply (7) term by term. Shrink $a$ so the exponent coming from $O(J\log V)$ is at most $(\log D)/20$. This leaves the asserted error for all the tests. This comparison uses only the bounded degrees and coefficients. Model independence is never assumed for the actual characters.

Choose a small absolute $\epsilon>0$ depending only on $\alpha$, and put $n=\lfloor\epsilon J\rfloor$. Bounded $J$ can be covered by increasing $C$, so assume $n\ge\epsilon J/2$. If at most $4n$ blocks have $U_j>1/4$, some set of $J-4n$ blocks has $U_j\le1/4$ throughout. Its indicator is bounded by the product of $P(U_j)$ on that set. Independence in the model, (7), and a union bound give an upper probability

$$
 {J\choose 4n}\big((1-\alpha)^{J-4n}+D^{-1/10}\big).
$$

Choose $\epsilon<1/16$ small enough that $(eJ/(4n))^{4n}(1-\alpha)^{J-4n}\le e^{-c_3J}$ for some $c_3>0$, using $s\log(e/s)\to0$ as $s\downarrow0$.

If more than $4n$ blocks have $U_j>1/4$, but fewer than $n$ starts satisfy both negative inequalities, at least $n$ indices have the same type $h$ with $T_{j,h}<-1/8$, by (4) and the pigeonhole principle. For that subset $(8T_I/n)^{2n}\ge1$. Equations (6) and (7) bound the probability by

$$
 2{J\choose n}\big(2(C_3/K)^n+D^{-1/10}\big)
$$

outside the short-Euler-product exceptions. Choose the fixed integer $K$ large enough that $(2e/\epsilon)(C_3/K)<1/2$. This makes the first term exponentially small in $J$. The remaining errors cost $O(2^J D^{-1/10}+D^{-1/4})$. Since $R\ge K^J$, (1) implies $J\ll\sqrt{\log D}$, and these errors are $O(e^{-c_4J})$. All choices are consistent: the variance, polynomial and overlap constants were absolute for every $K\ge4$, then $\epsilon$ and $K$ were fixed, and $a$ can finally be reduced. This proves the theorem with $\beta=\epsilon/2$. A strictly negative finite integral forces a negative point before the last endpoint of its window.

One consequence is a bounded fractional moment for the truncated first successful grid endpoint. Let $W_d$ be the first endpoint $K y_j$ at which both tests succeed on the fixed grid $b=y_0$, with $W_d=\infty$ if none does. For $0<s<\theta$ and $R_D=\exp(c_1\sqrt{\log D})$, integrating the corollary gives $\mathbb E_{\rm shell}\min(W_d,R_D)^s=O_s(1)$. This statement only controls the moment up to the stated cutoff.
