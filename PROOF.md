# Delayed Yokoi averages with small quadratic twist correlations

Lee Crossley

Let $`d=m^2+4`$ be squarefree, with $`m`$ positive and odd, and let $`\chi_d`$ denote its primitive quadratic character. For $`K=\mathbb Q(\sqrt d)`$ put

```math
 B_d(t)=\sum_{N\mathfrak p\le t}-\log(1-1/N\mathfrak p)-\gamma-\log L(1,\chi_d)-\log\log t,
 \qquad F_d(y)=\int_y^\infty B_d(t)y\,dt/t^2 .
```

For a real Dirichlet character $`\psi`$, including the trivial character $`1`$ of conductor one, measure agreement of prime signs by

```math
 T_{d,\psi}(y)=\sum_{p>y}\chi_d(p)\psi(p)(1-y/p)/p.
```

Matching split or inert signs contribute positively. Opposite signs contribute negatively, and a ramified factor contributes zero. Tails are ordered by increasing prime. Use RH for $`\zeta`$ and GRH for the primitive quadratic Dirichlet functions concerned, including the twists. [Critical-line statements](https://math.mit.edu/~drew/grh/)

**Theorem.** Fix $`K_0>0`$. There are positive constants $`B,c,C,b`$ depending at most on $`K_0`$, with $`B`$ a fixed sufficiently large dyadic integer. For every sufficiently large $`D`$, let

```math
 X=2^{\lfloor c(\log D/(\log\log D)^2)^{1/3}\rfloor}.
```

At least $`\sqrt D\exp[-C(\log X)^2(\log\log X)^2]`$ distinct Yokoi discriminants in $`(D/2,D]`$ have all the following properties on the same field.

1. $`F_d(y)>0`$ at every real start $`2\le y\le X`$. For $`B\le y\le X`$, both $`F_d(y)`$ and $`-T_{d,1}(y)`$ are at least $`b\log\log y/\sqrt y`$.
2. Simultaneously for each such $`y`$ and **every** nonprincipal primitive quadratic $`\psi`$ of conductor $`q\le y^{K_0}`$,

```math
 |T_{d,\psi}(y)|\le C/\sqrt y.
```

3. For $`B\le x\le X`$ the ordinary log-weighted bias on $`(x,2x]`$ obeys

```math
 \sum_{x\lt p\le2x}\chi_d(p)\log p\le-b\sqrt x\log x\log\log x.
```

For every nonprincipal quadratic reference as above with $`q\le x^{K_0}`$, every subinterval $`[s,t]\subset[x,2x]`$ satisfies

```math
 \left|\sum_{s\lt p\le t}\chi_d(p)\psi(p)\log p\right|\le C\sqrt x\log x .
```


In particular even a reference chosen after seeing the field and the start has correlation at most $`O_{K_0}(1/\log\log y)`$ times the untwisted bias in the same future weight. The discriminants counted are $`D^{1/2-o(1)}`$ in number. The cutoff $`X`$ exceeds every fixed power of $`\log D`$ and lies below $`D^a`$ for every fixed $`a>0`$ eventually. The result leaves open what survival as far as $`d^a`$ would imply.

**Where this strength of bias must end.** For every genuine primitive quadratic character, the integrated explicit formula gives $`\sqrt y\log y\,|T_{d,1}(y)|\ll\log(3d)`$ uniformly in $`y\ge2`$. The kernel per nontrivial zero is bounded by $`(1/4+\gamma^2)^{-1}`$, whose sum is $`O(\log(3d))`$ by the logarithmic derivative at 2. The contribution of higher prime powers is $`O(1)`$ after normalisation, by comparison with all rational prime powers. Thus a margin $`-T_{d,1}(y)\ge b\log\log y/\sqrt y`$, for fixed $`b>0`$, requires $`\log y\log\log y\ll_b\log d`$, in particular $`y\le d^{C_b/\log\log d}`$ for large $`d`$. A field can in principle remain positive with a smaller margin. [Integrated kernel and zero bound](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/fa7ed4741f735e37fc3552f497952a57f02cbaa2/results/signed-prime-tails/PROOF.md)

## The family measure

Use Dahl and Kala's independent prime variables $`Z_p`$ for this polynomial and extend them completely multiplicatively. At 2 the value is $`-1`$. For odd $`p`$, put $`b_p=1+(\frac{-1}p)`$. The two probabilities at $`s=\pm1`$ are $`p(p-b_p-s)/(2(p^2-b_p))`$. The rest is mass at 0. Write $`\mu_p=\mathbb EZ_p=-p/(p^2-b_p)`$, $`v_p=\mathrm{Var} Z_p`$. In particular $`|\mu_p|\ll 1/p`$ and $`v_p=1+O(1/p)`$ for odd $`p`$. With uniform probability on the shell,

```math
 \mathbb E_D\chi_d(n)=\mathbb E Z(n)+O(n^{2/3}D^{-1/6}\log D),\qquad
 \#\{d\in(D/2,D]\}\asymp\sqrt D .
 \tag{1}
```

This is Proposition 14 applied to $`(2j+1)^2+4`$ at the two endpoints before normalising. The first identity suffices term by term for finite polynomials in prime values. [Dahl and Kala, §3](https://arxiv.org/pdf/1611.02424) · [Earlier family tilt and moment transfer](https://github.com/leecrossley/yokoi-mertens-power-start-delays/blob/v1.0.2/PROOF.md)

Set $`V=X^{128}`$ and $`N=\lfloor D^{1/1000}\rfloor`$. Force all primes through $`B`$ to be inert, with indicator $`I=\prod_{p\le B}(Z_p(Z_p-1)/2)`$ and fixed model probability $`p_B>0`$. For $`p>B`$ prescribe the mean $`\nu_p=\mu_p+\Delta_p`$ where

```math
 \Delta_p=-\frac{\log p\log\log p}{\sqrt p}{\bf1}_{p\le4X}
           -A_0\frac{(\log p)^2}{\sqrt p}{\bf1}_{p\le4B}.
 \tag{2}
```

The extra fixed initial band ensures positivity at the small starts. Take $`A_0`$ a sufficiently large absolute constant, then $`B`$ sufficiently large. Under the full squared weight $`IR^2`$, $`R=\prod_{B<p\le4X}(1+a_p(Z_p-\mu_p))`$, the variables above $`B`$ remain independent with the indicated means. Indeed the shift is $`(2a v_p+a^2\mathbb E(Z_p-\mu_p)^3)/(1+a^2v_p)`$. On $`|a|\le1/16`$ its ratio to $`a`$ exceeds $`1/2`$ for $`p>B`$. Continuity gives $`|a_p|\le2|\Delta_p|`$. Partial summation of the ordinary prime count gives, up to additive constants depending on $`B,A_0`$,

```math
 \sum a_p^2\ll(\log X)^2(\log\log X)^2,\qquad
 \sum a_p^2\log p\ll(\log X)^3(\log\log X)^2.
 \tag{3}
```


Expand $`R`$ in squarefree centred monomials, and retain indices at most $`N`$ in $`R_N`$. Their orthogonality identifies the discarded fraction $`\varepsilon`$ of squared norm with the upper-tail probability of a product of independently selected primes, selection probabilities $`a_p^2v_p/(1+a_p^2v_p)`$. Exponential Markov at $`1/\log(4X)`$ gives

```math
 \varepsilon\le\exp\{[-\log N+(e-1)\sum a_p^2\log p]/\log(4X)\}.
```

Choose $`h_*=\lceil (K_0+6)\log(4V)\rceil+3`$. With sufficiently small $`c`$, (3) absorbs at most half the negative term, while $`h_*\log V\log(4X)=O_{K_0}((\log X)^3)=o(\log D)`$. Hence $`\sqrt\varepsilon\le V^{-100h_*}`$ eventually. Normalising the two model weights $`IR_N^2`$ and $`IR^2`$ changes expectations of bounded functions by $`O(\sqrt\varepsilon)`$ times their maximum, by Cauchy–Schwarz. The truncated model denominator is at least $`p_B/2`$.

## Simultaneous fluctuations for the reference characters

On real fields use the nonnegative weight $`W=IR_N^2`$, evaluating the polynomial at $`\chi_d(p)`$. For every interval of primes $`J\subset(B,V]`$, all deterministic coefficients $`|\alpha_p|\le1`$, and $`2\le h\le h_*`$, the weighted shell moment of

```math
 \left|\sum_{p\in J}\alpha_p(\chi_d(p)-\nu_p)/p\right|^{2h}
 \tag{4}
```

differs from the full tilted model moment by at most $`V^{-4h_*}`$ for real $`\alpha_p`$. Indeed $`R_N`$ has largest character index $`N`$ and sum of absolute expansion coefficients at most $`N^2`$. Each included monomial costs at most $`2^{\omega(n)}\le n`$. The two analogous bounds for the observable in (4) are $`V^{2h}`$ and $`(2V)^{2h}`$. The indicator is a fixed polynomial. Using (1) on the numerator and denominator costs $`O_B(D^{-1/6}N^{16/3}V^{O(h_*)}\log D)=O_B(D^{-1/8})`$. The denominator is at least $`p_B/3`$ after transfer. Its normalisation, and the model truncation error times $`(2V)^{2h_*}`$, fit the displayed moment tolerance since $`h_*\log V=o(\log D)`$. Deterministic character values do not enter the character *index* being averaged over fields.

In a dyadic block $`(z,2z]`$ above $`B`$, containing $`n_z\ll z/\log z`$ primes, each centred model summand has interval length at most $`2/z`$. The bounded-variable exponential moment inequality gives $`L^{2h}`$ norm $`O(\sqrt{h l}/z)`$ for a sum over $`l\ge1`$ consecutive primes. The additive error in (4) preserves this bound even when $`l=1`$. Pad the list of primes to a power of two with zeros. Every prefix uses at most one subinterval at each dyadic subdivision level. The $`L^{2h}`$ norm of the largest of the level-$`j`$ sums is $`\ll\sqrt{h n_z}\,2^{-j/2+j/(2h)}/z`$, by bounding the maximum power by the sum of powers. Minkowski and $`h\ge2`$ give the prefix maximum norm $`\ll\sqrt{h/(z\log z)}`$. [Hoeffding's estimate](https://doi.org/10.1080/01621459.1963.10500830)

Take $`h=\lceil(K_0+6)\log(4z)\rceil+2`$. Markov at $`e`$ times the norm makes the bad probability for each choice of $`\alpha`$ at most $`e^{-2h}`$. Take $`\alpha_p=\psi(p)`$ for every nonprincipal primitive quadratic character of conductor at most $`(4z)^{K_0}`$ and include the trivial character as well. There are at most $`2(4z)^{K_0}+1`$ choices. The union of bad events over these choices and all dyadic $`B\le z<V`$ has weight probability below $`1/4`$ for large fixed $`B`$. On the good event every such prefix sum of centred reciprocal primes is $`O_{K_0}(1/\sqrt z)`$. Differences of two prefixes control subintervals. Partial summation gives the same bound up to an absolute factor with any monotone weight in $`[0,1]`$. The same event handles every real start. A reference with $`q\le y^{K_0}`$ belongs to the tested set on every block meeting $`[y,V]`$.

For a nonprincipal $`\psi`$ in a block's bank, the deterministic mean has on each subinterval the bound

```math
 \left|\sum_{s\lt p\le t}\psi(p)\nu_p/p\right|\ll_{K_0,A_0}(\log z)^3/z .
 \tag{5}
```

The $`\mu_p`$ terms cost $`O(1/z)`$. For (2) use the prime estimate $`\sum_{p\le v}\psi(p)\log p\ll\sqrt v\log^2(3qv)`$ from quadratic GRH. Partial summation uses the functions $`(\log\log v)v^{-3/2}`$ and $`(\log v)v^{-3/2}`$, each with supremum plus variation $`O((\log z)z^{-3/2})`$ on a block. The two fixed cutoffs only trim the subinterval. The right side in (5) is $`O(1/\sqrt z)`$.

Summing the bounds over successive dyadic blocks gives $`O_{K_0}(1/\sqrt y)`$ for every twisted future sum through $`V`$, with the increasing weight $`(1-y/p)`$, and for the analogous **centred** untwisted sum. For every nonprincipal character $`\chi_d\psi`$, the tail after $`V`$ has size $`O((\log(3d q V))^2/\sqrt V)`$ by the same GRH prime estimate and partial summation. Local omissions in a product of two primitive quadratic characters cost at most $`O(\log(3dq)/(V\log V))`$ for the prime tail, by summing over prime divisors larger than $`V`$. This applies also to $`\chi_d`$ by itself. Here $`q\le X^{K_0}<d`$ eventually, so none of these products is principal, and the remainder is $`o(X^{-1/2})`$. This proves the twisted tail bound for $`y\ge B`$. For $`2\le y<B`$ the bound follows, on increasing the constant depending on $`B`$, by handling the fixed initial primes directly and using the same monotone weight on all blocks past $`B`$. Multiplying reciprocal terms by $`p\log p`$ via partial summation gives the claimed $`O_{K_0}(\sqrt x\log x)`$ on any subinterval of $`(x,2x]`$, covering by at most two dyadic blocks. [Critical-line prime estimates](https://arxiv.org/abs/1312.4463)

## Untwisted sign and count of fields

For $`B\le y\le X`$ all prescribed mean shifts have the same sign. On $`(2y,4y]`$ the future kernel is at least $`1/2`$, and the ordinary prime number theorem gives a contribution $`\gg\log\log y/\sqrt y`$ to minus the weak mean tail. The centred error above is $`O_{K_0}(1/\sqrt y)`$ and the $`\mu_p`$ contribution is $`O(1/y)`$. Thus $`-T_{d,1}(y)\gg\log\log y/\sqrt y`$ for sufficiently large $`B`$. Likewise the weak mean contributes $`\ll-\sqrt x\log x\log\log x`$ to the log-weighted untwisted sum on $`(x,2x]`$, the centred part there being $`O_{K_0}(\sqrt x\log x)`$.

Uniformly in $`d`$,

```math
 F_d(y)=-T_{d,1}(y)+O(1/(\sqrt y\log y)).
 \tag{6}
```

Indeed the field product at $`t`$ is the rational prime product times the character product through $`t`$, times $`\prod_{\sqrt t<p\le t,\ \chi_d(p)=-1}(1-p^{-2})`$. The last log costs $`O(1/(\sqrt t\log t))`$, and the difference between the logarithmic character tail and its linear part costs $`O(1/(t\log t))`$. Critical-line convergence justifies taking the Euler product at 1 in prime order and then averaging. The rational future average is $`O(1/(\sqrt y\log y))`$ under RH, by the integrated explicit formula or Cramér's mean estimate and partial summation. Pointwise, the rational log error costs $`O(\log t/\sqrt t)`$. [Integrated rational bound and factorisation, §1](https://github.com/leecrossley/yokoi-mertens-power-start-delays/blob/v1.0.2/PROOF.md) · [Integrated explicit formula](https://arxiv.org/abs/1312.4465). Equation (6) proves the asserted margin beyond $`B`$.

At $`t=B`$, use the untapered tail, with the same centred error. The extra tilt on $`(B,2B]`$ yields at least a constant times $`A_0\log B/\sqrt B`$ towards the raw $`B_d(B)`$. The pointwise rational estimate and the inert correction above are absolute. Choosing $`A_0`$ first and $`B`$ sufficiently large gives $`B_d(B)>5\log B/\sqrt B`$. With every prime through $`B`$ inert, the raw product $`P_d(B)`$ is at most $`\zeta(2)`$. For $`t\ge2`$, $`P_d(t)\ge\prod_{p\le\sqrt t}(1-p^{-2})^{-1}\ge\zeta(2)(1-1/\sqrt t)`$ by telescoping the omitted factors over integers. Since $`(1-t^{-1/2})/\log t=\int_0^{1/2}t^{-u}du`$ decreases, these estimates at $`B`$ imply $`B_d(t)>0`$ throughout $`[2,B]`$. For $`y<B`$ split the future integral at $`B`$. Its second part is $`(y/B)F_d(B)>0`$, and the first is nonnegative.

Finally $`\mathbb E_D W^2\ll_B\exp(C\sum a_p^2)`$. In the independent model expand $`R_N^4`$. A singleton prime has expectation zero. Take absolute values on terms without singletons and drop the truncations. The resulting Euler factors are $`1+O(a_p^2)`$ since centred signs have absolute value at most two. Transferring by (1) costs $`O_B(D^{-1/6}N^{32/3}\log D)=o(1)`$. Cauchy–Schwarz converts the good weighted probability into an unweighted fraction at least $`(3\mathbb E_D W/4)^2/\mathbb E_D W^2`$. The first estimate of (3) and the shell cardinality prove the count. The prime bias on these fields is visible without selecting a second character. It remains open whether reaching a fixed power of the discriminant changes this behaviour.
