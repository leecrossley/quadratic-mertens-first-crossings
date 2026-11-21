# Prescribing a first crossing and the earliest successful start

For odd positive $m$ with $d=m^2+4$ squarefree put $K_d=\mathbb Q(\sqrt d)$ and $\kappa_d=L(1,\chi_d)$, the residue of its Dedekind zeta function. Write $q=N\mathfrak p$, with one factor per prime ideal, and let

$$
 P_d(t)=\prod_{q\le t}(1-1/q)^{-1},\qquad
 B_d(t)=\log P_d(t)-\gamma-\log\kappa_d-\log\log t.
$$

Let $S_d=\inf\lbrace t\ge2:B_d(t)<0\rbrace$. Let $Y_d$ be the infimum of $y\ge2$ for which some bounded, measurable, nonnegative, nonincreasing $w$ on $[y,\infty)$ has negative integral against $B_d(t)\thinspace dt/t$. All integrals in this definition converge absolutely by the bound in §1. We allow an infimum of $+\infty$. A factor at a jump is included in the product.

**Theorem.** Assume the critical-line property for the Riemann zeta function and $L(s,\chi_d)$ for the quadratic discriminants in the theorem (field GRH). Fix $0<r\le1$ and $0<\eta\le r/4$. There exist $c,C>0$, depending only on these choices, such that for every sufficiently large $D$, setting $X=2^{\lfloor c(\log D)^{1/5}\rfloor}$, at least

$$
 \sqrt D\thinspace\exp\lbrace-C(\log D)^{4/5}\rbrace
$$

squarefree Yokoi discriminants $D/2<d\le D$ satisfy

$$
 (r-\eta)X\le Y_d\le rX,\qquad X < S_d<(1+\eta)X,\qquad
 \int_{rX}^\infty B_d(t)\frac{rX}{t}\frac{dt}{t}<0.
$$

The interval average from $rX$ to $(1+\eta)X$ is also strictly negative, using weight one. The exponent of the decreasing power weight is always one.

**Corollary.** The ratios $Y_d/S_d$ have every point of $[0,1]$ as a subsequential limit along fields whose waits exceed every fixed power of $\log d$ and lie below every fixed positive power of $d$. For a prescribed point, choose $r_j$ tending to it from $(0,1]$ and $\eta_j\downarrow0$ with $\eta_j\le r_j/4$. Choose successive shells so large that $X_j>(\log D_j)^j$ and $2X_j<(D_j/2)^{1/j}$. The ratio is squeezed between $(r_j-\eta_j)/(1+\eta_j)$ and $r_j$. A negative point has a negative right neighbourhood, so in general $Y_d\le S_d$ whenever $S_d$ is finite. The theorem constructs fields within each shell and gives no guarantee for an arbitrarily specified field.

## 1. Reducing the product to a prime tail

Write $G(t)=\log t/\sqrt t$, $V=X^{128}$. We use the critical-line theorems for the ordinary and primitive quadratic Dirichlet factors of $\zeta_{K_d}(s)=\zeta(s)L(s,\chi_d)$. The statements and independent kernel checks are available from MIT. The argument here is an analytic proof using those results. [Formal statements and audit](https://math.mit.edu/~drew/grh/)

Factor each rational prime in the quadratic field. The ratio of $P_d(t)$ to the ordinary rational Mertens product times $\prod_{p\le t}(1-\chi_d(p)/p)^{-1}$ is $\prod_{\sqrt t<p\le t,\ \chi_d(p)=-1}(1-p^{-2})$. Its log is $O(t^{-1/2})$. On the ordinary critical-line theorem, Schoenfeld's bound for $\psi(t)-t$ and partial summation give an $O(G(t))$ log error in the ordinary product. Indeed the boundary term is $O(G(t))$, the integral tail is $O(\int_t^\infty(\log u)u^{-3/2}\thinspace du)$, and the omitted prime powers cost $O(t^{-1/2})$. Proposition 2.2 of Granville and Soundararajan with $A=8,Q=D,y=V$ bounds the difference between $\log\kappa_d$ and the short Euler product logarithm by $O((\log D)V^{-1/32})=O(X^{-2})$, with at most $D^{1/4}$ exceptional primitive characters. Different family discriminants give distinct primitive characters. Linearising the log factors above $t$ costs $O(1/t)$. Uniformly for the others and $3\le t\le X^2$ this gives

$$
 B_d(t)=-\sum_{t < p\le V}\chi_d(p)/p+O(G(t)). \tag{1}
$$

All absolute constants in (1) are independent of the prescribed profile. [Schoenfeld](https://doi.org/10.1090/S0025-5718-1976-0457374-X) · [Granville and Soundararajan, Proposition 2.2](https://arxiv.org/pdf/math/0206031#page=7)

We also need the far tail. The real quadratic case of Corollary 1.2 of Grenié and Molteni gives $|\psi_K(t)-t|\ll \sqrt t\thinspace\log t(\log d+\log t)$ for $t\ge100$. Stieltjes summation against $1/(t\log t)$ gives $|B_d(t)|\ll(\log d+\log t)/\sqrt t$, with the constant at infinity from the number-field Mertens theorem. In moving from the prime-power sum $\sum_{q^k\le t}1/(kq^k)$ to the product, omitted terms for $q\le\sqrt t$ contribute at most $2/t$ per ideal and those for $q>\sqrt t$ at most $2/q^2$. At most two ideals have the same norm. Thus

$$
 \int_{X^2}^\infty |B_d(t)|\thinspace dt/t
 \ll(\log D+2\log X+2)/X=o(G(X)). \tag{2}
$$

Here $r,\eta,c$ are fixed before $D$ tends to infinity. [Grenié and Molteni, Corollary 1.2](https://arxiv.org/pdf/1312.4463#page=3) · [Hathi and Lee](https://arxiv.org/abs/2112.02166)

## 2. Fields with a prescribed small change in splitting probabilities

Fix an amplitude bound $A$. Take an arbitrarily large fixed dyadic $B$ and prescribe real numbers $\Delta_p$, supported on $B<p\le2X$, with $|\Delta_p|\le A(\log p)^2/\sqrt p$. In the following statement $B$ must be large enough in terms of $A$, and $c$ small enough in terms of $A$. For at least $\sqrt D\exp[-O_A((\log X)^4)]$ fields in the shell, all $p\le B$ are inert and

$$
 B_d(t)=-\sum_{t < p\le2X}\Delta_p/p+O(G(t))
 \qquad(B\le t\le X^2). \tag{3}
$$

The implied constant in the pointwise error is absolute. Fixed prefactors depending on $B$ can be absorbed into the counting exponential for sufficiently large $D$.

Here is the transfer, including a count in the ordinary unweighted family. Use the independent splitting variables $T_p$ of Dahl and Kala for $(2n+1)^2+4$. At $2$ the sign is $-1$. For odd $p$ set $b_p=1+(-1/p)$ using the Legendre symbol. The probability of $s=\pm1$ equals $p(p-b_p-s)/(2(p^2-b_p))$, with the rest at zero. Thus $\mu_p=\mathbb E T_p=-p/(p^2-b_p)$, and the variance $v_p$ tends to one. Extend completely multiplicatively. Their Proposition 14 gives family cardinality $k\sqrt D+O(D^{1/3}\log D)$ for a constant $k>0$. Subtracting the two unnormalised formulas at $D/2$ and $D$ and dividing by the shell count gives

$$
 \mathbb E_{\rm shell}\chi_d(n)
  =\mathbb E T(n)+O(n^{2/3}D^{-1/6}\log D). \tag{4}
$$

The polynomial used by Dahl and Kala also includes $m=1$ depending on indexing. A change at this single element leaves the shell unchanged for large $D$. [Dahl and Kala, family and Proposition 14](https://arxiv.org/pdf/1611.02424#page=11)

Write $z_p=T_p-\mu_p$, let $I$ be the indicator that all primes up to $B$ are inert, and note that $\mathbb EI=p_B>0$. At each odd prime its factor is $(T_p^2-T_p)/2$. Give the model weight $IR^2$, where $R=\prod_{B<p\le2X}(1+a_pz_p)$. The shift of the new mean at $p>B$ is

$$
 g_p(a)=(2a v_p+a^2\mathbb E z_p^3)/(1+a^2v_p).
$$

For $1/2\le v_p\le1$, $|a|\le1/16$, $|\mathbb E z_p^3|\le2v_p$, its sign agrees with $a$ and $|g_p(a)|\ge |a|/2$. Choose $B$ so $|\Delta_p|\le1/32$. Continuity between zero and $2\Delta_p$ gives a coefficient with $g_p(a_p)=\Delta_p$ and $|a_p|\le2|\Delta_p|$. Use $a_p=0$ at zero shifts. Under the normalised full weight the variables above $B$ remain independent, with means $\nu_p=\mu_p+\Delta_p$.

Let $N=\lfloor D^{1/1000}\rfloor$. Expand $R$ in squarefree centered monomials and retain those whose prime product is at most $N$, giving $R_N$. Their orthogonality shows the discarded fraction of squared norm equals the probability that an independent random product exceeds $N$, each prime included with probability $a_p^2v_p/(1+a_p^2v_p)$. Markov's inequality with exponent $1/\log(2X)$ bounds this fraction by

$$
 \exp[-\log N/\log(2X)+(e-1)\sum a_p^2].
$$

The prime number theorem and partial summation give $\sum a_p^2\ll_A(\log X)^4$. Choosing $c$ sufficiently small, the square root of the displayed quantity is at most $V^{-100}$ eventually. Cauchy–Schwarz gives $\mathbb E|R_N^2-R^2|\le2 V^{-100}\mathbb ER^2$. The independent indicator cancels on normalising, and $\mathbb E IR_N^2\ge p_B/2$.

Evaluate $W=IR_N^2$ at the real characters and normalise. For any interval $H\subset(B,V]$, put $U_H=\sum_{p\in H}(T_p-\nu_p)/p$ in the model, using $\chi_d(p)$ in the shell. Its fourth moment under the shell weight differs from the full tilted model's by at most $V^{-10}$ eventually, uniformly in $H$. Indeed $R_N$ has character indices at most $N$ and sum of absolute coefficients at most $N^2$ (each term costs at most $2^{\omega(n)}\le n$). In $U_H^4$ these bounds are $V^4$ and $(2V)^4$. The indicator costs a constant depending on $B$. By (4), the total transfer error for the numerator is

$$
 O_B(N^4(2V)^4(N^2V^4)^{2/3}D^{-1/6}\log D)=O_B(D^{-1/8}).
$$

The analogous denominator error leaves $\mathbb E_{\rm shell}W\ge p_B/3$. Normalisation and the full-model truncation cost at most $O_B((1+V^4)D^{-1/8}+V^4 V^{-100})$.

For a dyadic integer $z\ge B$, $2z\le V$, and an interval of $h$ integers in $(z,2z]$, the model fourth moment is $O(h^2/z^4)$ by independence, centering and $|T_p-\nu_p|\le2$. The same holds for the weighted fields by the preceding comparison. Call the maximum absolute prefix sum $M_z$. Each prefix uses at most one dyadic interval per subdivision level. Bounding the fourth power of the maximum on a level by the sum and using Minkowski across levels gives

```math
 \|M_z\|_4\ll\sum_{j\ge0}(2^j(z/2^j)^2/z^4)^{1/4}\ll z^{-1/2}.
```

By Markov the chance under the shell weight of any $M_z>G(z)$ is at most $\sum_{z=2^k\ge B}O((\log z)^{-4})<1/4$ after enlarging $B$. All constants here are absolute. On the good event the incomplete first block costs at most twice its prefix maximum. Summing the geometric tail of $G(2^kz)$ gives $|\sum_{t<p\le V}(\chi_d(p)-\nu_p)/p|\ll G(t)$ uniformly for $B\le t\le X^2$. Also $\sum_{p>t}|\mu_p|/p\ll1/t$.

To convert good weight into a count, expand $R_N^4$ in the independent model. A prime appearing once contributes zero. Taking absolute values of the other terms and dropping the four truncation restrictions gives

$$
 \mathbb E R_N^4\le\prod_p(1+6a_p^2v_p+4|a_p|^3\mathbb E|z_p|^3+a_p^4\mathbb E|z_p|^4)
 \le\exp(C_0\sum a_p^2)
$$

with an absolute $C_0$, since $|z_p|\le2$ and $|a_p|\le1/16$. This argument permits both signs of the coefficients. In transferring $W^2=IR_N^4$, the index and coefficient bounds are $O_B(N^4)$ and $O_B(N^8)$. Equation (4) costs $O_B(D^{-1/6}N^{32/3}\log D)=o(1)$. By Cauchy–Schwarz the unweighted probability of the good event with $I=1$ is at least $(3\mathbb E_{\rm shell}W/4)^2/\mathbb E_{\rm shell}W^2$. This gives $\gg_B\exp[-O_A((\log X)^4)]$. Removing the at most $D^{1/4}$ exceptions in (1) leaves the claimed count, because $(\log X)^4=o(\log D)$. Combining the estimates proves (3). [Earlier one-sided construction, §§2–4](https://github.com/leecrossley/yokoi-mertens-long-positive-intervals/blob/v1.0.0/PROOF.md)

## 3. Choosing the shape of the error

Set $K=16/(r\eta)$ and $H=16K$. Define a continuous piecewise linear $f$ on $[r/2,2]$ by successive vertices

$$
 (r/2,H),\ (r-\eta/2,H),\ (r,1),\ (1,1),
 \ (1+\eta/4,-K),\ (1+\eta,-K),\ (1+2\eta,0),\ (2,0).
$$

When $r=1$ the duplicate vertex is used once. Take positive constants $M_0,M$ and prescribe

$$
 \Delta_p=\begin{cases}
 -M_0(\log p)^2/\sqrt p & B < p\le rX/2,\\
 M G(X)(p\log p/X) f'(p/X) & rX/2 < p\le 2X,\\
 0 &\text{otherwise}.
 \end{cases}
$$

At corners either one-sided slope suffices. These satisfy the hypothesis of §2 with $A$ depending on $M_0,M,r,\eta$. On each linear piece, the prime sum of $\log p$ is the difference of two Chebyshev $\vartheta$ values. Uniformly on this compact range $\vartheta(zX)=zX+o(X)$ by the prime number theorem. Thus on the fields in (3), with $G=G(X)$,

$$
 B_d(zX)=M G f(z)+O_r(G)+o_{r,\eta,M}(G)\qquad(r/2\le z\le2). \tag{5}
$$

The constant in $O_r(G)$ is independent of $M,M_0$. For $t<rX/2$ the upper portion of the profile contributes $MHG+o(G)$ to the right side of (3). For $B\le t\le rX/4$ the additional lower portion contributes at least $M_0G(t)/32$ from $(t,2t]$ alone, by $\pi(2t)-\pi(t)\ge t/(2\log t)$ for large $B$. Choose $M_0$ large enough to dominate the absolute error in (3) by $5G(t)$. On $[rX/4,rX/2]$, $G(t)\ll_r G$ and the lower portion is nonnegative. Choose $M$ large enough for this range and (5). The result is $B_d(B)>5G(B)$ and $B_d(t)>0$ throughout $[B,X]$.

All primes through $B$ are inert, so $P_d(B)\le\zeta(2)$. At any $t\ge2$, $P_d(t)\ge\prod_{p\le\sqrt t}(1-p^{-2})^{-1}\ge\zeta(2)(1-1/\sqrt t)$, by telescoping the omitted product over all integers. Since $(1-1/\sqrt t)/\log t=\int_0^{1/2}t^{-s}\thinspace ds$ is decreasing, and $\exp(-5G(B))<1-1/\sqrt B$ for large $B$, positivity extends to $[2,B]$. The strict margin at $X$ and monotonicity of $P_d$ give $S_d>X$. Equation (5) is strictly negative inside $(1+\eta/4,1+\eta)$ in the $z$ coordinate, so $S_d<(1+\eta)X$.

## 4. The two starting-point inequalities

For $2X\le t\le X^2$ the prescribed tail in (3) vanishes. Hence

$$
 \int_{2X}^\infty |B_d(t)|\thinspace dt/t\ll G
$$

by integrating $G(t)$ and using (2). The constant here is absolute for sufficiently large $D$. The same bound holds when multiplied by $rX/t$ on this interval.

In $r\le z\le2$ the positive part of $f$ is at most one and vanishes by $1+\eta/4$. Its integral against $dz/z$ is at most $\log((1+\eta/4)/r)\le2/r$, and against $r\thinspace dz/z^2$ it is at most one. On $[1+\eta/4,1+\eta]$ of length $3\eta/4$ the value is $-K$. Since $z\le5/4$, the absolute size of this negative contribution is at least $3K\eta/5$ in the first measure and $12rK\eta/25$ in the second. Both exceed their respective positive bounds by a fixed margin. The remaining profile after $1+\eta$ is nonpositive. By (5), increasing $M$ if necessary and then taking $D$ sufficiently large, both the finite interval integral from $rX$ to $(1+\eta)X$ and the full integral with weight $rX/t$ are negative. This proves $Y_d\le rX$.

Conversely, whenever $2\le y\le(r-\eta)X$, every primitive $\int_y^u B_d(t)\thinspace dt/t$ with $u\le X$, $u\ge y$, is nonnegative. For $u\ge X$, the part already accumulated includes $[(r-\eta)X,(r-\eta/2)X]$, where the profile is $H$. This contributes at least $M G H\eta/2$ before the error in (5), since $z\le1$. The negative part of the entire profile on $[1,2]$ has integral at most $2K\eta$ in absolute value. All errors from (5) on these fixed intervals and from $t\ge2X$ cost at most $O_r(G)+o_{r,\eta,M}(G)$. Since $H=16K$, choose $M$ large enough that all the primitives stay nonnegative. The parameters are chosen in the order $r,\eta$, then $M_0,M$, then $A,B,c$, then $D$.

For any bounded nonnegative decreasing weight, its superlevel sets are initial intervals up to endpoints of measure zero. Integration over its levels, justified by absolute convergence, now gives a nonnegative weighted integral. This proves $Y_d\ge(r-\eta)X$ and completes the theorem.
