# Prescribing a second quadratic prime race in a sparse Euler product

Lee Crossley

Take the real quadratic characters $`\chi_5,\chi_{13}`$, and $`\chi_{65}=\chi_5\chi_{13}`$. Assume the critical-line property for $`\zeta`$ and these three fixed Dirichlet functions. Use the real critical strip convention $`0<\Re s<1`$. [Critical-line input](https://math.mit.edu/~drew/grh/)

**Theorem.** Let $`P`$ be sufficiently large, $`D=13e^{2P},\ 0\le\theta<\pi/3,\ 0\le\beta\le\pi`$. There is a real completely multiplicative prime assignment $`\xi`$, ramified only at 13, for which the following hold.

* Both Euler products, for $`\xi`$ and $`\xi\chi_5`$, continue to $`\Re s>1/4`$. Their additional zero ordinates relative to $`L(s,\chi_{13})`$ and $`L(s,\chi_{65})`$ are respectively $`(2\pi k\pm\theta)/P`$ and $`(2\pi k\pm\beta)/P`$, all on the critical line with the indicated multiplicities. Each adds $`PT/\pi+O(1)`$ positive ordinates through $`T`$, giving the change in the conductor term from 13 to $`D`$ and 65 to $`5D`$. $`D`$ is a scale parameter.
* All four joint prime counts for $`\xi,\chi_5`$ have their natural main term with the smoothed error $`O_\varphi(\sqrt x\log(3D))`$, uniformly in $`x\ge2`$. In particular the two opposite disagreement classes both occur on every dyadic scale above $`C_\varphi\log^2(3D)`$ for a fixed nonnegative bump of positive integral.
* Define $`N_y=\sqrt y\log y`$. With the quadratic local norms and the same weight $`y\,dt/t^2`$ as in the real-field question, $`N_yF_\xi(y)>1/100`$ for all $`y\ge2`$ when $`\theta=0`$. For $`0<\theta<\pi/3`$ this holds throughout $`\log2\le\log y\le P(\pi/(3\theta)-2)`$. For any fixed exponent $`a>0`$ one can first choose $`\theta>0`$ and then take arbitrarily large $`P`$ so that this includes $`2\le y\le D^a`$.
* Give primes split for $`\xi`$ and inert for 5 weight $`+1`$, the opposite class weight $`-1`$, and the rest weight zero, with ramified primes excluded. Write $`W_{\xi,5}(\log y)=N_y\sum_{p>y}a(p)(1-y/p)/p`$. Then

```math
 W_{\xi,5}(P-\log3)=-\frac{2\cos\theta}{3\sqrt3}\,P+O(1),
 \qquad W_{\xi,5}(P)=O(1).
 \tag{1}
```

The signed lead rises by order $`\log D`$ across a factor of three even when the average stays positive. One may fix $`\beta=\pi/2`$ while imposing an exact central zero or a near-central pair in the first product. Both statements concern the added zeros; any zeros of the fixed base functions are retained.

For $`\beta=\pi/2`$ the twist is nonzero at its centre. The base value $`1.2815<L(1/2,\chi_{65})<1.2816`$ is enclosed in [the arithmetic checks](scripts/verify.py), and $`Q_{\pi/2,P}(1/2)=2`$.

The assignment uses ordinary rational primes. It is an Euler-product model. The question for actual Yokoi discriminants imposes global reciprocity and a completed functional equation of the actual conductor.

## The four sign classes

For $`j\ge1`$ put $`X_j=e^{jP},\ c_j=\cos(j\theta),\ b_j=\cos(j\beta)`$, and

```math
 a_{j,\eta}=(c_j+\eta b_j)/2,\qquad \eta=\pm1.
```

In the packet $`[X_j,X_j+X_j^{3/4}]`$, for each $`\eta`$ take the first $`\lfloor|a_{j,\eta}|\sqrt{X_j}/j\rfloor`$ primes with $`\chi_5(p)=\eta`$ and $`\chi_{13}(p)=\operatorname{sgn}(a_{j,\eta})`$. A zero count requires no choice. Reverse their $`\chi_{13}`$ signs. Retain all other prime values, and extend multiplicatively.

The four eligible classes have indicators $`(1+\epsilon\chi_{13})(1+\eta\chi_5)/4`$ on primes away from 65. The log-weighted prime number theorem for the three fixed characters and $`\zeta`$ gives $`X^{3/4}/(4\log X)(1+o(1))`$ available primes per class in a packet at $`X`$, uniformly for $`X\ge e^P`$ as $`P\to\infty`$. The $`O(\sqrt X\log^2 X)`$ endpoint errors are smaller than the main term. Each selection exists uniformly in $`j`$. Summing the signed counts of changed primes with their *old* signs approximates $`c_j\sqrt X/j`$ with error at most 2. Multiplying those old signs by $`\chi_5(p)`$ instead gives $`b_j\sqrt X/j`$ with the same error. This follows from $`a_{j,+}+a_{j,-}=c_j`$ and $`a_{j,+}-a_{j,-}=b_j`$. The total number of changes is at most $`\sqrt X/j`$, since $`(|c+b|+|c-b|)/2=\max(|c|,|b|)`$.

## Both continuations and the joint prime counts

Initially take $`\Re s>1`$. In the quotient of either new Euler product by its base, expand the logarithms. Even powers cancel. The linear term in packet $`j`$ is $`-2\sum_{\rm changed}\chi_{13}(p)p^{-s}`$ for the first quotient, with an additional $`\chi_5(p)`$ for the other. On compact sets with $`\Re s\ge\sigma>1/4`$, replacing $`p`$ by $`X`$ costs $`O((1+|s|)X^{1/4-\sigma}/j)`$ by differentiation. Rounding costs $`O(X^{-\sigma})`$ and the odd powers of order at least three cost $`O_\sigma(X^{1/2-3\sigma}/j)`$. These bounds are summable locally. The remaining term is $`-2\sum_{j\ge1}\cos(j\alpha)e^{-jP(s-1/2)}/j`$ for $`\alpha=\theta,\beta`$ respectively. Exponentiating gives throughout $`\Re s>1/4`$

```math
 L_\xi=L_{13}Q_{\theta,P}e^{G_1},\qquad
 L_{\xi\chi_5}=L_{65}Q_{\beta,P}e^{G_2},\qquad
 Q_{\alpha,P}=1-2\cos\alpha\,e^{-P(s-1/2)}+e^{-2P(s-1/2)}
```

for holomorphic $`G_1,G_2`$. Factoring $`Q`$ proves the zero formulas. At $`\theta=0`$ its central order is two. The base $`L_{13}`$ has a fixed gap around zero by its inverse-square mass certificate. For sufficiently large $`P`$ the added near pair is the closest pair of the first product. [Base-field zero estimate](https://github.com/leecrossley/yokoi-mertens-positive-averages-5-13/blob/f7233ab4e1c85b9b37bffdaa11c4559d7713bd62/PROOF.md)

Precisely, for $`\varphi\in C_c^\infty((1,2))`$ the sum of $`\log p\,\varphi(p/x)`$ in each joint class is

```math
 \frac{x}{4}\int_1^2\varphi(v)\,dv+O_\varphi(\sqrt x\log(3D)).
```

The fixed base pair has error $`O_\varphi(\sqrt x)`$ by its smoothed explicit formulas. The Mellin transforms decay rapidly and prime powers of order at least two contribute $`O_\varphi(\sqrt x)`$ by Chebyshev. The interval $`[x,2x]`$ intersects at most one packet. With $`X_j\asymp x`$ its total changed weight is $`O_\varphi((\sqrt{X_j}/j)\log X_j)=O_\varphi(P\sqrt x)`$. This proves the stated bound at every scale. The same two-sided counts for genuine quadratic characters follow by expanding their four class indicators. [Prime tests for actual fields](https://github.com/leecrossley/split-inert-prime-test-obstruction/blob/v1.0.2/PROOF.md)

## Testing the zeros against the two prime sums

There is also a direct check on the prime side for both grids. Let $`(\eta,e,E,\alpha)`$ be $`(\xi,13,D,\theta)`$ or $`(\xi\chi_5,65,5D,\beta)`$. Write $`\Phi_H(v)=(\sin(Hv/2)/(Hv/2))^2`$ with its continuous value at zero. For the finite prime-power expression in the even explicit formula, evaluated at nominal conductor $`E`$, put

```math
 B_{\eta,E,H}(t)=\frac{\log(E/\pi)}H+
 \frac1{2\pi}\int_{\mathbb R}\Phi_H(v-t)\Re\psi(1/4+iv/2)\,dv
 -\frac2H\sum_{n\le e^H}\frac{\Lambda(n)\eta(n)}{\sqrt n}
        (1-\log n/H)\cos(t\log n).
```

Here $`\psi`$ in the integral is the digamma function. Uniformly for $`H\ge1`$, $`|t|\le1`$,

```math
 B_{\eta,E,H}(t)=\sum_{\lambda_e}\Phi_H(t-\lambda_e)
  +\sum_{k\in\mathbb Z,\pm}\Phi_H(t-(2\pi k\pm\alpha)/P)
  +O(Pe^{-P/4}/H).
```

For the genuine base character the first sum equals its prime expression. The change of conductor adds $`2P/H`$. The linear changes at each packet equal, before division by $`H`$, four times the sum of old signs (twisted when indicated) against $`v e^{-v/2}(1-v/H)_+\cos(tv)`$ at $`v=\log p`$. Its local Lipschitz constant on the packet is $`O((1+jP)/\sqrt{X_j})`$, including at the cutoff. Replacing $`v`$ by $`jP`$ and rounding costs $`O(PX_j^{-1/4}+jP/\sqrt{X_j})`$. Even powers agree and the higher odd powers cost $`O(P/X_j)`$. The total main change is

```math
 (2P/H)\left[1+2\sum_{jP\le H}(1-jP/H)\cos(j\alpha)\cos(jPt)\right].
```

Poisson summation of the triangular weight identifies this with the second sum, counting a coincident pair twice. The error estimate is for these finite tests. The analytic factors $`e^{G_1},e^{G_2}`$ need not obey the global functional equations of Dirichlet characters. [Single-character triangular test](https://github.com/leecrossley/split-inert-prime-test-obstruction/blob/v1.0.2/PROOF.md)

## The moving discrepancy and the Mertens average

For each prime $`p`$ take two copies of the norm $`p`$ at sign $`+1`$, one norm $`p^2`$ at sign $`-1`$, and one norm $`p`$ at sign 0. Put $`\ell(v)=-\log(1-1/v)`$ and

```math
 F_\xi(y)=\int_y^\infty
 [\sum_{v\le t}\ell(v)-\gamma-\log L_\xi(1)-\log\log t]\, y\,dt/t^2 .
```

The change in the Euler product at 1 converges absolutely since $`\sum_{\rm changed}1/p<\infty`$. Write $`u=\log y`$ and

```math
 S(u)=P\sum_{jP\ge u}c_j\, e^{-(jP-u)/2}(1-e^{-(jP-u)})\,u/(jP).
```

Uniformly for $`y\ge2`$,

```math
 N_y(F_\xi(y)-F_{13}(y))=2S(u)+O(Pe^{-P/4}),\qquad
 W_{\xi,5}(u)-W_{13,5}(u)=-S(u)+O(Pe^{-P/4}).
 \tag{2}
```

For the first identity the exact change is a sum over flipped primes with their old sign $`\chi_{13}(p)`$ times
$`2\ell(p)(1-y/p)_+-\ell(p^2)(1-y/p^2)_+`$.
Indeed an averaged jump has weight $`\min(1,y/v)`$ and the change of normalisation subtracts the full local log. For the second identity each flip changes the orientation by $`-\chi_{13}(p)`$, whichever $`\chi_5`$ sign was assigned to the packet.

For a packet at $`X`$, the functions $`\ell(p)(1-y/p)_+`$ and $`p^{-1}(1-y/p)_+`$ have Lipschitz constant $`O(1/X)`$ in $`\log p`$, uniformly even across the cutoff. They vanish for $`y>X+X^{3/4}`$, so $`N_y\ll\sqrt X\log X`$ on their support. Replacing $`p`$ by $`X`$ has normalised cost $`O(PX^{-1/4})`$, replacing $`\ell(X)`$ by $`1/X`$ costs $`O(P/X)`$, and rounding both counts costs $`O(jP/\sqrt X)`$. The square-norm term vanishes for $`y>(X+X^{3/4})^2`$, giving normalised cost $`O(P/\sqrt X)`$ for the packet. Sum in $`j`$ to get (2).

At $`\theta=0`$ every summand of $`S`$ is nonnegative. If $`0<\theta<\pi/3`$ and $`u\le P(\pi/(3\theta)-2)`$, the first two cosines starting at $`j_0=\lceil u/P\rceil`$ are at least $`1/2`$. The absolute tail from $`j_0+2`$ is bounded by the unsigned weight of $`j_0+1`$ times $`e^{-P/2}/[(1-e^{-P/2})(1-e^{-P})]<1/2`$; this includes $`u=j_0P`$. The certified base estimate $`N_y F_{13}>1/40`$ and the uniform error now give the claimed margin $`1/100`$. For fixed $`a`$ take, for example, $`0<\theta<\pi/[3(2a+3)]`$ and increase $`P`$ to absorb the fixed $`\log13`$. [All-start base estimate](https://github.com/leecrossley/yokoi-mertens-positive-averages-5-13/blob/f7233ab4e1c85b9b37bffdaa11c4559d7713bd62/PROOF.md)

For the fixed pair 13 and 5, $`W_{13,5}=O(1)`$. This follows from the absolutely summable zero kernels for the two fixed conductors, the bounded ramified corrections and the absolutely summable odd prime powers. At $`u=P-\log3`$ the $`j=1`$ contribution to $`S`$ is $`2\cos\theta(P-\log3)/(3\sqrt3)`$ and the remaining terms are $`O(Pe^{-P/2})`$. At $`u=P`$ the first term vanishes. Substitution in (2) gives (1).

A twist by $`\chi_{13}`$ detects the choice of base: away from the sparse changed primes, $`\xi\chi_{13}=1`$ outside ramification. Thus this example isolates the information furnished by the fixed reference field 5. It leaves open the use of further independent twists, periodicity, or the full conductor-specific functional equation for actual fields.
