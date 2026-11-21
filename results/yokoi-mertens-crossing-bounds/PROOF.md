# Bounds for the first crossing of the prime-ideal Mertens product in Yokoi’s family

Let $\mathcal D(D)=\lbrace m^2+4\le D:m\ge1\text{ odd},\ m^2+4\text{ squarefree}\rbrace$. Each member is a positive fundamental discriminant. For $K_d=\mathbb Q(\sqrt d)$, write $L_d=L(1,\chi_d)=\mathrm{res}_ {s=1}\zeta_{K_d}(s)$, where $\chi_d$ is the primitive quadratic character of conductor $d$. For real $x\ge2$ set

$$
P_d(x)=\prod_{N\mathfrak p\le x}(1-1/N\mathfrak p)^{-1},\qquad
S_d=\inf\lbrace x\ge2:P_d(x) < e^\gamma L_d\log x\rbrace.
$$

An empty set gives $S_d=+\infty$. All ideals of norm exactly $x$ enter the product. Density and lower density refer to the limit and lower limit of the proportion in $\mathcal D(D)$ as $D\to\infty$.

**Theorem.** For every function $f(d)\to\infty$, the fields with $S_d<f(d)$ have density one. For every fixed $B\ge2$, the fields with $B<S_d<B^2$ have positive lower density. For any fixed $\eta>0$, the second endpoint may be replaced by $(1+\eta)B$ for all sufficiently large $B$ (depending on $\eta$).

In particular a constant upper bound fails even among fields with finite first crossing. Section 5 gives a growth constraint on a discriminant-dependent worst-case bound. The argument allows an exceptional set of density zero. Johnston posed the original question during Ethan Lee’s talk at the 2024 Comparative Prime Number Theory Symposium at UBC. [Problem 8, pp. 4–5](https://arxiv.org/pdf/2407.03530#page=4)

## 1. The finite-window product

For a rational prime $p$, the value $s=\chi_d(p)$ records whether $p$ splits ($+1$), ramifies ($0$), or is inert ($-1$). The respective contributions are two prime ideals of norm $p$, one of norm $p$, or one of norm $p^2$. For $p=2$ the value is always $-1$, since $d\equiv5\bmod8$. Let $P_{\mathbb Q}(t)=\prod_{p\le t}(1-1/p)^{-1}$. Comparing the three possible factors gives the exact identity

```math
P_d(t)=P_{\mathbb Q}(t)
\prod_{p\le t}(1-\chi_d(p)/p)^{-1}
\prod_{\substack{\sqrt t < p\le t\\\chi_d(p)=-1}}(1-p^{-2}).
\tag{1}
```

The last product removes an inert factor whose norm $p^2$ has not yet entered. Each local contribution is at least the all-inert contribution. In particular

$$
P_d(t)\ \ge\ A(t):=\prod_{p\le\sqrt t}(1-p^{-2})^{-1}
\ \ge\ \zeta(2)(1-t^{-1/2}).
\tag{2}
$$

Indeed $A(t)/\zeta(2)$ is the product of $1-p^{-2}$ over $p>\sqrt t$. With $n=\lfloor\sqrt t\rfloor$, including all integers $j>n$ can only lower it, and $\prod_{j>n}(1-j^{-2})=n/(n+1)\ge1-t^{-1/2}$. The factor identity and inequality also hold for any assignment of local signs in place of $\chi_d(p)$.

## 2. Transfer to actual fields on a fixed interval

Use independent variables $X_p$ from the Yokoi specialization of Dahl and Kala’s model, with $X_2=-1$. At an odd prime let $c_p=2$ for $p\equiv1\bmod4$ and $c_p=0$ otherwise. The local law is

$$
\Pr(X_p=s)=\frac{p(p-c_p-s)}{2(p^2-c_p)}\ (s=\pm1),\qquad
\Pr(X_p=0)=\frac{c_p(p-1)}{p^2-c_p}.
$$

This counts residues of $m$ modulo $p^2$ with $p^2\nmid m^2+4$. There are $c_p$ roots modulo $p$, each with one lift to a root modulo $p^2$. The character sum of $m^2+4$ modulo $p$ is $-1$, since $(z-m)(z+m)=4$ has $p-1$ solutions. The resulting law has $\mathbb E X_p=-p/(p^2-c_p)$ and $\mathbb E X_p^2=1-O(1/p)$. [Dahl and Kala, §3 and Proposition 14](https://arxiv.org/pdf/1611.02424#page=11)

Put $Y_p=-\log(1-X_p/p)$. Uniformly at odd primes, $Y_p=X_p/p+O(p^{-2})$, so $|\mathbb E Y_p|\ll p^{-2}$ and $\mathrm{Var}Y_p=(1+O(1/p))p^{-2}$. The centered series converges almost surely and in mean square by independence and its summable variances. The means converge absolutely. Hence $Z=\exp(\sum_pY_p)$ is finite and strictly positive almost surely.

**Joint approximation.** For every fixed finite set of primes $H$, the distribution over $\mathcal D(D)$ of

$$
\big((\chi_d(p))_{p\in H},\log L_d\big)
$$

converges weakly to that of $((X_p)_{p\in H},\log Z)$. Keeping the local signs alongside the residue is necessary because both determine the crossing.

For the proof, Dahl and Kala’s Proposition 14 gives $|\mathcal D(D)|\asymp\sqrt D$ and, for each integer $n\ge1$,

$$
\mathbb E_D\chi_d(n)=\mathbb E X(n)+O(n^{2/3}D^{-1/6}\log D).
\tag{3}
$$

Here $\mathbb E_D$ is the uniform average and $X$ is extended completely multiplicatively in this family. The paper includes the Yokoi polynomial $(2k-1)^2+4$. Indicators of any specified finite pattern of signs are polynomials in those signs (interpolate on $\lbrace-1,0,1\rbrace$). Equation (3) gives convergence for each such pattern.

For the full residue we use Proposition 2.2, equation (2.1), of Granville and Soundararajan with $Q=D$, $A=8$, $y=(\log D)^{64}$. These parameters satisfy $A\le\log\log D$ and $y\le D/2$ eventually. Outside at most $D^{1/4}$ primitive characters of conductor at most $D$ the multiplicative error in their product through $y$ is $O(1/\log D)$. Since every $d$ gives a distinct primitive character and the family has order $\sqrt D$, discarding these exceptions costs a proportion tending to zero. [Granville and Soundararajan, Proposition 2.2](https://arxiv.org/pdf/math/0206031#page=7)

For fixed $w$ and $w<p\le y$, replacing the logarithmic factors by $\chi_d(p)/p$ costs $O(\sum_{p>w}p^{-2})$ uniformly. The empirical second moment of $\sum_{w<p\le y}\chi_d(p)/p$ differs from its model second moment by at most

$$
O\left(D^{-1/6}\log D\left(\sum_{p\le y}p^{-1/3}\right)^2\right)=o(1)
$$

by (3) applied to $pq$, including $p=q$. In the model, independence and $\mathbb E X_p=O(1/p)$ bound that second moment by $O(\sum_{p>w}p^{-2})$. For each fixed tolerance, Chebyshev’s inequality now shows that the upper limiting proportion where the truncation at $w$ misses $\log L_d$ by that tolerance tends to zero as $w\to\infty$. The random truncation converges to $\log Z$ in mean square. Applying these estimates first at fixed $w\ge\max H$ to bounded Lipschitz test functions, then sending $w$ to infinity, proves the joint approximation. In particular, the lower limiting proportion for an open condition on these variables is at least its model probability.

We also need that after fixing any finite allowed pattern, the conditional law of $\log Z$ assigns positive probability to every nonempty open interval. Choose a sufficiently large prime cutoff so that every subsequent increment is smaller than one quarter of the interval width and every remaining tail has mean and standard deviation smaller than one sixteenth of that width. Fix any allowed intervening signs. If the sum so far is below the midpoint, prescribe $X_p=1$ until it reaches the midpoint. If above, prescribe $X_p=-1$ until it passes the midpoint in the other direction. Both signs have positive local probability and the sums of their respective increment magnitudes diverge with $\sum_p1/p$. This fixes finitely many signs with positive probability and places the sum within a quarter-width of the midpoint. Independence and Chebyshev’s inequality give positive probability that the remaining tail stays within a further quarter-width.

## 3. An upper bound for density one

Define $P_X(t)$ by the same ideal-norm rule with $X_p$ in place of $\chi_d(p)$, and $T_t=\sum_{p>t}Y_p$. Taking logarithms in (1) gives

```math
\log\frac{P_X(t)}{e^\gamma Z\log t}
=\log\frac{P_{\mathbb Q}(t)}{e^\gamma\log t}
+\sum_{\substack{\sqrt t < p\le t\\X_p=-1}}\log(1-p^{-2})-T_t.
\tag{4}
```

The middle term is nonpositive. Diamond and Pintz’s Theorem 1.1 supplies a deterministic sequence $t_j\to\infty$ on which the first term is strictly negative. It suffices to show that $T_{t_j}>0$ infinitely often with probability one. [Diamond and Pintz, Theorem 1.1](https://www.numdam.org/article/JTNB_2009__21_3_523_0.pdf)

Let $s_t^2=\mathrm{Var}T_t$. The local estimates and the prime number theorem give $s_t^2\asymp1/(t\log t)$, $|\mathbb ET_t|\ll s_t^2$ and $\sup_{p>t}|Y_p-\mathbb E Y_p|\ll 1/t=o(s_t)$. For $V_t=(T_t-\mathbb ET_t)/s_t$ the independent fourth-moment expansion gives $\mathbb E V_t^4\le3+o(1)$. Indeed the sum of individual fourth moments is at most the squared maximum increment times the sum of the variances, and the cross terms are at most $3s_t^4$ before normalization. This computation passes to the infinite tail by convergence in fourth mean, using the same bound on differences of partial sums.

For large $t$, interpolation between the first and fourth absolute moments yields $\mathbb E|V_t|\ge1/\sqrt{\mathbb E V_t^4}\ge1/2$. Since $V_t$ is centered, $\mathbb E\max(V_t,0)\ge1/4$. Cauchy–Schwarz gives $\mathbb E\max(V_t,0)\le1/8+\Pr(V_t>1/8)^{1/2}$. Thus $\Pr(T_t>0)\ge1/64$ for large $t$, since $|\mathbb ET_t|/s_t<1/8$. As a check, the bounded increments also satisfy Lindeberg’s condition, which gives $\Pr(T_t>0)\to1/2$.

The probability of the limsup of $\lbrace T_{t_j}>0\rbrace$ is at least the limsup of their probabilities. This limsup event is unchanged by changing any finite set of local signs, so Kolmogorov’s zero–one law makes its probability one. No independence between tails at different $t_j$ is required.

By (4), almost every model realization has strict negative error at some $t_j$. Given $\epsilon>0$, the union of the first $k$ such tests has model probability greater than $1-\epsilon$ for some **finite** $k$. This union is an open condition in the joint variables of §2 with $H=\lbrace p:p\le\max_{j\le k}t_j\rbrace$. The fraction of actual fields hitting one of these negative values has lower limit at least $1-\epsilon$. Thus for a fixed $M>\max_{j\le k}t_j$ the lower density of $S_d<M$ is at least $1-\epsilon$. Since $f(d)>M$ eventually and $\epsilon$ is arbitrary, $S_d<f(d)$ has density one. The transfer here only requires a finite union at each tolerance.

## 4. First crossings beyond any prescribed cutoff

There is a short obstruction to a common cutoff. If $L_d<e^{-\gamma}/\log B$, then $P_d(x)\ge1>e^\gamma L_d\log x$ throughout $[2,B]$, with a strict margin at $B$. Dahl and Kala’s lower-tail theorem at the fixed parameter $\tau=\zeta(2)\log B>1$ gives a positive proportion of fields satisfying this sufficient condition. To place an actual finite crossing in a later window we also prescribe the local factors.

Fix $B\ge2$ and choose $v$ strictly between $B^{\zeta(2)}$ and $B^2$, possible since $\zeta(2)<2$. In the model prescribe that all primes through $v$ are inert. The sign at 2 already meets this condition, and each of the finitely many odd inert signs has positive probability. Prescribe also

$$
\frac{\zeta(2)e^{-\gamma}}{\log v}< Z < \frac{e^{-\gamma}}{\log B}.
$$

The interval is nonempty, so §2 gives positive probability and positive lower density of actual fields satisfying the same local conditions and residue inequalities. For every such field the error is strictly positive through $B$, with a margin that extends to its right since $P_d(x)\ge1$. At $v$ its product is $A(v)<\zeta(2)$, hence its error is strictly negative. This gives $B<S_d\le v<B^2$.

For the narrower multiplicative interval, $(1-x^{-1/2})/\log x$ decreases on $x>1$, by setting $u=\log x$ and using $e^{u/2}>1+u/2$. For sufficiently large $B$ choose $v<(1+\eta)B$ such that $\log v>\log B/(1-B^{-1/2})$. In the previous construction replace the upper threshold for $Z$ by $e^{-\gamma}\zeta(2)(1-B^{-1/2})/\log B$. By (2) the error stays positive through $B$ with an extension to the right, and it is negative at $v$. This proves the last assertion of the theorem.

## 5. A necessary growth rate for any all-field bound

Write $\log_j D$ for the $j$-fold iterated logarithm. For all sufficiently large $D$ there is a $d\in\mathcal D(D)$ that has no negative value through

$$
c\thinspace\frac{\log D}{(\log_2 D)^2\log_3 D}
\tag{5}
$$

for some fixed $c>0$. A nondecreasing bound in the discriminant valid for every field must therefore grow at least this fast. This assertion concerns the absence of an early negative value. It allows $S_d=+\infty$.

To see this, Dahl and Kala’s Theorem 2 gives a relative-error approximation to the proportion with $L_d<\zeta(2)e^{-\gamma}/\tau$. In its stated range the error is $O(e^\tau(\log_2 D)^2\log_3 D/\log D)$. Take $\tau=\log_2 D-2\log_3 D-\log_4 D-C$ with a sufficiently large fixed $C$ so this error is less than $1/2$. The model lower tail is positive by §2 (also by their Theorem 3), so at least one such field exists. For $r=\tau-1$ and $\tau\ge4$, we have $\tau e^{-r/2}<1$, hence $(1-e^{-r/2})/r>1/\tau$. By (2) and the monotonicity in §4, these fields have positive error throughout $2\le x\le e^r$. Substitution gives (5). [Dahl and Kala, Theorems 2–3](https://arxiv.org/pdf/1611.02424#page=4)

## 6. An upper bound for all discriminants through 10,000

Enumerate each positive odd $m$ with $m^2+4\le10000$ and retain the squarefree discriminants. The two calculations agree on all 45 rows. The largest boundary belongs to $d=9413$ and lies strictly between 525.474356978253 and 525.474356978254, in the prime-ideal norm window $[509,547)$. The other 44 boundaries from $x=2$ are below 37. If $q_d$ is the smallest prime-ideal norm, define $S_d^{\mathrm{ideal}}=\inf\lbrace x\ge q_d:\Delta_d(x)<0\rbrace$. Each program retains the first negative interval from 2 and continues until it finds one with left endpoint at least $q_d$. All ideals at a jump enter together. In 37 fields the original boundary precedes $q_d$, including 11 with $\Delta_d(2)<0$. Under the second convention the maximum stays at $d=9413$ and the next value is between 52.592121251681 and 52.592121251682 for $d=6245$. [Certified table](evidence/census.tsv)

The first calculation uses $\epsilon=(m+\sqrt d)/2$, a unit of norm $-1$. A unit $u>1$ has $u-u'=b\sqrt d$ for an integer $b\ge1$, with $u'=\pm1/u$. If $1<u<\epsilon$ then $0<u-u'\le u+1/u<\epsilon+1/\epsilon=\sqrt d$, impossible. The real quadratic class number formula gives $L_d=h_d\thinspace2\log(\epsilon)/\sqrt d$ with positive integral $h_d$.

To isolate $h_d$, sum the periodic Dirichlet series for $L_d$ through an integer number of periods, bounding each summand by lower and upper rationals. If $N$ is the final index and $H$ is the maximum absolute character partial sum within a period, partial summation bounds the remainder by $H/(N+1)$. Repeat periods until the interval for $h_d$ contains just one positive integer. The exact class number now yields a tight enclosure for $L_d$. Integer square roots bound $\sqrt d$. Monotone rational endpoints and outward-rounded exponentials and logarithms enclose the continuous quantities. The Euler–Maclaurin expansion at 128 bounds $\gamma$ with a remainder between zero and $1/(132\cdot128^{10})$ after the term $-1/(240\cdot128^8)$. [Standard-library verifier](verify.py) · [NIST DLMF §5.11](https://dlmf.nist.gov/5.11)

On a norm window $[a,b)$, $P_d(x)$ is the fixed rational $P_d(a)$. Comparing it with the main term at the left limit $b^-$ rules out a crossing on the entire window or places the zero at $\exp(P_d(a)e^{-\gamma}/L_d)$. The endpoint $2$ is recorded exactly when the error starts negative. All tested endpoint inequalities separated strictly. The independent verifier obtains $L_d$ directly from Arb for the unique primitive quadratic character of this odd squarefree conductor, enumerates prime ideals via the roots of $z^2-z+(1-d)/4\bmod p$, and works with logarithms of products. The two implementations compute their tables independently. A separate check counts the local signs modulo $p^2$ and verifies (1) and the local lower bound on either side of the sample cutoff points. [Arb verifier](independent.py) · [Finite identity checks](check_identities.py) · [Recorded results](evidence/check.txt)

## Earlier results and what remains open

Dahl and Kala established the family distribution of $L_d$ and the character averages used here. Granville and Soundararajan proved the short Euler-product approximation. Diamond and Pintz proved oscillation of the rational Mertens product. Hathi and Lee established oscillation of the prime-ideal error for an individual number field under a rightmost nonreal zero hypothesis, which holds under GRH for its Dedekind zeta function. This supplies conditional finiteness for each field. Their theorem gives no explicit bound on its first crossing. [Dahl and Kala](https://arxiv.org/abs/1611.02424) · [Granville and Soundararajan](https://arxiv.org/abs/math/0206031) · [Diamond and Pintz](https://doi.org/10.5802/jtnb.687) · [Hathi and Lee, Theorem 1](https://arxiv.org/pdf/2112.02166#page=3)

Under GRH for the relevant Dedekind zeta functions, a terminating search also gives a computable bound for every $d\le D$. For each of the finitely many fields, enumerate rational arguments $x\ge2$ and increasing interval precision by dovetailing both indices. The product is rational and the residue is computable. Every strict negative value has a right neighborhood of negative values, so a rational witness and a precision certifying its sign will eventually be reached under that hypothesis. The maximum witness is an upper bound for the finite family. Its a priori size and the unconditional termination for every $D$ are unresolved here.

The previous finite-window calculation computed the boundaries from 2 in the two fields named by Johnston and gave a 7% lower bound in a particular early interval. The present unconditional upper bound covers a set of fields of density one, and the census covers every field through discriminant 10,000. [Johnston’s question](https://arxiv.org/pdf/2407.03530#page=4) [Earlier proof and checks](https://github.com/leecrossley/quadratic-mertens-first-crossings/releases/tag/v1.0.0)

Prescribing small-prime behavior to control $L$-values and class numbers has other precedents. Bernardini uses prescribed local symbols and approximation by a short Euler product in a construction of fields of small class number. Here the local norm cutoffs enter an additional inequality for the first negative Mertens error. [Bernardini, p. 5](https://arxiv.org/pdf/2506.21301#page=5)

The literature check on 21 November 2026 included the workshop list, arXiv, searches under first crossing, first sign change, first negative value, density one and prime-ideal Mertens products, and the 17 OpenAlex records citing the list, Hathi–Lee or Dahl–Kala. The nearby results located concern fixed-field oscillation, integrated errors, explicit Mertens estimates and distributions of residues or class numbers. No earlier statement of the family theorem or the certified census maximum was located. This search leaves open the possibility of unpublished or unindexed work. [Citation query](https://api.openalex.org/works?filter=cites%3AW2554733538%7CW4400433728%7CW4200631075&per_page=100) · [Prior work on integrated errors](https://doi.org/10.1007/s40993-025-00640-y)
