# The earliest starting point in fields with a late first crossing

Take squarefree $d=m^2+4$, with $m$ odd and positive. For $K=\mathbb Q(\sqrt d)$ let $P_d(t)$ be its prime-ideal Mertens product, $c_d=e^\gamma L(1,\chi_d)$ and $B_d(t)=\log(P_d(t)/(c_d\log t))$. Write $S_d=\inf\lbrace t\ge2:B_d(t)<0\rbrace$. Write $Y_d$ for the infimum of starts $y\ge2$ where some bounded nonnegative nonincreasing weight gives $\int_y^\infty w(t)B_d(t)\thinspace dt/t<0$. An empty infimum is infinite. Let $\Pr_D$ be the proportion of these discriminants in $(D/2,D]$ and write $u=\log X$.

**Theorem.** Assume RH for the Riemann zeta function and GRH for the quadratic Dirichlet L-functions attached to these discriminants. For every $K_0>0$ there are positive $a,c$ such that, uniformly as $D,X\to\infty$ with $u\le c(\log D)^{1/5}$,

$$
 \Pr_D\big(S_d\ge X,\thinspace Y_d\le a X/u^8\big)\le\exp(-K_0 u^4).
 \tag{1}
$$

There is an absolute $C_0$ such that $\Pr_D(S_d\ge X)\ge\exp(-C_0u^4)$ in this range, after reducing $c$ if necessary. In particular, among the fields still positive through $X$, the proportion allowing any decreasing weight to succeed at any start below $aX/(\log X)^8$ tends to zero.

**At the actual first crossing.** Under the same hypotheses, there are absolute $a_1,c_1,b>0$ such that for $u\le c_1(\log D)^{1/20}$ and $D,X\to\infty$,

$$
 \Pr_D\left(Y_d\le a_1 S_d/(\log S_d)^8\ \middle|\ S_d\ge X,\thinspace S_d<\infty\right)
 \le e^{-b(\log X)^4}.
 \tag{2}
$$

The same conclusion holds in successive limits. Since $Y_d\le S_d$ whenever $S_d$ is finite, $\log Y_d/\log S_d$ tends to 1 in conditional probability. The theorem covers arbitrary decreasing weights and fields selected by the lateness of their first dip. It makes no claim for every individual field or for the optimal power of this logarithm.

Both statements use RH and GRH through the tail bound (4) below. RH enters through the rational Mertens product, and GRH for $L(s,\chi_d)$ through the far tail in [TAIL.md](TAIL.md). The lower bound for $\Pr_D(S_d\ge X)$ and the bound for fields with $S_d>Z$ in §4 use RH alone. The certificate in §5 assumes the critical-line property for the Riemann zeta function and $L(s,\chi_d)$ for the field concerned. The reduction to (3), the estimates (5) and (6), the Markov step, Dahl and Kala's moment comparison and Granville and Soundararajan's short Euler product are unconditional. So are the Lean checks and the computed contrast sums. Alpöge's announced Dirichlet GRH theorem supplies these inputs. [Announcement](https://alpo.ge/remark.pdf) [Independent formal checks](https://math.mit.edu/~drew/grh/)

## 1. A negative average needs an unusually quiet earlier interval

For any successful start, there is a finite $T$ with $\int_y^T B_d(t)\thinspace dt/t<0$, by decomposing the weight into its superlevel intervals. If $S_d\ge X$ then the error is nonnegative from 2 to $X$, including its left limit. Put $z=2aX/u^8$. If $Y_d\le aX/u^8$, there is an actual successful start below $z$ for sufficiently large $X$. Deleting the nonnegative initial part through $z$ leaves a negative interval integral. Its endpoint must be after $X$. Since $2z<X$ eventually,

$$
 0\le\int_z^{2z}B_d(t)\thinspace dt/t\le \int_X^\infty |B_d(t)|\thinspace dt/t .
 \tag{3}
$$

[Finite-interval criterion](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-optimal-starts/PROOF.md)

Given any $K_0$, outside a proportion at most $\exp[-(K_0+2)u^4]$ the right side of (3) is at most

$$
 \delta=C_{K_0}u^{3/2}/\sqrt X .
 \tag{4}
$$

The moment argument uses the prime count in the variance, RH for the rational Mertens product and GRH for $L(s,\chi_d)$ in the far tail. It is proved in [TAIL.md](TAIL.md).

## 2. Disjoint contrasts on the logarithmic axis

Divide $[\log z,\log(2z)]$ into $J=\lceil M u^4\rceil$ intervals of equal length $l=(\log 2)/J$. The constant $M$ will depend only on $K_0$. On the $i$-th interval $[v_i,v_i+l]$ take the function $f_i$ equal to $-1$ on its first half and $+1$ on its second. Put

$$
 D_i=\int_{v_i}^{v_i+l} f_i(v) B_d(e^v)\thinspace dv .
$$

If (3) and (4) hold, $\sum_i |D_i|\le\delta$. The zero integral of $f_i$ removes the benchmark and all log product contributions already present at the start of the interval.

For a rational prime $p$ with $\log p$ in this interval put

$$
 h_i(p)=\int_{\log p}^{v_i+l} f_i(v)\thinspace dv,\qquad a_{ip}=h_i(p)[-\log(1-1/p)] .
$$

The first function increases linearly from zero to $l/2$ and then falls to zero. The local norm-$`p`$ jump of the quadratic log product is $(1+\chi_d(p))[-\log(1-1/p)]$. In the independent sign model let $\mu_p$ and $v_p$ be the mean and variance of the sign. They satisfy $\mu_p=O(1/p)$ and $v_p=1+O(1/p)$. Define

$$
 \sigma_i^2=\sum_p a_{ip}^2 v_p,\qquad U_i=\sigma_i^{-1}\sum_p a_{ip}(\chi_d(p)-\mu_p).
$$

Replace $\chi_d(p)$ by the independent signs when evaluating model probabilities. The $U_i$ then have mean zero, variance one and are independent.

Uniformly in the intervals,

$$
 \sigma_i\asymp J^{-3/2}(z\log z)^{-1/2}.
 \tag{5}
$$

Indeed the central half in log coordinates contains $\asymp z/(J\log z)$ primes, with $h_i(p)\ge l/4$, while the whole interval contains $O(z/(J\log z))$ primes. These short-interval counts follow directly from the effective ordinary prime number theorem, as $J=O_M((\log z)^4)$. There is a deterministic shift $b_i$ such that

$$
 D_i/\sigma_i=U_i-b_i+o(1)
 \tag{6}
$$

uniformly over all fields and intervals. Include in $-b_i$ the mean prime jump contributions and the integral of $-\log v$, divided by $\sigma_i$. The remaining jumps come from inert squares $p^2$ in the interval. Their total contribution to $|D_i|$ is $O(J^{-2}/\sqrt z+J^{-1}/z)$, since the interval contains at most $O(\sqrt z/J+1)$ integer squares, each weighted by $O(1/(Jz))$. After dividing by (5) this tends uniformly to zero. No assumption on the size of $b_i$ is needed. [Ordinary prime estimates](https://arxiv.org/abs/2204.01980) · [Local model](https://arxiv.org/pdf/1611.02424#page=11)

## 3. It is rare for nearly every contrast to be small

In the independent model $\mathbb E U_i^4\le C$ absolutely. Expand the fourth moment of a centred sum. The paired terms contribute at most $3(\sum a_{ip}^2 v_p)^2$. The single-prime fourth terms are $O(\sum a_{ip}^4)$ before normalisation, and $v_p\ge1/2$ at these primes. For any real shift $b$ use the polynomial

$$
 Q_b(x)=\left[1-\lambda\thinspace\frac{(x-b)^2-1/4}{1+b^2}\right]^2 .
$$

It is nonnegative everywhere and at least one on $|x-b|\le1/2$. Uniformly in real $b$ and in $i$, there is a fixed $\lambda>0$ so small that $\mathbb E Q_b(U_i)\le q<1$. Indeed the mean of the expression multiplying $\lambda$ is $(1+b^2-1/4)/(1+b^2)\ge3/4$ and its second moment is bounded by an absolute constant using $\mathbb E U_i^4\le C$. All polynomial coefficients are bounded independently of $b$. Choose $\nu>0$ small enough that $\beta=(1+q)/2^{1-\nu}<1$.

For explicit choices, the normalised fourth moment is at most 11. The singleton fourth contributions cost at most 8 because $|T_p-\mu_p|\le2$ and $v_p\ge1/2$. The paired terms cost at most 3. Using $(x-b)^4\le8(x^4+b^4)$ gives 89 as a uniform bound for the second moment of $((U_i-b)^2-1/4)/(1+b^2)$. Thus $\lambda=1/256$, $q=255/256$ work. The area inequality and the arithmetic of this expectation calculation, taking $\mathbb E g\ge3/4$ and $\mathbb E g^2\le89$ as inputs, have [Lean checks](LateStarts.lean).

If $|U_i-b_i|>1/2$, (6) gives $|D_i|>\sigma_i/4$ for large $X$. By (3) and (4) at most $4\delta/\min_i\sigma_i$ intervals can do this. After division by $J$ this is at most $C\delta\sqrt{Jz\log z}\le C_{K_0}\sqrt{Ma}$. Choose $a>0$ sufficiently small given $M,K_0$ so it is below $\nu$. On the resulting event

$$
 \prod_i(1+Q_{b_i}(U_i))\ge2^{(1-\nu)J}.
$$

The model expectation is at most $(1+q)^J$ by independence. Its expectation over the actual shell differs by at most $D^{-1/8}$ for $u\le c(\log D)^{1/5}$ with $c$ sufficiently small depending on $M$. To see this, substitute the linear prime sums into the displayed product and expand as a polynomial in character values. Its maximal index is at most $(2z)^{4J}$. By (5) the coefficient sum of each linear form is at most $X^C$ for a fixed $C$, including its centring constant. Since the coefficients of $Q_b$ are uniformly bounded, the product has total absolute coefficient sum at most $\exp(C'J\log X)$. Dahl and Kala's character-moment error is $O(n^{2/3}D^{-1/6}\log D)$ per index. Thus the total error is $D^{-1/6}\log D\exp(O(Ju))\le D^{-1/8}$ after reducing $c$. [Moment comparison, Proposition 14](https://arxiv.org/pdf/1611.02424#page=11)

Markov's inequality now gives $\beta^J+D^{-1/8}$ for the fraction satisfying (3) and (4). Choose $M$ large enough that $\beta^J\le\exp[-(K_0+2)u^4]$. The choice of $M$ precedes the choices of $a,c$. Add the exceptional proportion in (4) to prove (1).

## 4. Conditioning on the late fields

The lower bound $\Pr_D(S_d\ge X)\ge e^{-C_0u^4}$ follows from a small bias towards inert primes through $2X$, with a count in the original family. The argument and the truncation needed for slow-growing $X$ are given in [SURVIVAL.md](SURVIVAL.md). Choosing $K_0>C_0+2$ in (1) proves the first conditional assertion.

To prove (2), put $Z=\exp(c_2(\log D)^{1/5})$, with $c_2$ small enough for (1) at this $K_0$. Divide $[X,Z]$ into dyadic ranges $[x,2x)$, stopping when the next lower endpoint would exceed $Z$. On such a range $S/(\log S)^8\le2x/(\log x)^8$. Use (1) with $a_1=a/2$. Summing gives $O(\exp[-K_0u^4])$, since successive log endpoints increase by $\log 2$. The remaining fields have $S>Z$. Under RH the geometric-window theorem bounds their fraction by $O(Z^{-\theta})$ for an absolute $\theta>0$. It also bounds the fraction with $S=\infty$. The denominator for conditioning on finite $S\ge X$ is at least $\exp(-C_0u^4)-O(Z^{-\theta})$. Take $u\le c_1(\log D)^{1/20}$ with $c_1$ sufficiently small. Then $Z^{-\theta}$ is at most $\exp[-(C_0+2)u^4]$. Division gives (2) for some $b>0$. All bounds also yield the asserted successive limits. Finally, every negative point has a negative right neighbourhood and gives a successful interval, so $Y_d\le S_d$. [Geometric scan and its exceptional proportion](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-geometric-starts/PROOF.md)

## 5. An individual certificate from a finite interval

For a fixed field compute $M=\sum_i|D_i|$ from the norms in $[z,2z]$. Every contrast has mean-zero test function, so the computation needs no residue or class number. The deadline below assumes the critical-line property for the Riemann zeta function and $L(s,\chi_d)$ for this field (field GRH). If a decreasing average succeeds at a start $y\le z$, its first crossing is strictly before any $N\ge2z$ such that

$$
 \sqrt N\log N\thinspace M>2(9+3\log d).
$$

Indeed survival to $N$ forces the nonnegative accumulated area from $y$ through $N$ to be at least $M$. The one-sided integrated zero estimate bounds the possible future loss after $N$ by the right side divided by $\sqrt N\log N$. This contradicts the negative endpoint. Thus the estimate can be tested on a specified field, although the existence of a successful start still needs evidence. [One-sided estimate](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-optimal-starts/PROOF.md) · [Two interval certificates](evidence/contrasts.txt)

The first certificate uses $z=1000$ in discriminant $2{,}380{,}853$ to demonstrate the numerical implication. In that field the previously certified earliest start exceeds 137123, so the premise at 1000 fails. In the second example, discriminant $82{,}864{,}613$, an interval starting at 2 does have a negative integral. Its actual first crossing is known to be much earlier than the computed upper bound. [First example's optimal start](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-optimal-starts/PROOF.md) · [Second example's actual threshold](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-crossing-lookahead/evidence/example.txt)
