# The earliest start for a negative decreasing average

Let $K$ be real quadratic with fundamental discriminant $d$, let $\kappa$ be the residue of $\zeta_K$ at one, and define
$$
 B(t)=\sum_{N\mathfrak p\le t}\log(1-1/N\mathfrak p)^{-1}
       -\gamma-\log\kappa-\log\log t,\qquad H(x)=\int_1^x B(t)\,dt/t .
$$
All logs are natural. The singularity in $H$ at one is integrable. Write $S=\inf\{t\ge2:B(t)<0\}$, and $Y$ for the infimum of $y\ge2$ allowing a bounded, nonnegative, nonincreasing weight $w$ on $[y,\infty)$ with $\int_y^\infty w(t) B(t)\,dt/t<0$. We take the infimum of the empty set to be $+\infty$. The integrals converge absolutely at infinity by the real quadratic prime ideal theorem on the critical line, or the estimate in §2.

**The finite result.** Assume the critical-line property for the Riemann zeta function and $L(s,\chi_d)$ for the quadratic discriminants in the theorem (field GRH). Among all 8,950 squarefree $d=m^2+4$ for odd $1\le m\le20001$, the unique maximum of $\log Y/\log d$ is attained by $d=2{,}380{,}853=1543^2+4$. Its value is in $(0.80560267,0.80560269)$. The infimum $Y$ is in $(137123.79815,137123.79818)$ and its first crossing is in $(143054.03953022,143054.03953023)$. No decreasing weight, even one extending arbitrarily far, works at any $y\le d^{4/5}$ in that field. The next two sections give an analytic certificate for the infinite tail and a uniform consequence for all real quadratic fields. The finite census places no lower bound on a possible asymptotic exponent for all sufficiently large $d$.

## 1. Turning a question about every weight into one minimum

There is a successful weight at $y$ if and only if $H(t)<H(y)$ at some finite $t>y$. A strict decrease supplies the indicator of $[y,t]$. Conversely, the superlevel sets of $w$ are initial intervals, up to endpoints. Integrating their signed areas over levels gives the assertion, by Fubini and absolute convergence. If strictly decreasing positive weights are required, add $\epsilon y/t$ to a successful indicator and take $\epsilon>0$ small. The strict sign persists. Whenever $B(t)<0$, the same holds on a right neighbourhood, hence $Y\le S$.

Between successive prime-ideal norms the product is constant. As a function of $u=\log t$, $H(e^u)$ has first derivative $B(e^u)$ and second derivative $-1/u$ there. It is continuous at each norm. The minimum on any such closed interval is therefore at an endpoint. With $\ell(q)=-\log(1-1/q)$ and $q$ repeated according to multiplicity, integration gives the finite formula
$$
 H(e^u)=u(1-\gamma-\log\kappa-\log u)
             +\sum_{q\le e^u}\ell(q)(u-\log q).
 \tag{1}
$$
In both record calculations $B>0$ before the first crossing, apart from equality at its infimum. Thus $H$ is strictly increasing up to $S$. If the minimum on $[S,\infty)$ is $H(q_*)$ and two points before $S$ strictly bracket this value of $H$, the unique solution $H(y)=H(q_*)$ between them is the desired infimum. At equality, a zero-area interval is possible. A strictly negative integral requires a larger start in this initial range.

## 2. How much area can be lost after a finite cutoff?

For $t\ge T>1$ the following *one-sided* bound holds:
$$
 H(t)-H(T)\ge -V\left(\frac1{\sqrt T\log T}+\frac1{\sqrt t\log t}\right),\qquad
 V=\sum_\rho |1-\rho|^{-2}\le9+3\log d.
 \tag{2}
$$
The zeros are those of $\zeta_K$ in the open critical strip, counted with multiplicity. We use the critical-line theorems for $\zeta$ and $L(s,\chi_d)$, the two factors of $\zeta_K$. The correction contributed by omitted prime powers is important to the direction of (2). [Upstream formal statements and independent checks](https://math.mit.edu/~drew/grh/)

Put $R(x)=\psi_K(x)-x$ and $A(x)=\sum_{q^k\le x}1/(kq^k)$. Writing $v=\log x$, we have
$$
 d\{A(e^v)-\gamma-\log\kappa-\log v\}=\frac{e^{-v}}v\,dR(e^v).
$$
The prime-power part of Mertens' theorem has the same constant as the product. Their difference is nonnegative and $O(x^{-1/2})$, since omitted powers for $q\le\sqrt x$ sum to at most $2/x$ per ideal and those for $q>\sqrt x$ to at most $2/q^2$ per ideal. There are at most two ideals at any norm. By Grenié and Molteni, $|R(x)|\ll\sqrt x\,\log x(\log d+\log x)$ for $x\ge100$. Partial summation therefore gives $|A(x)-\gamma-\log\kappa-\log\log x|\ll(\log d+\log x)/\sqrt x$. This proves the asserted convergence and makes the boundary term in the following integration by parts vanish. [Grenié and Molteni, Corollary 1.2](https://arxiv.org/pdf/1312.4463#page=3) · [Number-field Mertens theorem](https://arxiv.org/abs/2112.02166)

For $u>0$ the tail integral of the prime-power error is
$$
 I_A(u)=\int_u^\infty[A(e^v)-\gamma-\log\kappa-\log v]\,dv
       =-\int_u^\infty(1-u/v)e^{-v}\,dR(e^v).
$$
The explicit formula, in distributions on $v>0$, is
$$
 dR(e^v)=-\sum_\rho e^{\rho v}\,dv-\coth(v)\,dv. \tag{3}
$$
For the real quadratic signature $(2,0)$ the ordinary explicit formula for $R(e^v)$ has, besides the constant and $-\sum_\rho e^{\rho v}/\rho$, the terms $-v-\log(1-e^{-2v})$. Their derivative is $-\coth(v)$. Equivalently differentiate once to recover $R$ from the absolutely convergent integrated formula (1.3a) of Grenié and Molteni and a second time in distributions to get (3). [Integrated formula (1.3a) and its remainder, §3](https://arxiv.org/pdf/1312.4465#page=2)

Writing $a=1-\rho$, each zero contributes to $I_A(u)$ the quantity
$$
 Z_\rho(u)=e^{-au}\int_0^\infty \frac{h}{u+h} e^{-ah}\,dh
  =e^{-au}\int_0^\infty\frac{e^{-su}}{(a+s)^2}\,ds.
 \tag{4}
$$
Use $(u+h)^{-1}=\int_0^\infty e^{-s(u+h)}ds$. The interchange for each zero is absolutely convergent as $\Re a=1/2$. Since $|a+s|\ge|a|$, $|Z_\rho(u)|\le e^{-u/2}/(u|a|^2)$.

For completeness, testing (3) with the half-line kernel in (4) is legitimate even at a norm. After the critical-line exponential is absorbed, the test for the zero ordinates is $k(v)=(1-u/v)_+e^{-v/2}$ on $v>0$, extended by zero for $v\le u$. It is continuous at $u$, its first derivative has bounded variation, and its first two derivatives away from $u$ decay exponentially at infinity. First truncate smoothly beyond $v=R$, then smooth the corner by convolution on the real line, with radius less than $u/2$. The Fourier transforms are bounded by $C_u/(1+|\Im\rho|^2)$ uniformly in large $R$ and small smoothing radius, by two integrations by parts using total variation of the first derivative. Their pointwise limits are the transforms of $k$. Apply the explicit formula on compactly supported smooth tests, pass the smoothing limit on each compact interval by local finiteness of the prime measure, then remove the cutoff. On the prime side the limit at infinity for the **signed** measure follows by integration by parts against $R(e^v)=O_d(e^{v/2}(1+v)^2)$, including the cutoff derivative supported on $[R,R+1]$. The differentiated elementary term converges absolutely. On the zero side the sum of the dominating terms converges by the zero count, equivalently the bound for $V$ below.

Consequently $I_A(u)=\sum_\rho Z_\rho(u)+G(u)$ where $G(u)=\int_u^\infty(1-u/v)e^{-v}\coth(v)\,dv$ is nonnegative and decreases with $u$. For the full product, add $Q(u)=\int_u^\infty(\log P(e^v)-A(e^v))\,dv$, another nonnegative decreasing function. Write $I(u)=\int_u^\infty B(e^v)\,dv$. In $H(t)-H(T)=I(\log T)-I(\log t)$ both elementary corrections therefore have favourable signs. Estimating the two zero sums by (4) proves the first inequality of (2).

For the second inequality, the paired Hadamard product of $\Xi(s)=s(s-1)d^{s/2}\pi^{-s}\Gamma(s/2)^2\zeta_K(s)$ gives $\Xi'(2)/\Xi(2)=\sum_\rho (3/2)/((3/2)^2+(\Im\rho)^2)$. Pair about $1/2$ using the functional equation, retaining any central zeros with multiplicity. Term by term $|1-\rho|^{-2}$ is at most six times that summand. The log derivative of the defining product at $2$ is at most $3/2+(\log d)/2$ since $-\log\pi$, $\Gamma'(1)/\Gamma(1)$ and $\zeta'_K(2)/\zeta_K(2)$ are negative. This establishes (2). [Grenié and Molteni, zero sums in §3](https://arxiv.org/pdf/1312.4465#page=6)

## 3. A uniform deadline from any successful start

If there is a negative decreasing-weight average starting at $y$, set $n=\lceil y\rceil$. There is a negative point in $[y,X)$ whenever $X\ge2n$ and
$$
 \sqrt X\log X>128n(9+3\log d). \tag{5}
$$
To prove it, suppose $B\ge0$ up to $X$ on this interval. Divide $[n,2n]$ at the distinct prime-ideal norms. There are at most $J\le 1+\pi(2n)+\pi(\sqrt{2n})\le8n/\log(2n)$ pieces, by Rosser and Schoenfeld's bound $\pi(t)<1.25506\,t/\log t$. On each piece $[a,b)$ the comparison with the left limit of $B$ at $b$ gives $B(t)\ge\log\log b-\log\log t\ge (b-t)/(2n\log(2n))$. Integrating against $dt/t$ yields at least $(b-a)^2/(8n^2\log(2n))$. The lengths sum to $n$. Cauchy–Schwarz gives total area at least $1/(64n)$. By (2) and (5) this exceeds every possible future loss after $X$. All the primitives from $y$ are nonnegative, contrary to §1. [Rosser and Schoenfeld, (3.6)](https://doi.org/10.1215/ijm/1255631807)

For each $a>0$, a successful start $y\le d^a$ thus gives $S\le C_a d^{2a}$ with no logarithmic factor. For instance take $C_a=\max(4,(1400/a)^2)$, using $n\le2d^a$ and $9+3\log d<9\log d$ for $d\ge5$. For a successful start at $2$, (5) gives $S=O((\log d/\log\log d)^2)$ as $d\to\infty$, by substituting a sufficiently large constant multiple. Conversely $Y\le S$ by §1. The existence of some uniform polynomial starting-point bound in the Yokoi family is therefore equivalent to the existence of some polynomial first-crossing bound. If only the start infimum is bounded, enlarge the polynomial bound by a fixed factor to obtain an actual successful start. These implications leave the existence question open.

## 4. The calculation and its independent check

For each of the two fields below, (1) was evaluated with directed real-ball arithmetic. Between $2$ and $S$ the verifier checks the sign before every norm, where the product is smallest relative to its main term. On $[S,T]$ it checks the primitive at $S$, all subsequent norms, and $T$. It checks two rational probes against the minimum and verifies $H(T)-H(q_*)>2(9+3\log d)/(\sqrt T\log T)$. This last comparison extends the minimum to all $t>T$ by (2).

| $d$ | $S$ (approximate) | Minimum after $S$, attained at $q_*$ | Strict bracket for $Y$ | $T$ | $H(T)-H(q_*)$ | Maximum later loss |
|---:|---:|---:|---|---:|---:|---:|
| 9,413 | 525.47436 | 2,017 | (337.87434, 337.87436) | 4,000,000 | $>0.0041876$ | $<0.0023978$ |
| 2,380,853 | 143,054.03953 | 154,877 | (137123.79815, 137123.79818) | 125,000,000 | $>0.0006879$ | $<0.0005090$ |

The second implementation uses a dense odd-prime sieve, square-residue tables for the two prime discriminants, and a running multiplicative Euler product. It integrates directly between consecutive log endpoints $u,v$ using $(v-u)(1+B(e^u))-v\log(v/u)$, with $u$ taken after the previous jump. It finds the minimum from the data. Both implementations agree on all 141,781 and 3,554,753 norm counts, the minima, the two start brackets and the positive margins at the cutoffs. [First verification](optimal_starts.py) · [Independent calculation](independent_windows.py) · [Second output](evidence/independent.txt)

The ordinary class-number formula gives $\kappa=2h\log((m+\sqrt d)/2)/\sqrt d$. The indicated unit has norm $-1$ and is fundamental. For any unit $v>1$, $v-v'$ is a positive integral multiple of $\sqrt d$, and $v-v'\le v+1/v$. Since $\epsilon+1/\epsilon=\sqrt d$ for the indicated unit, $v\ge\epsilon$. Independently, for even quadratic $\chi=\chi_d$, the theta integral gives
$$
 L(1,\chi)=\sum_{n\ge1}\chi(n)\left[\operatorname{erfc}(n\sqrt{\pi/d})/n+E_1(\pi n^2/d)/\sqrt d\right].
$$
This follows from splitting the completed Mellin integral at one and applying the theta functional equation on the lower piece. After $\lfloor5\sqrt d\rfloor$, the absolute remainder is below $3e^{-25\pi}$. Indeed the summand is bounded by $e^{-\pi n^2/d}(1/5+1/(25\pi))/\sqrt d$ there, and the Gaussian tail by its first term plus its integral from $5\sqrt d$. The class numbers obtained are 3 and 29. A third field with $d=98{,}346{,}893$, class number 196, has a negative interval average from $1{,}105{,}000$ to $20{,}886{,}007$. [Theta integral](https://publi.math.unideb.hu/paper/1837/download/10_5486_PMD_2013_5670.pdf#page=2) · [Interval output](evidence/optimal.txt)

For the complete census, the integer program enumerates the primitive reduced quadratic irrationals $(b+\sqrt d)/(2a)>1$ with conjugate in $(-1,0)$. They have odd $1\le b\le\lfloor\sqrt d\rfloor$, $a\mid(d-b^2)/4$, and $\lfloor\sqrt d\rfloor-b<2a\le\lfloor\sqrt d\rfloor+b$. Primitivity follows from squarefreeness. The continued-fraction step with $k=\lfloor(b+\sqrt d)/(2a)\rfloor$ sends $b$ to $b'=2ak-b$ and $a$ to $(d-b'^2)/(4a)$. By continued-fraction reduction each ideal class gives one cycle, so counting all cycles gives $h$. The census verifier independently factors every $m^2+4$ to check the field list and uses the class-number formula and interval arithmetic to certify the first crossings. [Continued-fraction reduction, §2.4](https://pages.cpsc.ucalgary.ca/~jacobs/PDF/mthesis.pdf#page=39) · [Cycle enumeration](class_numbers.cpp) · [Census verifier](verify.py) · [Complete crossing intervals](crossings.txt)

Exact fifth-power comparisons show 8,948 fields have $S<d^{4/5}$, hence $Y<d^{4/5}$. At $d=5$ a negative interval from $18/5<5^{4/5}$ to $4$ certifies the same inequality for $Y$. In the sole remaining field, (1) and (2) give $Y>d^{4/5}$ and the claimed exponent interval. This proves uniqueness across the entire stated range.
