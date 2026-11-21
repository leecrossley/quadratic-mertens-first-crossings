# A signed-prime criterion for negative Mertens averages

Let $d>1$ be a positive fundamental discriminant, $K=\mathbb Q(\sqrt d)$, and $\chi=\chi_d$ its primitive quadratic character. All prime-ideal sums count ideals with multiplicity, writing $q=N\mathfrak p$. Set

$$
B_d(t)=\sum_{q\le t}-\log(1-1/q)-\gamma_E-\log L(1,\chi)-\log\log t,\qquad
F_d(y)=\int_y^\infty B_d(t)\frac{y\thinspace dt}{t^2}.
$$

Write $u=\log y$, $T_d(y)=\sum_{p>y}(1-y/p)\chi(p)/p$ in increasing prime order, and $N_y=\sqrt y\log y$. A split prime contributes positively and an inert prime negatively. Assume the critical-line property for the Riemann zeta function and $L(s,\chi_d)$ for the quadratic discriminants concerned (field GRH). It is used throughout. Alpöge's announced Dirichlet GRH theorem supplies this input. [Announcement](https://alpo.ge/remark.pdf) [Independent formal checks](https://math.mit.edu/~drew/grh/)

**Signed prime window.** Assume field GRH for every $d$. Fix $0<b\le a$ and $\epsilon>0$. Uniformly for every $d$ and $d^b\le y\le d^a$, put $V=y(\log(3d))^{4+\epsilon}$. As $d\to\infty$,

$$
 N_y\left(F_d(y)+\sum_{y < p\le V}(1-y/p)\frac{\chi(p)}p\right)
 = Z_{\mathbb Q}(u)+o_{a,b,\epsilon}(1),
 \qquad
 Z_{\mathbb Q}(u)=\sum_{\zeta(\rho)=0}^{*}
 \frac{e^{i\thinspace\Im(\rho)u}}{(1-\rho)(2-\rho)}.
 \tag{1}
$$

The star denotes the nontrivial zeros with multiplicity, of both signs. The rational correction satisfies $|Z_{\mathbb Q}|\le 2+\gamma_E-\log(4\pi)<0.046192$. Thus a normalised split-prime excess exceeding $0.046192$ by a fixed positive margin suffices for a negative average for all sufficiently large $d$ in this range, depending on the margin. The full correction in (1) gives either sign when the margin is bounded away from zero.

Assuming field GRH for an individual $d$, there is also a numerical test valid at that $d$ and $y\ge10^4$. The explicit allowance and finite truncation error appear below (5).

**A polynomial starting point under a local zero condition.** Assume field GRH for each field considered. In the rest of the statement only take the ordinates $\lambda$ of $L(s,\chi)$, with multiplicity. Write

$$
 c_\lambda=((1/2-i\lambda)(3/2-i\lambda))^{-1},\quad
 P_0=\sum_\lambda |c_\lambda|/\lambda^2,\quad
 P_\tau=\sum_{\lambda\ne\tau}|c_\lambda|/(\lambda-\tau)^2 .
$$

A central zero gives $P_0=+\infty$. In $P_\tau$ every occurrence of $\tau$ is omitted. For every sufficiently large $d$ there is an ordinate $\tau\in[1/4,1/2]$. More generally, take **any** field with a positive ordinate $0<\tau\le1/2$ and $P_0<\infty$. There is an absolute $C$ such that for every

$$
 H\ \ge\ C\bigl(1+\log d+\sqrt{P_0+P_\tau}\bigr)
 \tag{2}
$$

some $u\in[H,3H]$ satisfies $N_yT_d(y)>1/8$ and $N_yF_d(y)<-1/16$, with $y=e^u$. In particular, on any set of discriminants with $P_0+P_\tau\le M\log^2(3d)$ for at least one such ordinate per field, a **single** exponent $a(M)$ works for the whole set. For each sufficiently large individual field with $L(1/2,\chi)\ne0$, (2) also gives arbitrarily late negative starts. The local sum bound for all Yokoi fields remains open.

## The common quadratic contribution

Let $A_K(t)=\sum_{q^j\le t}1/(jq^j)$ and $A_\chi(t)=\sum_{p^j\le t}\chi(p)^j/(jp^j)$. The constant in $A_K(t)-\log\log t$ is $\gamma_E+\log L(1,\chi)$, and the limit of $A_\chi$ is $\log L(1,\chi)$. The latter follows from the prime number theorem for the character and the Euler product by Abelian passage to $s=1$. The Mertens formula and prime ideal estimates justify the tail integrals used below. [Hathi and Lee](https://arxiv.org/abs/2112.02166) · [Grenié and Molteni, Corollary 1.2](https://arxiv.org/pdf/1312.4463#page=3)

Average the errors of $A_K,A_\chi,A_{\mathbb Q}$ with the same probability measure $y\thinspace dt/t^2$ and denote the results by $J_K,J_\chi,J_{\mathbb Q}$. Factorisation of the zeta function gives $J_K=J_{\mathbb Q}+J_\chi$ exactly. Define

$$
 Q_K(t)=\sum_{q\le t,\ q^j>t}\frac1{jq^j},\qquad
 D_\chi(t)=\sum_{j\ge2,\ p^j>t}\frac{\chi(p)^j}{jp^j}.
$$

With angle brackets denoting this average, one has $F_d=J_K+\langle Q_K\rangle$ and $-T_d=J_\chi+\langle D_\chi\rangle$. Indeed the average of the tail at $p>t$ assigns weight $1-y/p$ to $p>y$. Truncate in increasing prime order first. The character prime number theorem gives uniform convergence of the ordinary reciprocal tail on half-lines, and the terms of order at least two converge absolutely. Subtracting eliminates $J_\chi$ **before** estimating any errors.

The same function $M(t)=\tfrac12\int_{\sqrt t}^\infty dv/(v^2\log v)$ approximates $Q_K$ and $D_\chi$. To see this, the even terms for $Q_K$ are $\frac12\int_{\sqrt t}^\infty d\psi_K(v)/(v^2\log v)$ after adding the norms $q>t$, at a cost $O(1/t)$. For $D_\chi$ they give the same expression with $\psi_{\mathbb Q}$ after adding the ramified prime powers. For each $p\mid d$ their cost is $O(1/t)$ by a geometric sum. Upper endpoints at $\sqrt t$ are excluded in these Stieltjes integrals. Odd powers of index at least three cost $O(t^{-2/3})$ in either sum. The bound per prime or norm is $2/(3t)$ for $q\le t^{1/3}$ and $2/(3q^3)$ for $q>t^{1/3}$. There are at most two ideals at any integer norm.

Put $z=\sqrt t$. Corollary 1.2 cited above gives $|\psi_K(v)-v|\ll \sqrt v\thinspace(1+\log v)(\log(3d)+\log v)$, also valid for the ordinary function with $d=1$. Integrating by parts against $1/(v^2\log v)$ bounds the integral error by $O((\log(3d)+\log t)t^{-3/4})$ for large $t$. Consequently, for $u\ge10$, each of $N_y\langle Q_K\rangle$ and $N_y\langle D_\chi\rangle$ differs from $N_y\langle M\rangle$ by $O(E)$, where $E=(1+u+\log(3d))^3e^{-u/6}$. Substituting $t=ye^r$ and $v=\sqrt t\thinspace e^w$ gives

$$
 N_y\langle M\rangle
 =\int_0^\infty\int_0^\infty e^{-3r/2-w}\frac{u}{u+r+2w}\thinspace dw\thinspace dr
 =\tfrac23+O(1/u).
 \tag{3}
$$

The absolute difference from $2/3$ is at most $16/(9u)$.

## The future integral of the prime-power error

Put $s_\lambda=1/2-i\lambda$. The contribution of a nontrivial zero of either factor to the normalised prime-power average is

$$
 e^{i\lambda u}h_\lambda(u),\qquad
 h_\lambda(u)=u\int_0^\infty\frac{e^{-vu}\thinspace dv}{(s_\lambda+v)(1+s_\lambda+v)} .
 \tag{4}
$$

For a derivation, write $R(x)=\psi_K(x)-x$ for the quadratic field. The differential of the prime-power error in $z=\log x$ is $e^{-z}dR(e^z)/z$. Integrate from $z$ to infinity, then average in $z\ge u$. The resulting test against $-dR(e^z)$ is $(1-e^{u-z})e^{-z}/z$ on $z\ge u$. Each nontrivial zero contributes $e^{\rho z}dz$. Writing $1/z$ as a Laplace integral and integrating first in $z$ gives (4). For the quadratic signature the remaining density is $\coth z$, and for the rational field it is $1/(e^{2z}-1)$. Their difference is $1/(1-e^{-2z})$ for the primitive even quadratic factor. Each contributes between zero and $e^{-u/2}\coth(u)/2$ in the normalised formula. These densities follow by differentiating the standard explicit formula, or the absolutely convergent integrated formula. The test is continuous at $u$, its first derivative has bounded variation after absorbing the critical-line exponential, and it decays exponentially. Smooth cutoff and convolution therefore give a uniform $O_u((1+|\lambda|)^{-2})$ bound on its Fourier transforms. The zero count allows dominated passage to the limit. Integration by parts against the preceding bound on $R$ controls the arithmetic side at the upper endpoint. The same argument applies to $\mathbb Q$ and the difference. [Grenié and Molteni, formula (1.3a) and §3](https://arxiv.org/pdf/1312.4465#page=2)

The kernel obeys $|h_\lambda|\le |c_\lambda|\le |s_\lambda|^{-2}$ and $|h_\lambda-c_\lambda|\le 8|c_\lambda|/(3u)$. Differentiate the reciprocal product in $v$, use $|s_\lambda+v|\ge|s_\lambda|$ and $|1+s_\lambda+v|\ge|1+s_\lambda|$, then average $v$ against $u e^{-uv}dv$. For $\zeta$, the paired Hadamard product gives $\sum_\rho|\rho|^{-2}=2+\gamma_E-\log(4\pi)$. For the two factors together the sum is $\le9+3\log d$. Indeed at 2 the logarithmic derivative of $s(s-1)d^{s/2}\pi^{-s}\Gamma(s/2)^2\zeta_K(s)$ is $\sum_\lambda (3/2)/(9/4+\lambda^2)\le 3/2+(\log d)/2$, and each inverse square is at most six times the corresponding summand. Pair about $1/2$ using the functional equation, retaining any central zeros. [Zero-sum estimates](https://arxiv.org/pdf/1312.4465#page=6)

It follows **for every field** that

$$
 N_y(F_d+T_d)=Z_{\mathbb Q}(u)+O(1/u+E),\qquad
 -N_yT_d=\tfrac23+\sum_{\lambda}c_\lambda e^{i\lambda u}
       +O((1+\log(3d))/u+E).
 \tag{5}
$$

Only quadratic ordinates occur in the second sum. The absence of a conductor factor in the first $1/u$ error matters when $u$ is a fixed multiple of $\log d$.

Finally $\sum_{p\le x}\chi(p)\log p\ll\sqrt x(1+\log x)(\log(3d)+\log x)$ by subtracting the ordinary prime ideal theorem from the quadratic one and removing higher powers. Partial summation for $V\ge y$ gives

$$
 \left|\sum_{p>V}(1-y/p)\chi(p)/p\right|
 \ll(\log(3d)+\log V)/\sqrt V .
$$

This includes the boundary term at $V$. For the choice in (1) the normalised cost is $O_{a,b,\epsilon}((\log(3d))^{-\epsilon/2})$, proving that formula.

**Explicit allowances.** For $y\ge10^4$, $w=(\log y)/2$ and $(n,\Delta)=(2,d)$ or $(1,1)$, set

$$
 \delta_{n,\Delta}=e^{-w/2}[(w/(2\pi)+2)\log\Delta+n(w^2/(8\pi)+2)] .
$$

Let $\omega(d)$ count the distinct ramified primes. Then

$$
 |N_y(F_d+T_d)|\le
 2+\gamma_E-\log(4\pi)+\tfrac12 e^{-u/2}\coth u+
 2(\delta_{2,d}+\delta_{1,1})+\tfrac{78}{5}e^{-u/6}
 +\tfrac12(\omega(d)+2)u e^{-u/2}.
 \tag{5a}
$$

For all $V\ge y$, truncating $T_d$ at $V$ costs at most $4(\log(3d)+\log V+2)/\sqrt V$ before normalisation.

Indeed $\delta_{n,\Delta}$ bounds $|\psi(v)-v|/v$ for every $v\ge\sqrt y$ by Corollary 1.2, since the terms decrease for $\log v>4$. For $z=\sqrt t$, partial summation against $g(v)=1/(v^2\log v)$ bounds the error in $\int_z^\infty g\thinspace d\psi$ by $3\delta_{n,\Delta}/(z\log z)$. Subtract the two even-power contributions before averaging, so their continuous integrals cancel. Completing the field's even powers at norms $q>t$ costs at most $2/t$ by a geometric sum and the two-ideals-per-norm bound. Completing the character's even powers at ramified primes costs at most $\omega(d)/t$. In each expansion the remaining odd powers cost at most $13t^{-2/3}/\log t$. For $r=t^{1/3}$ the contribution per norm is at most $2/(3t)$ below $r$, and $2/(3q^3)$ above it. The norm count is at most $2\pi(v)<2.511v/\log v$. Sum the second estimate by parts using $2\int_r^\infty 2.511\thinspace dv/(v^3\log r)$ and add the first estimate. Averaging the combined bounds gives (5a) with the pointwise kernel bound in (4) for $\zeta$. [Rosser and Schoenfeld, Corollary 1](https://doi.org/10.1215/ijm/1255631807)

For the truncation, removing powers $j\ge2$ from $\psi_K(x)-\psi_{\mathbb Q}(x)$ costs at most $\sqrt x\log x$ since each prime through $\sqrt x$ contributes at most $\log x$. The two explicit prime ideal bounds give $|\theta_\chi(x)|\le\sqrt x\log x(\log(3d)+\log x)$ for $x\ge100$. Integrate by parts with $\phi(x)=(1-y/x)/(x\log x)$. At $x\ge V$ its absolute derivative is at most $5/(4x^2\log x)$. The boundary term plus the integral of $(5/4)(\log(3d)+\log x)x^{-3/2}$ gives the stated allowance. In particular, a finite normalised prime sum above (5a) plus its normalised truncation cost proves $F_d(y)<0$.

## Extracting a single frequency

For $H>0$ average in $u$ with the probability density $H^{-1}\max(1-|u-2H|/H,0)$. Its Fourier transform at $\xi$ is $\Phi(\xi)=e^{2iH\xi}(\sin(H\xi/2)/(H\xi/2))^2$ with the value one at zero. Hence $|\Phi(\xi)|\le 4/(H^2\xi^2)$ for $\xi\ne0$. Write $f(u)=-N_yT_d(y)$ and let $\eta$ be a uniform error bound in its formula (5) on $[H,3H]$. If $f\ge-1/8$ there, then

$$
 \big|\langle(f+1/8)e^{-i\tau u}\rangle_H\big|
 \le \langle f+1/8\rangle_H .
$$

The right hand side is at most $2/3+1/8+4P_0/H^2+\eta$. On the left the entire multiplicity $m_\tau$ contributes $m_\tau c_\tau$. The reverse triangle inequality bounds the left side below by

$$
m_\tau|c_\tau|-(2/3+1/8)4/(H^2\tau^2)-4P_\tau/H^2-\eta .
$$

For $0<\tau\le1/2$ we have $|c_\tau|\ge2/\sqrt5>2/3+1/8$ and $\tau^{-2}\le(\sqrt5/2)P_0$ from the term at $\tau$. With $H$ as in (2), increase the absolute $C$ so all the errors fit within this gap. This proves $N_yT_d>1/8$ somewhere in the window. The first identity in (5) there gives $N_yF_d<-1/16$ since $1/8-1/16>0.046192$. On a polynomial window the finite sum in (1) also exceeds $1/9$ in normalised units for all sufficiently large $d$ in the indicated subclass.

For completeness the needed low ordinates exist for every sufficiently large conductor. For fixed $v>1/2$ the paired logarithmic derivative of the completed quadratic $L$-function at $1/2+v$ gives $\sum_\lambda(v^2+\lambda^2)^{-1}=(\log d)/(2v)+O_v(1)$. The gamma term is fixed and the absolutely convergent Euler product bounds $L'/L$ uniformly there. Map $\lambda$ to $x=(1+\lambda^2)^{-1}$ and give the image mass $x/\log d$ per ordinate. These measures on $[0,1]$ have bounded total mass. For every subsequential weak limit, integrating $(1+(v^2-1)x)^{-1}$ gives $1/(2v)$. The image of $d\lambda/(2\pi(1+\lambda^2))$ gives the same integrals. Expanding about $v=1$ identifies all moments and polynomial approximation identifies the measures. The limiting measure assigns positive mass to the image of $(1/4,1/2)$ and no mass to its boundary. Symmetry gives a positive ordinate in that interval in every sufficiently large conductor. For fixed $d$ the sums $P_0,P_\tau$ converge in the absence of a central zero, by discreteness and summability of $|c_\lambda|$. This proves the individual assertion. No uniform lower bound on a zero spacing is inferred here.

## Checking the hypothesis at two points

The local sums in (2) can also be tested using derivatives of a single function. Write $\Lambda$ for the completed quadratic $L$-function and $s_\xi=1/2+i\xi$. At $\xi=0,\tau$ divide out the zero at $s_\xi$ with its full multiplicity $m_\xi$, setting $g_\xi(s)=\Lambda(s)/(s-s_\xi)^{m_\xi}$. Assume $\Lambda(1/2)\ne0$. The Hadamard factorisation gives

$$
 D_\xi=(\log g_\xi)''(s_\xi)=\sum_{\lambda\ne\xi}(\lambda-\xi)^{-2}.
 \tag{6}
$$

Indeed the second logarithmic derivative is minus the sum of the reciprocal squared complex displacements, and on the critical line the factor $i^2$ supplies a second minus sign. At zero this is just $\Lambda''(1/2)/\Lambda(1/2)$ by the functional equation. At a simple zero it is $\Lambda'''(s_\tau)/(3\Lambda'(s_\tau))-(\Lambda''(s_\tau)/(2\Lambda'(s_\tau)))^2$.

One has $P_0+P_\tau\le(4/3)(D_0+D_\tau)$. Conversely, on $|\lambda|\le2$ the weights $|c_\lambda|$ are at least $1/6$. On $|\lambda|>2$ each reciprocal squared displacement is at most $2/(1/4+\lambda^2)$ for $0\le\xi\le1/2$. Thus $D_0+D_\tau\le6(P_0+P_\tau)+O(\log(3d))$. The condition for the polynomial bound is equivalent, up to absolute factors, to bounds on two local Taylor expansions. A uniform estimate for those derivatives, or a different signed-prime argument for fields where they are large, would address the remaining family question.
