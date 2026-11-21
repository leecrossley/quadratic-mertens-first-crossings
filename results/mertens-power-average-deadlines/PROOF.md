# How far can the first crossing be from a negative power average?

Write $c=e^\gamma\mathrm{res}_ {z=1}\zeta_K(z)$, $P(t)=\prod_{N\mathfrak p\le t}(1-1/N\mathfrak p)^{-1}$ and $B(t)=\log(P(t)/(c\log t))$. For real $y\ge2$, $s>0$ define

$$
 F_s(y)=\int_y^\infty s(y/t)^s B(t)\thinspace dt/t,\qquad S=\inf\lbrace t\ge2:B(t)<0\rbrace.
$$

Use $+\infty$ for the infimum of the empty set. Let $\mathcal S(y,s)$ be the supremum of $S$ over squarefree Yokoi discriminants $d=m^2+4$ with odd positive $m$ and $F_{d,s}(y)<0$. The same start and exponent are used in every field. All logarithms are natural. The power weight gives convergence since $1\le P(t)\le P_{\mathbb Q}(t)^{[K:\mathbb Q]}$.

**Results.** The sharp Yokoi supremum $\mathcal S(2,1)$ lies in $(3.46133211,3.46133212)$ and is approached from below by genuine fields. Section 3 gives its exact expression and a finite variational formula for every fixed $y,s$. For arbitrary number fields the sign $F_s(y)<0$ alone certifies a negative point in $[y,X)$ at a deadline independent of degree and discriminant. As $y\to\infty$ with $s$ fixed one may take any

$$
 X=C\thinspace y^{1+1/s}/(\log y)^{1/s},\qquad C>(2/s)^{1/s}.
$$

Section 2 also solves the corresponding extremal problem when jumps are allowed at every integer. For varying $s$ the sharp Yokoi supremum has a further asymptotic. [Slow weights and the extremal area](SLOW-WEIGHTS.md)

## 1. The least possible product under a sign constraint

Let $\mathcal J$ be an unbounded locally finite set of permitted jump locations. Write $j(t)$ for its first element **strictly** above $t$. Assume $P$ is positive, right-continuous, nondecreasing and constant between jumps in $\mathcal J$. If $B(t)\ge0$ on $[y,N)$, then for every $t\ge y$

$$
 P(t)\ge c\log\min(j(t),N).
 \tag{1}
$$

For $t<N$, take the left limit of the benchmark at the next jump or at $N$, whichever comes first. For $t\ge N$, use monotonicity and the left limit at $N$. The right side of (1) itself has the required monotonicity and jumps, and it gives nonnegative error up to $N$.

Let $E(y,s,N)$ be the normalised average for this least product. Its integrand after dividing by $c\log t$ and taking logs is $\log(\log\min(j(t),N)/\log t)$. It is continuous and strictly increasing as a function of $N$ after integration, since the capped height increases on the entire tail beyond the larger cutoff. At $N=y$ it is negative. As $N\to\infty$ it increases to a positive integral by monotone convergence after subtracting the integrable baseline at $N=y$. Thus there is exactly one root $U_{\mathcal J}(y,s)>y$. Every product with $F_s(y)<0$ has a negative point in $[y,U_{\mathcal J}(y,s))$. Conversely for any $y<N<U_{\mathcal J}(y,s)$ the least product in (1) has negative average and first negative point at infimum $N$ when extended to $[2,y)$ by the same rule. The equality at $N$ becomes strict negativity immediately to its right. If convergence of $P(t)/(c\log t)$ to one is also desired for the integer or prime-power sets, switch the least product to $c\log j(t)$ at a sufficiently distant permissible jump. In both sets $j(t)\ll t$ by Bertrand's postulate, so the modification changes the average by an amount tending to zero and preserves its strict sign. Sharpness here concerns the class with the specified jump locations and free jump sizes.

The numerical recurrence has a simple origin. At $N=y$ the average is $-e^a E_1(a)$, $a=s\log y$, where $E_1(a)=\int_a^\infty e^{-v}\thinspace dv/v$. This follows by one integration by parts. On advancing the cap from $a_0$ to $a_1$ between consecutive permitted jumps (starting with $a_0=y$), the value increases by

$$
 (y/a_0)^s\log(\log a_1/\log a_0).
$$

The only affected part is the tail from $a_0$ onwards, of mass $(y/a_0)^s$. It is therefore possible to interpolate the root exactly within its last gap. For example at $y=2,s=1$ the integer deadline is between 6.86560495 and 6.86560496. The rational-prime-power deadline for **all** number fields is between 6.70852607 and 6.70852608. It is further sharpened for the actual Yokoi family in §3. [Ten interval certificates](evidence/deadlines.txt) · [Direct independent check](independent.py)

## 2. Large starts at fixed exponent

First allow all positive integers as possible jumps. Write $E/s$ as a positive integral up to $N$ minus a tail. For $N\sim C y^{1+1/s}$, with fixed $s,C>0$, the positive part is

$$
 \frac{1+o(1)}{2(s+1)y\log y}.
$$

Indeed on $k\le t\le k+1$ the integrand before weighting is $\int_t^{k+1}dv/(v\log v)=(1+O(1/k))(k+1-t)/(k\log k)$. The weight $(y/t)^s/t$ equals $(1+O_s(1/k))y^s/k^{s+1}$. The first and last incomplete unit intervals cost $O_s(1/(y^2\log y))$. Sum the complete terms by integral comparison for $\sum_{k\ge y}k^{-s-2}/\log k$, whose asymptotic is $y^{-s-1}/((s+1)\log y)$. The part beyond $N$ is negligible. The negative tail in absolute value is

$$
 (y/N)^s\int_0^\infty e^{-sv}\log(1+v/\log N)\thinspace dv
 \sim (y/N)^s/(s^2\log N)
$$

by dominated convergence. Hence $y\log y\thinspace E/s$ tends to $[1/2-1/(s C^s)]/(s+1)$. By §1 this proves the sharp equivalent

$$
 U_{\mathbb N}(y,s)\sim(2/s)^{1/s}y^{1+1/s}.
 \tag{2}
$$

Now use the set of all rational prime powers, which includes all prime-ideal norms in any number field. We show that if $B\ge0$ throughout $[y,N)$, $N/y\to\infty$, then

$$
 \liminf_{y\to\infty} y\int_y^N (y/t)^s B(t)\thinspace dt/t\ \ge\ 1/(2(s+1)).
 \tag{3}
$$

The bound is uniform over admissible products. Fix $R>1$ and partition $[1,R]$ into finitely many fixed subintervals $[u,v]$. Subdivide $[yu,yv]$ at every prime power. By the ordinary prime number theorem its number of pieces is $(1+o(1))y(v-u)/\log y$. Higher powers contribute $O_R(\sqrt y\log y)$ points. On a piece of length $l$, comparison with the log benchmark just before its right endpoint gives a contribution at least $v^{-s}l^2/[2(yv)^2\log(yv)]$. Cauchy–Schwarz bounds the sum of $l^2$ from below by $y^2(v-u)^2$ divided by the number of pieces. After multiplying by $y$ the lower bound on this block tends to at least $(v-u)/(2v^{s+2})$. Refine the finite partition and then send $R$ to infinity. This proves (3).

After $N$ monotonicity gives $B(t)\ge-\log(\log t/\log N)$. Apply the same tail estimate as above with $N=C y^{1+1/s}/(\log y)^{1/s}$. The absolute possible loss times $y$ tends to $1/(s(s+1)C^s)$. For $C>(2/s)^{1/s}$ this is strictly smaller than (3), contradicting $F_s(y)<0$. This proves the stated number-field bound. The asymptotic constant is sharp for the integer model (2). No sharpness assertion for the prime-power asymptotic is needed.

In real quadratic fields a second estimate keeps the discriminant $d$ explicit and improves the exponent when the start is known to be polynomial. Write $H(t)=\int_1^t B(v)\thinspace dv/v$. The one-sided bound $H(t)-H(N)\ge-2(9+3\log d)/(\sqrt N\log N)$ for every $t\ge N$ follows from the integrated zero formula. Its input is the critical-line theorem for the ordinary and quadratic factors. Integrating by parts with the decreasing power weight shows that the unnormalised loss after $N$ costs at most $(y/N)^s$ times this bound in absolute size on the adverse side. If $n=\lceil y\rceil$ and $B\ge0$ throughout $[y,N)$ with $N\ge2n$, the unweighted area on $[n,2n]$ is at least $1/(64n)$ by the norm-gap bound in the same proof. The contribution after weighting is at least $(y/(2n))^s/(64n)$. Thus a successful start gives $S<N$ whenever

$$
 N\ge2n,\qquad N^{s+1/2}\log N>128n(2n)^s(9+3\log d).
 \tag{4}
$$

For fixed $a,s>0$ and $y\le d^a$, this gives $S\ll_{a,s} d^{a(s+1)/(s+1/2)}$, in particular $S\ll_a d^{4a/3}$ for $s=1$. The same bound using $s=s_0$ suffices for any successful $s\ge s_0>0$, since $N/(2n)\ge1$. A proof of such a start in every sufficiently large field remains open. [One-sided loss and gap area, §§2–3](https://github.com/leecrossley/yokoi-mertens-optimal-starts/blob/v1.0.0/PROOF.md)

## 3. The sharp answer for actual Yokoi fields

The splitting pattern assigns $\chi(p)\in\lbrace-1,0,1\rbrace$ to each rational prime. The sign at two is inert, or $-1$. At odd primes both nonzero signs are allowed. Zero is allowed exactly when $p\equiv1\bmod4$. The prime-ideal factors at $p$ are two norm-$`p`$ factors if split, one if ramified, and one norm-$`p^2`$ factor if inert. At all times the inert contribution is the smallest of the allowed choices.

We use the fact that any fixed finite pattern of allowed signs and any nonempty open positive interval for $c_d=e^\gamma L(1,\chi_d)$ occur together with positive lower density in the Yokoi family. It follows from joint weak convergence of the finite signs and the residue to the independent Euler-product model. For clarity, Dahl and Kala compare moments of $\chi_d(n)$ to those of the independent model with error $O(n^{2/3}D^{-1/6}\log D)$. Finite sign indicators are polynomials. Granville and Soundararajan approximate the residue by the Euler product through $(\log D)^{64}$ outside $D^{1/4}$ characters. The centered tail beyond a fixed $w$ up to that truncation has mean-square $O(\sum_{p>w}p^{-2})+o_D(1)$ by the family moments applied to $pq$, and the logarithmic linearisation costs $O(\sum_{p>w}p^{-2})$. This proves the joint convergence on sending $D$, then $w$, to infinity. In the model the two nonzero signs have positive probabilities. After any fixed pattern a finite further choice can approximate any desired residue logarithm because the positive and negative available increments tend to zero and their separate sums diverge. The rest has arbitrarily small mean and variance. The limiting model thus has full conditional support, and the open-set inequality for weak convergence gives the assertion. [Detailed support proof, §2](https://github.com/leecrossley/yokoi-mertens-crossing-bounds/blob/v1.0.0/PROOF.md) · [Dahl and Kala, Proposition 14](https://arxiv.org/pdf/1611.02424#page=11) · [Granville and Soundararajan, Proposition 2.2](https://arxiv.org/pdf/math/0206031#page=7)

Choose an integer $R>U_{\mathbb N}(y,s)$. For each allowed pattern $\sigma$ on $p\le R$, extend with all primes inert above $R$ and denote the product by $P_\sigma$. Define

$$
 c_\sigma=\exp\left(\int_y^\infty s(y/t)^s\log(P_\sigma(t)/\log t)\thinspace dt/t\right).
$$

If an actual field with that pattern has negative average, its $c_d$ is strictly greater than $c_\sigma$ by minimality of the extension. For the model product put $s_\sigma(C)=\inf\lbrace t\ge2:P_\sigma(t)<C\log t\rbrace$. Then the **exact finite variational formula** is

$$
 \mathcal S(y,s)=\max_{\sigma} \lim_{\epsilon\downarrow0}s_\sigma(c_\sigma+\epsilon).
 \tag{5}
$$

The upper bound uses monotonicity in $C$ and the agreement of the products up to $R$. For $C>c_\sigma$ the model's average is strictly negative, so §1 guarantees $s_\sigma(C)<R$. For the reverse bound fix $\epsilon>0$, impose the pattern through $R$ and all further primes through $Q$ inert. Any remaining signs can increase the mean logarithm of the product by at most

$$
 2\sum_{p>Q}(y/p)^s\log(1-1/p)^{-1}\le (4/s)(y/Q)^s
$$

when $Q\ge\max(y,R)$. Take $Q$ large, then use local support to impose $c_\sigma+\epsilon/2<c_d<c_\sigma+\epsilon$. These fields have negative averages and their first crossings are at least $s_\sigma(c_\sigma+\epsilon)$. Sending $\epsilon$ down to zero proves (5). Only finitely many patterns enter, although their minimal extensions contain an infinite, convergent prime sum. The one-sided limit handles possible tangencies at a jump.

For $y=2,s=1$ write

$$
 M=\sum_p\frac{2}{p^2}\log(1-p^{-2})^{-1},\qquad
 c_0=\exp\lbrace M-\log\log 2-2 E_1(\log 2)\rbrace.
$$

This is $c_\sigma$ for all primes inert. In that model the log product jumps by $\log(1-p^{-2})^{-1}$ at $p^2$ and the remaining averaging mass there is $2/p^2$. If the average in a field is negative then $c_d>c_0$. When $3$ is inert there are no norm jumps until $4$, so the first crossing is at $2$ or below $\exp(1/c_0)$. If $3$ splits the stronger necessary benchmark is

$$
 c_d>c_0\exp\left\lbrace\tfrac43\log(1-1/3)^{-1}-\tfrac29\log(1-1/9)^{-1}\right\rbrace>1/\log 3 .
$$

Hence the error is already negative somewhere before $3$ in that case. Three cannot ramify. As $3<\exp(1/c_0)<4$, leaving all primes through $Q$ inert and tuning $c_d$ down towards $c_0$ as in (5) gives fields approaching the stated bound. In particular

$$
 \mathcal S(2,1)=\exp(1/c_0)=3.461332112486105\ldots .
$$

The supremum is not attained, since $F_1(2)<0$ forces $c_d>c_0$. Two separate finite evaluations with explicit remainders certify the eight-decimal bracket. [Direct prime sum and quadrature](independent.py) · [Independent Möbius inversion of integer zeta values](zeta_check.py) · [Interval output](evidence/zeta.txt)
