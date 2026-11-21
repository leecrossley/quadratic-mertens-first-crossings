# A weighted race between two quadratic splitting laws

Lee Crossley

Let $`d>1`$ be a positive fundamental discriminant different from 5. At an ordinary prime unramified in both fields, assign $`a_d(p)=1`$ for split in $`\mathbb Q(\sqrt d)`$ and inert in $`\mathbb Q(\sqrt5)`$, and $`-1`$ for the reverse. All other primes get 0. Thus $`2a_d(p)=\chi_d(p)-\chi_5(p)`$ away from $`5d`$. Throughout use the critical-line property for $`\zeta,L(s,\chi_5),L(s,\chi_d)`$. The comparison covers squarefree $`d=m^2+4`$ with $`m`$ odd. Alpöge's announced Dirichlet GRH theorem supplies the critical-line property. [Announcement](https://alpo.ge/remark.pdf) · [Independent formal checks](https://math.mit.edu/~drew/grh/)

Write $`u=\log y,\ N_y=\sqrt y\log y,\ L=\log(3d),\ h=\log 8`$, and put

```math
 T(y)=\sum_{p>y}a_d(p)(1-y/p)/p,\qquad W(u)=N_yT(y),\qquad q(u)=W(u+h)-W(u).
```

Sum in increasing prime order. Convergence follows from the prime number theorem for the two fixed characters at each $`d`$.

**Theorem.** There are absolute $`A,c>0`$ such that for every sufficiently large $`d`$, beyond a bound the argument does not make effective, the interval $`L^{3/2}\le y\le d^A/8`$ contains a start with $`q(\log y)>0.46`$ and another with $`q(\log y)<-0.46`$. Somewhere in this range $`|q(\log y)|>c\sqrt L`$. More precisely, for every sufficiently large fixed absolute $`B`$, with $`H=BL,\ U=(3/2)\log L`$ and $`\mu_H(u)=2(1-u/H)/H`$ on $`[0,H]`$,

```math
 \int_U^H |q(u)|^2\mu_H(u)\,du\ \ge\ c^2 L .
 \tag{1}
```

The same $`c`$ works for all such fixed $`B`$, once $`d`$ is sufficiently large. The two signed bounds hold with $`.45`$ for a finite sum using primes only through $`16K y`$, $`K=C L^2`$. The root-mean-square conclusion gives a finite-window absolute excursion of order $`\sqrt L`$ with $`K=C L`$.

For a prime ideal of norm $`v`$ put $`\ell(v)=-\log(1-1/v)`$. Define

```math
 F_d(y)=\int_y^\infty\left(\sum_{N\mathfrak p\le t}\ell(N\mathfrak p)-\gamma
 -\log L(1,\chi_d)-\log\log t\right)\frac{y\,dt}{t^2}.
```

This is the signed log-product average. A negative value implies a point of negative log-product error at some $`t\ge y`$. The location of that $`t`$ is a separate question.

**Consequence for a field with a late crossing.** After increasing the absolute $`A`$, if $`F_d(y)\ge0`$ for every $`2\le y\le d^A`$, then for some $`z\ge L^{3/2}`$, $`2Kz\le d^A,\ K=C L`$, the following finite discrepancy is below $`-c_1\sqrt L`$:

```math
 W_K(\log z)=N_z\left[
 \sum_{z\lt p\le Kz} \frac{a_d(p)}p(1-z/p)
 +(1-1/K)\sum_{Kz\lt p\le 2Kz}\frac{a_d(p)}p(2Kz/p-1)\right].
 \tag{2}
```

Thus on any subclass where these negative leads are uniformly $`o(\sqrt L)`$ over the indicated windows, a single exponent suffices for a negative average. The theorem permits central zeros, repeated zeros and arbitrarily close pairs.

## The zero series and the cost of the prime powers

Write $`\lambda`$ for a nontrivial zero ordinate, with its full multiplicity and both signs. Put $`s_\lambda=1/2-i\lambda,\ c_\lambda=1/[s_\lambda(1+s_\lambda)],\ w_\lambda=|c_\lambda|`$. Use subscripts 5 and $`d`$ for the two multisets. The absolutely convergent real series

```math
 Z(u)=\tfrac12\left(\sum_5-\sum_d\right)c_\lambda e^{i\lambda u}
```

satisfies $`|Z|\ll L`$. Indeed the paired logarithmic derivative at 2 gives $`\sum_d(9/4+\lambda^2)^{-1}\ll L`$, and $`w_\lambda\le(1/4+\lambda^2)^{-1}`$. Define $`W^*(u)`$ by replacing $`a_d(p)/p`$ in $`W`$ by the full prime-power difference $`(\chi_d(p)^k-\chi_5(p)^k)/(2kp^k)`$, with cutoff $`p^k>y`$ and weight $`1-y/p^k`$. The integrated explicit formula gives

```math
 W^*(u)=\tfrac12\left(\sum_5-\sum_d\right)e^{i\lambda u}h_\lambda(u),\qquad
 h_\lambda(u)=u\int_0^\infty
 \frac{e^{-ut}\,dt}{(s_\lambda+t)(1+s_\lambda+t)} .
 \tag{3}
```

For the sign, the future prime-power tail is minus the averaged partial-sum error. Testing the negative differential of the Chebyshev error at $`e^v`$ against $`(1-e^{u-v})e^{-v}/v`$ on $`v\ge u`$ gives the positive zero contribution to the partial-sum error. The two primitive even characters have identical trivial-zero densities, so those cancel. Inserting $`1/v=\int_0^\infty e^{-tv}dt`$ yields (3). Smooth truncation of the test gives an $`O_u((1+\lambda^2)^{-1})`$ transform, and the prime number theorem controls its upper endpoint. In particular $`|h_\lambda|\le w_\lambda,\ |h_\lambda-c_\lambda|\le 8w_\lambda/(3u)`$ by differentiating the reciprocal product in $`t`$. [Explicit formula, including the test and endpoint estimates](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/ef3e53c/results/signed-prime-tails/PROOF.md) · [Grenié and Molteni](https://arxiv.org/abs/1312.4465)

On $`u\ge u_0=\log2`$, $`R=W^*-W`$ has both $`L^1(du)`$ and supremum norms $`O(\sqrt L)`$. For a single term of index $`p^k`$, bound either norm by $`O((\log p)p^{-k/2})`$, by integrating $`u e^{u/2}/(kp^k)`$ up to $`k\log p`$ or taking its maximum there. The linear terms come only from ramified primes, as do all even powers. Bound their total by $`\sum_{p\mid5d}\log p/(\sqrt p-1)\ll\sqrt L`$, splitting at $`L`$ and using Chebyshev's estimate. The odd powers $`k\ge3`$ sum absolutely over all primes. Consequently $`\int |R|^2du\ll L,\ |W|\ll L`$.

The initial segment will be removed. Uniformly for $`u_0\le u\le U+h`$,

```math
 |W(u)|\ll u e^{u/2}\log(2+L).
 \tag{4}
```

Indeed truncate the linear character tails at $`d^2`$. Partial summation of $`\sum_{p\le x}\chi_d(p)\log p\ll\sqrt x\log^2(3dx)`$ bounds the unnormalised remainder by $`O(1)`$ uniformly for these $`y`$, including the factor $`1-y/p`$. Ramified primes lie below $`d^2`$ for large $`d`$. Up to $`d^2`$ use the elementary upper bound for the sum of $`1/p`$. Thus on that initial segment $`\int |W|\,du=o(L)`$ and $`\int |W|^2du=o(L^2)`$, from $`e^{U/2}=L^{3/4}`$. [Prime ideal theorem under the critical-line hypothesis](https://arxiv.org/abs/1312.4463)

## A one-sided Fourier average

Use $`\langle f\rangle=\int_0^H f\mu_H\,du,\ K_H(v)=\langle e^{ivu}\rangle`$. Direct integration gives

```math
 \Re K_H(v)=\Phi_H(v)=\left(\frac{\sin(Hv/2)}{Hv/2}\right)^2,\qquad
 |K_H(v)|\le\min(1,4/(H|v|)).
```

The value at zero is 1. Put $`G(u)=Z(u+h)-Z(u)`$ and $`M(t)=\langle G e^{-itu}\rangle`$. The zero coefficient of this difference vanishes. From $`|e^{ihv}-1|\le h|v|`$, and then from the same estimate with $`v=\lambda-t`$,

```math
 |\langle G\rangle|\ll_h L/H,\qquad
 |M(t)-(e^{iht}-1)\langle Ze^{-itu}\rangle|\ll_h L/H.
```

For $`D_e(t)=\sum_e w_\lambda\Phi_H(t-\lambda)`$, rotation by $`\arg c_t`$ gives

```math
 \Re\{-e^{-i\arg c_t}\langle Ze^{-itu}\rangle\}
       =\tfrac12(D_d(t)-D_5(t))+O(L/H).
```

Indeed $`|(\arg c_t)'|\le 8/3`$. Pair the resulting $`O(|\lambda-t|)`$ error with $`|K_H(\lambda-t)|`$; summability of the $`w_\lambda`$ controls the whole sum. For $`0.6\le t\le0.8`$ there is a fixed gap to the conductor-five ordinates: their total inverse-square mass is less than $`0.204`$ even with the zeta ordinates included. Thus $`D_5(t)\ll H^{-2}`$, and

```math
 |M(t)|\ge |\sin(ht/2)|D_d(t)-O_h(L/H).
 \tag{5}
```

[Conductor-five certificate](https://github.com/leecrossley/yokoi-mertens-positive-averages-5-13/blob/f7233ab4e1c85b9b37bffdaa11c4559d7713bd62/PROOF.md)

For any fixed nonempty positive interval $`J`$, the number of $`d`$-ordinates there is $`(|J|/(2\pi)+o(1))\log d`$. For completeness, for fixed $`v>1/2`$ the paired logarithmic derivative gives
$`\sum_d(v^2+\lambda^2)^{-1}=(\log d)/(2v)+O_v(1)`$; the Euler product at $`1/2+v>1`$ bounds its logarithmic derivative uniformly. Weight each ordinate by $`(1+\lambda^2)^{-1}/\log d`$ and map it to $`x=(1+\lambda^2)^{-1}`$. The finite measures on $`[0,1]`$ are bounded. For any weak limit, integration of $`(1+(v^2-1)x)^{-1}`$ gives $`1/(2v)`$. The image of $`d\lambda/[2\pi(1+\lambda^2)]`$ gives the same values. Expansion near $`v=1`$ identifies the moments, hence the measure. The limiting measure has no boundary atoms for finite nondegenerate intervals. Undo the weight and use symmetry to count one sign. [Earlier low-ordinate argument](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/ef3e53c/results/signed-prime-tails/PROOF.md)

## Size and both directions

For $`I=[0.6,0.8]`$, $`J=[0.65,0.75]`$, positivity of $`\Phi_H`$ gives

```math
 \int_I D_d(t)^2dt\ \ge\ \sum_{\lambda\in J} w_\lambda^2
  \int_{|t-\lambda|\le 1/H}\Phi_H(t-\lambda)^2dt\ \gg\ L/H.
```

Here $`H`$ is large, the kernel is bounded below on each small integration interval and the count includes multiplicities. Hence (5) gives $`\|M\|_{L^2(I)}\ge c_0\sqrt{L/H}-C L/H`$. For $`H=BL`$, take $`B`$ large enough to retain at least half the first term. Plancherel gives

```math
 \int_{\mathbb R}|M(t)|^2dt=2\pi\int_0^H |G|^2\mu_H^2du
       \le (4\pi/H)\langle |G|^2\rangle .
```

It follows that $`\|G\|_{L^2(\mu_H)}\gg\sqrt L`$ with an absolute constant. Extend $`W`$ by zero below $`u_0`$ for this comparison only. By (3), $`|W^*-Z|\ll L/u`$. The small fixed initial interval costs $`O(L^2/H)`$ in squared norm; integrating $`u^{-2}`$ and adding the squared norm of $`R`$ gives $`\|G-q\|_{L^2(\mu_H)}\ll L/\sqrt H`$. This includes the shifted terms by $`\mu_H\le2/H`$. Increase the absolute lower bound on $`B`$ to absorb this cost. By (4) the squared norm of $`q`$ before $`U`$ is $`o(L^2/H)`$. This proves (1).

For the separate signed conclusions an $`L^1`$ comparison with $`O(L/H)`$ error is needed. For $`u\ge u_0`$ introduce the positive operator

```math
 {\cal A} f(u)=f(u)+\int_0^\infty k(r)\frac{f(u+r)}{u+r}\,dr,
 \qquad k(r)=e^{-r/2}(1+e^{-r}).
```

It maps $`W^*`$ to $`Z`$ exactly. To check a single ordinate, express $`h_\lambda(u)`$ as $`\int_0^\infty e^{-s_\lambda v}(1-e^{-v})u/(u+v)\,dv`$. In the added term convolution gives
$`\int_0^v(1+e^{-r})(1-e^{-(v-r)})\,dr=v(1-e^{-v})`$.
Adding the two kernels leaves the transform $`c_\lambda`$. Absolute summability in (3) allows application of the operator term by term. Its $`L^1`$ and supremum operator norms on the half-line are at most $`1+\|k\|_1/u_0`$. Commuting it with translation by $`h`$ costs $`O_h(L/u^2)`$ pointwise when applied to $`W`$, since the denominators differ by $`h`$ and $`\|W\|_\infty\ll L`$.

Suppose $`q\le m=0.46`$ on $`[U,2H]`$. Then

```math
 \langle(G-m)_+\rangle \ll_h L/H+o(1).
 \tag{6}
```

To see this, on $`[u_0,H]`$ write $`G={\cal A}q`$ plus the commutator and the translate difference of $`{\cal A}R`$. Their weighted $`L^1`$ costs are $`O_h(L/H)`$ and $`O(\sqrt L/H)`$. Positivity gives $`{\cal A}q\le m(1+\|k\|_1/u)+{\cal A}(q-m)_+`$. The extra $`1/u`$ contributes $`O(\log H/H)`$. In the last term the part below $`U`$ costs $`o(L/H)`$ by (4) and the $`L^1`$ operator bound. The part beyond $`2H`$ is $`O(L e^{-H/2})`$ on $`[u_0,H]`$. The omitted $`[0,u_0]`$ costs $`O(L/H)`$ using $`|G|\ll L`$. This also proves (6) for $`-G`$ under the corresponding bound on $`-q`$.

Take an ordinate $`\tau\in[0.699,0.701]`$. In (5) it contributes $`D_d(\tau)\ge w_\tau`$, even in a cluster. On this interval $`\sin(ht/2)w_t>0.4660`$, using the smaller sine and the larger denominator at the two endpoints. On the other hand

```math
 |M(\tau)|\le m|K_H(-\tau)|+\langle|m-G|\rangle
 =m(1+|K_H(-\tau)|)-\langle G\rangle+2\langle(G-m)_+\rangle.
```

Choose $`B`$ sufficiently large and then $`d`$ sufficiently large. The upper bound is strictly below the lower bound from (5). Applying the argument to $`-G`$ rules out the other one-sided bound. The witnesses have $`U\le u\le 2H`$. A single increased exponent $`A`$ absorbs $`h`$ and all logarithmic factors.

## Finite prime windows and the absolute level

An exact identity expresses (2) as

```math
 W_K(\log y)=N_y\{T(y)-(2-1/K)T(Ky)+(1-1/K)T(2Ky)\}.
```

It follows by comparing the coefficient at each prime, including either endpoint. Since $`\|W\|_\infty\ll L`$ and $`N_y/N_{Ky}\le K^{-1/2}`$, the uniform error is $`|W_K-W|\ll L/\sqrt K`$. Applying this to both ends of an eightfold step proves the finite-window assertions for sufficiently large absolute $`C`$.

Finally put $`\mathcal J=N_y(F_5-F_d)/2`$. At norm $`p`$ the local multiplicity is $`1+\chi(p)`$, at norm $`p^2`$ it is $`(\chi(p)^2-\chi(p))/2`$. Integrating a local jump assigns weight $`\min(1,y/v)`$. The difference of the log normalisations is the difference of the complete local log products, by the Euler product at 1 in increasing prime order. Subtraction therefore gives the oriented future linear term with the **positive** sign in $`\mathcal J`$. Its difference from $`W`$ is

```math
 |\mathcal J-W|\ll 1 + L/\sqrt y .
 \tag{7}
```

Indeed $`\ell(p)-1/p=O(p^{-2})`$ off the ramified set and $`\sum_{p>x}p^{-2}\ll1/(x\log x)`$ by Chebyshev. The entire square-norm tail costs $`O(N_y/(\sqrt y\log y))=O(1)`$. Primes dividing $`5d`$ cost $`O(N_y\log(5d)/(y\log y))`$. All estimates hold for $`y\ge2`$, with constants enlarged on bounded intervals. For the reference field $`N_y F_5(y)`$ is bounded: (3) for the field zeta function bounds its zero and trivial-zero terms, and the prime-power correction is bounded by splitting off the squares and summing the higher powers. Equivalently use (3) and (5) of the [signed-prime estimate](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/ef3e53c/results/signed-prime-tails/PROOF.md) with $`d=5`$, plus continuity on compact intervals.

At a late field both endpoint values of $`W`$ in (1) are at most $`O(1+L^{1/4})`$ by (7) and $`y\ge L^{3/2}`$. Their separation is at least a constant times $`\sqrt L`$, so the lower endpoint value is at most $`-c_2\sqrt L`$. Choose $`K=C L`$ with sufficiently large absolute $`C`$ to preserve half this deficit, and enlarge $`A`$ to cover $`2Kz`$. This gives (2). The proof leaves open whether the negative lead so obtained can occur persistently in the Yokoi family.

## When the weighted difference actually forces a negative average

For a direct sign test write $`b_y(v)=(1-y/v)_+`$ and use the exact identity

```math
 \mathcal J =
 N_y\sum_{p\nmid5d} a_d(p)
  [\ell(p)b_y(p)-\tfrac12\ell(p^2)b_y(p^2)] + J_{\rm ram}.
```

For each $`p\mid 5d`$ write $`a=\chi_d(p),b=\chi_5(p)`$. Its contribution to $`J_{\rm ram}/N_y`$ is $`(a-b)\ell(p)b_y(p)/2+(a^2-b^2-a+b)\ell(p^2)b_y(p^2)/4`$. These coefficients follow from the two norm multiplicities above. A negative average is equivalent to $`\mathcal J>N_y F_5(y)/2`$. For $`d=533`$ at $`y=30`$, $`W`$ lies in $`(0.5142549,0.5142550)`$, the corrected lead $`\mathcal J`$ in $`(0.329780,0.329783)`$ and the threshold in $`(0.293944,0.293946)`$. A second calculation forms the corrected prime sum directly and proves $`\mathcal J>0.327>0.295>N_yF_5(y)/2`$. [Two arithmetic checks](CHECKS.md)
