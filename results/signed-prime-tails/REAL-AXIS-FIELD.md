# Four signs from 51 real measurements

For $d=2{,}380{,}853=1543^2+4$ write $f(u)=u e^{u/2}F_d(e^u)$ for the normalized future Mertens average. Assume RH and the critical-line property of $L(s,\chi_d)$. Each row gives a value attained at some real start in the indicated interval.

| Range of $y$ | Certified value of $f(\log y)$ |
|---|---:|
| $d^4\le y\le d^{10}$ | below $-1.3$ |
| $d^{11}\le y\le d^{18}$ | above $1.8$ |
| $d^{19}\le y\le d^{27}$ | below $-0.5$ |
| $d^{28}\le y\le d^{36}$ | above $0.25$ |

The four intervals are disjoint and ordered, so the average changes sign at least three times between the first and fourth witnesses. An earlier calculation already found a negative start at $d^{7/3}$. The present witnesses describe later behaviour and use only real values of the completed quadratic function and its derivative. [Earlier first crossing bracket](../fixed-weight-delay-2380853/PROOF.md) · [Primary intervals](evidence/real-axis-signs.txt) · [Second calculation](evidence/real-axis-gauss.txt)

## Transfer from the quadratic transform

In the notation of the [real-axis test](REAL-AXIS.md#from-the-weighted-average-to-real-derivatives) use $A=1/2$, $B=3/2$, $b=2/3$ and $G(u)=b+\sum_{\gamma\in\chi_d}c_\gamma e^{i\gamma u}$. Define $V=L\sqrt{P_d(AL)P_d(BL)/(AB)}$. Cauchy–Schwarz applied to the two sequences $(A^2+\gamma^2)^{-1/2}$ and $(B^2+\gamma^2)^{-1/2}$ gives $\sum_\gamma|c_\gamma|\le V$. The computed upper bound is $V<8.423$. The entire ordinary zero contribution with the varying kernel has absolute value at most $V_0=2+\gamma_E-\log(4\pi)<0.046192$.

Write $\sigma=+1$ to seek a positive value and $\sigma=-1$ to seek a negative one. Let $\ell=\log y_{\min}$, $w=\ell/2$ and

$$
 \delta=\left[(w/(2\pi)+2)\log d+2(w^2/(8\pi)+2)\right]e^{-w/2}.
$$

On the target interval $\sigma G(u)\le\sigma f(u)+E_\sigma$ where

$$
 E_+=\frac{8V}{3\ell}+V_0+b,\qquad
 E_-=\frac{8V}{3\ell}+V_0+2\delta+
      \frac{e^{-\ell/2}}{2\tanh\ell}+\frac{39}{5}e^{-\ell/6}.
$$

Indeed each varying zero coefficient differs from $c_\gamma$ by at most $8|c_\gamma|/(3u)$. The archimedean and missing prime-power terms in $f$ are nonnegative. Their upper bound is $b$ plus the last three terms in $E_-$. The bound decreases for $u\ge\ell$, since $\ell/2>4$. At all other $u\ge0$ use $\sigma G(u)\le V+\sigma b$. These estimates require no zero brackets. [Zero kernels](PROOF.md#the-future-integral-of-the-prime-power-error) · [Explicit bounds for the prime powers](../fixed-weight-delay-2380853/PROOF.md)

With $v=u/L$, set $z=\exp(-v/16)$. For a rational centre $c$ form the nonnegative polynomial

$$
 W_c(z)=\left(1+2\sum_{j=1}^{12}T_j(2c-1)T_j(2z-1)\right)^4
       =\sum_{k=0}^{48}w_kz^k,
$$

where $T_j(\cos\theta)=\cos(j\theta)$. Use $c=2/3,5/12,1/4,1/6$ for the four intervals respectively. Give $z\in[0,1]$ probability density $W_c(z)/C$, $C=\int_0^1W_c(z)dz$. Its density in $v$ is proportional to $e^{-v/16}W_c(e^{-v/16})$. Let $p$ be its probability of the target interval in $u$. Equation (3) of the real-axis test, with the quadratic trace in place of the two-factor trace, computes $I_\chi(x)=\int_0^\infty e^{-xv}G(Lv)dv$. Thus the exact mean is

$$
 J=\mathbb E[G(u)]=\frac1{16C}\sum_{k=0}^{48}w_k I_\chi((k+1)/16).
$$

This uses 49 points $s=1/2+j/(16L)$, $1\le j\le49$, and the two endpoints $s=1,2$. Set $D_\sigma=\sigma J-pE_\sigma-(1-p)(V+\sigma b)$. Integrating the bounds above gives $D_\sigma\le p\sup_{\rm interval}\sigma f$. In the four rows $D_\sigma$ exceeds $1.3,1.8,0.5,0.25$ respectively and $0<p<1$. This proves the asserted strict inequalities.

## Numerical checks

Both calculations use outward-rounded Arb intervals. The primary program evaluates the quadratic theta integral by a trapezoidal rule, generates the weights using exact rational polynomials and computes $p$ from their antiderivatives. The second constructs the character by listing squares modulo $d$, sums each Gaussian directly, and uses 64-point Gauss–Legendre quadrature on each of 22 intervals for the 51 real derivatives. It reconstructs the weight polynomial from 49 rational values by finite differences and integrates the weight on each outside interval with a 25-point Gaussian rule, exact through degree 49. Its transfer uses the slightly looser constants $V=8.423$, $V_0<0.046192$ and a uniform prime-power and archimedean excess below $0.001$ on all four intervals.

For the theta weights at horizontal displacement $0<q\le3/2$ the factors on the positive half-axis are $\cosh(qt/2)$ and $(t/2)\sinh(qt/2)$. On the strip $|\Im t|\le1$ the earlier bound $|G_\theta(t)|\le d^2e^{-7|\Re t|/4}$ absorbs $e^{3|\Re t|/4}$ and the derivative factor. The edge integrals for trapezoidal error are below $100d^2$. On the radius-one disks for Gaussian quadrature the much looser bound $8d^2e^{32}$ covers both weights. At $t\ge22$ the same double-exponential theta tail absorbs these real weights. These give the published error allowances also at the right endpoint $s=2$. [Theta representation, truncations and quadrature proof](../fixed-weight-delay-2380853/QUADRATURE.md) · [Trapezoidal program](real_axis.py) · [Gaussian program](real_axis_gauss.py)

Run both programs from this directory using Python with python-flint 0.9.0.

~~~sh
python3 -B real_axis.py
python3 -B real_axis_gauss.py
~~~

The [review packet](review/README.md) contains all 51 intervals, a standard-library replay of the four signs, and commands to reconstruct the table by both quadrature rules.
