# The density and shape of late first crossings

Throughout, $d=m^2+4$ is squarefree with $m$ odd and positive. For $K=\mathbb Q(\sqrt d)$ put $c_d=e^\gamma L(1,\chi_d)$, let $P_d(t)$ be its prime-ideal Mertens product over norms up to $t$, and set

$$
 B_d(t)=\log\big(P_d(t)/(c_d\log t)\big),\qquad
 J_d(T)=\int_2^T B_d(t)\thinspace dt/t.
$$

Write $S_d=\inf\lbrace t\ge2:B_d(t)<0\rbrace$, $W_d=\inf\lbrace T\ge2:J_d(T)<0\rbrace$, with empty infimum infinite. Finite $W_d$ means that some decreasing nonnegative weight starting at 2 gives a strictly negative integral. Let $p_D(X)$ be the fraction of family discriminants in $(D/2,D]$ for which $S_d\ge X$ and $W_d<\infty$.

Define $A_\ast$ as the least possible integral of an everywhere nonnegative log error in the space of admissible splitting patterns with a free positive benchmark, and put $\Lambda=2\sqrt{A_\ast}$. The finite minima $A_X$ for the same problem through $X$ increase to $A_\ast>0$. They give $A_\ast>0.4829182931$ by a finite certificate. [Definition, existence and finite approximation](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/mertens-power-average-deadlines/SLOW-WEIGHTS.md) · [Finite certificates](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/mertens-power-average-deadlines/evidence/areas.txt)

**Frequency theorem.** Assume the critical-line property for the Riemann zeta function and $L(s,\chi_d)$ for the quadratic discriminants in the theorem (field GRH). For each fixed $X>2$ the fraction $p_D(X)$ converges to a positive natural density $p(X)$. As $X\to\infty$,

$$
 \log\log(1/p(X))=\log X+\big(\Lambda+o(1)\big)\sqrt{\log X}.
 \tag{1}
$$

The same formula holds with $p_D(X)$ for every sequence $D,X\to\infty$ such that, for fixed $\epsilon>0$,

$$
 \log X\le\log\log D-(\Lambda+\epsilon)\sqrt{\log\log D}.
 \tag{2}
$$

The logarithmic scale in (1) matters. It does not specify a multiplicative equivalent for $p(X)$.

**Conditional shape.** Under the same hypothesis, among the fields counted by $p_D(X)$, put $u=\log X$. Uniformly over $0\le w\le\Lambda$ the rescaled error

$$
 f_d(w)=\sqrt u\thinspace B_d(Xe^{w\sqrt u})
$$

converges in conditional probability to $-\min(w,\Lambda-w)$. Also $J_d(X)\to A_\ast$ in conditional probability. These limits hold first with $D$ tending to infinity and then $X$ tending to infinity, or along any of the growing ranges (2). [Concentration and its proof](SHAPE.md)

Field GRH enters through the pointwise bound beyond $V$ in [MOMENTS.md](MOMENTS.md). Every statement above uses it, including the existence of $p(X)$ for each fixed $X$, through the tightness step in §1. Alpöge's announced Dirichlet GRH theorem supplies this input. [Announcement](https://alpo.ge/remark.pdf) [Independent formal checks](https://math.mit.edu/~drew/grh/)

## 1. The limit over fields

In the independent model let $T_p$ follow the Yokoi sign law, including $T_2=-1$. Write

$$
 C=e^\gamma\prod_p(1-T_p/p)^{-1},\quad B(t)=\log(P(t)/(C\log t)),\quad
 J(T)=\int_2^T B(t)\thinspace dt/t.
$$

The model log product converges almost surely. Its summands have a convergent series of means and variances since $\mathbb E T_p=O(1/p)$ and $|T_p|\le1$. Define $S,W$ from this $B,J$. The local product $P(t)$ uses the same norm rules as in real fields. The vector of any fixed finite list of signs together with $c_d$ converges in law to the corresponding model vector and $C$. This follows from Dahl and Kala's moment comparison and the short Euler product approximation to $L(1,\chi_d)$, by truncating the centred prime tail in mean square. [Details of the joint residue limit](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/mertens-power-average-deadlines/PROOF.md) · [Dahl and Kala, Proposition 14](https://arxiv.org/pdf/1611.02424#page=11) · [Granville and Soundararajan, Proposition 2.2](https://arxiv.org/pdf/math/0206031#page=7)

Define the two errors at $R$ by $|B_d(R)|$ and $\int_R^\infty |B_d(t)|\thinspace dt/t$. The estimates in [MOMENTS.md](MOMENTS.md), which use field GRH for the far tail, show that the latter converges to zero in probability uniformly in the limit $D\to\infty$, followed by $R\to\infty$. The model tail has expectation tending to zero and is absolutely integrable almost surely. Therefore the laws of $J_d$ on the compactified interval $[2,\infty]$ with the supremum norm converge to the law of $J$. Indeed truncate every primitive at a fixed $R$, keeping it constant thereafter. Truncated functions depend continuously on finite discrete signs and the log benchmark. The uniform distance to the original is bounded by its absolute tail integral. Apply the triangle inequality to bounded Lipschitz tests and then take $R\to\infty$. This convergence holds jointly with the signs through $X$ and the benchmark.

Two absence-of-atoms observations handle the boundary of the event. The model log benchmark has no atoms even conditional on finitely many signs. Also $J(\infty)$ has no atoms. To see this, use primes $p\equiv3\bmod4$ beyond any finite prescribed set. Each has two possible signs, both of probability bounded below. Switching from inert to split strictly increases $\log C$. For $J(\infty)$ the switch changes its value by

$$
 -[2\ell(p)-\ell(p^2)]\log(p/2)+\ell(p^2)\log p,\qquad
 \ell(q)=-\log(1-1/q).
 \tag{3}
$$

For $t<p$ only the benchmark changes, for $p\le t<p^2$ the error increases by $\ell(p^2)$, and for $t\ge p^2$ the effect on the error cancels exactly. The expression is strictly negative for every sufficiently large $p$ since its leading term is $-2\log(p)/p$. Absolute integrability is preserved under every finite switch.

Here is a direct anti-concentration argument for either variable. On each of $n$ chosen primes write its sign as a mixture of a fair choice (with probability bounded below uniformly) and a constant, independently across primes. With probability tending to one the number $k$ of fair choices tends to infinity, by variance or an elementary binomial bound. Condition on these choices of positions and on all other randomness. Strict monotonicity in each of the remaining coordinates makes each level set an antichain of the Boolean cube. Its proportion is at most $\binom{k}{\lfloor k/2\rfloor}/2^k=O(k^{-1/2})$. For completeness a chain arising from a uniform permutation contains a given subset of size $j$ with probability $1/\binom{k}{j}$ and can meet an antichain at most once. Sending $n$ to infinity proves both assertions.

For fixed $X>2$, survival up to $X$ compares $C$ to the minimum of finitely many left-limit and terminal benchmarks. Equality has probability zero conditional on the relevant signs. On survival, $W<\infty$ is equivalent to $\min_{T\in[X,\infty]}J(T)<0$. The probability that this minimum equals zero is also zero. At a finite endpoint $t>2$, $J(t)$ contains $-\log C\log(t/2)$ plus a function of finitely many signs. Its law has no atom at zero. Between successive norm jumps $J(e^v)$ is strictly concave in $v$, so a minimum must occur at $X$, some integer endpoint, or infinity. Equation (3) deals with infinity. The joint convergence therefore gives $p_D(X)\to\Pr(S\ge X,W<\infty)=p(X)$. A common limit over dyadic shells also gives the cumulative natural density by summing the shells and bounding the discarded initial segment using the family count $\asymp\sqrt D$. Positivity follows from the construction below for large $X$ and monotonicity covers every smaller fixed $X$.

## 2. The cost of a late dip

Take $u=\log X$. For any fixed $\delta$ with $0<\delta<\Lambda$ put

$$
 R_-=X\exp((\Lambda-\delta)\sqrt u).
$$

Suppose a field survives through $X$ and satisfies

$$
 |B_d(R_-)|\le1/u,\qquad \int_{R_-}^\infty|B_d(t)|\thinspace dt/t\le 1/u .
 \tag{4}
$$

It cannot have $W_d<\infty$ for large $X$. Its positive area to $X$ is at least $A_X$. Write $h=\log(R_-/X)$. The log error on the ensuing interval, at $t=Xe^v$, is at least $-v/u$ by monotonicity. It is also at least $-(h-v)/u-1/u-O(e^{-c\sqrt u})$ by the upper prime-growth bound and the terminal value in (4). Indeed even the choice of two split factors for every new rational prime contributes at most $2\log(\log R_-/\log t)+O(e^{-c\sqrt u})$ to the log product, including the $O(t^{-1/2})$ delayed inert-square correction. The ordinary effective prime number theorem supplies this bound uniformly. The largest possible negative area on any subset before $R_-$ is thus at most $h^2/(4u)+o(1)=(\Lambda-\delta)^2/4+o(1)<A_\ast$. The future absolute area in (4) cannot cover the fixed deficit. The same proof works in the independent model, whose products have the identical norm rules. [The two-sided area bound](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-crossing-lookahead/PROOF.md) · [Ordinary prime number theorem](https://arxiv.org/abs/2204.01980)

The moment bound shows that failure of (4) has probability at most $C\exp[-cR_-/u^2]$ in the model, and at most $C\exp[-cR_-/u^2]+O(D^{-1/4})$ in the growing shells (2). This proves the lower bound for $\log\log(1/p)$ in (1), since $\log(R_-/u^2)=u+(\Lambda-\delta)\sqrt u-O(\log u)$.

For the reverse inequality, fix $b>\sqrt{A_\ast}$ as close to $\sqrt{A_\ast}$ as desired. The finite construction of the lookahead theorem prescribes signs through a recovery endpoint $Q$ satisfying

$$
 \log Q=u+2b\sqrt u+O(1).
$$

Through $X$ the error for its prescribed benchmark $c$ is nonnegative. At $Q$ its value is $-u^{-2}+O(e^{-u})$. The signed area through $Q$ is strictly negative with a fixed margin, which persists if the log benchmark is shifted by $O(u^{-2})$. The model probability of the pattern is at least $\exp[-C Q/\log Q]$, because all but finitely many of its choices are nonzero signs. Conditional on this pattern, with probability tending to one $|B(Q)|<u^{-3}$. This follows from (ordinary) Mertens' theorem, the deterministic $O(Q^{-1/2})$ delayed-square term, and the untouched independent Euler tail of variance $O(1/Q)$ and mean $O(1/Q)$. Therefore the actual model benchmark differs from $\log c$ on the log scale by $-u^{-2}+O(u^{-3})$. The prefix through $X$ becomes strictly positive and the integral through $Q$ stays negative. [Construction and signs](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-crossing-lookahead/FAMILY.md)

For the same estimate in (2), take $2b<\Lambda+\epsilon/2$. Then $Q=o(\log D)$ uniformly along the indicated sequences: the largest $u$ gives $\log Q\le \log\log D-c_\epsilon\sqrt{\log\log D}$. Fixing the signs through $Q$ and including two further primes up to $(\log D)^{128}$ has family-moment error $D^{-1/6+o(1)}$ before normalisation. The pattern probability is $D^{-o(1)}$. Conditional on it, $|B_d(Q)|<u^{-3}$ still holds for a proportion tending to one by the second-moment calculation in the construction. This argument requires only $Q=o(\log D)$ and $u\to\infty$. In particular for slow $u$ the short product error $(\log D)^{-3}$ and the exceptional character proportion remain negligible. Thus $p_D(X)$ and $p(X)$ are at least $\frac12\exp[-CQ/\log Q]$ in their respective ranges. This gives the upper bound for $\log\log(1/p)$ with coefficient $2b$. Let $b\downarrow\sqrt{A_\ast}$ and $\delta\downarrow0$ to prove (1) and (2).

## 3. Conditional on the first dip itself being late

Equation (1) has the same two terms if $p(X)$ is replaced by $\Pr(W<\infty\mid S\ge X)$, or by its shell counterpart in (2). To see this, force all primes through $2X$ inert. This costs at most $\exp(CX/\log X)$ in reciprocal probability. Conditional on the pattern, the residue estimate from §2 at $2X$ gives $|B(2X)|\le(\log X)^{-2}$ with probability tending to one, in either setting. The inert product obeys $\zeta(2)\exp(-C/\sqrt t)\le P(t)\le\zeta(2)$ up to $2X$. For $t\le\sqrt X$, $C\log t\le(\zeta(2)/2)(1+o(1))<1$ where $C$ here denotes the model or actual field benchmark. For $\sqrt X\le t\le X$, $P(t)\ge\zeta(2)\exp(-O(X^{-1/4}))$ and $\log(2X)/\log X$ exceeds 1 by $\log 2/\log X$. This exceeds the possible benchmark error. Hence the product survives through $X$ with probability at least $\exp(-C'X/\log X)$. Its logarithmic cost is negligible compared with $R_-/u^2$ for any fixed $0<\delta<\Lambda$. Dividing the joint probability by the survival probability proves the claim.
