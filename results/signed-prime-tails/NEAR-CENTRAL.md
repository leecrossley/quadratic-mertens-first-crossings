# Which near-central zeros can delay a negative prime average?

Lee Crossley

Take a positive fundamental discriminant $`d`$, put $`L=\log(3d)`$, and write $`\gamma`$ for a nontrivial zero ordinate of the primitive quadratic Dirichlet function $`L(s,\chi_d)`$. Assume RH for the Riemann zeta function and GRH for each quadratic character considered (field GRH). All statements about the fields below use these hypotheses. They apply in particular to the Yokoi fields with $`d=n^2+4`$ squarefree and $`n`$ odd.

Write $`B_d(t)`$ for the logarithm of the prime-ideal Mertens product over norms through $`t`$, less $`\gamma_E+\log L(1,\chi_d)+\log\log t`$. The question concerns the first starting point $`y`$ at which its future average $`F_d(y)=\int_y^\infty B_d(t)y\,dt/t^2`$ is negative.

**An isolated pair.** There are absolute constants $`a,C>1`$ with the following property for every sufficiently large $`d`$. Suppose the interval $`|\gamma|\le 1/L`$ contains a pair, possibly a double zero at zero, and these are the only two ordinates in $`|\gamma|\le C/L`$, counting multiplicity. Then $`F_d(y)<0`$ for some $`2\le y\le d^a`$. The constants are independent of the height of the pair. They and the threshold for $`d`$ are not made explicit. Order the pairs by their nonnegative heights, with multiplicity. A central zero of order $`2r`$ contributes $`r`$ pairs at height zero. Write $`g_d`$ and $`h_d`$ for the first two heights. In particular this works along sequences with $`g_dL\to0`$ and the next pair at height $`h_d`$ with $`h_dL\to\infty`$. A second test uses two occupied windows, near $`t`$ and $`3t`$, and two empty windows, near $`2t`$ and $`4t`$. The result leaves open the existence of one exponent for the whole family.

## How many other zeros a delay requires

Let $`N_d(t)`$ count quadratic ordinates with $`L|\gamma|\le t`$, with both signs and multiplicities. Let $`J_d(T)`$ count **distinct positive heights** with $`1<L\gamma\le T`$.

**Theorem 1.** For each integer $`m\ge2`$ there are positive constants $`a_m,c_m,\eta_m,T_m`$, with $`T_m>1`$, such that for all sufficiently large $`d`$, the assumptions

$$
N_d(1)\le m,\qquad F_d(y)\ge0\quad (2\le y\le d^{a_m})
$$

imply

$$
J_d(T)\ge c_m T\qquad(T_m\le T\le\eta_m L).
$$

A shortage at even one of these scales gives a negative starting point. Taking $`m=2`$ and $`C=T_2`$ gives the isolated-pair result.

**Theorem 2.** Suppose $`d_n\to\infty`$, $`b_n\to\infty`$ and $`F_{d_n}`$ stays nonnegative from 2 to $`d_n^{b_n}`$. Along any subsequence on which $`N_{d_n}(1)`$ is bounded, the counting measures of the rescaled ordinates $`x=L_n\gamma`$ have vaguely convergent subsequences. Here vague convergence means convergence against every continuous compactly supported function. For **every** such limit $`\mu`$ the following hold.

- Its support is infinite and locally finite. Its point masses are bounded positive integers on the support.
- Each positive multiplicity level set, and the support itself, differs in finitely many points from a finite union of two-sided arithmetic progressions $`\beta+\alpha\mathbb Z`$, $`\alpha>0`$. The union for the support contains at least one progression. The steps may differ.

On any subsequence with $`N_{d_n}(1)\to\infty`$, one has $`N_{d_n}(\epsilon)\to\infty`$ for **every** fixed $`\epsilon>0`$. One can also choose $`\epsilon_n\downarrow0`$ with $`N_{d_n}(\epsilon_n)\to\infty`$ on that subsequence.

The progressions describe limiting heights. Inferring exact relations between the zeros of an individual field would require further information.

## Why the lowest pair can be held at the centre

Put $`u=\log y`$ and $`k(v)=e^{-v/2}(1-e^{-v})`$. In the formula for $`u e^{u/2}F_d(e^u)`$ the pair at $`\pm g`$ contributes $`2\int_0^\infty k(v)u\cos(g(u+v))/(u+v)\,dv`$. Holding all other terms fixed and replacing the pair by two central terms increases this expression by

```math
0\le 2\int_0^\infty k(v)\frac{u}{u+v}\{1-\cos(g(u+v))\}\,dv
\le g^2\left(\frac43u^2+\frac{32}{9}u\right).
```

Use $`1-\cos z\le z^2/2`$ and the zeroth and first moments of $`k`$. Thus for fixed $`a`$ the change tends uniformly to zero for $`2\le y\le d^a`$ when $`gL\to0`$. The replacement is a comparison of terms of the explicit formula. The proof below keeps the actual quadratic character. [Explicit formula, equation (2)](NEAREST-ZERO.md#removing-the-varying-denominator)

## A uniform count in short intervals

The nearest-zero proof bounds the weighted negative part in (3) and gives the Fourier estimates in (4)–(7). Both use $`F_d\ge0`$ through $`e^{2H}`$ with $`H\ge L`$. [Equation (3)](NEAREST-ZERO.md#removing-the-varying-denominator) [Equations (4)–(7)](NEAREST-ZERO.md#a-positive-fourier-weight-for-nearby-zeros)

The frequency $`\lambda`$ runs over both the ordinary and the quadratic ordinates. Set

$$
c_\lambda=((1/2-i\lambda)(3/2-i\lambda))^{-1},\quad
w_\lambda=|c_\lambda|,\quad b=2/3,\quad
Z(u)=b+\sum_\lambda c_\lambda e^{i\lambda u}.
$$

Let brackets denote the triangular probability weight $`2(1-u/H)\,du/H`$ on $`[0,H]`$, and put $`M_H(t)=\langle Z(u)e^{-itu}\rangle`$, $`K_H(t)=\langle e^{itu}\rangle`$ and $`D_H(t)=\sum_\lambda w_\lambda\,\mathrm{sinc}^2(H(\lambda-t)/2)`$. The negative part of $`Z`$ has weighted mean $`O(L/H)+o(1)`$ uniformly for $`H\ge L`$. The total $`w`$-mass on any interval of length $`1/H`$ is at most $`2(D_H(0)+C_0)`$. The contribution to $`D_H(t)`$ from $`|\lambda-t|>R/H`$ is at most $`C_1(D_H(0)+C_0)/R`$ for $`R\ge2`$, with absolute constants. Also $`|M_H(t)|\le b+D_H(0)+O(L/H)+o(1)`$, and for $`\theta_t=\arg c_t`$ chosen continuously with $`\theta_0=0`$,

$$
\Re(e^{-i\theta_t}M_H(t))
=D_H(t)+b\Re(e^{-i\theta_t}K_H(-t))+O(L/H).
\tag{1}
$$

Here $`\mathrm{sinc}(x)=\sin(x)/x`$ with value one at zero, and $`|K_H(t)|\le\min(1,4/(H|t|))`$ for $`t\ne0`$. The $`o(1)`$ terms here are uniform for $`H\ge L`$ as $`d\to\infty`$.

Fix $`0<\delta\le1`$ and an absolute $`K>\max(2,2C_1)`$. Take $`H\ge KL/\delta`$. The ordinary factor has no zero within $`\delta/L`$ for large $`d`$. Split $`D_H(0)`$ at that radius, use $`w_\lambda\le4/3`$ inside and apply the tail estimate with $`R=H\delta/L`$ outside. Absorbing its $`D_H(0)`$ term gives $`D_H(0)\ll 1+N_d(\delta)`$. In particular, first taking $`H=KL/\delta`$ and covering an interval of length $`1/L`$ gives a $`w`$-mass bound $`O_\delta(1+N_d(\delta))`$ on **every** such interval. Each use requires nonnegativity up to the corresponding $`e^{2H}`$. On a fixed bounded interval in the unscaled ordinates, $`w_\lambda`$ is bounded below, so this also bounds the number of ordinates there per interval of length $`1/L`$.

## Four short intervals that suffice with a central pair

**Finite test.** There are absolute constants $`a,r,\epsilon>0`$ such that every sufficiently large $`d`$ with the following properties has $`F_d(y)<0`$ for some $`2\le y\le d^a`$. Assume $`N_d(1/4)\le2`$. Suppose some $`t`$ with $`1/L\le t\le r`$ has a quadratic ordinate within $`\epsilon/L`$ of each of $`t`$ and $`3t`$, and no quadratic ordinate within $`1/(4L)`$ of either $`2t`$ or $`4t`$. These are the only four off-centre windows that need checking. Zeros elsewhere, including at $`5t`$, may have arbitrary multiplicity. The criterion allows an exact double central zero.

To prove this, assume a delay, take $`H=AL`$ and put $`m_j=(3/4)\Re M_H(jt)`$, $`0\le j\le5`$. Fix $`\nu=1/100`$. For suitably chosen absolute constants, (1) gives

$$
m_0\le5/2+\nu,\quad m_1,m_3\ge1-\nu,\quad
m_2,m_4\le\nu,\quad m_5\ge-\nu .
$$

Indeed the short-interval estimate at $`\delta=1/4`$ first gives $`D_H(0)=O(1)`$. Its tail beyond $`1/(4L)`$ costs $`O(1/A)`$, leaving $`D_H(0)\le8/3+O(1/A)`$. At the empty windows the same tail estimate gives $`D_H(2t),D_H(4t)=O(1/A)`$ once $`5r`$ and the window radii lie inside the ordinary central zero-free interval. At $`t`$ and $`3t`$ one observed zero contributes at least $`(4/3-O(r+1/L))(1-O((A\epsilon)^2))`$ since $`A\epsilon`$ can be chosen small. At $`5t`$ use $`D_H(5t)\ge0`$. For $`j>0`$ the bias term in (1) costs $`O(1/A)`$ because $`Ht\ge A`$. Removing the phase costs $`O(r)`$ by the bound on $`|M_H(jt)|`$. The implicit constants are absolute here. Take $`A`$ sufficiently large, $`r`$ sufficiently small, then $`\epsilon`$ sufficiently small and $`d`$ sufficiently large. Set $`a=4A`$.

Use the six coefficients $`1,-1,1,-1,1,-1`$ at frequencies $`0,t,\ldots,5t`$. Expanding the square gives

$$
\frac34\left\langle Z(u)\left|\sum_{j=0}^5(-1)^j e^{ijtu}\right|^2\right\rangle
=6m_0-10m_1+8m_2-6m_3+4m_4-2m_5
\le -1+36\nu .
$$

The modulus of the sum is at most six. Hence the left side is at least $`-27\langle Z_-\rangle`$, which exceeds $`-1/2`$ for sufficiently large $`A,d`$. The bounds contradict each other. This argument only needs a lower bound at the fifth height because its coefficient is negative. [Exact coefficients and checks](central_patterns.py)

## Proof of Theorem 1

Fix $`m`$. Use the constants of the [difference test, Theorem 2](NEAREST-ZERO.md#a-test-in-the-presence-of-a-central-zero), with $`k=\lfloor(m+1/2)^2\rfloor+1`$. As in its proof, fix $`R,r`$ first and take $`H=AL`$ with $`A`$ sufficiently large, in particular $`A>\max(K,4R)`$. A delay through $`d^{a_m}`$ covers $`e^{2H}`$ upon choosing $`a_m=4A`$. There are at most $`m`$ quadratic ordinates in $`[-R/H,R/H]`$. For large $`d`$ the entire fixed interval $`I=[r/2,r]`$ lies in $`[R/H,r]`$. The fixed-interval count gives $`(|I|/(2\pi)+o(1))L`$ positive quadratic ordinates in $`I`$. This follows from weak convergence there to Lebesgue measure divided by $`2\pi`$, using symmetry and the paired logarithmic derivatives at real points greater than one. [Fixed-interval count](PROOF.md#extracting-a-single-frequency)

For $`2\le T\le |I|L`$, partition $`I`$ into $`\lceil 2|I|L/T\rceil`$ equal intervals, assigning endpoints once. Some interval of length at most $`T/(2L)`$ contains at least a constant times $`T`$ ordinates. Choose one ordinate at a time there and discard everything within $`3/L`$ of it. Each choice discards at most $`O_m(1)`$ ordinates by the preceding short-interval bound with $`\delta=1`$. We obtain a set of $`s\ge\beta_m T`$ distinct heights, separated by more than $`3/L`$, for some $`\beta_m>0`$ independent of $`T,d`$.

Join two chosen heights if their difference is within $`R/H`$ of a quadratic ordinate. Symmetry makes this an undirected graph. Every signed ordinate responsible for an edge has $`1<L|\lambda|\le T`$ by the separation and the length of the interval. At a given vertex, one signed ordinate can account for at most one neighbor, since $`2R/H<3/L`$. The maximum degree is therefore at most $`2J_d(T)`$, even if a zero has high multiplicity. An independent set of size $`k`$ would satisfy every separation and difference hypothesis of the earlier test, contradicting the assumed delay. A maximal independent set covers the graph by its closed neighborhoods, so

$$
\beta_m T\le s\le(k-1)(1+2J_d(T)).
$$

Take $`\eta_m=|I|`$, $`c_m=\beta_m/(4(k-1))`$ and $`T_m`$ sufficiently large. All constants were chosen before $`d`$ and $`T`$.

## Proof of Theorem 2

First suppose $`N_{d_n}(1)\le m`$, increasing $`m`$ to two if necessary. The short-interval bound at $`\delta=1`$ applies eventually. It gives a bounded count on every compact interval in scaled coordinates. By extraction on expanding compact intervals, the counting measures have vague limit points. Local boundedness and unit integer masses imply that each limit is itself an integer counting measure, allowing coalescence. In fact every unit interval in a fixed compact set in scaled coordinates eventually corresponds to $`|\lambda|\le1`$, where $`w_\lambda`$ has an absolute positive lower bound. The resulting bound per unit interval, with endpoints covered by two slightly larger intervals if needed, is independent of the compact set. All atom multiplicities in the limit are bounded in terms of $`m`$. The ordinary ordinates leave every scaled compact set.

For fixed $`T\ge T_m`$, Theorem 1 for large $`n`$ gives at least $`c_mT`$ mass in the compact interval $`[-T,T]`$. The closed-set inequality for vague convergence gives $`\mu([-T,T])\ge c_mT`$. Thus the limit has infinite support. The same extraction and bounds apply to any specified convergent subsequence.

Write $`n(x)=\mu(\{x\})`$, with value zero off the support. We claim that the function

```math
a(x)=n(x)+\tfrac12\,\mathbf 1_{\{0\}}(x)
\tag{2}
```

is positive definite on the additive group of reals with the discrete topology. Fix any finite list $`x_i`$ and let $`E`$ be its finite set of differences, including zero. Around each $`x\in E`$ choose a fixed interval containing no other limiting atom and with atom-free endpoints. For a point off the support choose an interval containing no atoms. Integer counts and vague convergence give exactly $`n(x)`$ rescaled ordinates there eventually, all tending to $`x`$. Let $`e_n`$ be the largest of their distances to their respective $`x`$, or zero for an empty collection. Choose $`B_n\to\infty`$ slowly enough that $`B_n e_n\to0`$ and $`2B_n L_n\le b_n\log d_n`$. Set $`H_n=B_n L_n`$. This choice counts nearby zeros together even when the original ordinates are distinct.

At $`t=x/L_n`$ each of these ordinates contributes $`4/3+o(1)`$ to $`D_{H_n}(t)`$. All others are at distance at least $`\epsilon/L_n`$ for some fixed $`\epsilon>0`$ depending on $`E`$. The tail estimate with $`R=B_n\epsilon/2`$ gives $`o(1)`$ because $`D_{H_n}(0)=O_m(1)`$. Thus (1), the bound on $`|M_{H_n}|`$ and $`\theta_{x/L_n}\to0`$ give

```math
\Re M_{H_n}(x/L_n)\longrightarrow (4/3)n(x)+b\,\mathbf 1_{\{0\}}(x).
```

For real $`p_i`$ the quadratic form in these real parts is the triangular mean of $`Z(u)|\sum_i p_i e^{i x_i u/L_n}|^2`$. It is bounded below by $`-(\sum_i|p_i|)^2\langle Z_-\rangle`$, which tends to zero. Pass to the limit and divide by $`4/3`$. The resulting matrix with entries $`a(x_i-x_j)`$ is real symmetric, hence its nonnegativity for real vectors also gives nonnegativity for complex vectors. This proves (2). The additional half at the origin is $`b/(4/3)`$.

By Bochner's theorem for a discrete abelian group, $`a`$ is the Fourier transform of a finite positive measure on its compact dual. Its finite range consists of integers and the half-integer at the origin. For any nonzero level, polynomial interpolation on this finite range expresses its indicator as a polynomial in $`a`$. Products of such transforms are transforms of convolutions and the constant one is the transform of the unit point mass. The indicator is therefore a Fourier–Stieltjes transform taking only the values zero and one. Cohen's idempotent theorem puts that level set in the coset ring of the discrete group. It is locally finite in the usual real line. Rosenthal's classification says precisely that such a set is a finite union of two-sided arithmetic progressions up to a finite symmetric difference. Taking finite unions or restoring the point at zero gives the assertion for each positive multiplicity and for the support. [Bochner's theorem](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118165621) · [Green and Sanders on the idempotent theorem](https://annals.math.princeton.edu/2008/168-3/p09) · [Rosenthal’s classification, statement (4.4)](https://eigen-space.org/ps/tilings.pdf#page=18)

Finally suppose $`N_{d_n}(1)\to\infty`$. For each fixed $`0<\delta\le1`$, take $`H=KL_n/\delta`$, permitted eventually by the growing deadline. Covering $`[-1/L_n,1/L_n]`$ by the short-interval estimate gives $`N_{d_n}(1)\ll_\delta 1+N_{d_n}(\delta)`$. Consequently $`N_{d_n}(\delta)\to\infty`$ for every such $`\delta`$, and monotonicity gives the claim for larger $`\delta`$. For $`\delta=1/j`$ choose successively increasing indices after which the count is at least $`j`$. This gives the shrinking sequence in the statement.

The [earlier grid model](GRID.md) checks the scope of the conclusion. With $`D=5e^{2P}`$, $`P\to\infty`$ and shifts $`\pm\theta/P`$ with $`\theta\to0`$, the added ordinates rescaled by $`\log(3D)`$ converge to the double lattice $`4\pi\mathbb Z`$. Its function (2) is $`2\mathbf 1_{4\pi\mathbb Z}+\tfrac12\mathbf 1_{\{0\}}`$, which is positive definite. The model's prime coefficient violates the quadratic Euler factor. Proving that the two alternatives cannot occur in a delaying sequence of genuine Yokoi characters is the remaining arithmetic step. [Comparison and novelty search](PRIOR-WORK.md#near-central-zeros-on-the-conductor-scale) · [Verification and replay](README.md#near-central-zeros-on-the-conductor-scale)

## A test using values on the real axis

For $`x>0`$ and the completed quadratic function $`\Lambda_d(s)=(d/\pi)^{s/2}\Gamma(s/2)L(s,\chi_d)`$, put

$$
P_d(x)=\frac{1}{L}\frac{\Lambda_d'}{\Lambda_d}\left(\frac12+\frac{x}{L}\right).
$$

**Corollary.** Along a sequence of delays in Theorem 2, if $`N_d(1)\to\infty`$ then $`P_d(x)\to+\infty`$ for each $`x>0`$. Along a bounded-count subsequence converging to $`\mu`$, the functions $`P_d`$ converge locally uniformly on $`x>0`$. The limit is a finite **integer linear combination** of functions of the two forms

$$
\frac{x}{x^2+t^2},\qquad
\frac{\pi}{\alpha}
\frac{\sinh(2\pi x/\alpha)}
     {\cosh(2\pi x/\alpha)-\cos(2\pi\beta/\alpha)}
\qquad(t,\beta\in\mathbb R,\ \alpha>0).
$$

Indeed the paired Hadamard product gives $`P_d(x)=\sum_\gamma x/(x^2+(L\gamma)^2)`$, including $`1/x`$ for each central zero. Every term is positive, so the first conclusion follows from the zeros with $`L|\gamma|\le1`$. In the bounded case take $`x`$ in a compact subinterval of $`(0,\infty)`$. The mass with $`T<L|\gamma|\le L`$ costs $`O_m(1/T)`$ in the transform, uniformly on that compact set, by the unit-interval count at $`|\gamma|\le1`$. The terms with $`|\gamma|>1`$ cost $`O(1/L)`$ since $`\gamma^{-2}\ll w_\gamma`$ there and $`\sum w_\gamma\ll L`$. Vague convergence on the remaining compact range, using a continuous cutoff, gives the transform of $`\mu`$. Convergence there is uniform in $`x`$ by equicontinuity of the compactly truncated kernels and the uniform bound on the enclosed mass.

The integer weight of $`\mu`$ is a finite integer combination of singleton and progression indicators by Theorem 2 and inclusion-exclusion. Two progressions intersect in a progression, a single point or the empty set. A singleton gives the first function above. Periodizing $`x/(x^2+t^2)`$ on a progression gives the second. Its Fourier coefficients are $`(\pi/\alpha)e^{-2\pi |k|x/\alpha}`$ before translation, and summing the two geometric series gives the displayed quotient.

For example, the double lattice in the grid model gives $`P(x)=\tfrac12\coth(x/4)`$. This is also a check on the coefficient of a double zero at small $`x`$. A bounded measurement of $`P_d`$ at one positive $`x`$ rules out unbounded $`N_d(1)`$ along that sequence. The formula then gives a concrete restriction to test using completed quadratic functions on the real axis.

### Three real measurements in the late field

For $`d=2{,}380{,}853`$ the values $`P_d(1/4),P_d(1/2),P_d(1)`$ lie within $`10^{-11}`$ of $`1.899512107795`$, $`2.232132467629`$, $`1.704476593310`$, respectively. They prove

$$
0.4480 \lt Lg_d \lt 0.4524,\qquad N_d(1)=2 .
$$

For the lower bound write $`s=Lg_d`$ and use $`P_d(x)\ge2x/(x^2+s^2)`$. A noncentral zero occurs with its conjugate, and a zero at the centre has even order by the functional equation. For $`0<x<z`$ put $`R=(P_d(x)/x)/(P_d(z)/z)`$. This is a positive weighted mean of $`(z^2+t^2)/(x^2+t^2)`$ over rescaled ordinates $`t`$. That ratio decreases in $`t^2`$. Hence $`R>1`$ and $`s^2\le(z^2-Rx^2)/(R-1)`$. Take $`x=1/4,z=1/2`$. Finally each zero with $`|t|\le1`$ contributes at least $`1/2`$ to $`P_d(1)`$, which gives $`N_d(1)<4`$. The height bound and evenness give the exact count.

The program evaluates $`\Lambda_d`$ and $`\Lambda_d'`$ at the three real arguments with the theta integral. For $`v=x/(2L)`$ the two weights on the positive integration axis are $`\cosh(vt)`$ and $`(t/2)\sinh(vt)`$. Since $`0<v<1/4`$, the strip-edge integrals of each weighted integrand are bounded by $`100d^2`$ using $`|G(z)|\le d^2e^{-7|\Re z|/4}`$ on $`|\Im z|=1`$. The previously certified spatial tail and trapezoidal allowance $`10^{-48}`$ cover both weights. The program reads no zero brackets. The earlier sign-bracketing calculation puts $`Lg_d`$ between $`0.4496174`$ and $`0.4496176`$. This field illustrates the real-axis test. The finite computation supplies no discriminant threshold or exponent for the general theorem. [Trace code](central_trace.py) · [Interval enclosures](evidence/near-central-trace.txt) · [Theta integral and errors](../fixed-weight-delay-2380853/QUADRATURE.md) · [Earlier critical-line calculation](../fixed-weight-delay-2380853/PROOF.md)
