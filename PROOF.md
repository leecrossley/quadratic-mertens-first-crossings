# Delayed detection by all power averages in a fixed range

Let $d=m^2+4$ be squarefree, $m$ positive and odd. For $K_d=\mathbb Q(\sqrt d)$ write
$$
 B_d(t)=\sum_{N\mathfrak p\le t}-\log(1-1/N\mathfrak p)-\gamma-\log L(1,\chi_d)-\log\log t,\qquad
 S_d=\inf\{t\ge2:B_d(t)<0\}.
$$
For $s>0$ let $F_{d,s}(y)=\int_y^\infty s(y/t)^s B_d(t)\,dt/t$. The positive factor $s$ normalises the total mass to one.

**Theorem.** Fix $0<s_0\le s_1<\infty$. There are $c,c',C>0$ depending only on this interval such that for all sufficiently large $D$ put
$$
 X=2^{\lfloor c\sqrt{\log D/\log\log D}\rfloor}.
$$
For any dyadic $T$ tending to infinity with $D$ and $T\le\exp(c'(\log D)^{1/5})$, at least
$$
 \sqrt D\exp[-C\{(\log T)^4+\log X\log\log X\}]
 \tag{1}
$$
squarefree Yokoi discriminants in $D/2<d\le D$ have all the following properties:
- $B_d(t)>0$ on $[2,T]$ and $T<S_d<8X$.
- $F_{d,s}(y)>0$ for **every real** $2\le y\le X$ and every $s_0\le s\le s_1$.
- At the single start $4X$ all these power averages are negative. For every such $s$ the integral on $[4X,8X]$ alone is also negative.

One may take $T$ of order $\exp(c''(\log D)^{1/5})$. A second choice, dyadically rounding $\exp((\log D\log\log D)^{1/8})$, gives a count of at least $\sqrt D\exp[-C'\sqrt{\log D\log\log D}]$ and still forces the first crossing beyond every fixed power of $\log d$. All scales and signs are chosen before selecting a field. The delay through $X$ concerns the prescribed range of power exponents. A different decreasing weight or a very large exponent can detect an earlier negative interval.

## 1. Averaging the product before estimating it

Put $H(y)=\sqrt{\log\log y/(y\log y)}$ for large $y$. Choose an integer $L\ge128$ with $(L-1)s_0\ge4$ and set $V=X^L$. For the full average define $k_p(y,s)=0$ for $p\le y$ and $1-(y/p)^s$ otherwise. For the truncated average on $[y,2y]$ replace $p/y$ in that expression by $\min(p/y,2)$. These are the integrals of the averaging measure up to $p$, and both functions of $p$ increase from zero and are bounded by one.

Outside at most $D^{1/4}$ primitive characters the residue logarithm is the short Euler product logarithm through $V$ up to $O((\log D)V^{-1/32})$, by Granville and Soundararajan, Proposition 2.2 with $A=8$. The rational factorisation of the prime-ideal product contains the ordinary prime product, the twisted Euler product through $t$, and an inert correction $\prod_{\sqrt t<p\le t,\ \chi_d(p)=-1}(1-p^{-2})$. The absolute log of that correction is $O(1/(\sqrt t\log t))$ by the prime number theorem. Integrating the twisted portion and subtracting the short Euler product times the mass of the averaging measure yields, for both kinds of integral $A_d(y,s)$,
$$
 A_d(y,s)=-\sum_{y<p\le V}k_p(y,s)\chi_d(p)/p
             +O_{s_0,s_1}(1/(\sqrt y\log y))+o(H(4X)),\qquad B\le y\le4X.
 \tag{2}
$$
Here $B$ is any sufficiently large fixed constant. Replacing each logarithmic local factor by $\chi_d(p)/p$ costs $O(1/y)$. Terms beyond $V$ for the infinite average are bounded by $O_{s_0}((y/V)^s)$ using $\sum_{n>V} n^{-1-s}$, and vanish for the finite window. These and the short-product error are $o(H(4X))$. The estimate is uniform in $s$ in the stated interval. [Granville and Soundararajan, Proposition 2.2](https://arxiv.org/pdf/math/0206031#page=7) · [Exact quadratic factorisation](https://github.com/leecrossley/yokoi-mertens-crossing-bounds/blob/v1.0.0/PROOF.md)

For the ordinary rational error in (2), Cramér's estimate $\int_z^{2z}|\psi(t)-t|dt\ll z^{3/2}$ and partial summation give $\int_z^{2z}|B_{\mathbb Q}(t)|\,dt/t\ll1/(\sqrt z\log z)$. Indeed the boundary term is $(\psi(t)-t)/(t\log t)$, the integral remainder is bounded by dyadically summing $|\psi(v)-v|(1+\log v)/(v^2\log^2v)$, and omitted prime powers cost $O(1/(\sqrt t\log t))$. Summing these bounds over doubled intervals gives the uniform averaged error in (2). We also use the pointwise rational bound $B_{\mathbb Q}(t)=O(\log t/\sqrt t)$ from Schoenfeld, by the same partial summation. It gives the pointwise version for nonexceptional fields,
$$
 B_d(t)=-\sum_{t<p\le V}\chi_d(p)/p+O(\log t/\sqrt t),\qquad B\le t\le T .
 \tag{3}
$$
These rational estimates use the critical-line theorem for the ordinary zeta function. [Cramér estimate, (4.3)](https://www.numdam.org/item/10.5802/jtnb.687.pdf#page=7) · [Schoenfeld](https://doi.org/10.1090/S0025-5718-1976-0457374-X) · [Formal input and independent checks](https://math.mit.edu/~drew/grh/)

## 2. Biasing the splitting probabilities at two different scales

Use the independent random signs $Z_p$ of Dahl and Kala for this family, with mean $\mu_p=-p/(p^2-b_p)$ and variance $v_p=1+O(1/p)$ at odd $p$, where $b_p=1+(-1/p)$. Each inert sign has positive mass, and $Z_2=-1$. Write $z_p=Z_p-\mu_p$ in the model or $\chi_d(p)-\mu_p$ on the field side. Let $I$ require every prime through a large fixed dyadic $B$ to be inert. It has positive model probability $p_B$ and is a fixed polynomial in the signs since its odd-prime factors are $(Z_p^2-Z_p)/2$. Subtracting Dahl and Kala's counting and character formulas at $D/2$ from those at $D$ gives
$$
 \mathbb E_D\chi_d(n)=\mathbb E Z(n)+O(n^{2/3}D^{-1/6}\log D)
 \tag{4}
$$
on the uniform shell of cardinality $\asymp\sqrt D$. The variables are extended completely multiplicatively. [Dahl and Kala, Proposition 14](https://arxiv.org/pdf/1611.02424#page=11)

Write $h_p=\sqrt{\log p\,\log\log p/p}$ and $\ell_p=(\log p)^2/\sqrt p$. Fix amplitudes $A_+,A_-,A_0>0$, to be chosen in §4. Prescribe mean shifts
$$
 \Delta_p=
 -A_- h_p\,{\bf1}_{B<p\le4X}
 -A_0\ell_p\,{\bf1}_{B<p\le4T}
 +A_+h_p\,{\bf1}_{8X<p\le16X}.
$$
For large $D$, $T=o(X)$. In the independent model weight by $IR^2$ with $R=\prod_{B<p\le16X}(1+a_p z_p)$. Under its normalisation the means above $B$ can be made exactly $\nu_p=\mu_p+\Delta_p$, with $|a_p|\le2|\Delta_p|$ and $|a_p|\le1/16$. Indeed the shift for coefficient $a$ is $(2av_p+a^2\mathbb E z_p^3)/(1+a^2v_p)$. For $|a|\le1/16$ its signed ratio to $a$ is at least $1/2$, since $|\mathbb E z_p^3|\le2v_p$ and $1/2\le v_p\le1$ eventually. Increase $B$ so that all shifts have size at most $1/32$ and apply continuity. Independence above $B$ survives the full tilt. [Signed tilt and its algebraic checks](https://github.com/leecrossley/yokoi-mertens-prescribed-crossings/blob/v1.0.0/PROOF.md)

Partial summation over primes gives two separate estimates, with implied constants depending on the amplitudes:
$$
 \sum a_p^2\ll (\log T)^4+\log X\log\log X,\qquad
 \sum a_p^2\log p\ll(\log T)^5+(\log X)^2\log\log X. \tag{5}
$$
For example the long weak tilt contributes $\sum_{p\le16X}(\log p)\log\log p/p\ll\log X\log\log X$. The shorter strong tilt contributes $\sum_{p\le4T}(\log p)^4/p\ll(\log T)^4$. Multiplication by $\log p$ gives the respective bounds in the second estimate.

Truncate the expansion of $R$ into squarefree centered monomials at index $N=\lfloor D^{1/1000}\rfloor$, yielding $R_N$. Orthogonality identifies the fraction $\varepsilon$ of discarded squared norm with the probability that a random product exceeds $N$, where $p$ is selected independently with probability $a_p^2 v_p/(1+a_p^2v_p)$. For $\theta=1/\log(16X)$, $p^\theta-1\le(e-1)\theta\log p$. Markov's inequality therefore gives
$$
 \varepsilon\le \exp\left[\frac{-\log N+(e-1)\sum a_p^2\log p}{\log(16X)}\right].
 \tag{6}
$$
Keeping this $\log p$ inside the sum is important for the shorter strong tilt. Let $H_*=\lceil4\log\log V\rceil+2$. By making $c,c'$ sufficiently small after the amplitudes, (5)–(6) yield $\sqrt{\varepsilon}\le V^{-100H_*}$. Indeed the two positive terms in the numerator cost $O((c')^5\log D+c^2\log D)$, and $H_*\log V\log(16X)=O_L(c^2\log D)$. The indicator is independent of $R,R_N$. The two normalised model weights $IR^2,IR_N^2$ thus differ on expectations of bounded observables by $O(\sqrt{\varepsilon})$ times their sup norm, by Cauchy–Schwarz. Also $\mathbb E IR_N^2\ge p_B/2$.

## 3. Controlling all starts and all exponents together

On actual fields use the normalised weight $W=IR_N^2$. For every interval of primes $\mathcal H\subset(B,V]$ and integer $2\le h\le H_*$, the $2h$-th moment of
$$
 C_{\mathcal H}=\sum_{p\in\mathcal H}(\chi_d(p)-\nu_p)/p
$$
under the shell weight differs from the full tilted model's moment by at most $V^{-4H_*}$ eventually. Here are the sizes in (4). The sum of absolute character coefficients of $R_N$ is at most $N^2$ and its largest index at most $N$, since each retained centered monomial with its coefficient costs at most $2^{\omega(n)}\le n$. The indicator has fixed norm and index bounds depending on $B$. For $C_{\mathcal H}^{2h}$ the bounds are $(2V)^{2h}$ and $V^{2h}$. Transferring the numerator gives error at most $O_B(D^{-1/6}N^{16/3} V^{O(H_*)}\log D)=O_B(D^{-1/8})$ because $H_*\log V=o(\log D)$. The denominator without the observable is at least $p_B/3$ after transfer. Normalisation costs at most $O_B((2V)^{2H_*}D^{-1/8})$. The difference between full and truncated model weights contributes at most $O((2V)^{2H_*}\sqrt\varepsilon)$. These errors imply the stated moment comparison.

For dyadic $z\ge B$, $2z\le V$, the block $(z,2z]$ has $m_z\ll z/\log z$ primes. On any interval of $l\ge1$ consecutive **primes** in the block, the centered tilted summands are independent, with interval lengths at most $2/z$. The bounded-variable exponential moment inequality gives model $L^{2h}$ norm at most $C\sqrt{hl}/z$ by integrating the subgaussian tail. The additive moment comparison preserves this bound with an absolute constant even for $l=1$, since $z\le V$ and $h\le H_*$. Pad the ordered list of primes to the next power of two with zeros. A prefix is a union of at most one interval from each level of dyadic subdivision of this list. At level $j$ the maximum of the $2^j$ interval sums in absolute value has $L^{2h}$ norm at most $C\sqrt{hm_z}2^{-j/2+j/(2h)}/z$ by summing the individual $2h$-th moments. Minkowski across levels now gives the same bound $C'\sqrt{h/(z\log z)}$ for the maximum absolute prefix sum, uniformly for $h\ge2$. Empty blocks have maximum zero. [Hoeffding's bounded-variable estimate](https://doi.org/10.1080/01621459.1963.10500830)

Choose $h=\lceil4\log\log z\rceil+2$. Markov's inequality at $e$ times that norm makes each bad-block probability at most $e^{-2h}\le(\log z)^{-8}$. The sum over all such dyadic $z$ is less than $1/4$ for sufficiently large fixed $B$. On the complementary event each maximum is $O(H(z))$ with an absolute constant. For any $B\le y\le4X$, incomplete endpoint intervals cost at most twice their block maximum. Abel summation gives the same bound, up to an absolute factor, on weighting the terms by **any** increasing coefficients in $[0,1]$ in each block. Summing over successive blocks uses $\sum_{j\ge0}H(2^jz)\ll H(z)$, since the exponential decay dominates the logarithms. Thus simultaneously
$$
 \left|\sum_{y<p\le V}k(p)(\chi_d(p)-\nu_p)/p\right|\le C_5 H(y) \tag{7}
$$
for every real $y$ in this range and every nondecreasing $k(p)\in[0,1]$, including $k=1$. This single event handles the continuum of power exponents. No union over those exponents is taken.

For the unweighted count, expanding $R_N^4$ in the independent model kills any quadruple with a singleton prime. After taking absolute values drop all four truncation restrictions. This bounds the moment by
$\prod_p(1+6a_p^2v_p+4|a_p|^3\mathbb E|z_p|^3+a_p^4\mathbb E|z_p|^4)\le\exp(C\sum a_p^2)$. Transfer $W^2=IR_N^4$ by (4), with coefficient norm $O_B(N^8)$ and indices $O_B(N^4)$, at cost $O_B(D^{-1/6}N^{32/3}\log D)=o(1)$. Cauchy–Schwarz shows that the unweighted probability of (7) together with $I=1$ is at least $(3\mathbb E_D W/4)^2/\mathbb E_D W^2$. Using (5), subtracting the at most $D^{1/4}$ short-product exceptions, and absorbing fixed factors proves the count (1). [Signed fourth-moment count](https://github.com/leecrossley/yokoi-mertens-prescribed-crossings/blob/v1.0.0/PROOF.md)

## 4. Signs and the actual first crossing

The mean correction in (2)–(3) costs $O(1/y)$ since $|\mu_p|\ll1/p$. At $y=4X$ only the positive prescribed band contributes to the main prime tail. On $8X<p\le16X$ both kernels at this start are at least $1-2^{-s_0}>0$. The prime number theorem gives $\sum_{8X<p\le16X}h_p/p\asymp H(4X)$ with absolute constants. Fix $A_+$ large enough to dominate (7) and the errors in (2). Both tested integrals at $4X$ are then strictly negative for every $s\in[s_0,s_1]$, so there is an actual negative point before $8X$.

For any $B\le y\le X$, $(2y,4y]$ is inside the negative weak tilt and both kernels are at least $1-2^{-s_0}$ throughout that block. Its contribution to minus the mean tail is $\gg_{s_0} A_- H(y)$ by the prime number theorem. The entire positive band costs $O(A_+H(X))\ll A_+H(y)$ because $H$ decreases eventually. Choose $A_-$ large enough after $A_+$ to leave a strict positive margin in (2) and (7). The strong tilt can only add to this margin. This proves in particular $F_{d,s}(y)>0$ on $[B,X]$.

On $B\le t\le T$, $(t,2t]$ lies in the strong negative tilt. Its contribution to (3) is $\gg A_0\log t/\sqrt t$ by the prime number theorem. The positive band costs $O(A_+H(X))$, uniformly negligible relative to $\log t/\sqrt t$ here, and (7) costs $O(H(t))$. Choose $A_0$ large enough that $B_d(t)>5\log t/\sqrt t$ on $[B,T]$. At $B$, the all-inert condition gives $P_d(B)\le\zeta(2)$. At arbitrary $t\ge2$, $P_d(t)\ge\prod_{p\le\sqrt t}(1-p^{-2})^{-1}\ge\zeta(2)(1-1/\sqrt t)$ by comparison with the telescoping product over all integers. Since $(1-t^{-1/2})/\log t=\int_0^{1/2}t^{-v}\,dv$ is decreasing and $\exp(-5\log B/\sqrt B)<1-B^{-1/2}$ for large $B$, the raw error is positive throughout $[2,B]$. Its strict margin at $T$ persists to the right by monotonicity of the product, hence $S_d>T$.

Finally for $y<B$, split $F_{d,s}(y)$ at $B$. Its first part is nonnegative and its second is $(y/B)^s F_{d,s}(B)>0$. The choices are made in the order $s_0,s_1,L$, then the amplitudes, then $B,c,c'$, and finally $D$. All signs and bounds now hold on the same set of fields.

## 5. What information about the first split prime can decide

The late fields just constructed already contain many split and inert primes below $T$. In fact, uniformly for every family field as $d\to\infty$ and every $x\ge(\log d)^4$, the sums of $\log p$ over split primes in $(x,2x]$ and over inert primes in the same interval are each $x/2+o(x)$. To see this, the quadratic prime ideal theorem on the critical line gives $\psi_K(2x)-\psi_K(x)=x+O(\sqrt x\log x(\log d+\log x))$. After discarding contributions from powers of rational primes with exponent at least two, of total size $O(\sqrt x\log^2x)$, and ramified primes, of total size at most $\log d$, this is twice the split-prime sum. The errors divided by $x$ tend uniformly to zero in this range. Subtracting from the ordinary prime sum then gives the inert-prime assertion. [Grenié and Molteni, Corollary 1.2](https://arxiv.org/pdf/1312.4463#page=3) · [Dirichlet critical-line statements](https://math.mit.edu/~drew/grh/)

For the two choices of $T$ above there are many such doubled intervals before the first crossing. Even correct leading proportions on every one of them coexist with all the positive averages proved here. A bound on a least residue or nonresidue records the presence of one prime; deciding the Mertens sign requires finer information on the signed tail. The Fourier optimisation theorems for least primes pose different inequalities. [Carneiro, Milinovich, Quesada-Herrera and Ramos, Theorems 1–3](https://arxiv.org/pdf/2404.08380#page=2)
