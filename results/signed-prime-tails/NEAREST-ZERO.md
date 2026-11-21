# How close must a zero be to the centre to delay a negative prime average?

Write $d>1$ for a positive fundamental discriminant and $\chi_d$ for its primitive quadratic character. The Yokoi fields in this note have squarefree $d=n^2+4$ with $n$ odd. For $K=\mathbb Q(\sqrt d)$ set

$$
 B_d(t)=\sum_{N\mathfrak p\le t}-\log(1-1/N\mathfrak p)
        -\gamma_E-\log L(1,\chi_d)-\log\log t,\qquad
 F_d(y)=\int_y^\infty B_d(t)\frac{y}{t^2}\thinspace dt .
$$

A negative value means that the prime-ideal product falls below its Mertens prediction somewhere at or after $y$. We bound the starting point $y$ of the average. The first negative value of the unaveraged error is a different quantity. The number-theoretic input on zeros is RH for the ordinary zeta function and GRH for the primitive quadratic Dirichlet function. Alpöge's announced Dirichlet GRH theorem supplies this input. The completed functions count all nontrivial zeros with multiplicity. [Announcement](https://alpo.ge/remark.pdf) · [Critical-line statements and verification](https://math.mit.edu/~drew/grh/) · [Earlier explicit formula](PROOF.md)

**Theorem 1.** Assume the stated critical-line property for each field considered. Let $L=\log(3d)$ and let $g_d$ be the minimum of $|\Im\rho|$ over the nontrivial zeros of $L(s,\chi_d)$, including the centre. There is an absolute constant $C$ such that for every sufficiently large $d$ with $g_d>0$,

$$
 F_d(y) < 0\qquad\text{for some }2\le y\le\exp\negthinspace \big(C(L+1/g_d)\big).
 \tag{1}
$$

Consequently a single exponent works for every sufficiently large $d$ in any set of fields with $g_d L\ge c>0$. Noncentral zeros may have arbitrary multiplicities and arbitrary separations. If every exponent fails on arbitrarily large Yokoi fields, there must be a sequence of those failures with $g_d L\to0$, with a central zero counted as height zero.

**Theorem 2.** Under the same critical-line hypothesis, fix a nonnegative integer $m$ and set $k=\lfloor(m+1/2)^2\rfloor+1$. There are constants $A_m,R_m>2$ and $r_m>0$ with the following property. Put $H=A_m L$. Suppose that

1. The quadratic factor has at most $m$ ordinates in $[-R_m/H,R_m/H]$, counting both signs and all multiplicities.
2. There are $k$ positive quadratic ordinates $t_j\in[R_m/H,r_m]$ with $|t_i-t_j|\ge2R_m/H$ for $i\ne j$. Each such difference has distance greater than $R_m/H$ from every quadratic ordinate.

Then $F_d(y) < 0$ somewhere in $[2,e^{2H}]$ for every sufficiently large $d$ satisfying these conditions. A double zero at the centre uses two places in the first condition. In that case seven selected ordinates and their 21 positive differences suffice if the central interval contains just that double zero. The same test accepts a symmetric pair arbitrarily close to the centre. Extra zeros close to a selected ordinate may be present. The theorem makes no assertion that all Yokoi fields provide the specified differences.

## Removing the varying denominator

Put $u=\log y$, $u_0=\log 2$, $b=2/3$, and $f(u)=u e^{u/2}F_d(e^u)$. In the proof, $\lambda$ ranges over **both** the ordinary and the quadratic ordinates. Put $\alpha_\lambda=1/2-i\lambda$, $c_\lambda=1/[\alpha_\lambda(1+\alpha_\lambda)]$ and $w_\lambda=|c_\lambda|$. The explicit formula and square estimates give

$$
 \begin{aligned}
 f(u)&=\sum_\lambda e^{i\lambda u}h_\lambda(u)+e_d(u),\\
 h_\lambda(u)&=\int_0^\infty e^{-\alpha_\lambda v}(1-e^{-v})\thinspace \frac{u}{u+v}\thinspace dv,\\
 |h_\lambda(u)|&\le w_\lambda,\qquad V=\sum_\lambda w_\lambda\le9+3\log d .
 \end{aligned}
 \tag{2}
$$

Indeed inserting $u/(u+v)=u\int_0^\infty e^{-(u+v)s}ds$ gives the absolutely convergent Laplace formula (4) of the earlier note. The arithmetic remainder $e_d$ consists of the archimedean term and the prime powers omitted from the prime-ideal product. For $u\ge10$ it equals $b+O(1/u+(1+u+L)^3e^{-u/6})$ by formula (3) there. [Explicit formula and square estimates](PROOF.md)

We also need $|e_d(u)|\ll1$ **uniformly** for $u\ge u_0$. The archimedean term is at most $e^{-u/2}\coth(u)/2$. At each $t\ge2$, the omitted powers are $\sum_{q\le t,\thinspace q^j>t}1/(jq^j)$ over prime-ideal norms $q$ and $j\ge2$. They are bounded by twice the analogous ordinary-prime sum. For an inert prime $q=p^2$, twice the ordinary terms of index $2j$ cover its contribution individually. For the ordinary square terms use $\sum_{p>\sqrt t}p^{-2}\ll1/(\sqrt t\log t)$ by $\pi(x)\ll x/\log x$ and partial summation. All indices $j\ge3$ cost $O(t^{-2/3})$ by splitting at $t^{1/3}$ and summing the geometric tails. Multiplying their future average by $u e^{u/2}$ gives an absolute bound. In particular $|f(u)|\ll L$. [Elementary prime-count bound](https://doi.org/10.1215/ijm/1255631807)

Define a positive linear operator on bounded functions on $[u_0,\infty)$ by

$$
 (\mathcal A f)(u)=f(u)+\int_0^\infty
       e^{-r/2}(1+e^{-r})\frac{f(u+r)}{u+r}\thinspace dr .
$$

It sends the summand $e^{i\lambda u}h_\lambda(u)$ exactly to $e^{i\lambda u}c_\lambda$. In the double integral put $s=r+v$. The inner integral is

$$
 \int_0^s (1+e^{-r})(1-e^{-(s-r)})\thinspace dr=s(1-e^{-s}) .
$$

This supplies $s/(u+s)$ alongside the original $u/(u+s)$. All integrations for a single summand are absolutely convergent, and the summed operator is justified by $V < \infty$ and (2). Hence

$$
 \mathcal A f=Z+\epsilon_d,\qquad Z(u)=b+\sum_\lambda c_\lambda e^{i\lambda u},\qquad
 \epsilon_d=\mathcal A e_d-b .
$$

$Z$ is real and defined on the whole line. The error is uniformly bounded on $[u_0,\infty)$ and is $O(1/u+(1+u+L)^3e^{-u/6})$ for $u\ge10$, since the extra integral of $e_d$ costs $O(1/u)$.

Write $\langle\cdot\rangle$ for integration against $2(1-u/H)\thinspace du/H$ on $[0,H]$, and $Z_-=\max(0,-Z)$. Assume for contradiction that $F_d(y)\ge0$ from 2 through $e^{2H}$. For $u_0\le u\le H$, the only negative contribution to $\mathcal A f$ can come from $u+r>2H$, at cost $O(Le^{-H/2}/H)$. For $0\le u < u_0$ use $|Z|\le b+V$. Thus, uniformly for $H\ge L$ as $d\to\infty$,

$$
 \langle Z_-\rangle\ll L/H+o(1).
 \tag{3}
$$

For the error average up to $100\log(3+L)$ use its uniform bound. Beyond that point $(1+u+L)^3e^{-u/6}=o(1)$ uniformly, as is seen by writing the cube as $O((1+u)^3+L^3)$. The mean of $1/u$ over the remaining interval is $O((\log H)/H)$. This treatment of small $u$ permits a window with left endpoint zero.

## A positive Fourier weight for nearby zeros

Let $K_H(x)=\langle e^{ixu}\rangle$. Direct integration and integration by parts give

$$
 \Re K_H(x)=\mathrm{sinc}^2(Hx/2),\qquad
 |K_H(x)|\le\min(1,4/(H|x|)),
$$

with $\mathrm{sinc}(v)=\sin(v)/v$ and $\mathrm{sinc}(0)=1$. Set

$$
 M(t)=\langle Z(u)e^{-itu}\rangle,\qquad
 D(t)=\sum_\lambda w_\lambda \mathrm{sinc}^2(H(\lambda-t)/2).
$$

Use the continuous phase $\theta_t=\arctan(2t)+\arctan(2t/3)$ of $c_t$. It satisfies $|\theta'_t|\le8/3$, giving for every $t$

$$
 \Re(e^{-i\theta_t} M(t))
 =D(t)+b\Re(e^{-i\theta_t}K_H(-t))+O(V/H).
 \tag{4}
$$

In fact $|e^{i(\theta_\lambda-\theta_t)}-1|\thinspace |K_H(\lambda-t)|\le32/(3H)$, also at equality of ordinates. Thus neighboring zeros enter $D$ with the same sign. By reality and (3),

$$
 |M(t)|\le\langle|Z|\rangle=M(0)+2\langle Z_-\rangle,\qquad
 M(0)=b+D(0)+O(V/H).
 \tag{5}
$$

Combining (3)–(5) gives

$$
 D(t)\le D(0)+b+b\min(1,4/(H|t|))+O(L/H)+o(1).
 \tag{6}
$$

For $d$ sufficiently large and $H\ge L$, there is an absolute $C_0$ such that the $w$-mass of **every** interval of length $1/H$ is at most $2(D(0)+C_0)$. Apply (6) at its midpoint, where each included squared sinc is at least $1/2$. In particular, for every $x$ and $R\ge2$ there is an absolute $C_1$ with

$$
 \sum_{|\lambda-x|>R/H}w_\lambda\mathrm{sinc}^2(H(\lambda-x)/2)
 \le \frac{C_1}{R}(D(0)+C_0).
 \tag{7}
$$

Cover the two tails by intervals of length $1/H$ beginning at distance $R/H$. On the $j$-th interval the square is at most $4/(R+j)^2$, $j\ge0$, and sum the bounds. Multiplicities require no change.

## The nearest ordinate

Every sufficiently large $d$ has a quadratic ordinate $\tau\in[1/4,1/2]$. This follows from the fixed-interval limiting measure for the zeros, proved using the logarithmic derivative at real points greater than 1 in the earlier note. There is no microscopic spacing input. Now $D(\tau)\ge w_\tau\ge2/\sqrt5>b$. Choose an absolute $A$ sufficiently large in $H\ge AL$, then take $d$ sufficiently large. Inequality (6) forces $D(0)\ge(2/\sqrt5-b)/2$. [Fixed-interval argument](PROOF.md#extracting-a-single-frequency)

If all ordinates have $|\lambda|>R/H$, (7) at zero gives $D(0)\le(C_1/R)(D(0)+C_0)$. Choose $R$ large enough that this contradicts the preceding lower bound. For $g_d>0$ take $H=\max(AL,2R/g_d)$. The fixed ordinary zeta function has a zero-free interval around the centre since $\zeta(1/2)\ne0$ (for example, by the alternating eta series). For large $d$ the radius $R/H$ lies in that interval. This proves (1). Choosing a sequence of growing discriminants that fail successively larger exponents proves the last assertion of Theorem 1.

## A test in the presence of a central zero

Fix $m,k$ as in Theorem 2. Let $\delta>0$ be small, depending only on $m$. Choose $R$ large, $r$ small and $A$ large as follows, with $H=AL$. Take $2r$ inside the ordinary central zero-free interval and $R/H < r$ for large $d$. Under the first condition of the theorem, apply (7) at zero. Since $w_\lambda\le4/3$, absorb $(C_1/R)D(0)$ to obtain $D(0)\le4m/3+\delta$ by increasing $R$. Under the second condition, (7) gives $D(t_i-t_j)\le\delta$ for $i\ne j$ after another increase of $R$. Indeed the interval of radius $R/H$ about each difference misses both factors.

Equations (3) and (5) now bound $|M(t)|$ by a constant depending only on $m$ and give $M(0)\le b+4m/3+O(\delta)$ after increasing $A$. For $|t|\le r$, passage from $\Re(e^{-i\theta_t}M(t))$ to $\Re M(t)$ costs $O_m(r)$. Choose $r$ small enough that this error is at most $\delta$ and that $w_t\ge4/3-\delta$ there. For every selected frequency and every nonzero difference the bias term in (4) costs at most $4b/R$. Take $R,A$ large enough and $d$ sufficiently large to absorb this term and the errors in (3) and (4). It follows that

$$
 \Re M(t_j)\ge 4/3-O(\delta),\qquad
 |\Re M(t_i-t_j)|=O(\delta)\quad(i\ne j).
$$

The implied constants here can depend on the fixed $m$. Form the real quadratic average

$$
 Q=\left\langle Z(u)\left|1-\frac1{\sqrt k}\sum_{j=1}^k e^{it_j u}\right|^2\right\rangle.
$$

Its lower bound is $-(1+\sqrt k)^2\langle Z_-\rangle$. Expanding the square and pairing conjugates gives the upper bound

$$
 Q\le2(b+4m/3)-(8/3)\sqrt k+O_m(\delta).
$$

The leading term is strictly negative since $\sqrt k>m+1/2$. Choose $\delta$ sufficiently small for this margin, then $R,r,A$ as above, enlarging $A$ also for the lower bound. This contradicts (3) for all sufficiently large $d$ and proves Theorem 2.

The remaining question is whether arithmetic forces a negative average also when $g_d L$ becomes arbitrarily small and the low ordinates fail the difference test. The [grid example](GRID.md) gives an explicit obstruction to using the zero count and functional equation alone. The [prime inequalities](PRIME-TEST.md) give necessary conditions on the excess of inert primes and on several frequencies together. The [field certificate](WITHHELD.md) illustrates a different way to handle missing central data.
