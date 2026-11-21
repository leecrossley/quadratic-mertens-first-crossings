# What the split and inert prime inequalities can detect

Put $L=\log(3d)$ and write $\Phi_H(t)=(\sin(Ht/2)/(Ht/2))^2$, with value 1 at zero. For an even primitive quadratic character $\chi_d$ write $\lambda$ for the ordinates of its nontrivial zeros, with multiplicity. Assume RH for $\zeta$ and the critical-line property for the Dirichlet functions used in each assertion. The construction itself requires just $\zeta$ and $L(s,\chi_5)$. For the final comparison of actual characters one also needs their quadratic twists. [Critical-line input](https://math.mit.edu/~drew/grh/)

## The scalar test in genuine fields

Set $S_{d,H}(t)=\sum_\lambda\Phi_H(t-\lambda)$ and

$$
 P_{d,H}=\frac1H\sum_{p\le e^H}\chi_d(p)\frac{\log p}{\sqrt p}
             (1-\log p/H).
$$

The explicit formula with the triangular Fourier weight gives, uniformly for $H\ge L$,

$$
 P_{d,H}=-\frac14+\frac{\log d}{2H}-\frac12 S_{d,H}(0)
              +O\big(\log(2+L)/H\big).
 \tag{1}
$$

Indeed the full prime-power sum divided by $H$ is $(\log d)/(2H)-S_{d,H}(0)/2+O(1/H)$. Its squares contribute $1/4+O(\log(2+L)/H)$ by partial summation from Mertens' first theorem, with the missing ramified primes split at $p=L$. All higher powers together cost $O(1/H)$. The earlier necessary scalar test for a nonnegative average up to $e^{2H}$ is $P_{d,H}\le-1/2+\varepsilon$ once $H\ge A_\varepsilon L$ and $d$ is large. [Explicit formula and both prime tests](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/ef3e53c/results/signed-prime-tails/PRIME-TEST.md)

If $L(s,\chi_d)$ vanishes at the centre, its central order $m$ is even by the functional equation and at least two. Then $S_{d,H}(0)\ge m$. If it has a pair at $\pm g$ with $0<g\le\pi/H$, then $S_{d,H}(0)\ge2\Phi_H(g)\ge8/\pi^2$ by the chord bound for sine on $[0,\pi/2]$. Hence for every sufficiently large $d$ in either case and every eligible $H\ge4L$,

$$
 P_{d,H}\le-\frac18-\frac4{\pi^2}+O\big(\log(2+L)/H\big)<-0.52 .
 \tag{2}
$$

For fixed $d$ one also has $\lim_{H\to\infty}P_{d,H}=-1/4-m/2$, allowing $m=0$. All nonzero ordinates contribute $O_d(H^{-2})$ since $\sum_{\lambda\ne0}\lambda^{-2}<\infty$. In a sequence with $g\log(3d)\to0$, (2) applies at every fixed scale $H=A L$, $A\ge4$, for sufficiently large $d$.

## A prime assignment with a central zero or an arbitrarily close pair

Fix $P$ sufficiently large, $0\le\theta<\pi/3$ and $D=5e^{2P}$. Here $D$ is a reference parameter for the prime tests. Starting with $\chi_5$, put $X_j=e^{jP}$, $c_j=\cos(j\theta)$ and

$$
 n_j=\left\lfloor |c_j|\sqrt{X_j}/j\right\rfloor,\qquad j\ge1 .
$$

In $[X_j,X_j+X_j^{3/4}]$ take the first $n_j$ ordinary primes whose $\chi_5$ sign is $\operatorname{sgn}(c_j)$, and reverse their signs. An empty selection needs no sign. Leave all other primes unchanged and extend completely multiplicatively to obtain $\xi$. The choices exist uniformly in $j,\theta$. The prime number theorem with critical-line remainder for $\zeta$ and $L(s,\chi_5)$ gives $x/2+O(\sqrt x\log^2 x)$ for the log-weighted count of primes of either sign through $x$. The interval thus contains $\sim X_j^{3/4}/(2\log X_j)$ of either type as $P\to\infty$, uniformly in $j\ge1$. The ratio to $\sqrt{X_j}/j$ tends uniformly to infinity. The intervals are disjoint.

Write $L_\xi(s)=\prod_p(1-\xi(p)p^{-s})^{-1}$ initially for $\Re s>1$. On $\Re s>1/4$ it continues as

$$
 L_\xi(s)=L(s,\chi_5)\big(1-2\cos\theta\,e^{-P(s-1/2)}
                      +e^{-2P(s-1/2)}\big)e^{G(s)}
 \tag{3}
$$

for a holomorphic $G$. To prove this, expand the logs of the local ratios first on $\Re s>1$. On a compact set with $\Re s\ge\sigma>1/4$, replacing $p^{-s}$ in the linear term of packet $j$ by $X_j^{-s}$ costs $O((1+|s|)X_j^{1/4-\sigma}/j)$, by differentiation. Rounding the count costs $O(X_j^{-\sigma})$. Even powers agree exactly. The sum of all odd powers of order at least three in this packet is $O_\sigma(X_j^{1/2-3\sigma}/j)$. All three errors are locally summable. What remains is $-2\sum_{j\ge1} c_j e^{-jP(s-1/2)}/j$, the logarithm of the displayed quadratic factor on $\Re s>1/2$. Exponentiating gives (3) across the larger open half-plane.

Thus the added zero ordinates are exactly $(2\pi k\pm\theta)/P$ for $k\in\mathbb Z$, adding $PT/\pi+O(1)$ positive ordinates up to $T$. At $\theta=0$ there is a double central zero. At $\theta>0$ the closest pair is at $\pm g$, $g=\theta/P$, since the conductor-five factor has a fixed central gap. Each prime factor of $\zeta L_\xi$ has precisely the local form of a split, inert or ramified prime. This construction assigns the signs directly. It supplies neither a primitive Dirichlet character of conductor $D$ nor a completed functional equation.

## The average for this assignment

For $\xi(p)=1$ take two norms $p$, for $\xi(p)=-1$ one norm $p^2$, and for $\xi(p)=0$ one norm $p$. Define $F_\xi$ by averaging the log error against $y\,dt/t^2$, subtracting $\gamma+\log L_\xi(1)+\log\log t$. The ratio $L_\xi(1)/L(1,\chi_5)$ is a positive absolutely convergent product since $\sum_{p\ {\rm flipped}}p^{-1}<\infty$.

Writing $x_+=\max(x,0)$ and $\ell(q)=-\log(1-1/q)$, the exact change relative to discriminant 5 is
$$
 F_\xi(y)-F_5(y)=
 \sum_{p\ {\rm flipped}}\chi_5(p)
 [\,2\ell(p)(1-y/p)_+-\ell(p^2)(1-y/p^2)_+\,].
 \tag{4}
$$

Indeed each norm has averaged weight $\min(1,y/q)$ and the change in the log normalisation is the difference of the two full local products. Absolute convergence permits termwise averaging. Put $u=\log y$, $N_y=\sqrt y\log y$. Uniformly for all $y\ge2$, (4) gives

$$
 N_y(F_\xi(y)-F_5(y))=
 2P\sum_{jP\ge u}c_j e^{-(jP-u)/2}(1-e^{-(jP-u)})\,\frac{u}{jP}
 + O(Pe^{-P/4}).
 \tag{5}
$$

Here are explicit bounds in order of magnitude for a single packet, writing $X=X_j$. Its linear term is supported on $y\le X+X^{3/4}$, so $N_y\ll\sqrt X\log X$. As a function of $\log p$, $\ell(p)(1-y/p)_+$ is Lipschitz with constant $O(1/X)$ on the packet, uniformly in $y$, including at its kink. Replacing $p$ by $X$ therefore costs $O(PX^{-1/4})$ after normalisation and summation. Replacing $\ell(X)$ by $1/X$ costs $O(P/X)$. Rounding the count costs $O(jP/\sqrt X)$. The $p^2$ term vanishes above $(X+X^{3/4})^2$, so its total normalised size is $O(P/\sqrt X)$. Summing the errors in $j$ proves (5), with an absolute constant independent of $\theta,y$.

For $\theta=0$ the main sum is nonnegative for every $u$. For $\theta>0$ it is nonnegative whenever $u\le P(\pi/(3\theta)-2)$. Indeed for $j_0=\lceil u/P\rceil$ the first two cosines are at least $1/2$. The unsigned tail starting at $j_0+2$, divided by the weight of $j_0+1$, is at most $e^{-P/2}/[(1-e^{-P/2})(1-e^{-P})]<1/2$. This also covers $u=j_0P$. The normalised base average exceeds $0.183894$ everywhere. Choose $P$ large enough that the uniform error is below $0.08$. Then $N_y F_\xi(y)>0.1$ throughout this entire range, and for every $y\ge2$ when $\theta=0$. Given any fixed $a>0$, $\theta$ can be chosen small enough to cover $2\le y\le D^a$ with $\theta>0$. [Proof of the base-field bound](https://github.com/leecrossley/yokoi-mertens-positive-averages-5-13/blob/v1.0.0/PROOF.md) · [Earlier spectral grid](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/ef3e53c/results/signed-prime-tails/GRID.md)

## All the several-frequency inequalities

This check uses the finite prime sums themselves. Denote by $\mathcal S_{\xi,D,H}(t)$ the right-hand prime expression of the explicit formula, evaluated with reference parameter $D$, prime power coefficients $\Lambda(n)\xi(n)$ and the usual even gamma term. Explicitly it is
$$
 \frac{\log(D/\pi)}H+G_H(t)
 -\frac2H\sum_{n\le e^H}\frac{\Lambda(n)\xi(n)}{\sqrt n}
        (1-\log n/H)\cos(t\log n).
$$
Here $G_H(t)=(2\pi)^{-1}\int_{\mathbb R}\Phi_H(v-t)\Re\psi(1/4+iv/2)\,dv$, with $\psi$ the digamma function. For the actual conductor-five character this expression equals $S_{5,H}(t)$. We evaluate it directly for $\xi$ without assuming an explicit formula for that assignment.

Uniformly for $H\ge1$ and $|t|\le1$ its value is
$$
 S_{5,H}(t)+\frac{2P}{H}
 \left[1+2\sum_{jP\le H}(1-jP/H)c_j\cos(jPt)\right]
 + O(Pe^{-P/4}/H).
 \tag{6}
$$
The constant change in the conductor term is $2P/H$. Before dividing by $H$, the change for the linear prime terms is $4\operatorname{sgn}(c_j)$ times the packet sum of $v e^{-v/2}(1-v/H)_+\cos(tv)$ at $v=\log p$. This continuous function has local Lipschitz bound $O((1+v)e^{-v/2})$ even across $v=H$. Replacement by $v=jP$ and rounding cost $O(PX_j^{-1/4}+jP X_j^{-1/2})$ per packet. All even powers cancel and odd powers of order at least three cost $O(P/X_j)$. This proves (6).

The lattice contribution (the bracket times $2P/H$) equals $\sum_{k,\pm}\Phi_H(t-(2\pi k\pm\theta)/P)$ by the triangular Fourier transform or Poisson summation. At $t=0$ this contains $2\Phi_H(g)$, with multiplicity two also at $g=0$. Separating the squares as in (1), here with only $5$ ramified, proves the scalar inequality $P_{\xi,H}<-0.52$ for $H\ge4\log(3D)$ and $Hg\le\pi$, uniformly for sufficiently large $P$.

Let $w(t)=((1/4+t^2)(9/4+t^2))^{-1/2}$ and $E(t)=w(t)\mathcal S_{\xi,D,H}(t)+(2/3)\Phi_H(t)$. If $Hg\le\pi/2$, or if $\theta=0$ with arbitrary $H$, all the cosine coefficients in the bracket in (6) are nonnegative. Its difference matrices are positive semidefinite: the quadratic form for $\cos(x_i-x_j)$ is the sum of the squares of the cosine and sine sums. Each $(b^2+t^2)^{-1/2}$ is a positive mixture of Gaussians by the Gamma integral, and Gaussian difference kernels are positive semidefinite. Products preserve this property, as does addition of the triangular-transform kernel $\Phi_H$. On $|t|\le1/4$ the conductor-five zeros contribute $S_{5,H}(t)=O(H^{-2})$ by their fixed gap and summable inverse squares. Thus for *every* finite family $t_i\in[0,1/4]$, $v_i\in\mathbb R$,
$$
 \sum_{i,j}v_i v_j E(t_i-t_j)
 \ \ge\ -C\left(\sum_i |v_i|\right)^2
       \left(H^{-2}+Pe^{-P/4}/H\right).
 \tag{7}
$$
For $H\ge\log(3D)$ this error is $o(\log(3D)/H)$ as $P\to\infty$, uniformly in $H$. It lies within the allowance in the earlier necessary matrix inequality. Choosing $\theta$ sufficiently small relative to any prescribed upper bound on $H/\log(3D)$ makes both tests consistent throughout the range $4\log(3D)\le H$ up to that bound. The central case allows all such $H$.

## Which arithmetic distinguishes a field?

Every fixed finite prefix of the original $\xi$ table is attained by infinitely many squarefree Yokoi discriminants. At each odd $p$ the sum of $(\frac{m^2+4}{p})$ over $m\bmod p$ equals $-1$ (count $(z-m)(z+m)=4$). There are at most two zero classes, and both signs occur, including at $p=3$. At 5 a class with $5\parallel m^2+4$ exists. At 2 every odd $m$ has the required inert sign. Choose the indicated classes modulo prime squares by the Chinese remainder theorem. The quadratic polynomial on this progression has no fixed square divisor, and the squarefree-value theorem for quadratics gives a positive density of squarefree values there. Equivalently one may use the finite local law of Dahl and Kala. This is an assertion at a *fixed* cutoff. The conductor of the field obtained need not be close to $D$. [Dahl and Kala, §§3–4](https://arxiv.org/pdf/1611.02424) · [Squarefree quadratic values](https://www.cambridge.org/core/journals/proceedings-of-the-edinburgh-mathematical-society/article/squarefree-values-of-quadratic-polynomials/F7023D0C01F0F50F6BDDCB6586475B63)

There is also a same-conductor comparison for the tests. Given a large actual Yokoi $d$, put $P=\tfrac12\log(d/5)$ so $D=d$. Override $\xi(p)$ by $\chi_d(p)$ for all $p\le R$ and all $p\mid5d$. The modified assignment now has the right ramification and the actual initial prime factors. The finite local ratios are holomorphic and nonzero on $\Re s>0$, preserving the zeros in (3). Formula (6) changes by $O((\sqrt R+\sqrt{\log(3d)})/H)$: each changed prime costs $O(\log p/(\sqrt p-1))$ before dividing by $H$, partial summation gives $O(\sqrt R)$ up to $R$, and splitting the ramified primes at $\log(3d)$ bounds their extra cost. For $R=o(\log^2(3d))$ this is $o(\log(3d)/H)$. Both prime tests still admit these inputs in the preceding ranges. This modification asserts only the test and zero conclusions; (5) applies to the original assignment.

Actual fields satisfy a further constraint. Fix a nonnegative smooth weight $\varphi$ supported in $(1,2)$ with integral one. For a genuine $d\ne5$, the character $\chi_d\chi_5$ is nonprincipal of conductor at most $5d$. The smoothed explicit formula gives
$$
 \sum_p\chi_d(p)\chi_5(p)\log p\,\varphi(p/x)
     = O_\varphi(\sqrt x\log(3d)).
$$
Indeed the Mellin transform decays faster than $(1+|t|)^{-2}$ on vertical lines. The critical-line zero sum has size $O_\varphi(\sqrt x\log(3d))$ by the unit-interval zero count. Prime powers of order at least two cost $O_\varphi(\sqrt x)$ by Chebyshev's estimate; imprimitive Euler factors cost $O_\varphi(\log(3d))$ at the prime level. Apply the same estimate to the two individual nonprincipal characters and the smoothed prime number theorem to the principal term. For either $\eta=\pm1$, the log-weighted count with $\chi_5(p)=\eta$ and $\chi_d(p)=-\eta$ is $x/4+O_\varphi(\sqrt x\log(3d))$, excluding ramified primes at cost $O_\varphi(\log(3d))$. For $x\ge C_\varphi\log^2(3d)$ both directions of disagreement therefore occur with positive weight. The unmodified model agrees with $\chi_5$ until $e^P$. This twist distinguishes it from a field at the indicated scale. The two directions enter the untwisted sum with opposite signs. Their separate counts leave the sign of the required difference open.
