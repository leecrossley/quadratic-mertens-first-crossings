# Delayed quadratic Mertens averages force deficits on rough integers

Lee Crossley

Let $`d>1`$ be a positive fundamental discriminant, $`\chi=\chi_d`$ its real primitive even character, and $`k=\mathbb Q(\sqrt d)`$. The Yokoi family considered here has $`d=m^2+4`$ squarefree with $`m`$ odd. Write $`L=\log d`$ and $`\ell=\log L`$ for large $`d`$. The prime-ideal product and its future average are measured by

```math
 B_d(t)=\sum_{N\mathfrak p\le t}-\log(1-1/N\mathfrak p)-\gamma-\log L(1,\chi)-\log\log t,
 \qquad F_d(y)=\int_y^\infty B_d(t)\frac{y}{t^2}\,dt.
```

Use RH for the ordinary zeta function and GRH for $`L(s,\chi)`$. The proof identifies where the zero-location hypotheses enter. The original first-crossing problem asks about the unaveraged product. Alpöge's announced Dirichlet GRH theorem supplies this input. [Johnston's Problem 8](https://arxiv.org/html/2407.03530v1) · [Announcement](https://alpo.ge/remark.pdf) · [Independent formal checks](https://math.mit.edu/~drew/grh/)

For a squarefree integer $`q\ge1`$ remove every multiple of its prime factors. The Gaussian sum and the ordinary partial sum of the remaining character values are

```math
 H_q(x)=\frac1{\sqrt x}\sum_{\substack{n\ge1\\(n,q)=1}}\chi(n)e^{-\pi(n/x)^2},
 \qquad S_q(m)=\sum_{\substack{n\le m\\(n,q)=1}}\chi(n).
```

Write $`V_q(x)=S_q(\lfloor x\rfloor)/\sqrt x`$, taking $`S_q(0)=0`$. For either real function $`J=H_q`$ or $`J=V_q`$, let $`P(J)`$ and $`N(J)`$ be the integrals of its positive and negative parts against $`dx/x`$ on $`(0,\infty)`$.

**Theorem.** Fix $`K>0`$. There are $`A_0,B,C,c_1,c_2>0`$ depending at most on $`K`$. For all sufficiently large $`d`$, suppose $`A\ge A_0`$ and $`F_d(y)\ge0`$ at every real $`2\le y\le d^A`$. Then for **every** squarefree $`q`$ with $`\log q\le K L^2`$ there are integers $`m_-<m_+\le d^B`$ such that

```math
 S_q(m_-)<-c_1\,\frac{\sqrt{m_-}}L,\qquad
 S_q(m_+)>c_2\,\frac{\log m_-}{L^2}\sqrt{m_+}.
 \tag{1}
```

One can take $`m_-`$ to be the **first** integer that crosses the indicated negative threshold. If $`m_-\ge d^\epsilon`$ the recovery is at least $`c_2\epsilon\sqrt{m_+}/L`$.

The two profiles also satisfy

```math
 1-\frac{C}{A^2}-O_K(e^{-L/\ell})\le\frac{N(J)}{P(J)}\le1
 \qquad (J=V_q,\ H_q).
 \tag{2}
```

**For every subset of the primes through $`(\log d)^2`$, one may take $`B=8`$ in (1).** The exponent 8 bounds the two character-sum witnesses. The hypothesis still concerns survival of the prime average to a sufficiently large fixed power.

The choice of primes can depend on the field. One may remove all primes through $`K'(\log d)^2`$ for any fixed $`K'>0`$, since $`\sum_{p\le z}\log p\ll z`$. In that case $`m_->K'(\log d)^2`$ because the only surviving integer through that threshold is 1.

Conversely, if one allowable $`q`$ per field satisfies $`N(J)/P(J)\le1-\eta`$ for either profile and a fixed $`0<\eta\le1`$, some $`y\le d^{O_K(1/\sqrt\eta)}`$ has $`F_d(y)<0`$ for all sufficiently large fields in that set. Failure of the ordered pair in (1) for one allowable deletion also suffices. A field with an exact central zero has equal masses for both profiles and every $`q`$. The recovery in (1) still follows in that case, as the proof below shows.

## The reciprocal transform

Put $`G=H_1`$. The Gaussian transformation for a real even primitive character is $`G(x)=G(d/x)`$. Its Mellin transform, with $`s=1/2+it`$, is

```math
 \int_0^\infty G(x)x^{-it}\frac{dx}{x}
 =\tfrac12\pi^{-s/2}\Gamma(s/2)L(s,\chi).
 \tag{3a}
```

The identity follows first for the Mellin variable with $`\Re s>1`$ by integration of the individual Gaussians, then everywhere by continuation. Reciprocity gives exponential decay at both ends in the primitive sum. In particular the reciprocal scales have the same sign. [Gaussian transformation and completed Mellin formula, equations (1)–(3)](https://publi.math.unideb.hu/paper/1837/download/10_5486_PMD_2013_5670.pdf)

Inclusion-exclusion gives two exact expressions for the same sieved sum,

```math
 H_q(x)=\sum_{j\mid q}\frac{\mu(j)\chi(j)}{\sqrt j}\,G(x/j)
       =\sum_{j\mid q}\frac{\mu(j)\chi(j)}{\sqrt j}\,G(dj/x).
 \tag{3b}
```

Its Mellin transform is (3a) multiplied by $`\prod_{p\mid q}(1-\chi(p)p^{-s})`$. Each factor is nonzero on the critical line and positive at its real midpoint. All $`H_q`$ therefore have vanishing transform at the same quadratic zero. For the sharp sum the corresponding transform is

```math
 \int_0^\infty V_q(x)x^{-it}\frac{dx}{x}
 =\frac{L(s,\chi)}{s}\prod_{p\mid q}(1-\chi(p)p^{-s}).
 \tag{3c}
```

For $`q=1`$ this is summation by parts, valid for $`\Re s>0`$ by boundedness of the periodic partial sums. For a general $`q`$ use the finite divisor expansion (3b) with $`H_q,G`$ replaced by $`V_q,V_1`$ in its **first** expression. The reflected Gaussian identity is used only for $`G`$. At $`t=0`$ both signed integrals are nonnegative since $`L(\sigma,\chi)>0`$ for real $`\sigma>1/2`$ under GRH, by continuity from the Euler product. This gives $`N(J)\le P(J)`$ and equality at a central zero.

## Keeping the scale polynomial after deletion

Although $`q`$ can exceed every fixed power of $`d`$, there is $`b=b_K>2`$ such that, uniformly in the allowed $`q`$ for both profiles,

```math
 \int_{x\notin I}\left(1+\frac{|\log x|}{L}\right)|J(x)|\,\frac{dx}{x}
 \ll_K e^{-L/\ell},\qquad I=[L^{-1/2},d^b].
 \tag{4}
```

On $`x\le1`$ use the defining coefficients of $`H_q`$, all of absolute value at most 1. The absolute sum is $`O(x^{-1/2}e^{-\pi/x^2})`$. On $`3/4\le x\le1`$ the $`n=1`$ term is positive and the rest costs at most its size times $`\sum_{h\ge1} e^{-3\pi h}`$. For the sharp sum $`V_q`$ vanishes below 1 and equals $`1/\sqrt x`$ on $`[1,2)`$. Thus $`P(J)\ge c_0>0`$ absolutely and the lower tail in (4) is exponentially small in $`L`$.

We need the following primitive estimate,

```math
 \int_0^\infty (1+|\log x|/L)|G(x)|\,dx/x\le \exp(C_0 L/\ell)
 \tag{5}
```

for an absolute $`C_0`$. Mellin inversion on the critical line bounds $`\sup |G|`$ by a constant times the integral of $`|\Gamma(1/4+it/2)L(1/2+it,\chi)|`$. For $`|t|\le d`$ the GRH bound of Chandee is $`\exp(O(L/\ell))`$. For $`|t|>d`$ the same bound with analytic conductor $`d(2+|t|)`$ is at most a fixed power of that conductor, and the gamma factor decays exponentially. On $`[1,d]`$ integrate this supremum over logarithmic length $`L`$. On the two outer intervals use the small Gaussian bound and reflection. Increasing $`C_0`$ gives (5). [Chandee, Corollary 1.2](https://arxiv.org/pdf/0906.4177#page=3)

For the analogue of (5) with $`V_1`$, apply Plancherel in $`\log x`$ to (3c) at $`q=1`$. For fixed $`d`$, $`|S_1|\le d`$ by periodicity and zero mean of the character, so the original function is integrable and square integrable. Its squared norm is

```math
 \frac1{2\pi}\int_{\mathbb R}\frac{|L(1/2+it,\chi)|^2}{1/4+t^2}\,dt
 \le \exp(O(L/\ell)).
```

For $`|t|\le d`$ use Chandee's bound as above. For $`|t|>d`$ the same estimate implies $`|L(1/2+it,\chi)|\ll |t|^{1/4}`$ for all sufficiently large $`d`$. Cauchy–Schwarz on $`1\le x\le d^4`$ costs only $`O(\sqrt L)`$ in the weighted first norm. On $`x>d^4`$ use $`|V_1(x)|\le d/\sqrt x`$. Increase $`C_0`$ to cover both estimates (5).

Take $`\delta=1/\ell`$, with $`d`$ large enough that $`\delta<1/2`$. There is $`C_1=C_1(K)`$ such that

```math
 \sum_{j\mid q} j^{-1/2+\delta}
  =\prod_{p\mid q}(1+p^{-1/2+\delta})
  \le \exp(C_1 L/\ell).
 \tag{6}
```

For $`p\le L^2`$, $`p^\delta\le e^2`$ and partial summation with $`\pi(v)\ll v/\log v`$ gives $`\sum_{p\le L^2}p^{-1/2}\ll L/\ell`$. There are at most $`K L^2/(2\ell)`$ prime factors above $`L^2`$, each contributing at most $`e^2/L`$ to the logarithmic upper bound. This also covers primes ramified in $`k`$.

For the upper tail in (4) split the divisor sum in (3b) at $`j=d^{b-4}`$. For smaller $`j`$ and $`x>d^b`$ use the reflected argument $`t=dj/x<1/d`$. The extra logarithmic weight is bounded by $`2+b+|\log t|/L`$, so the weighted Gaussian integral is $`O_b(e^{-d^2})`$. For the sharp sum use $`|V_1(x/j)|\le d\sqrt{j/x}`$. Its weighted integral over $`x>d^b`$ is $`O_b(d^{1-b/2}\sqrt j)=O_b(d^{-1})`$ for each such $`j`$. Multiplying either bound by (6) still gives $`o(e^{-L/\ell})`$. For the larger divisors, translating by $`\log j`$ in (5) costs a factor at most $`1+K L`$. Their total weight satisfies

```math
 \sum_{\substack{j\mid q\\j>d^{b-4}}}j^{-1/2}
 \le \exp\big((C_1-b+4)L/\ell\big).
```

Choose $`b>C_0+C_1+7`$. This proves (4), including the logarithmic weight needed below. In particular the two masses in (2) can be recovered to absolute error $`O_K(e^{-L/\ell})`$ using only $`I`$.

### An explicit exponent after removing small primes

For $`q`$ supported on $`p\le L^2`$ one may use $`b=8`$ in (4) with error $`O(e^{-L/(16\ell)})`$. We give the constants because a bound in terms of the full induced modulus $`dq`$ would be much larger.

First, $`C_0=1/2`$ is admissible in the weighted bounds (5) for large $`d`$. For $`|t|\le d^{1/10}`$, Chandee's Corollary 1.2 gives $`\log |L(1/2+it,\chi)|\le(33/80+o(1))L/\ell`$, from the leading constant $`3/8`$ and $`\log(d(|t|+1/2))\le(11/10+o(1))L`$. For $`d^{1/10}<|t|\le d`$ the weaker bound $`\exp(O(L/\ell))`$ is absorbed by the gamma integral or by the integral of $`dt/t^2`$ in the squared-norm calculation. The previous estimates cover $`|t|>d`$. The powers of $`L`$ in converting to (5) are absorbed by the gap between $`33/80`$ and $`1/2`$.

Use $`\delta=1/(2\ell)`$. The prime number theorem and partial summation give $`\sum_{p\le L^2}p^{-1/2}\sim L/\ell`$. Since $`p^\delta\le e`$, the divisor sum in (6) is at most $`\exp((11/4)L/\ell)`$ for all sufficiently large $`d`$. For $`j>d^{27/4}`$ the sum of $`j^{-1/2}`$ is therefore at most $`\exp(-5L/(8\ell))`$. Multiplication by (5) and $`1+O(L)`$ gives $`O(e^{-L/(16\ell)})`$.

For smaller $`j`$ and $`x>d^8`$, $`x/j\ge d^{5/4}`$. In the Gaussian integral the reflected argument is at most $`d^{-1/4}`$. In the sharp integral use $`|S_1(m)|\ll\sqrt d\log(2d)`$, which follows by expanding $`\chi`$ into its finite Fourier series. Each Fourier coefficient at a nonzero frequency has magnitude at most $`1/\sqrt d`$ by the primitive Gauss sum. The partial geometric sums are bounded by $`O(d/\min(h,d-h))`$ for $`1\le h<d`$, and the zero coefficient vanishes. Thus the weighted sharp tail for each $`j`$ is $`O(L d^{-1/8})`$. Summing either tail with (6) leaves the asserted error. The small-$`x`$ bound also applies on this interval. This gives the polynomial interval used in the ordered sign test below.

## Cancellation on reciprocal scales

Let $`g`$ be the minimum absolute ordinate of the nontrivial quadratic zeros, counting a central zero as zero. The previous nearest-zero bound gives a negative average by $`\exp(C_2(\log(3d)+1/g))`$ if $`g>0`$. Thus positivity through $`d^A`$, for $`A\ge4C_2`$ and $`d`$ large, implies $`g L\le 2C_2/A`$. This implication includes $`g=0`$ and uses no lower bound on the distance between other zeros. [Nearest-zero theorem and proof](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/cae0113ded2504f0f29857045ca2a3028ddaab55/results/signed-prime-tails/NEAREST-ZERO.md)

Let $`u_*`$ be the midpoint of $`\log I`$ and put $`v=\log x-u_*`$. By the two transform identities, $`\int J(x)\exp(-igv)\,dx/x=0`$. On $`I`$ one has $`|gv|\ll_K 1/A`$ and hence $`1-C_K/A^2\le\cos(gv)\le1`$. The real part of the vanishing integral gives

```math
  (1-C_K/A^2)P(J)-N(J)\ll_K e^{-L/\ell}.
```

Here (4) bounds the omitted tails and $`A_0`$ can be chosen so the factor on $`P(J)`$ is positive. Dividing by its uniform lower bound proves the assertion (2). Taking an exponent larger than a suitable multiple of $`1/\sqrt\eta`$ gives the stated converse.

There is also a constraint on where the signed mass lies. For $`g>0`$ the imaginary part gives $`\int J(x)\sin(gv)/(gL)\,dx/x=0`$. On $`I`$ the difference from $`v/L`$ is $`O_K(A^{-2})`$, by $`|\sin t-t|\le |t|^3/6`$. Outside $`I`$ both weights are bounded by $`|v|/L`$, and (4) applies. Consequently

```math
 \left|\int_0^\infty \frac{v}{L} J(x)\frac{dx}{x}\right|
 \ll_K (P(J)+N(J))/A^2+e^{-L/\ell}.
```

At $`g=0`$ this first signed moment vanishes exactly. The completed primitive function is even about $`1/2`$, so a central zero has even order. The gamma factor and the deletion factors preserve that order, and differentiating the corresponding transform at zero gives the moment identity.

## An ordered deficit and recovery

Use $`J=V_q`$. Increase $`A_0`$ until (2) gives $`N(V_q)\ge c_0/2`$ and $`gbL\le\pi/2`$. By (4) a fixed amount of negative mass lies in $`[1,d^b]`$. If $`S_q(n)\ge-c_1\sqrt n/L`$ for every integer there, the negative mass on that interval is at most $`bc_1`$. Choose $`c_1`$ sufficiently small, and let $`m_-`$ be the first integer there below this threshold. Then $`m_-\ge3`$ since $`S_q(1)=1`$ and $`S_q(2)\ge0`$.

Put $`\tau=\log m_-`$. Test the sharp transform with the real function

```math
 W(x)=(\tau-\log x)\mathrm{sinc}(g(\tau-\log x)),\qquad \mathrm{sinc}(0)=1,\quad \mathrm{sinc}(t)=\sin(t)/t\ \ (t\ne0).
```

Its signed integral against $`V_q(x)\,dx/x`$ is exactly zero. For $`g>0`$ this is the imaginary part of (3c) multiplied by $`e^{ig\tau}/g`$. For $`g=0`$ use both the value and the first derivative of the transform at the double or higher central zero.

On $`[1,d^b]`$ the weight has the sign of $`\tau-\log x`$ and lies in absolute value between $`2|\tau-\log x|/\pi`$ and $`|\tau-\log x|`$. On $`[1,3/2]`$ its positive contribution to the integral is $`\ge c_3\tau`$ with absolute $`c_3>0`$, because $`\tau\ge\log3`$ and $`S_q=1`$ there. On the rest of $`[1,m_-)`$ the negative contribution has magnitude at most $`c_1\tau^2/(2L)\le c_1 b\tau/2`$ by the first-choice condition. This uses $`\sqrt{\lfloor x\rfloor}\le\sqrt x`$.

Suppose that no $`m_+`$ in (1) occurs through $`d^b`$. On $`[m_-,d^b]`$ we would have $`V_q(x)\le c_2\tau/L^2`$, including the negative value at the left endpoint. Since $`W\le0`$ there, the negative contribution would have magnitude at most $`c_2\tau b^2/2`$. Outside $`[1,d^b]`$ the absolute contribution is $`O_K(L e^{-L/\ell})`$ by (4) and $`|W|\le|\tau-\log x|`$. Choose $`c_1,c_2`$ with $`c_1b/2+c_2b^2/2<c_3/2`$. For large $`d`$ the full integral is strictly positive, a contradiction. This gives the ordered pair with $`B=b`$. For the stated small primes the same proof on $`[1,d^8]`$ uses $`O(L e^{-L/(16\ell)})=o(1)`$ for the omitted first moment.

In particular an exact central zero alone forces the two arithmetic signs, even without assuming delay of $`F_d`$, since the transform and its first derivative vanish. The same proof works whenever $`gL`$ is sufficiently small in terms of $`K`$. The theorem supplies necessary tests for a late prime average. The field-wide crossing would follow if every sufficiently large Yokoi field admitted a deletion violating at least one test. That arithmetic assertion remains open.
