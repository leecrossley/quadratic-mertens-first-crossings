# A first crossing for every real quadratic field

## Theorem

Let $K$ be a real quadratic field of fundamental discriminant $d$. Write $\kappa_K$ for the residue of $\zeta_K$ at 1, $\gamma_E$ for Euler's constant, and $q=N\mathfrak p$ for a prime ideal norm. Every product or sum over $\mathfrak p$ counts distinct ideals separately. Put

$$
P_K(x)=\prod_{q\le x}(1-q^{-1})^{-1},\qquad
S_d=\inf\lbrace x\ge2:P_K(x) < e^{\gamma_E}\kappa_K\log x\rbrace.
$$

Use $\inf\varnothing=+\infty$. The product includes its jumps. A first crossing can be an infimum where the two sides are equal.

**There exists a real $x$ with $2\le x<2^{2^{d^{30000}}}$ and $P_K(x)<e^{\gamma_E}\kappa_K\log x$.** In particular $S_d<2^{2^{d^{30000}}}$. This applies to every squarefree $d=m^2+4$ with $m$ positive and odd, the Yokoi family in the earlier prime-window calculation.

The proof gives the smaller integer cutoff $U_\ast=2^{8Q^N}$, where

$$
\ell=\lceil\log_2 d\rceil,\quad H=512+128\ell,\quad
\delta=2^{-16H},\quad T=16\delta^{-2},\quad Q=32T,\quad N=2HT^2.
$$

Only $d$ is needed to specify these integers $H,T,Q,N$ and the cutoff. Throughout, $\log$ without a subscript denotes the natural logarithm.

## 1. Which zeros enter

Let $\chi_d$ be the primitive quadratic character of discriminant $d$. The quadratic Euler factors give $\zeta_K(s)=\zeta(s)L(s,\chi_d)$ on $\Re s>1$, and continuation gives the same identity in the open critical strip. For a split prime the two degree-one factors are equal, for an inert prime their product is the degree-two factor, and a ramified prime contributes one degree-one factor. Thus the identity includes primes dividing $2d$. Also $\kappa_K=L(1,\chi_d)>0$.

Every zero of this product in the strip has real part $1/2$ by Levent Alpöge's Dirichlet zero-location theorem. The trivial character of modulus one gives the Riemann zeta factor. In Mathlib this last equality is literal, and the continued Dirichlet function agrees with its Dirichlet series for $\Re s>1$. The file FirstCrossing.lean checks the inference from the exact upstream statement to the product. The independent checks of its upstream proof are recorded by Andrew Sutherland. Without that input, the argument that follows proves the stated cutoff for every real quadratic field satisfying the critical-line hypothesis for its own zeta function. [Alpöge's announcement](https://alpo.ge/remark.pdf) · [Theorem declarations](https://github.com/Deicyde/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean) · [Mathlib, Dirichlet continuation](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/NumberTheory/LSeries/DirichletContinuation.lean) · [Sutherland's audit](https://math.mit.edu/~drew/grh/)

Write $\rho=\tfrac12+i\lambda$ for every nontrivial zero, with multiplicity, including any central zero. Define $V=\sum_\rho|\rho|^{-2}$. The completed entire function of order one is

$$
\Xi(s)=s(s-1)d^{s/2}\pi^{-s}\Gamma(s/2)^2\zeta_K(s).
$$

It satisfies $\Xi(s)=\Xi(1-s)$. Pairing conjugate zeros in the Hadamard product gives $\Xi'(s)/\Xi(s)=\sum_\rho\Re(1/(s-\rho))$ on the real axis away from its zeros. Equivalently, write the product in $z=s-1/2$. Each positive ordinate contributes a factor $1+z^2/\lambda^2$, central zeros give a power of $z$, and evenness removes the linear exponential. The paired product converges locally because $\sum_{\rho}|\rho|^{-2}<\infty$. These are also the completed-product identities in §3 of Grenié and Molteni. [Completed function and zero sums, equations (3.3)–(3.7)](https://arxiv.org/pdf/1312.4465#page=7)

For each ordinate,
$1/(1/4+\lambda^2)\le6(3/2)/(9/4+\lambda^2)$.
At 2 the logarithmic derivative of the completed function is $3/2+\tfrac12\log d-\log\pi-\gamma_E+\zeta_K'(2)/\zeta_K(2)$. The last term is nonpositive by its Dirichlet series. Hence

$$
V\le 6\thinspace\Xi'(2)/\Xi(2)\le 9+3\log d .
\tag{1}
$$

## 2. The explicit formula near one

Put $\psi_K(x)=\sum_{q^j\le x}\log q$, where $j\ge1$, $B(x)=\psi_K(x)-x$, and $\Phi(u)=e^{-u/2}B(e^u)$. On $u>0$ the explicit formula, as an identity of distributions, is

$$
\Phi(u)=-\sum_\rho \frac{e^{i\lambda u}}{\rho}+b(u),\qquad
b(u)=e^{-u/2}\bigl(C_K-u-\log(1-e^{-2u})\bigr).
\tag{2}
$$

Here $C_K=-\lim_{s\to0}(\zeta_K'(s)/\zeta_K(s)-1/s)$. In the Perron integrand $-(\zeta_K'/\zeta_K)(s)x^s/s$, the simple pole of $\zeta_K$ at 1 contributes $x$. Its simple zero at 0 gives $C_K-\log x$. The order-two zeros at $-2j$, $j\ge1$, give $x^{-2j}/j$. Summing these terms gives $-\log(1-x^{-2})$. For a justification without pointwise summation of the zero series, differentiate equation (1.3a) of Grenié and Molteni in distributions on $x>1$. Its once-integrated zero series is locally absolutely convergent. In Lemma 3.3 of that paper, the derivative of the remainder for signature $(2,0)$ is $-\log x-\log(1-x^{-2})$. Changing variables and multiplying by $e^{-u/2}$ gives (2). [Integrated formula](https://arxiv.org/pdf/1312.4465#page=2) · [Remainder and residue computation](https://arxiv.org/pdf/1312.4465#page=9)

At $s=0$ the paired product gives $\Xi'(0)/\Xi(0)=-V/2$. Expanding $\Gamma'(s/2)/\Gamma(s/2)=-2/s-\gamma_E+O(s)$ in the completed logarithmic derivative gives

$$
C_K=V/2-1+\tfrac12\log d-\log\pi-\gamma_E,\qquad
|C_K|\le8+2\log d.
\tag{3}
$$

This sign will matter. For small positive $u$ the last logarithm in $b(u)$ gives a **positive** term which grows without bound.

## 3. From a prime-count deficit to a negative product error

For $t\ge2$ let $F(t)=\int_2^t B(w)\thinspace dw$. The integral of the zero terms between 2 and $t$ is

$$
-\sum_\rho\frac{t^{1+\rho}-2^{1+\rho}}{\rho(1+\rho)} .
$$

Its absolute value is at most $2Vt^{3/2}$ since $|1+\rho|\ge|\rho|$. The remaining integral has absolute value at most $t(|C_K|+\log t+1)\le(|C_K|+2)t^{3/2}$. Indeed $-\log(1-w^{-2})<1$ for $w\ge2$, and $\log t\le\sqrt t$. Thus

$$
|F(t)|\le Mt^{3/2},\qquad M=2V+|C_K|+2\le28+8\log d .
\tag{4}
$$

Set $f(t)=1/(t\log t)$ and $A(x)=\sum_{q^j\le x}1/(jq^j)$. Then $dA=f\thinspace d\psi_K$. The number-field Mertens product theorem and the vanishing correction estimated below give $A(x)-\log\log x\longrightarrow\gamma_E+\log\kappa_K$. Integration by parts, first up to a finite endpoint and then to infinity, gives

$$
A(x)-\log\log x-\gamma_E-\log\kappa_K
=f(x)B(x)+\int_x^\infty f'(t)B(t)\thinspace dt .
\tag{5}
$$

The boundary term at infinity vanishes by the prime ideal theorem. For $x\ge e$, $|f'(x)|\le2/(x^2\log x)$ and $|f''(x)|\le7/(x^3\log x)$. Integrating the last integral in (5) once more by parts and using (4) bounds it by $16M/(\sqrt x\log x)$. The boundary term at $x$ costs $2M$ in these units, and the integral of $7Mt^{-3/2}/\log t$ costs at most $14M$. [Number-field Mertens theorem](https://arxiv.org/abs/2007.10313)

Here is the prime-power correction with its dependence on degree made explicit. Write $\theta_K(y)=\sum_{q\le y}\log q$. Each rational prime $p$ contributes at most $2\log p$, so $\theta_K(y)\le2\theta_{\mathbb Q}(y)\le8y$ for all $y\ge1$. To see the last estimate, the primes $n<p\le2n$ divide $\binom{2n}{n}\le4^n$. Sum the estimate at integer powers of two up to the first power at least $y$.

If $q\le\sqrt x$, let $j_0$ be the least $j$ with $q^j>x$. Then $1/j_0<\log q/\log x$ and $\sum_{j\ge j_0}q^{-j}\le2/x$. Summing gives a total contribution at most $16/(\sqrt x\log x)$. If $\sqrt x<q\le x$, all terms with $j\ge2$ together contribute at most $1/q^2$ per ideal. For $y=\sqrt x$, partial summation gives

$$
\sum_{q>y} q^{-2}
\le \frac{2}{\log x}\sum_{q>y}\frac{\log q}{q^2}
\le\frac{2}{\log x}\int_y^\infty\frac{2\theta_K(t)}{t^3}\thinspace dt
\le\frac{32}{\sqrt x\log x}.
$$

Together these bounds give $0\le\log P_K(x)-A(x)\le48/(\sqrt x\log x)$. In particular (5) yields, for $x\ge e$ away from jumps,

$$
\left|\sqrt x\log x\thinspace\log\frac{P_K(x)}{e^{\gamma_E}\kappa_K\log x}-\Phi(\log x)\right|
\le16M+48\le496+128\log d < H .
\tag{6}
$$

It suffices to find one such point with $\Phi(\log x)<-H$.

## 4. A negative average and a bound on when it returns

Use the triangular probability density $k_\delta(t)=\max(1-|t|/\delta,0)/\delta$. Its Fourier multiplier $w(\lambda)=(\sin(\delta\lambda/2)/(\delta\lambda/2))^2$, with $w(0)=1$, satisfies $0\le w\le1$ and $w(\lambda)\le4/(\delta^2\lambda^2)$ for $\lambda\ne0$. Define the real-valued function

$$
Z(v)=-\sum_\rho w(\lambda)\thinspace\frac{e^{i\lambda v}}{\rho}.
$$

The series converges absolutely and uniformly by (1) and the decay of $w$. For $v>\delta$, equation (2) gives

$$
Z(v)=\int_{\mathbb R} k_\delta(u-v)(\Phi(u)-b(u))\thinspace du .
\tag{7}
$$

All such integrals use the support on $u>0$. To justify the triangle in a distributional identity, first convolve it with a nonnegative smooth approximate identity supported in a sufficiently small interval. On the zero side its additional multiplier has absolute value at most one. Dominated convergence there and uniform convergence of the smoothed triangle on a compact subset of $u>0$ give (7).

For $v_0=2\delta$, the averaging interval is $[\delta,3\delta]$. On it $1<e^u<2$, so $\psi_K(e^u)=0$ and $\Phi(u)=-e^{u/2}<-1$. Since $1-e^{-2u}\le6\delta$, $\log 2\ge2/3$, $\log6<2$, $|C_K|\le H$ and $u<1$, the bracket in $b(u)$ is at least $(29/3)H-3$. Multiplication by $e^{-u/2}\ge1/2$ leaves $b(u)>4H$. Thus $Z(v_0)<-4H$. At the far end of the argument we will use $|b(u)|\le |C_K|+2\le H$ for all $u\ge1$ because $ue^{-u/2}\le2/e$ and $-\log(1-e^{-2u})<1$.

For $|\lambda|>T$ one has $|\rho|\le2|\lambda|$. The entire high-frequency tail of $Z$ is therefore at most $8V/(\delta^2T)=V/2$ in absolute value. For $|\lambda|\le T$, the sum of $w(\lambda)/|\rho|$ is at most $2TV$, and the number $n$ of ordinates counted with multiplicity is at most $(T^2+1/4)V\le2HT^2=N$. These bounds follow by comparison term by term with $|\rho|^{-2}$.

For each of these $n$ ordinates put $\alpha_j=\lambda_j/\pi$. Partition the unit cube into $Q^n$ half-open boxes of side $1/Q$. Of the $Q^n+1$ points $(\lbrace a\alpha_j\rbrace)_j$, $0\le a\le Q^n$, two are in the same box. Subtracting their indices gives an integer $1\le q_0\le Q^n\le Q^N$ with $|e^{2iq_0\lambda_j}-1|\le2\pi/Q$ for every $j$. This includes zero and repeated ordinates. The argument uses no arithmetic hypothesis on their relations. Put $Y=2q_0$. Between $v_0$ and $v_0+Y$, the two high tails cost at most $V$ together. The low terms cost at most $4\pi TV/Q$. Thus

$$
|Z(v_0+Y)-Z(v_0)|\le(1+\pi/8)V<2H .
\tag{8}
$$

The averaging window is now $[Y+\delta,Y+3\delta]$, contained in $u\ge2$. Equations (7)–(8) and the bound on $b$ show that the average of $\Phi$ there is strictly less than $-H$. A set of positive measure in that window has $\Phi(u)<-H$. Removing the countable set of prime-power jumps leaves a point to which (6) applies. For that point $P_K(e^u)<e^{\gamma_E}\kappa_K u$ and $e^u<e^{2Q^N+1}<2^{8Q^N}=U_\ast$. This proves the sharper cutoff.

## 5. A single formula in the discriminant

Since $T=2^{32H+4}$, $Q=2^{32H+9}$ and $N=H2^{64H+9}$, one has

$$
\log_2\log_2 U_\ast = 3 + H(32H+9)2^{64H+9}\le2^{65H}.
$$

For the inequality, $3+512H(32H+9)\le2^H$ for every integer $H\ge64$. It holds at 64 and the polynomial grows by less than a factor of two at each subsequent step. Multiply by $2^{64H}$.

Finally $2^\ell\le2d$ and $d\ge5$, so

$$
2^{65H}=2^{33280}(2^\ell)^{8320}
 \le 4^{20800}d^{8320}\le d^{29120}\le d^{30000}.
$$

Exponentiating twice gives $U_\ast\le2^{2^{d^{30000}}}$. The displayed cutoff is far too large to guide a numerical search. It proves that every individual field has a finite first crossing, even when its early prime windows stay on the positive side.

[Prior work and scope](PRIOR-WORK.md) · [Verification and reproduction](README.md#verification)
