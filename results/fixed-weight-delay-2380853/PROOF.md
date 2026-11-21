# A fixed-weight crossing between two powers of 2,380,853

Let $d=1543^2+4=2{,}380{,}853$, a prime, and $K=\mathbb Q(\sqrt d)$. Write $q=N\mathfrak p$, counted with prime-ideal multiplicity, $\ell(q)=-\log(1-1/q)$, and $c=e^{\gamma_E}L(1,\chi_d)$. For every real $y\ge2$ put

$$
 B(t)=\sum_{q\le t}\ell(q)-\log c-\log\log t,\qquad
 F(y)=\int_y^\infty B(t)\frac{y\thinspace dt}{t^2},\qquad
 T(y)=\sum_{p>y}(1-y/p)\frac{\chi_d(p)}p .
$$

The signed prime series is taken in increasing order. Let $Y=\inf\lbrace y\ge2:F(y)<0\rbrace$.

**Theorem.** Assume the critical-line property for the Riemann zeta function and $L(s,\chi_d)$ for this $d$ (field GRH). Then $F(y)>0$ at every real $2\le y\le d^{9/4}$. At $y=d^{7/3}$, writing $N_y=\sqrt y\log y$, one has $N_yF(y)<-0.22$ and $N_yT(y)>0.26$. In particular

$$
 222{,}663{,}129{,}634{,}336 < d^{9/4} < Y < d^{7/3}<756{,}907{,}294{,}748{,}218.
$$

Strict positivity on the first interval and strict negativity at the witness give the strict interior inequalities by continuity. The proof uses field GRH for the zero expansion (2), the bound for the total zero mass, the bounds $\delta$ below and the bound for $\theta_\chi$. Alpöge's announced Dirichlet GRH theorem supplies this input. Every numerical inequality below is an outward-rounded enclosure or an integer comparison. [Announcement](https://alpo.ge/remark.pdf) [Independent formal checks](https://math.mit.edu/~drew/grh/) · [Numerical certificate](evidence/verification.txt) · [Second witness calculation](evidence/witness.txt)

## Small starts and the full infinite average

Termwise integration of the nonnegative Euler factors and integration by parts for the logarithm give

$$
 F(y)=\sum_{q\le y}\ell(q)(1-y/q)+yD-\log c-\log\log y-yE_1(\log y),
 \quad D=\sum_q\ell(q)/q ,
$$

where $E_1(x)=\int_x^\infty e^{-t}dt/t$. At a norm, $F'$ has a downward jump of $\ell(q)/q$ per ideal. Between norms $F''(y)=1/(y^2\log y)$. On $[a,b]$ subtract $y^2/(2a^2\log a)$ to get a concave function, including across the jumps. Thus the full curve is above its endpoint chord minus $(b-a)^2/(8a^2\log a)$. This controls every real start.

For $D$, begin with $\log\zeta_K(2)$ and add $\ell(q)/q+\log(1-q^{-2})$ through $q=1{,}203{,}000$. Each correction is nonnegative by comparing powers and is at most $q^{-3}$. At most two prime ideals have any integer norm, so the remaining correction is at most the inverse square of the cutoff. Quadratic reciprocity here gives $\chi_d(p)=(p/d)$, including $p=2$ by the supplementary law. A split prime gives two norms $p$, an inert prime one norm $p^2$, a ramified prime one norm $p$. The calculation encloses $L(1,\chi_d)$ and $L(2,\chi_d)$ as described below. It tests 2,058 chords from 2 to 1,203,000, beyond $e^{14}$. [Direct verifier](early.py)

## A zero expansion with a certified unused tail

Define $A_K(t)=\sum_{q^j\le t}1/(jq^j)$ and $A_\chi(t)=\sum_{p^j\le t}\chi_d(p)^j/(jp^j)$. Write $J_K$ for the $y\thinspace dt/t^2$ average of $A_K(t)-\log c-\log\log t$, and $J_\chi$ for the corresponding average of $A_\chi(t)-\log L(1,\chi_d)$. Then

$$
 F=J_K+\left\langle\sum_{q\le t,\ q^j>t}\frac1{jq^j}\right\rangle,\qquad
 -T=J_\chi+\left\langle\sum_{j\ge2,\ p^j>t}\frac{\chi_d(p)^j}{jp^j}\right\rangle .
 \tag{1}
$$

Angle brackets denote the same average. Integrating the tail indicator $t<p$ yields $1-y/p$. The prime number theorem for $\chi_d$ justifies this partial summation in increasing prime order. The higher powers converge absolutely.

For $u=\log y$ and each $\rho=1/2+i\lambda$ of the appropriate function, write $a=1/2-i\lambda$. The contribution to $N_yJ$ is

$$
 e^{i\lambda u}h(a,u),\qquad
 h(a,u)=\int_0^\infty\frac{e^{-s}\thinspace ds}{(a+s/u)(1+a+s/u)} .
 \tag{2}
$$

Indeed the differential of the prime-power error is $e^{-v}dR(e^v)/v$ in $v=\log t$, where $R(x)=\psi_K(x)-x$. Integrating from $v$ to infinity and then averaging from $u$ applies the test $(1-e^{u-v})e^{-v}/v$ to $-dR(e^v)$. The ordinary explicit formula contributes $e^{\rho v}dv$ per zero and $\coth(v)\thinspace dv$ from the real-quadratic trivial zeros and the origin. For the rational factor the remaining density is $1/(e^{2v}-1)$, so for the even quadratic factor it is $1/(1-e^{-2v})$. The factorisation $\zeta_K=\zeta L$ also gives the quadratic case by subtraction. Inserting $1/v=\int_0^\infty e^{-vr}dr$ gives (2). The remaining normalised term is in $[0,e^{-u/2}\coth(u)/2]$ in both cases. For example, bound $1/v$ by $1/u$ before integrating $(1-e^{u-v})e^{-v}$. The half-line test is continuous with derivative of bounded variation after absorption of the critical-line exponential. Smooth truncations and smoothing the corner bound its Fourier transforms by $O_u((1+|\lambda|)^{-2})$ uniformly. This permits passage from smooth tests by summability over zeros, and integration by parts against the prime ideal theorem handles the upper arithmetic cutoff. [Integrated explicit formula](https://arxiv.org/pdf/1312.4465#page=2) · [Prime ideal bound](https://arxiv.org/pdf/1312.4463#page=3)

Each omitted zero costs at most $1/(1/4+\lambda^2)$ in normalised units. The total mass for the quadratic function is $2\Lambda_\chi'(1)/\Lambda_\chi(1)$, where $\Lambda_\chi(s)=(d/\pi)^{s/2}\Gamma(s/2)L(s,\chi_d)$. This is its paired Hadamard logarithmic derivative at 1, using the functional equation about $1/2$. The ordinary mass adds $2+\gamma_E-\log(4\pi)$. We certify one conjugate pair for each of 152 disjoint positive brackets by opposite endpoint signs and add 20 ordinates of $\zeta$ with their negatives. Subtracting their verified weights from the total leaves less than 0.109479. Extra zeros, central zeros, higher multiplicities and all heights above the computation are included in that allowance. [Brackets in units of one hundred-millionth](brackets.txt) · [Verification code](verify.py)

The main verifier evaluates (2) by partial fractions followed by geometric expansion. Through $j=k-1$ use the terms $(-1)^jj!u^{-j}(a^{-j-1}-(1+a)^{-j-1})$. The remainder is at most $k!u^{-k}(|a|^{-k-1}+|1+a|^{-k-1})$ since $|a+s/u|\ge|a|$. We use $k=6$ and evaluate interval phases over each entire log interval of width $1/160$.

The same data give a check on how close the low zeros are. The quadratic residual inverse-square mass is less than $1/(1/4+2.9^2)$, excluding any unaccounted zero with $|\lambda|\le2.9$. Thus the lowest ordinate $\tau$ is in $(0.02849001,0.02849002)$. For $c_\lambda=((1/2-i\lambda)(3/2-i\lambda))^{-1}$ the verifier obtains

$$
 \sum_\lambda\frac{|c_\lambda|}{\lambda^2}+
 \sum_{\lambda\ne\tau}\frac{|c_\lambda|}{(\lambda-\tau)^2}
 < 14.859\thinspace\log^2(3d)
$$

for the quadratic zeros. For the unseen ordinates the two denominators are at least $2.9^2$ and $(2.9-\tau)^2$, respectively.

As a direct check, write $Z(t)=\Lambda_\chi(1/2+it)$. The program encloses $Z(0)$ and verifies $Z'(\tau)\ne0$. Taking two logarithmic derivatives of the paired Hadamard product gives the sum of the two **unweighted** inverse squared distances as $-Z''(0)/Z(0)-Z'''(\tau)/(3Z'(\tau))+(Z''(\tau)/(2Z'(\tau)))^2$. The computed quotient by $\log^2(3d)$ is between 11.21236 and 11.21238.

## Prime squares and the signed witness

For the lower bound on $F$, the omitted prime powers in (1) are nonnegative. Where the zero sum alone does not prove positivity, take $A\le u\le B$. Each split prime $e^{B/2}<p\le\min(e^A,64e^{A/2})$ supplies two omitted squares on $p\le t<p^2$. Their contribution to $N_yF$ is at least

$$
 A e^{A/2}\left(p^{-2}-e^B p^{-4}\right).
$$

The verifier uses an integer sieve and sums lower fixed-point approximations to $p^{-2}$ and upper ones to $p^{-4}$ with denominator $2^{144}$. This resolves all 311 intervals requiring the squares. The largest prime cutoff is 22,189,573. The 3,046 log intervals cover $14\le u\le5286/160$, strictly past $(9/4)\log d$.

For the upper bound at $u=(7/3)\log d$, the squared-prime term in (1) is bounded above in the field case by $\frac12\int_{\sqrt t}^\infty d\psi_K(v)/(v^2\log v)$, where the lower endpoint is excluded. Here only exponent two is needed, and the integral includes higher powers with positive weights. For the character case use $\psi_{\mathbb Q}$ since $\chi_d(p)^2\le1$. All indices $j\ge3$ cost at most $13t^{-2/3}/\log t$ for these $t$. To see this, put $r=t^{1/3}$. Each norm $q\le r$ contributes at most $2/(3t)$, and for $q>r$ at most $2/(3q^3)$. The norm counting function is at most $2\pi(x)\le 2.511x/\log x$. Integrating $2\int_r^\infty 2.511\thinspace dv/(v^3\log r)$ for the second sum gives the stated constant. The same bound covers unrestricted rational primes in the character case. [Rosser and Schoenfeld, Corollary 1](https://doi.org/10.1215/ijm/1255631807)

Let $w=u/2$, and choose $(n,\Delta)=(2,d)$ or $(1,1)$, respectively. For $z\ge e^w$ Corollary 1.2 of Grenié and Molteni bounds $|\psi(z)-z|/z$ by

$$
 \delta=e^{-w/2}\left[(w/(2\pi)+2)\log\Delta+n(w^2/(8\pi)+2)\right],
$$

since $w>4$ and the individual terms decrease. Integration by parts against $g(v)=1/(v^2\log v)$ gives $\int_z^\infty g\thinspace d\psi\le(1+3\delta)/(z\log z)$ including the endpoint error. Set $t=ye^r$ and integrate $r$ with weight $e^{-r}$. The normalised upper cost of all prime powers in (1) is at most $2(1+3\delta)/3+(39/5)e^{-u/6}$. Applying the formula once for $K$ and once for $\chi_d$ proves the two signs with the margins stated above. [Explicit prime ideal theorem](https://arxiv.org/pdf/1312.4463#page=3)

**A finite signed-prime certificate.** At the same $y=d^{7/3}$ the normalised sum over $y<p\le10^{26}$ exceeds $0.23$. To check directly that this forces a negative average, write $\delta_K,\delta_{\mathbb Q}$ for the corresponding two values of $\delta$. In $F+T$ all quadratic zero terms cancel. The field's even-power correction in (1) is $\tfrac12\int_{\sqrt t}^\infty g\thinspace d\psi_K$ up to the omitted $q>t$ portion, of size at most $2/t$. The character's even correction is $\tfrac12\int_{\sqrt t}^\infty g\thinspace d\psi_{\mathbb Q}$ up to the single ramified prime's powers, of size at most $1/t$. Subtracting cancels the continuous square contribution. The remaining odd powers cost at most twice the $13t^{-2/3}/\log t$ bound above. Thus

$$
 |N_y(F+T)|\le 2+\gamma_E-\log(4\pi)
 +e^{-u/2}\coth(u)/2+2(\delta_K+\delta_{\mathbb Q})
 +(78/5)e^{-u/6}+(3u/2)e^{-u/2}<0.15 .
$$

The character Chebyshev function restricted to primes satisfies $|\theta_\chi(x)|\le\sqrt x\log x(\log(3d)+\log x)$ for $x\ge100$, by subtracting the quadratic and ordinary prime ideal estimates and removing powers at a cost $\le\sqrt x\log x$. Partial summation with $(1-y/x)/(x\log x)$ gives a normalised truncation error at most $4N_y(\log(3d)+\log V+2)/\sqrt V<0.03$ at $V=10^{26}$. Here $|\phi'(x)|\le5/(4x^2\log x)$ for that weight on $x\ge V$. The verified full tail $>0.26$ gives the finite lower bound. Conversely that finite bound alone implies $N_yF<0.15+0.03-0.23<0$. This certifies the finite sum analytically without enumerating primes through $10^{26}$.
