# First negative values of the prime-ideal Mertens error

For a number field $K$, write $\kappa_K$ for the residue of its Dedekind zeta function at 1, and $\gamma$ for Euler’s constant. For real $x\ge 2$ put

$$
P_K(x)=\prod_{N\mathfrak p\le x}(1-1/N\mathfrak p)^{-1},\qquad
\Delta_K(x)=P_K(x)-e^\gamma\kappa_K\log x.
$$

Define $S_K=\inf\lbrace x\ge2:\Delta_K(x)<0\rbrace$, with $\inf\varnothing=+\infty$. Every prime ideal of norm exactly $x$ contributes to $P_K(x)$. Daniel R. Johnston asked for the first negative values of this error for two real quadratic fields and for an upper bound in a family. [Comparative Prime Number Theory Problem List, Problem 8, pp. 4–5](https://arxiv.org/pdf/2407.03530#page=4)

## 1. The first interval

Let $q$ be the smallest prime-ideal norm of $K$. For $2\le x<q$ the product equals 1, so the error is strictly decreasing there. If

$$
2 < r_K=\exp(e^{-\gamma}/\kappa_K) < q,
$$

then $S_K=r_K$, the error vanishes at $r_K$, and every $r_K<x<q$ has negative error. In particular a least strictly negative real argument does not exist in this case. This uses the same observation as the earlier prime-window calculation. Partition at the points where the arithmetic term changes, then keep the continuous main term between successive points. [Earlier prime-window calculation](https://github.com/leecrossley/prime-band-critical-all-scales/tree/ecb4538f96452cd25fff0d10fab52f71117d57ea)

## 2. The two fields in the question

Write $K_d=\mathbb Q(\sqrt d)$ and $S_d=S_{K_d}$. Take $(d,m)=(5,1)$ or $(13,3)$. In both cases $d$ is a fundamental discriminant, $d=m^2+4$ and $\epsilon=(m+\sqrt d)/2$ has norm $-1$. Minkowski’s bound for a real quadratic field is $\sqrt d/2<2$ here, hence the class number is one. To see that $\epsilon$ generates the units modulo sign, let $u>1$ be a unit in the positive real embedding, with conjugate $u'=\pm1/u$. Then $u-u'=b\sqrt d$ for an integer $b\ge1$. If $1<u<\epsilon$, monotonicity of $t+1/t$ for $t>1$ gives

$$
0 < u-u'\le u+1/u<\epsilon+1/\epsilon=\sqrt d.
$$

This is impossible. The factorization $\zeta_{K_d}(s)=\zeta(s)L(s,\chi_d)$ and the real quadratic class number formula therefore give

$$
\kappa_{K_d}=L(1,\chi_d)=\frac{2\log\epsilon}{\sqrt d},
\qquad
S_d=\exp\left(\frac{e^{-\gamma}\sqrt d}{2\log\epsilon}\right)
$$

once the first-interval inequality is checked. In both fields 2 is inert since $d\equiv5\bmod 8$. At 3, the discriminant 5 is a nonsquare modulo 3, whereas 13 is a nonzero square. Thus the smallest norm is 4 for $d=5$ and 3 for $d=13$. The rigorous enclosures are

$$
3.685768810485 < S_5 < 3.685768810486,\qquad
2.333070011801 < S_{13} < 2.333070011802.
$$

Both satisfy the required inequality. The initial negative intervals are exactly $(S_5,4)$ and $(S_{13},3)$, since the error becomes positive again at the respective right endpoints.

### Integer arguments and prime-ideal norms

At a norm $n$, multiply the previous product by $(n/(n-1))^a$, where $a$ is the number of prime ideals with that norm. A split rational prime $p$ contributes two ideals of norm $p$, a ramified prime contributes one of norm $p$, and an inert prime contributes one of norm $p^2$. This enumerates every factor through the stopping point. Checking all integers up to the first negative one and all norms up to the first negative norm gives the following.

| $d$ | First integer with negative error | First norm with negative error | Distinct norms checked, including the last |
| ---: | ---: | ---: | ---: |
| 5 | 28 | 8581 | 538 |
| 13 | 16 | 101 | 13 |

For each sign the first calculation compares the exact rational product with upper and lower bounds on $e^\gamma\kappa_{K_d}\log n$. It encloses $\sqrt d$ by integer square roots and uses monotonicity and outward rounding for logarithms and exponentials. To enclose $\gamma$ it uses the digamma expansion at $n=128$. If

$$
A_n=H_n-\log n-\frac1{2n}+\frac1{12n^2}-\frac1{120n^4}+\frac1{252n^6}-\frac1{240n^8},
$$

then $0<\gamma-A_n<1/(132n^{10})$ by the first omitted term bound. [Verifier](verify.py) · [NIST DLMF §5.11(i–ii)](https://dlmf.nist.gov/5.11)

The second calculation evaluates the residue independently. For these positive prime discriminants the real quadratic Gauss sum is $+\sqrt d$. Taking the Abel limit of the Fourier series for $-\log|1-e^{2\pi i a/d}|$ gives

$$
L(1,\chi_d)=-\frac1{\sqrt d}\sum_{a=1}^{d-1}\chi_d(a)\log\bigl(2\sin(\pi a/d)\bigr).
$$

The ring of integers has generator $(1+\sqrt d)/2$ with polynomial $t^2-t+(1-d)/4$. Counting its distinct roots modulo each prime gives the degree-one prime ideals, also at ramified primes. An irreducible polynomial gives an inert prime. The second calculation takes this route and compares logarithms of both sides using 180-bit Arb intervals. Both calculations require strict separation of each sign they report. [Independent verifier](independent.py) · [Recorded output](evidence/check.txt)

## 3. A positive proportion of Yokoi’s family

Let $\mathcal D(X)$ consist of squarefree $d=m^2+4\le X$ with positive odd $m$. Define $g(z)=e^{-\gamma}/\log z$. For $2<u<v<3$, the first interval gives the exact equivalence

$$
u < S_d\le v\quad\Longleftrightarrow\quad g(v)\le L(1,\chi_d) < g(u).
$$

Indeed all these discriminants are $5\bmod 8$, so the product is 1 throughout $[2,3)$. An error already negative at 2 has $S_d=2$ and is excluded by the upper threshold on $L(1,\chi_d)$. The endpoint conventions also cover a zero exactly at $u$ or $v$.

Dahl and Kala’s Theorem 2 gives the limiting proportion of $L(1,\chi_d)<\zeta(2)e^{-\gamma}/\tau$ in this family as the lower-tail probability for their random Euler product $L(1,\mathbb X_D)$. They include Yokoi’s polynomial explicitly. For fixed $2<z<3$ take $\tau=\zeta(2)\log z>1$, which is in their stated range for all sufficiently large $X$. Subtracting the two strict distribution functions gives

$$
\lim_{X\to\infty}\frac{\#\lbrace d\in\mathcal D(X):u < S_d\le v\rbrace}{\#\mathcal D(X)}
=\Pr\bigl(g(v)\le L(1,\mathbb X_D) < g(u)\bigr).
$$

This yields an unconditional proportion across fields ordered by discriminant. We now bound it from below at $u=401/200$ and $v=299/100$. [Dahl and Kala, Theorem 2 and §3](https://arxiv.org/pdf/1611.02424#page=4)

### The local factors

In the Dahl–Kala model the primes are independent. The factor at 2 is always $2/3$. For an odd prime $p$, let $c_p$ be the number of roots of $m^2+4\bmod p$, equal to 2 for $p\equiv1\bmod4$ and 0 otherwise. Each of these roots has one lift to a root modulo $p^2$. Of the $p^2$ possible residues of $m$, squarefreeness therefore leaves $p^2-c_p$ allowed at this prime.

For $s=\pm1$, the number of residues modulo $p$ with Legendre symbol $s$ is $(p-c_p-s)/2$. Indeed the character sum is $-1$, since the solutions to $z^2=m^2+4$ correspond to the $p-1$ factorizations $(z-m)(z+m)=4$ over $\mathbb F_p$. Counting lifts gives the local law

$$
\Pr(X_p=s)=\frac{p(p-c_p-s)}{2(p^2-c_p)}\quad(s=\pm1),\qquad
\Pr(X_p=0)=\frac{c_p(p-1)}{p^2-c_p}.
$$

The random factor is $(1-X_p/p)^{-1}$. The restriction to odd $m$ leaves the uniform local parameter at odd $p$ intact, since $m=2n-1$ is an invertible change of variable there.

### An explicit lower bound

Let $U$ be the product through $p=31$, including the factor $2/3$. Exact enumeration gives

$$
\Pr(59/100\le U\le7/10)
=\frac{116900317682048}{964766068682647}>\frac3{25}.
$$

One can reproduce this fraction by starting with the pair $(2/3,1)$. For each successive odd $p\le31$, replace each pair $(v,w)$ by $(vp/(p-s),\thinspace w\Pr(X_p=s))$ for every allowed $s$. Of the resulting 5,184 configurations sum the weights whose product is in the displayed interval. [Exact enumeration](family_bound.py)

For $p>31$ put $Y_p=-\log(1-X_p/p)$ and $T=\sum_{p>31}Y_p$. We have $|Y_p|\le1/(p-1)$ and $|Y_p-X_p/p|\le1/[p(p-1)]$ by the logarithm series. The local law gives $\mathbb E X_p=-p/(p^2-c_p)$. Consequently $|\mathbb E Y_p|\le2/(p-1)^2$ and $\operatorname{Var}(Y_p)\le1/(p-1)^2$. Independence and summability give an $L^2$ limit for $T$. Set

$$
\nu=\sum_{31 < p\le4000,\ p\ {\rm prime}}\frac1{(p-1)^2}+\frac1{3999}<\frac1{150}.
$$

The last summand bounds even the sum over all integers greater than 4000 by the integral test. The displayed finite inequality is checked by rational arithmetic. It follows that $|\mathbb ET|<2/150$ and $\operatorname{Var}(T)<1/150$. Chebyshev’s inequality with $r=7/50$ gives

$$
\Pr(|T| < r)\ \ge\ 1-\frac{1/150}{(7/50-2/150)^2}=\frac{211}{361}.
$$

At the endpoints the two verifiers establish

$$
g(299/100)<(59/100)e^{-7/50},\qquad (7/10)e^{7/50} < g(401/200).
$$

Thus on both events $L(1,\mathbb X_D)=Ue^T$ is in the required interval. The finite product and its tail are independent. The limiting proportion of $d$ with $2.005<S_d\le2.99$ therefore exceeds

$$
\frac3{25}\frac{211}{361}=\frac{633}{9025}>\frac7{100}.
$$

The independent check counts allowed $m$ modulo $p^2$ directly, recomputes the finite probability and verifies the variance and endpoint comparisons using Arb. This bound covers a positive proportion of the family. A bound valid for every Yokoi discriminant is a further question. [Independent calculation](independent.py)

## Prior work and scope

Johnston posed the question during Ethan Lee’s talk in June 2024. Alia Hamieh, Habiba Kadiri, Greg Martin and Nathan Ng collected it as Problem 8. Büthe gave an upper bound for the first negative error in the sum of reciprocals of rational primes. It also bounds the first negative product error over the rationals, since the logarithmic product error equals that sum error minus the positive tail $\sum_{p>x}\sum_{k\ge2}1/(kp^k)$. Garcia and Lee gave explicit Mertens estimates valid for all number fields. [Original problem](https://arxiv.org/pdf/2407.03530#page=4) · [Büthe](https://arxiv.org/abs/1503.01277) · [Garcia and Lee](https://arxiv.org/abs/2007.10313)

Hathi and Lee studied the same two fields. Under hypotheses on the zeros they obtained oscillation and, under GRH and a linear independence hypothesis, the logarithmic density of positive error. Table 1 reports approximately 0.9876 and 0.9298. These measure how often $x$ gives positive error within one field. Dahl and Kala established the distribution of $L(1,\chi_d)$ as the field varies, which supplies the distributional input in §3. [Hathi and Lee, §5.4 and Table 1](https://arxiv.org/pdf/2112.02166#page=20) · [Dahl and Kala](https://doi.org/10.1017/S0013091518000159)

On 21 November 2026 the literature check covered the workshop list, arXiv, the papers citing the list and Hathi–Lee in OpenAlex, and searches for the two fields with “first sign change”, “first negative”, “prime ideal Mertens product”, the numerical crossings and the Yokoi-family bound. The closest earlier results located are identified above. The search found no earlier statement of these two first crossings or of the explicit 7% bound. An unindexed calculation or unpublished observation could still predate this one. [Workshop list](https://arxiv.org/abs/2407.03530) · [OpenAlex citation query](https://api.openalex.org/works?filter=cites%3AW4400433728%7CW4200631075&per_page=100)
