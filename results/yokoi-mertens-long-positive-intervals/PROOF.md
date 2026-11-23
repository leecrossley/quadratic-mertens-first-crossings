# A lower bound for the longest wait in Yokoi's family

Let $\mathcal D(D)=\lbrace d=m^2+4\le D:m\ge1\text{ odd},\ d\text{ squarefree}\rbrace$. For $K_d=\mathbb Q(\sqrt d)$ put $L_d=L(1,\chi_d)=\mathrm{res}_ {s=1}\zeta_{K_d}(s)$. Define

$$
P_d(t)=\prod_{N\mathfrak p\le t}(1-1/N\mathfrak p)^{-1},\qquad
S_d=\inf\lbrace t\ge2:P_d(t) < e^{\gamma_E}L_d\log t\rbrace,\qquad
M(D)=\max_{d\in\mathcal D(D)}S_d .
$$

The first crossing is the infimum of the strictly negative set, with value $+\infty$ for an empty set. GRH for $\zeta(s)L(s,\chi_d)$ gives finiteness for each field by the earlier all-field upper bound. This additional input gives infinitely many distinct fields with finite waits in the corollary. [Finiteness theorem](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-explicit-upper-bound/PROOF.md) Logarithms are natural except for $\log_2$ denoting base 2.

**Theorem.** Assume the ordinary Riemann hypothesis, or just the prime estimate (2) below. There exists an absolute $c>0$ such that, for every sufficiently large $D$,

$$
M(D)>\exp\lbrace c(\log D)^{1/5}\rbrace.
$$

In particular no fixed power of $\log d$ can bound $S_d$ for every member of the family. The statement is about the largest crossing below a discriminant cutoff. It allows most fields to cross much earlier, as the density-one theorem proves. The proof gives an asymptotic bound. The numerical value of $c$ and the starting $D$ are not evaluated here. [Earlier worst-case obstruction, §5](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-crossing-bounds/PROOF.md)

## 1. What would keep the product positive?

Write $P_{\mathbb Q}(t)$ for the ordinary rational prime product. Factoring the rational primes in $K_d$ gives the exact identity

$$
P_d(t)=P_{\mathbb Q}(t)
\prod_{p\le t}(1-\chi_d(p)/p)^{-1}
\prod_{\sqrt t < p\le t,\ \chi_d(p)=-1}(1-p^{-2}).
\tag{1}
$$

It holds at jumps as well. The last factor corrects the norm of an inert prime ideal, which is $p^2$. The rational error satisfies

$$
\left|\log P_{\mathbb Q}(t)-\gamma_E-\log\log t\right|
 \le C_0\thinspace\frac{\log t}{\sqrt t}\qquad(t\ge3).
\tag{2}
$$

For example, the ordinary Riemann hypothesis gives $\psi(t)-t=O(\sqrt t\log^2t)$ by von Koch's estimate in Schoenfeld's explicit form. Partial summation against $1/(t\log t)$ then gives (2) for the prime-power sum $\sum_{p^j\le t}1/(jp^j)$. The boundary term is $O(\log t/\sqrt t)$, and the integral tail is bounded by a constant times $\int_t^\infty(\log v)v^{-3/2}\thinspace dv$. The omitted powers in the product cost $O(1/\sqrt t)$, by splitting at $p=\sqrt t$. The character approximation below uses the unconditional exceptional-set theorem of Granville and Soundararajan. [Schoenfeld](https://doi.org/10.1090/S0025-5718-1976-0457374-X) · [Prime-power correction](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-explicit-upper-bound/PROOF.md)

Choose $K=\lfloor c_0(\log D)^{1/5}\rfloor$, $X=2^K$, and $Y=X^{128}$, with a fixed sufficiently small $c_0>0$ chosen in §3. All estimates henceforth concern sufficiently large $D$. By Proposition 2.2 (2.1) of Granville and Soundararajan with $Q=D$ and $A=8$, all but at most $D^{1/4}$ primitive characters of conductor up to $D$ satisfy

$$
\log L_d=\sum_{p\le Y}-\log(1-\chi_d(p)/p)+O((\log D)Y^{-1/32})
        =\sum_{p\le Y}-\log(1-\chi_d(p)/p)+O(X^{-2}).
\tag{3}
$$

Here $8\le\log\log D$ and $Y\le D/2$ eventually. Every discriminant in the family gives a distinct primitive character. In (1), the log of the inert correction is at least $-C/\sqrt t$ by comparison with the sum of $n^{-2}$ over all integers $n>\sqrt t$. For $t<p\le Y$, replacing $-\log(1-\chi_d(p)/p)$ by $\chi_d(p)/p$ costs $O(1/t)$ in total. Inserting (2) and (3) into (1), some absolute $C_1$ therefore satisfies, for all nonexceptional fields and $3\le t\le X$,

$$
\log\frac{P_d(t)}{e^{\gamma_E}L_d\log t}
 \ \ge\ -C_1\frac{\log t}{\sqrt t}-\sum_{t < p\le Y}\frac{\chi_d(p)}p.
\tag{4}
$$

We will construct a field for which the tail sum on the right is sufficiently negative at every real $t$ in a growing interval. [Granville and Soundararajan, Proposition 2.2](https://arxiv.org/pdf/math/0206031#page=7)

## 2. Biasing many primes a little

Use the independent variables $X_p\in\lbrace-1,0,1\rbrace$ of Dahl and Kala for this family. They have the same limiting local splitting laws as $\chi_d(p)$. Here $X_2=-1$. At odd $p$ put $c_p=2$ if $p\equiv1\bmod 4$, and $c_p=0$ otherwise. The probabilities of $s=\pm1$ are $p(p-c_p-s)/(2(p^2-c_p))$, and the remaining mass is at zero. In particular $\mu_p=\mathbb E X_p=-p/(p^2-c_p)\le0$, $v_p=\mathrm{Var}(X_p)\to1$, and every inert sign has positive probability. Extend the variables completely multiplicatively. Proposition 14 of Dahl and Kala gives $|\mathcal D(D)|\asymp\sqrt D$ and, uniformly for integers $n\ge1$,

$$
\mathbb E_D\chi_d(n)=\mathbb E X(n)+O(n^{2/3}D^{-1/6}\log D),
\tag{5}
$$

where $\mathbb E_D$ averages uniformly over $\mathcal D(D)$. [Family identification and Proposition 14](https://arxiv.org/pdf/1611.02424#page=11)

Let $A>0$ be a sufficiently large absolute constant. Choose a fixed large power of two $B$ so that, for $p>B$, $v_p\ge1/2$ and $a_p=A(\log p)^2/\sqrt p\le1/16$. We may enlarge $B$ later. Require all primes up to $B$ to be inert. The indicator $I$ of this finite event is a fixed polynomial in the local variables, using $(X_p^2-X_p)/2$ for each odd prime. Its expectation $p_B$ is positive.

With $z_p=X_p-\mu_p$, form the real product

$$
R=\prod_{B < p\le4X}(1-a_pz_p).
$$

Weight the independent model by $IR^2/\mathbb E(IR^2)$. Independence persists above $B$, since the weight factors by prime. Write $\nu_p$ for the resulting mean. Outside $(B,4X]$ and above $B$ it is $\mu_p\le0$. Within the interval it equals

$$
\nu_p=\mu_p+
 \frac{-2a_p v_p+a_p^2\mathbb Ez_p^3}{1+a_p^2v_p}
 \le -a_p/2.
\tag{6}
$$

Indeed $|z_p|\le2$, $|\mathbb Ez_p^3|\le2v_p$, and $1/2\le v_p\le1$. Choose $B$ also so that $\pi(2t)-\pi(t)\ge t/(2\log t)$ for $t\ge B$, by the prime number theorem. Then for $B\le t\le X$,

$$
\sum_{t < p\le Y}\frac{\nu_p}{p}
 \le-\frac A2\sum_{t < p\le2t}\frac{(\log p)^2}{p^{3/2}}
 \le-\frac{A}{32}\frac{\log t}{\sqrt t}.
\tag{7}
$$

Thus a mild negative bias per prime supplies the required margin on each scale.

## 3. Transferring the weight to actual fields

Let $N=\lfloor D^{1/1000}\rfloor$. Expand $R$ as a multilinear polynomial in the centered $z_p$, indexed by squarefree products of the chosen primes. Retain terms with product $n\le N$ and call the result $R_N$. The centered monomials are mutually orthogonal in the original model. Consequently the relative squared norm discarded from $R$ is exactly the probability that a random product exceeds $N$, where each prime is included independently with probability $a_p^2v_p/(1+a_p^2v_p)$. This follows by expanding $`\|R\|_2^2=\prod_p(1+a_p^2v_p)`$.

With $\theta=1/\log(4X)$, Markov's inequality bounds that probability by

$$
\varepsilon\le
\exp\left(-\frac{\log N}{\log(4X)}+(e-1)\sum_{B < p\le4X} a_p^2\right).
\tag{8}
$$

Indeed $p^\theta\le e$ for every selected prime. Partial summation and $\pi(t)\ll t/\log t$ give $\sum a_p^2\ll A^2(\log(4X))^4$. Choose $c_0$ small after $A$ so the negative term dominates by a fixed factor. This is possible since $(\log X)^5\le(c_0\log2)^5\log D$. Then $\varepsilon\le\exp(-c_2(\log X)^4)$ for some $c_2>0$. In particular $\sqrt\varepsilon\le Y^{-100}$ eventually. The fifth power here pays both for the squared coefficients and the lengths of the integers carrying them.

By Cauchy–Schwarz, $\mathbb E|R_N^2-R^2|\le2\sqrt\varepsilon\thinspace\mathbb E R^2$. The initial indicator is independent of both polynomials. Expectations of a bounded function under the two normalized weights $IR_N^2$ and $IR^2$ therefore differ by $`O(\sqrt\varepsilon)\|F\|_\infty`$. Also $\mathbb E(IR_N^2)=p_B(1-\varepsilon')\mathbb E R^2\ge p_B/2$ for large $D$, where $0\le\varepsilon'\le\varepsilon$.

Evaluate $IR_N^2$ at the actual characters and normalize it to a probability measure on $\mathcal D(D)$. The following fourth-moment comparison is uniform over all intervals $H\subset(B,Y]$. Write $S_H=\sum_{p\in H}(\chi_d(p)-\nu_p)/p$ on the field side, with $X_p$ in its place on the model side. Then

$$
\left|\mathbb E_{D,w} S_H^4-\mathbb E_{*,w} S_H^4\right|\le Y^{-10}
\tag{9}
$$

eventually, where the model weight on the right is the full normalized $IR^2$.

Here are quantitative details needed because the family of intervals grows. In an expansion in completely multiplicative characters, let the coefficient norm mean the sum of absolute coefficients before or after gathering like terms. Products have coefficient norm at most the product of the norms. Each retained centered monomial including its coefficient has norm at most $2^{\omega(n)}\le n$, since $a_p\le1$. Thus $R_N$ has norm at most $N^2$ and all its character indices are at most $N$. The fixed $I$ contributes constants depending on $B$. The polynomial $S_H^4$ has norm at most $(2Y)^4$ and indices at most $Y^4$. Applying (5) to $IR_N^2S_H^4$ gives total error

$$
\ll_B N^4(2Y)^4(C_B N^2Y^4)^{2/3} D^{-1/6}\log D
 =O_B(D^{-1/8}),
$$

since $Y=D^{o(1)}$. The same bound applies to the normalization with $S_H^4$ omitted. That normalization is therefore at least $p_B/3$ on the field side. Upon division, the errors are $O_B(D^{-1/8}(1+Y^4))$. Passing to the full tilted model costs $O(Y^4\sqrt\varepsilon)$. Together these estimates imply (9). The total weight of fields exceptional in (3) is $O_B(D^{1/4}N^4/\sqrt D)=o(1)$ by the same coefficient norm and the lower bound on the normalization.

## 4. Keeping control between the sampled endpoints

Take any dyadic integer $z$ with $B\le z<Y$ and an interval of $h$ consecutive integers in $(z,2z]$. In the tilted model the summands above $B$ are independent and centered. Each has absolute value at most $2/z$. Expansion of the fourth moment yields $\mathbb E_{*,w}|S_H|^4\ll h^2/z^4$ because only quadruples with no singleton index contribute. By (9), $h\ge1$ and $z\le Y$, the same bound holds under the field weight with an absolute constant, uniformly in $z,H$ for large $D$.

Write $M_z$ for the largest absolute centered sum from $z$ to any endpoint up to $2z$. A prefix of $(z,2z]$ partitions into at most one dyadic interval from each subdivision level. At level $j$ there are $2^j$ intervals of size $z/2^j$. Bounding the fourth moment of the maximum there by the sum of the fourth moments and applying Minkowski across levels gives

```math
\|M_z\|_4\ll \sum_{j=0}^{\log_2 z}
  \left(2^j\frac{(z/2^j)^2}{z^4}\right)^{1/4}
 \ll z^{-1/2}.
```

The probability that $M_z>(\log z)/\sqrt z$ is at most $C/(\log z)^4$. The sum of these bounds over powers of two $z\ge B$ is less than $1/4$ if the fixed $B$ is large enough. The constants here are absolute. This choice of $B$ is consistent with §2. Since the exceptional fields in (3) have weight tending to zero, at least one nonexceptional field satisfies every one of the prefix bounds and the condition $I=1$.

For this field and every real $t\in[B,X]$ sum the centered prime tail to $Y$ by dyadic blocks. The first incomplete block costs at most twice its prefix maximum. Summing the rest uses $\sum_{k\ge0}(\log z+k\log2)2^{-k/2}\ll\log z$ for $z\ge2$. It follows uniformly that

$$
\left|\sum_{t < p\le Y}\frac{\chi_d(p)-\nu_p}{p}\right|
 \le C_3\thinspace\frac{\log t}{\sqrt t}
$$

with an absolute $C_3$ independent of $A,B,c_0$. Choose $A$ in §2 so that $A/32>C_1+C_3+5$. By (4) and (7) the logarithmic product error exceeds $5\log t/\sqrt t$ on $[B,X]$.

## 5. The initial interval and the maximum

At $B$ the selected field has only inert primes up to $B$, so $P_d(B)=\prod_{p\le\sqrt B}(1-p^{-2})^{-1}\le\zeta(2)$. The margin just proved gives

$$
e^{\gamma_E}L_d\log B\le\zeta(2)\exp(-5\log B/\sqrt B)
 <\zeta(2)(1-B^{-1/2})
$$

for large $B$. At any $t\ge2$, every splitting pattern satisfies $P_d(t)\ge\prod_{p\le\sqrt t}(1-p^{-2})^{-1}\ge\zeta(2)(1-t^{-1/2})$. For the second inequality, multiply the missing factors over all integers larger than $\lfloor\sqrt t\rfloor$ and telescope. Since $(1-t^{-1/2})/\log t$ is decreasing for $t>1$, positivity extends to the entire interval $[2,B]$. The strict margin at $X$ and monotonicity of $P_d$ extend positivity to a right neighborhood of $X$. Thus $S_d>X$.

For all large $D$, $X=2^{\lfloor c_0(\log D)^{1/5}\rfloor}>\exp\lbrace(c_0\log2/2)(\log D)^{1/5}\rbrace$. This proves the theorem. Under the additional field GRH input, each individual $S_d$ is finite, so the fields supplying these longest waits include infinitely many distinct discriminants.
