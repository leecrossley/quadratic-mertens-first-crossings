# A real-axis test for a negative prime average

Lee Crossley

Let $`d>1`$ be a positive fundamental discriminant, $`\chi_d`$ its primitive quadratic character and $`L=\log(3d)`$. In $`\mathbb Q(\sqrt d)`$ take the error in the logarithm of the Mertens product over prime ideals and its weighted average from a real starting point $`y`$,

```math
 B_d(t)=\sum_{N\mathfrak p\le t}-\log(1-1/N\mathfrak p)
   -\gamma_E-\log L(1,\chi_d)-\log\log t,\qquad
 F_d(y)=\int_y^\infty B_d(t)\frac y{t^2}\,dt .
```

Use RH for the ordinary zeta function and GRH for each primitive quadratic character in the statement in question. These are the zero-location hypotheses in the proofs. Alpöge's announced Dirichlet GRH theorem supplies this input. Yokoi's family consists here of squarefree $d=n^2+4$ with $n$ odd. Daniel R. Johnston's Problem 8 concerns the first crossing of the underlying product. The question here concerns a starting point of its future average. [Problem 8](https://arxiv.org/html/2407.03530v1) · [Announcement](https://alpo.ge/remark.pdf) [Independent formal checks](https://math.mit.edu/~drew/grh/)

For $x>0$ let $\Lambda_d(s)=(d/\pi)^{s/2}\Gamma(s/2)L(s,\chi_d)$ and put

$$
 P_d(x)=\frac1L\frac{\Lambda'_d}{\Lambda_d}(1/2+x/L),\qquad
 Q_d(x)=P_d(x)+\frac1{2x}-\frac12,\qquad M_d=1+P_d(1).
$$

**The finite test.** Fix $x_j>0$ and real $a_j$ such that $K(v)=\sum_j a_j e^{-x_jv}\ge0$ for every $v\ge0$. For each $\eta>0$ there are $a,d_0$ depending only on the test and $\eta$ such that, for every $d\ge d_0$,

$$
 \sum_j a_j Q_d(x_j) \lt -\eta M_d
 \quad\Longrightarrow\quad
 F_d(y)\lt 0\ \text{for some }2\le y\le d^a .
 \tag{1}
$$

Both the exponent and the threshold are uniform in the number of zeros at or near the centre. A finite menu of tests uses the maximum of their exponents and thresholds. For example $K(v)=e^{-xv}(1-e^{-hv})^k$, $h>0$, gives a test on $k+1$ equally spaced points. The case $k=0$ says that $P_d(x)\lt1/2-1/(2x)-\eta M_d$ suffices. The proof does not compute $a$ or $d_0$, because $d_0$ comes from the weak limit (4), which is proved without a rate. The theorem says nothing about a field whose test has no such shortfall.

There is a companion test using ordinary primes. On a fixed interval of powers, a smoothed split-prime excess exceeding a field-independent error of order $1/\log\log(3d)$ forces a negative start in that same interval. It gives explicit prime-sum limits for the double lattice and the concentrated central pattern. [Local identity and the two prime sums](REAL-AXIS-PRIMES.md)

In the field of discriminant 2,380,853 a finite calculation gives four witnesses, in increasing order, with signs $-,+,-,+$. Both computations use the same 51 real arguments and require no individual zero ordinates. [Four intervals, proof and computations](REAL-AXIS-FIELD.md)

## From the weighted average to real derivatives

Write $u=\log y$, $u_0=\log 2$, $b=2/3$, $f_d(u)=u e^{u/2}F_d(e^u)$. In this section $\lambda$ runs over the ordinates of both the quadratic and ordinary factors, with both signs and full multiplicities. Put

$$
 c_\lambda=\frac1{(1/2-i\lambda)(3/2-i\lambda)},\qquad
 Z_d(u)=b+\sum_\lambda c_\lambda e^{i\lambda u}.
$$

We use the established identities $\sum |c_\lambda|\ll L$, $|f_d(u)|\ll L$, and

```math
 f_d(u)+\int_0^\infty e^{-r/2}(1+e^{-r})\frac{f_d(u+r)}{u+r}\,dr
   =Z_d(u)+E_d(u).
 \tag{2}
```

Here $E_d$ is bounded uniformly for $u\ge u_0$ and is $O(1/u+(1+u+L)^3e^{-u/6})$ for $u\ge10$. These estimates include the contribution of prime squares. [Explicit formula and positive integral operator](NEAREST-ZERO.md#removing-the-varying-denominator)

Write $`P_*(x)=\sum_\lambda x/(x^2+(L\lambda)^2)`$. Pairing conjugate zeros in the Hadamard product gives $`P_*=P_d+P_\zeta`$, where $P_\zeta$ uses the ordinary completed entire function $\xi$ and the same scale $L$. Put $A=1/2$, $B=3/2$, $q=x/L$. For $q\ne A,B$ direct integration gives

```math
 I_d(x):=\int_0^\infty e^{-xv}Z_d(Lv)\,dv
  =\frac b x+\frac{P_*(x)}{(A-q)(B-q)}
      -\frac{P_*(AL)}{A-q}+\frac{P_*(BL)}{B-q}.
 \tag{3}
```

For a single zero the integral in the sum is $1/[L(q-i\lambda)(A-i\lambda)(B-i\lambda)]$. Resolve into three simple fractions, then pair the signs before summing. Each paired trace is absolutely convergent. A central zero contributes with its multiplicity. The original interchange follows from $\sum|c_\lambda|<\infty$.

At fixed $x>0$, the ordinary term is $O_x(L^{-2})$ since $\zeta(1/2)\ne0$ and $\sum_{\lambda\in\zeta}\lambda^{-2}<\infty$. At $AL$ and $BL$ it is $O(1/L)$. For the quadratic factor both endpoint traces tend to $1/2$. Here are also the details needed at the lower end of the $u$ integral. The finite measures

$$
 \frac1{\log d}\sum_{\gamma\in\chi_d}\frac{\delta_\gamma}{1+\gamma^2}
  \ \longrightarrow\ \frac{dt}{2\pi(1+t^2)}
 \tag{4}
$$

converge weakly with uniformly small tails as $d\to\infty$. Indeed the fixed-scale argument in the earlier proof establishes weak convergence of the images under $t\mapsto(1+t^2)^{-1}$ on $[0,1]$. The limit gives zero mass to 0, which gives tightness on the real line. Symmetry recovers (4) on both half-lines. Testing with $(1+t^2)A/(A^2+t^2)$ or its counterpart with $B$ gives the endpoint assertion since $\log d/L\to1$. [Fixed-scale measure and its moment proof](PROOF.md#extracting-a-single-frequency)

For $u$ in any fixed compact subinterval of $[0,\infty)$, (4) gives $Z_d(u)/L\to0$ uniformly. On a bounded frequency interval this follows from uniform continuity in $u$ and a continuous cutoff. The tails cost a constant times those in (4), uniformly in $u$. The limiting Fourier integral of $c_t e^{itu}$ is zero there. In fact $c_t=\int_0^\infty e^{-v/2}(1-e^{-v})e^{itv}dv$, and Fourier inversion evaluates this continuous kernel at $-u$, including its zero value at the origin. The fixed ordinary part contributes $O(1/L)$. Finally $P_d(x)\ll_x P_d(1)$ by termwise comparison of the positive kernels. The short square-sinc estimate gives $P_d(1)\ll L/\log L$, so the factor error $O_x(P_d(1)/L)$ tends to zero even in the crowded case. [Short-interval bound](REAL-AXIS-PRIMES.md#proof-of-the-error-bound) Equation (3) now gives

$$
 I_d(x)=\frac43 Q_d(x)+o_x(1).
 \tag{5}
$$

The constant $-1/2$ in $Q_d$ comes from the two endpoints in (3).

## Why the tail cost is uniform in central crowding

Choose $H\ge1$ and a smooth cutoff $0\le\psi_H\le1$, equal to one up to $H$ and zero from $H+1$ onwards, with uniformly bounded first two derivatives. Set $g=(1-\psi_H)K$ on $[0,\infty)$. The integrals of $|g|$ and $|g''|$ are $O_K(e^{-cH})$ with $c=\min_j x_j$. Two integrations by parts give

```math
 \left|\int_0^\infty g(v)e^{itv}\,dv\right|
 \ll_K\frac{e^{-cH}}{1+t^2},\qquad
 \left|\int_0^\infty g(v)Z_d(Lv)\,dv\right|
 \ll_K e^{-cH}M_d .
```

The second bound uses $|c_\lambda|\le4/3$ and $\sum_\lambda(1+(L\lambda)^2)^{-1}=P_*(1)$. It charges the tail to the same real measurement as (1).

Suppose $F_d$ stays nonnegative from 2 to $\exp(2(H+1)L)$. On $u_0\le u\le (H+1)L$ the left side of (2) is at least $-O(Le^{-(H+1)L/2}/((H+1)L))$, since a negative integrand can enter only when $u+r>2(H+1)L$. The integral of $|E_d(Lv)|$ on $[u_0/L,H+1]$ is $o_H(1)$. Up to $u=100\log(3+L)$ use its uniform bound. Beyond that point the exponential error tends uniformly to zero, and integration of $1/u$ costs $O_H(\log L/L)$. On $0\le v\le u_0/L$ the uniform estimate following (4) gives $\int|Z_d(Lv)|dv=o(1)$. Since $\psi_H K\ge0$, (2) yields $\int \psi_H K Z_d(Lv)dv\ge-o_{H,K}(1)$.

Combine this inequality with (5) and the tail estimate. Choose $H$ large enough that the relative tail cost is less than $\eta/3$, then $d$ large enough for the two little-oh errors. This contradicts the premise of (1). For large $d$, taking $a=4(H+1)$ covers $\exp(2(H+1)L)$.

## Restrictions on the two possible limits

Consider a sequence $d\to\infty$ with $F_d\ge0$ up to $d^{b_d}$, $b_d\to\infty$. The normalized $Q_d/M_d$ have locally uniformly convergent subsequences on $\Re x>0$. On any compact subset the complex kernel $x/(x^2+t^2)$ is bounded by $C/(1+t^2)$ uniformly in real $t$. The paired series and the definition of $M_d$ thus give a normal family. For every limit $R$, (1) gives $\sum a_j R(x_j)\ge0$ for every test in (1). Use $K(v)=e^{-xv}(1-e^{-hv})^k$, divide by $h^k$, and let $h\downarrow0$. This gives $(-1)^kR^{(k)}(x)\ge0$ for all $k\ge0$. Such a function is called completely monotone. It is the Laplace transform of a positive measure on $[0,\infty)$. [Bernstein–Widder theorem](https://doi.org/10.1515/9781400876457-005)

With unbounded central counts tending to infinity, $P_d(1)\to\infty$. The limits of $P_d(x)/M_d$ are then completely monotone and have value one at $x=1$. With bounded central counts, the earlier classification gives locally uniform limits $P$ of $P_d$ from a counting measure $\mu$ whose multiplicity levels are finite unions of progressions up to finitely many points. Here $P+1/(2x)-1/2$ itself is completely monotone. [Counting, subsequences and real transforms](NEAR-CENTRAL.md#a-test-using-values-on-the-real-axis)

In particular the multiplicity-weighted density of the progressions satisfies

$$
 \lim_{T\to\infty}\frac{\mu([-T,T])}{2T}\ \ge\ \frac1{2\pi}.
 \tag{6}
$$

Indeed write $\mu$ as an integer linear combination of singleton and two-sided progression counting measures. A singleton contributes $x/(x^2+t^2)\to0$ as $x\to\infty$. A progression of step $\alpha$ contributes a periodized Poisson kernel tending to $\pi/\alpha$. Its density is $1/\alpha$. Now let $x\to\infty$ in $P(x)+1/(2x)-1/2\ge0$. For a single lattice of multiplicity $m$, even with finitely many exceptions, (6) bounds its spacing by $2\pi m$.


The full test on any proposed bounded-crowding pattern is explicit. Write its counting measure as singleton terms $m_i\delta_{t_i}$ plus progression terms of coefficient $n_j$, step $\alpha_j$ and shift $\beta_j$. These signed coefficients refer to this representation of the measure. Expanding each periodized Poisson kernel as a geometric series gives the unique inverse Laplace measure of $P+1/(2x)-1/2$,

```math
 \left(\pi\sum_j n_j/\alpha_j-1/2\right)\delta_0
 +\left(1/2+\sum_i m_i\cos(t_i v)\right)dv
 +2\pi\sum_j\frac{n_j}{\alpha_j}\sum_{k\ge1}
       \cos(2\pi k\beta_j/\alpha_j)\,\delta_{2\pi k/\alpha_j}.
```

It is positive exactly when the mass at zero is nonnegative, the displayed continuous density is nonnegative, and the weights at each common positive atom sum to a nonnegative number. For instance a single half-step translate of a lattice, with constant positive multiplicity and no other progression, has negative weight at its first positive atom. Finitely many added or removed ordinates change only the continuous density and cannot repair that weight. A double lattice through zero passes all three tests.

## Two patterns that pass the test

Choose any sequence of large Yokoi discriminants and give a model completed function the same conductor parameter $d$. Set $p=\log(d/5)/(2r)$ and multiply $\Lambda_5(s)$ by

```math
 \prod_{j=1}^r 2\{\cosh(p(s-1/2))-\cos\theta_j\}.
```

The critical-line symmetry is exact. Each factor adds the two grids $(2\pi k\pm\theta_j)/p$. Together they add $rpT/\pi+O(r)$ positive heights through $T$. Their contribution to $P$ is exactly

$$
 \frac pL\sum_{j=1}^r
 \frac{\sinh(px/L)}{\cosh(px/L)-\cos\theta_j}.
$$

Take $r=1$ and $\theta_1\to0$. The scaled zero measure from these grids tends to the double lattice $4\pi\mathbb Z$. Its density is exactly $1/(2\pi)$, and its corrected real trace is
$1/(e^{x/2}-1)+1/(2x)$, a Laplace transform with positive masses at $k/2$ for $k=1,2,\ldots$ and positive constant density. This attains (6) at the level of the model.

Alternatively take $r=\lfloor\sqrt L\rfloor$ and $0<\theta_j$ distinct with $r\max_j\theta_j\to0$. Then $p\to\infty$. The $2r$ nearest added ordinates all have scaled height tending uniformly to zero. Taylor expansion of the displayed quotient gives $(2r/x)(1+o(1))$ for their grids' full trace, locally uniformly for positive $x$. The fixed conductor-five term is $O_x(L^{-2})$. The normalized trace tends to $1/x$, also completely monotone. The grids in both constructions can have strictly positive first heights. For either kernel of the earlier explicit formula the model's bias plus zero sum stays positive throughout each fixed interval $0<u\le aL$ for all large $d$. Indeed each pair of grids contributes nonnegatively up to $p(\pi/(3\theta_j)-2)$, whose ratio to $L$ tends uniformly to infinity. The fixed factors cost less than $1/4$ against the bias $2/3$. [Grid periodization and the fixed-factor bound](GRID.md)

After removing the gamma and conductor factors the model is $L(s,\chi_5)\prod_j(1-2\cos\theta_j e^{-p(s-1/2)}+e^{-2p(s-1/2)})$. Its first new Dirichlet monomial has base $e^p$ and coefficient $-2e^{p/2}\sum_j\cos\theta_j$. For a nonintegral base, uniqueness of the leading exponent at real $s\to\infty$ excludes any ordinary Dirichlet series with integer bases. For an integral base the change exceeds two in absolute value for large $d$, whereas two quadratic coefficients differ by at most two. Also the model's logarithmic derivative after removing conductor and gamma tends to $L'/L(s,\chi_5)$ on every compact set to the right of the centre, since $rp e^{-\delta p}\to0$ for fixed $\delta>0$. Genuine Yokoi fields can share these outer values and can keep the average positive on any prescribed **fixed** interval. [Arithmetic approximation and its quantifiers](REAL-AXIS-OUTER.md)

The examples rule out a deduction from these limiting positivity conditions alone. To get one exponent for every sufficiently large field one still needs arithmetic that excludes all delaying configurations at distance comparable to $1/\log d$ from the centre, or another way to force the sign. [Earlier work and scope](PRIOR-WORK.md#real-values-and-the-sign-of-the-future-average)
