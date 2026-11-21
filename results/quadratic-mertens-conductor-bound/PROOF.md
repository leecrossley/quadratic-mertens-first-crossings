# A smaller discriminant bound for the first prime-ideal Mertens crossing

Let $d\ge5$ be a positive real quadratic fundamental discriminant. For the field $K$ of discriminant $d$ let $\kappa$ be the residue of $\zeta_K$ at 1 and put

$$
P(x)=\prod_{N\mathfrak p\le x}(1-1/N\mathfrak p)^{-1},\qquad
S_d=\inf\lbrace x\ge2:P(x) < e^{\gamma_E}\kappa\log x\rbrace.
$$

Here $\gamma_E$ is Euler's constant and $\inf\varnothing=+\infty$. The infimum can equal 2 if the error is already negative there. The two sides may be equal at an interior infimum. The point of strict negative error constructed below has $x>e^{1000L}$, after the first ideal norm. All unqualified logarithms are natural.

**Theorem.** Assume the nontrivial zeros of $\zeta(s)L(s,\chi_d)$ have real part $1/2$ (GRH for this field). The following integers give a point of strict negative error before $U(d)$ for every such field. In particular $S_d<U(d)$.

$$
\begin{aligned}
L&=16+\lceil\log_2 d\rceil, & m&=1024+16\lceil\log_2 L\rceil,\\
T&=2^{257}mL^2, & N&=64TL,\\
Q&=128TL, & J&=1000L,\\
U(d)&=2^{4JQ^N}. &&
\end{aligned}
$$

Consequently $\log\log U(d)\ll (\log d)^3(\log\log d)^2$ as $d\to\infty$, with an absolute implied constant. The explicit expression covers small discriminants too. The earlier cutoff had $\log\log U_{\rm old}(d)$ polynomial in $d$. All members of Yokoi's family have the required signature. [Earlier cutoff and definitions](https://github.com/leecrossley/yokoi-mertens-explicit-upper-bound/blob/v1.0.0/PROOF.md)

## 1. The zero sum and its real constant

We use the zero-location theorem for Dirichlet characters announced by Levent Alpöge. The factors of $\zeta_K(s)=\zeta(s)L(s,\chi_d)$ are the Dirichlet functions for the modulus-one character and the primitive quadratic character $\chi_d$. All their zeros in the open critical strip have real part $1/2$. Write $\rho=1/2+i\lambda$ and include multiplicities and any central zero throughout. Andrew Sutherland's verification includes an independent comparison of the formal statement with the theorem proved. The analytic argument below requires just the critical-line property for these factors. [Theorem declarations](https://github.com/Deicyde/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean) · [Independent verification](https://math.mit.edu/~drew/grh/)

With $\psi_K(x)=\sum_{N\mathfrak p^j\le x}\log N\mathfrak p$, $j\ge1$, put $\Phi(u)=e^{-u/2}(\psi_K(e^u)-e^u)$. Write $V=\sum_\rho|\rho|^{-2}$ and

$$
C=V/2-1+\tfrac12\log d-\log\pi-\gamma_E,\qquad
b(u)=e^{-u/2}\lbrace C-u-\log(1-e^{-2u})\rbrace.
$$

On $u>0$ the prime ideal explicit formula in distributions reads

$$
D(u):=\Phi(u)-b(u)=-\sum_\rho e^{i\lambda u}/\rho .
$$

The once-integrated formula of Grenié and Molteni has a locally absolutely convergent zero sum. Differentiating it gives this identity. The paired logarithmic derivative of $\Xi(s)=s(s-1)d^{s/2}\pi^{-s}\Gamma(s/2)^2\zeta_K(s)$ at 2 gives $V\le9+3\log d$. Hence $V\le3L$ and $|C|\le8+2\log d\le2L$. Details of the residues and those estimates are in §§1–2 of the earlier proof. [Integrated explicit formula, (1.3a) and Lemma 3.3](https://arxiv.org/pdf/1312.4465#page=2) · [Derivation of the constants](https://github.com/leecrossley/yokoi-mertens-explicit-upper-bound/blob/v1.0.0/PROOF.md)

We need the **difference** $V-C$. At 1, $\Xi'(1)/\Xi(1)=V/2$. The residue expansion of the Riemann zeta function and the identity $\Gamma'(1/2)/\Gamma(1/2)=-\gamma_E-2\log2$ give

$$
V/2=1+\tfrac12\log d-\log\pi-2\log2+(L'/L)(1,\chi_d),\qquad
V-C=2-2\log2+\gamma_E+(L'/L)(1,\chi_d).
\tag{1}
$$

In particular $V-C\le80+2\log L$. For $d<10^{30}$ the elementary estimate $V-C\le8+\log d$ suffices. For $d\ge10^{30}$ use Theorem 1 of Chirre, Valås Hagen and Simonič. It gives $|(L'/L)(1,\chi_d)|\le2\log\log d-0.4989+5.91(\log\log d)^2/\log d$. The last term is below 2 in this range since $(\log t)^2/t$ decreases for $t>e^2$. [Logarithmic derivative bound](https://arxiv.org/pdf/2206.00819#page=1)

## 2. A signed formula for the product

The real continuous function $W(u)=\sum_\rho e^{i\lambda u}/|\rho|^2$ satisfies $|W|\le V$. Termwise distributional differentiation gives

$$
W'-W/2=D,\qquad Z:=D+W=W'+W/2=\sum_\rho e^{i\lambda u}/(1-\rho).
\tag{2}
$$

Here $1-\rho=\overline\rho$. Since $D=\Phi-b$ is locally integrable, $W$ is locally absolutely continuous on $u>0$. This permits ordinary integration by parts with $W$ even though the unsmoothed series for $Z$ is used in distributions.

Let $A(x)=\sum_{q^j\le x}1/(jq^j)$, with $q=N\mathfrak p$. Define $E_A(u)=e^{u/2}u(A(e^u)-\log u-\gamma_E-\log\kappa)$. Stieltjes summation with $1/(x\log x)$ and the number-field Mertens theorem give, away from prime-power jumps,

$$
E_A(u)=\Phi(u)-\int_0^\infty e^{-t/2}a_u(t)\Phi(u+t)\thinspace dt,\qquad
a_u(t)=\frac{u}{u+t}+\frac{u}{(u+t)^2}.
\tag{3}
$$

This is the earlier argument's partial summation identity after the change of variables $x=e^u$. For $u\ge1$, $a_u(0)=1+1/u$, $0<a_u(t)\le2$ and $|a_u'(t)|\le3/u$. Substitute $D+b$ in (3), use $D=W'-W/2$, and integrate the derivative of $e^{-t/2}W(u+t)$. The terminal boundary term vanishes since $|W|\le V$. We obtain

$$
E_A(u)-Z(u)=\frac{W(u)}{u}+\int_0^\infty e^{-t/2}a'_u(t)W(u+t)\thinspace dt
 +b(u)-\int_0^\infty e^{-t/2}a_u(t)b(u+t)\thinspace dt .
$$

In particular its absolute value is at most $7V/u+3e^{-u/2}(|C|+u+2)$. For the second term use $|b(v)|\le e^{-v/2}(|C|+v+1)$ for $v\ge1$ and integrate $(|C|+u+t+1)e^{-t}$. The correction for ideal powers satisfies $0\le e^{u/2}u(\log P(e^u)-A(e^u))\le48$ for $u\ge1$. This bound follows by splitting the ideals at $e^{u/2}$ and using $\sum_{q\le y}\log q\le8y$ as in §3 of the earlier proof. [Partial summation and prime-power correction](https://github.com/leecrossley/yokoi-mertens-explicit-upper-bound/blob/v1.0.0/PROOF.md)

Set $E(u)=e^{u/2}u\log(P(e^u)/(e^{\gamma_E}\kappa u))$. For $u\ge J$ the two bounds give, almost everywhere,

$$
|E(u)-Z(u)|<50.
\tag{4}
$$

Indeed $7V/u\le21/1000$ and $3e^{-u/2}(|C|+u+2)<1$ since $u\ge1000L$. Equation (4) keeps the sign of the $W$ term. Bounding that term by its absolute size in (2) would cost order $\log d$.

## 3. A negative interval near one

Write $\delta=2^{-256}L^{-2}$. Throughout $\delta\le u\le3\delta$, there are no prime powers at $e^u<2$. Thus $\Phi(u)=-e^{u/2}$ and $Z(u)=\Phi(u)-b(u)+W(u)$. Since $1-e^{-2u}\le2u$, $1-e^{-u/2}\le u/2$, $|C|u/2\le1$ and $u\log(1/u)/2\le1$, we have

$$
Z(u)\le V-C+3+\log(2u)
 \le80+2\log L+3+\log(6\delta)<-80 .
\tag{5}
$$

For the last inequality use $\log2\ge2/3$ and $\log6<2$. The terms $2\log L$ cancel. This is why the interval width can now be an inverse square of $\log d$.

## 4. Bringing the negative average back

Take the $m$-fold convolution $k$ of the uniform probability density on $[-\delta/m,\delta/m]$. This nonnegative density is supported in $[-\delta,\delta]$. Its Fourier transform $w(\lambda)=\mathrm{sinc}(\delta\lambda/m)^m$ satisfies $|w|\le\min(1,(m/(\delta|\lambda|))^m)$, with $w(0)=1$. Write $Z_k(v)=\int k(u-v)Z(u)\thinspace du$ for $v>\delta$. Its zero series is absolutely and uniformly convergent after multiplication by $w$. One may test (2) first against a smooth approximation to $k$, then pass to the limit by absolute convergence and local integrability. By (5), $Z_k(2\delta)<-80$.

For $|\lambda|>T=2m/\delta$, $|\rho|^2\le2\lambda^2$ and hence

$$
\sum_{|\lambda|>T}\frac{|w(\lambda)|}{|1-\rho|}
 \le 2VT\thinspace2^{-m}<1 .
\tag{6}
$$

For an integer check on the last inequality put $k_0=\lceil\log_2 L\rceil$. Since $L\le2^{k_0}$ and $m\le2^{11+k_0}$, $2VT\le6\cdot2^{257}mL^3\le 2^{271+4k_0}<2^m$.

We count the remaining frequencies with one evaluation of the completed zeta function. At $s=1/2+T$ each $|\lambda|\le T$ contributes at least $1/(2T)$ to $\Xi'(s)/\Xi(s)$. Its logarithmic derivative and the Euler product imply

$$
\mathrm{card}\lbrace|\lambda|\le T\rbrace\le2T\thinspace\Xi'(s)/\Xi(s)
 \le 2T\bigl(2+\tfrac12\log d+\log(T+1)\bigr)\le N .
\tag{7}
$$

The gamma term satisfies $\Gamma'(a)/\Gamma(a)\le\log a$ for $a>0$ by Jensen's inequality for the logarithm under the gamma density of mean $a$. For the elementary last bound, $m\le80L$ for $L\ge19$, $\log(T+1)\le258\log2+\log(80)+3\log L\le 16L$, and $\log d\le L$. The sum of absolute coefficients at these low frequencies is at most $2TV$, by $|\rho|\le2T$.

Partition the unit cube of dimension the number of low frequencies into boxes of side $1/Q$. Two of the first $Q^n+1$ multiples of the vector with coordinates $J\lambda/(2\pi)$ fall in one box when $n$ coordinates are present. Their difference $q$ satisfies $1\le q\le Q^N$ and $|e^{iJq\lambda}-1|\le2\pi/Q$ for every low frequency. Repeated or central zeros pose no issue. The simultaneous approximation statement was checked in Lean in the earlier release. [Formal recurrence lemma](https://github.com/leecrossley/yokoi-mertens-explicit-upper-bound/blob/v1.0.0/FirstCrossing.lean)

On translating the average by $Jq$, the low terms change by at most $4\pi TV/Q\le12\pi/128<1$. Each high tail costs less than 1 by (6). Consequently $Z_k(2\delta+Jq)<-77$. Throughout this last averaging interval (4) applies. The average of $E$ is strictly negative, so it is negative on a positive-measure subset, including points away from jumps. At any such $u$, $P(e^u)<e^{\gamma_E}\kappa u$ and $u\le JQ^N+3\delta$. Hence $e^u<U(d)$.

Finally $m=O(\log L)$, $T=O(L^2\log L)$, $N=O(L^3\log L)$ and $\log Q=O(\log L)$. It follows directly that $\log\log U(d)=\log(4J\log2)+N\log Q=O(L^3(\log L)^2)$. This completes the bound.

The displayed cutoff also improves the earlier one at each $d\ge5$. For a direct integer comparison, $L\le5d$, $m\le80L$, $N\le2^{270}L^4\le2^{280}d^4$ and $Q\le2^{281}d^4$. Thus $\lceil\log_2 Q\rceil\le281+4d\le61d$ and $\lceil\log_2(4J)\rceil\le15+d\le4d$. The integer $H=\lceil\log_2(4J)\rceil+N\lceil\log_2Q\rceil$ satisfies $U(d)\le2^{2^H}$ with $H<2^{287}d^5<d^{30000}$. For the earlier exact cutoff put $H_0=512+128\lceil\log_2 d\rceil$. Its double binary logarithm is $3+H_0(32H_0+9)2^{64H_0+9}>2^{64H_0}\ge2^{32768}d^{8192}>2^{287}d^5$. This compares the two cutoffs for every $d\ge5$. The new upper estimate, earlier exact integer and earlier simplified exponent have respectively 89, 17,273 and 20,970 decimal digits at $d=5$, and 90, 44,400 and 119,212 at $d=9413$. [Earlier exact formula](https://github.com/leecrossley/yokoi-mertens-explicit-upper-bound/blob/v1.0.0/PROOF.md)
