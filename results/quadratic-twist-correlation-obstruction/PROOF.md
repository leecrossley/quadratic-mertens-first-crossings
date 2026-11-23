# A positive prime model that passes every fixed quadratic twist test

Lee Crossley

For an assignment $`\eta(p)\in\{-1,0,1\}`$ on ordinary primes extend it completely multiplicatively and put

```math
 V_\eta(y)=\sqrt y\log y\sum_{p>y}\eta(p)(1-y/p)/p.
```

Assign two local prime-ideal norms $`p`$ at sign $`+1`$, one norm $`p^2`$ at $`-1`$, and one norm $`p`$ at 0. Put $`\ell(v)=-\log(1-1/v)`$ and

```math
 F_\eta(y)=\int_y^\infty\left[\sum_{v\le t}\ell(v)-\gamma
                      -\log L_\eta(1)-\log\log t\right]\frac{y\,dt}{t^2}.
```

The Euler product for $`L_\eta`$ starts on $`\Re s>1`$. Its ordinary ordered log product at 1 converges in this construction. Use RH and quadratic Dirichlet GRH, including the quadratic characters used to count primes in the construction.

**Theorem.** There are arbitrarily large $`P`$, with scale $`D=13e^{2P}`$, such that the following construction works. Choose $`0\le\theta<\pi/3`$ and any finite $`H\ge P`$. There is one real assignment $`\xi`$ on the primes for all the tests below. Write $`N_y=\sqrt y\log y`$.

* At $`\theta=0`$, $`N_yF_\xi(y)>1/100`$ for every $`y\ge2`$, and the untwisted product has a double central zero. At $`\theta>0`$ it has a pair at heights $`\pm\theta/P`$ and the same inequality holds for $`2\le y`$ with $`\log y\le P(\pi/(3\theta)-2)`$. The interval contains a start precisely when $`\theta\le\pi/[3(2+(\log 2)/P)]`$. It includes any prescribed power of $`D`$ on choosing $`\theta`$ sufficiently small.
* For each fixed nonprincipal primitive quadratic $`\psi`$ one has $`|V_{\xi\psi}(y)|=O_\psi(1)`$ throughout $`2\le y\le e^H`$ for all sufficiently large $`P`$. Uniformly at sufficiently large starts with $`q=\mathrm{cond}\psi\le(\log y)/2`$ the bound there is $`O(\log(3q))`$. Nonetheless $`V_\xi(e^P/3)=-4(\cos\theta)P/(3\sqrt3)+O(1)`$. Taking $`H=P^2`$ works simultaneously through every fixed power of $`D`$ eventually.
* The products for the trivial character and every fixed nonprincipal twist continue to $`\Re s>1/4`$. Their specified extra zeros lie on the critical line. Counting positive ordinates with multiplicity, each has the degree-one zero-count main term

```math
 \frac{T}{2\pi}\log\frac{\mathcal C_\psi T}{2\pi e},
 \qquad \mathcal C_\psi=\frac{Dq}{\gcd(13,q)^2}
```

with error $`O(\log(3q(T+2))+k)`$ as $`T\to\infty`$, where $`k`$ is the number of shorter periods in the construction. The twist by $`\chi_{13}`$ is nonzero at the centre. This factor is the usual conductor ratio for an odd quadratic discriminant $`d`$ with $`\gcd(d,q)=\gcd(13,q)`$.
* There is also a version in which every twist's extra sequence of prime packets starts at its first nonzero coefficient. In that version $`|V_{\xi\psi}(y)|\ll_\psi\sqrt{P\log P}`$ through each fixed power of $`D`$, or $`O(\log(3q)+\sqrt{P\log P})`$ for the growing set $`q\le(\log y)/2`$, $`\log y\le cP\log P`$ with absolute $`c>0`$. Both versions have zero limiting prime-sign correlation with every fixed nonprincipal quadratic character. For a fixed $`\psi`$ this means the average of $`\xi(p)\psi(p)`$ over primes up to $`x`$ tends to zero as $`x\to\infty`$.

Here $`D`$ is a scale parameter. The products have the stated zero counts. A quadratic field also has periodic prime characters and completed functional equations for the field and its twists. The implication for genuine Yokoi fields through $`d^a`$ remains open.

## Redistributing the prime signs without losing the base average

Let $`\chi_e`$ be the primitive quadratic character of fundamental discriminant $`e`$. For a primitive real quadratic reference $`\psi`$, including the trivial character, let $`\rho_\psi`$ be the primitive character inducing $`\chi_{13}\psi`$, except that $`\rho_{\chi_{13}}=\chi_{17}`$. Thus every target is nonprincipal, $`\rho_1=\chi_{13}`$, and $`\mathrm{cond}(\rho_\psi)\le\max(17,13q)`$. A character on the units modulo a multiple of its conductor uses the target of its primitive representative.

Choose a large dyadic $`X_0`$. Retain the actual $`\chi_{13}`$ values through $`X_0`$. In each subsequent dyadic shell $`(x,2x]`$ set $`M=\mathrm{lcm}(1,\ldots,\lfloor\log x\rfloor)`$, $`G=(\mathbb Z/M)^\times`$, and let the $`h`$ square classes be the elements of $`G/G^2`$. There are $`h`$ real characters of this quotient. The bound $`\log M=O(\log x)`$ follows from Chebyshev's estimate, and $`h\le4\cdot2^{\pi(\log x)}=x^{o(1)}`$ by the square-class count at each prime power. Successive moduli are nested. Put

```math
 L_x=\sqrt x\,h(\log x)^8=x^{1/2+o(1)}
```

and divide the shell into $`\lfloor x/L_x\rfloor`$ equal bins. Each has length between $`L_x`$ and $`2L_x`$ eventually. On a bin $`(b,b+l]`$ write $`t_p=(p-b)/l`$.

In **each quarter** of a bin every square class $`C`$ contains $`\asymp L_x/(h\log x)`$ primes, uniformly. Its indicator on units is $`h^{-1}\sum_\psi\psi(C)\psi(p)`$. The principal term yields its length divided by $`h`$ in the log-weighted count. Each character's endpoint error is $`O(\sqrt x\log^2(3Mx))`$ by RH and quadratic GRH, including the ordinary prime estimate. The averaged errors fit inside the main term. All primes in the shell exceed every prime divisor of $`M`$.

For $`j=0,1`$ prescribe in class $`C`$ the two moments

```math
 t_{C,j}=\frac1h\sum_\psi\psi(C)\sum_{p\ {\rm in\ bin}}\rho_\psi(p)t_p^j .
```

Each target has size $`O(\sqrt x\log^2(3Mx))`$ by the nonprincipal prime estimate and partial summation. Choose a fractional sign $`f_p=A_C+B_Ct_p`$ to realise both moments in that class. The two-by-two Gram matrix is $`\sum(1,t_p)^{\!T}(1,t_p)`$, interpreting $`(1,t_p)`$ as a row. Its trace is at most $`2n_C`$ and its determinant is $`\sum_{i<j}(t_i-t_j)^2\gg n_C^2`$ by the outer quarters, where $`n_C\asymp L_x/(h\log x)`$ counts the class. Inverting shows $`|A_C|+|B_C|\le1/2`$ eventually, uniformly in the bin and class. Character orthogonality now gives

```math
 \sum_{p\ {\rm in\ bin}} [f_p\psi(p)-\rho_\psi(p)]t_p^j=0
                    \qquad (j=0,1)
 \tag{1}
```

for every captured character.

Round throughout each *whole shell*, within each class in prime order. With $`r_i=(1+f_i)/2`$, give the $`i`$th prime sign $`2(\lfloor\sum_{j\le i}r_j\rfloor-\lfloor\sum_{j<i}r_j\rfloor)-1`$. The result, $`\eta`$, has actual signs $`\pm1`$ with every prefix discrepancy from $`f`$ in that class bounded by 2. Thus any captured twist has prefix rounding discrepancy at most $`2h`$ on the shell. Also both old signs occur at least $`n/4-O(1)`$ times on an interval of $`n`$ primes in one class. These assertions follow from telescoping and $`|f|\le1/2`$.

For a twice differentiable weight $`g`$ on a shell, (1) bounds its fractional discrepancy, summed over any union of whole bins, by $`O(xL_x^2\|g''\|_\infty)`$ using Taylor's theorem and at most $`2x`$ primes. Rounding costs $`O(h(\|g\|_\infty+x\|g'\|_\infty))`$ uniformly on an interval. For a continuous piecewise smooth weight with one kink the single affected bin costs an additional $`O(L_x^2\|g'\|_\infty)`$, since matching the constant still suffices there. These bounds also apply to a smooth compactly supported function extended by zero. The constants in derivative estimates can be taken separately on either side of the kink.

Taking $`g(p)=p^{-s}`$ gives a dyadic discrepancy $`O_{\mathcal K,\epsilon}(x^{-\Re s+\epsilon})`$ for every $`\epsilon>0`$ locally on compact sets $`\mathcal K`$. For each fixed $`\psi`$ all sufficiently large shells capture it. Grouped by shells, $`\sum_p(\eta(p)\psi(p)-\rho_\psi(p))p^{-s}`$ continues holomorphically to $`\Re s>0`$, agreeing with the Euler series in its initial half-plane. At $`s=1`$ the ungrouped series has the same limit because a partial terminal bin costs $`O(L_x/x)`$ and all earlier whole bins satisfy the same Taylor bound. Even powers in the log Euler ratio agree off finite ramification. Each odd power uses the same linear series at $`ks`$. For a compact sub-half-plane the sufficiently high powers converge absolutely. Finite local factors are nonzero in $`\Re s>0`$. This proves

```math
 L_{\eta\psi}(s)=L(s,\rho_\psi)\exp G_\psi(s),\qquad \Re s>0,
 \tag{2}
```

for a holomorphic $`G_\psi`$ there. For a fixed smooth bump $`\varphi`$ supported in $`(1,2)`$, the choice $`g(p)=\log p\,\varphi(p/z)`$ gives smoothed discrepancy $`O_{\varphi,\epsilon}(z^\epsilon)`$ whenever the conductor is captured on the intersecting shells. This follows from the same bounds on at most two shells. The reference $`\rho_\psi`$ has smoothed prime sum $`O_\varphi(\sqrt z\log(3q))`$ under GRH, by Mellin inversion, rapid transform decay and the standard unit-interval zero count.

For the average use $`b_y(v)=(1-y/v)_+`$. The exact change from field 13 is

```math
 F_\eta(y)-F_{13}(y)=-\sum_{p>X_0}(\eta(p)-\chi_{13}(p))
           [\ell(p)b_y(p)-\tfrac12\ell(p^2)b_y(p^2)] .
 \tag{3}
```

An averaged local jump contributes $`\min(1,y/v)`$ and the change in normalisation subtracts the complete local log factors. The ordered products converge as above. On a shell of size $`x`$, the $`j`$th derivatives ($`j=0,1,2`$) of the two weights away from their kinks cost respectively $`O(x^{-1-j})`$ and $`O(x^{-2-j})`$. The linear weight vanishes for $`y\ge2x`$ and the square weight for $`y\ge4x^2`$. The preceding shell estimates therefore bound their two discrepancies by $`O_\epsilon(x^{-1+\epsilon})`$ and $`O_\epsilon(x^{-2+\epsilon})`$. Multiply by $`\sqrt y\log y`$ on each support and sum dyadically from $`X_0`$. The supremum of the normalised difference over **all** $`y\ge2`$ tends to zero as $`X_0\to\infty`$. Fix $`X_0`$ so large that $`\sqrt y\log y\,F_\eta(y)>1/50`$ everywhere, using the previously certified $`1/40`$ bound for field 13. [Corrected base proof and its two certificates](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-positive-averages-5-13/PROOF.md)

The same derivative estimates with $`g(p)=p^{-1}b_y(p)`$ show that $`V_{\eta\psi}(y)=V_{\rho_\psi}(y)+O_\epsilon(y^{-1/2+\epsilon})`$, uniformly for $`y\ge2X_0`$ with $`q\le(\log y)/2`$. For fixed $`\psi`$ the remaining compact interval costs $`O_\psi(1)`$. For a nonprincipal primitive quadratic character $`\rho`$ of conductor $`q'`$ the integrated prime-power formula gives $`|V_\rho(y)|\ll\log(3q')`$ for all $`y\ge2`$. Indeed the kernel of each nontrivial ordinate $`\lambda`$ has absolute value at most $`(1/4+\lambda^2)^{-1}`$. The paired logarithmic derivative at 2 bounds their total by $`O(\log(3q'))`$. The trivial-zero density is uniformly bounded in the integrated formula for either parity on $`\log y\ge\log2`$. The squares cost $`O(1)`$ after normalisation by the ordinary prime count. Powers of order at least three cost $`O(\sqrt y\log y\,y^{-2/3})`$. [Integrated kernel and prime powers](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/ef3e53c/results/signed-prime-tails/PROOF.md)

## Assigning the extra zeros of the twists

Let $`\lambda=(\log17)/2`$. Choose $`k`$ distinct primes $`\ell_1<\cdots<\ell_k`$ between $`2k\log k`$ and $`5k\log k`$ as $`k\to\infty`$, possible by the prime number theorem. Write $`S=\sum_i\ell_i`$ and $`P=\lambda S`$. Thus $`P\asymp k^2\log k`$, $`\ell_k\ll\sqrt{P\log P}`$ and $`\ell_1^2\gg P\log P`$. The periods in log-prime coordinates are $`\lambda`$ times these integers. Use the list $`I=(\ell_1,\ldots,\ell_k)`$ for ordinary secondary tests and $`I'=(\ell_1-1,\ell_2,\ldots,\ell_k)`$ for the twist by 13.

For $`t_n=\lambda n`$ and positive integers $`n`$ define

```math
 A_n={\bf1}_{S\mid n}\,P\cos((n/S)\theta),\qquad
 b_n(J)=\lambda\sum_{v\in J,\ v\mid n}v\cos((n/v)\pi/2).
```

In the version that starts immediately put $`B_n=b_n(I)`$, $`E_n=b_n(I')`$. To impose the bound through $`e^H`$, put both coefficients equal to zero when $`t_n<2H`$ and use the same values thereafter. Leave $`A_n`$ as written. This finite change can be arbitrarily long, depending on $`P`$. It preserves the analytic zeros of each product as shown below.

Skip any index with three zero quotas. At $`X=e^{t_n}`$ use a packet $`[X,X+X^{3/4}]`$ with the square classes of the dyadic shell containing $`X`$ (at a boundary use the shell to the right). The earlier choice of $`X_0`$ captures $`\chi_{13}`$ on all these shells for large $`k`$. Write $`C_0=G^2`$ for the identity square class. Assign signed quotas

```math
 w_C=(A_n-B_n)/h+B_n{\bf1}_{C=C_0}+(E_n-B_n)\chi_{13}(C)/h.
 \tag{4}
```

Character orthogonality gives total $`A_n`$. Weighting by any captured nonprincipal character gives $`B_n`$ except at $`\chi_{13}`$, where it gives $`E_n`$. In each class reverse the first $`\lfloor |w_C|\sqrt X/t_n\rfloor`$ primes whose old sign is $`\mathrm{sgn}w_C`$. Zero quota requires no primes. The total count is at most $`5P\sqrt X/t_n`$. The class has $`\gg X^{3/4}/(h\log X)`$ primes in the packet by the preceding character estimate. If the packet crosses a dyadic boundary, the rounding error for a coarser class in the second shell costs at most twice the new number of classes on its prefix. Hence either old sign is available on at least a quarter of the class count, up to $`X^{o(1)}`$. This exceeds each quota since the first possible index with a nonzero quota is $`n\ge\ell_1-1`$, $`P\ll n^2`$, and $`h=X^{o(1)}`$. The packets are disjoint. Each signed old mass differs from $`\sqrt X/t_n`$ times its prescribed coefficient by at most $`h`$.

Write $`Q_{\alpha,v}(s)=1-2\cos\alpha\,e^{-v(s-1/2)}+e^{-2v(s-1/2)}`$. On $`\Re s>1/4`$ the products are

```math
 L_\xi(s)=L(s,\chi_{13})Q_{\theta,P}(s)e^{J_1(s)},\qquad
 L_{\xi\psi}(s)=L(s,\rho_\psi)\prod_{v\in I_\psi}Q_{\pi/2,\lambda v}(s)e^{J_\psi(s)}
 \quad(\psi\ne1),
 \tag{5}
```

where $`I_{\chi_{13}}=I'`$, the other $`I_\psi=I`$, and each $`J`$ is holomorphic. Each flip contributes minus twice its old twisted sign in the linear term of the log Euler ratio from (2). Replacing $`p^{-s}`$ by $`X^{-s}`$ in a packet costs $`O_{\mathcal K}(PX^{1/4-\sigma}/t_n)`$ on compact sets with $`\Re s\ge\sigma>1/4`$. Rounding costs $`O(hX^{-\sigma})`$, higher odd powers cost $`O_\sigma(PX^{1/2-3\sigma}/t_n)`$, and even powers agree. All errors are locally summable. For fixed $`\psi`$, the finitely many uncaptured packets contribute holomorphic log corrections. The full main logarithm of a grid of period $`v`$ is $`-2\sum_{j\ge1}\cos(j\alpha)e^{-jv(s-1/2)}/j`$ in its half-plane of absolute convergence. Omitting finitely many of its coefficients changes this logarithm by an entire finite sum of exponentials. This proves (5) for both versions.

Each grid has ordinates $`(2\pi j\pm\alpha)/v`$ with multiplicity and positive-height count $`vT/\pi+O(1)`$. The underlying primitive Dirichlet function contributes the standard main term with its own conductor. For every $`\psi\ne\chi_{13}`$ the base conductor is $`13q/\gcd(13,q)^2`$ and the extra periods sum to $`P`$. For $`\psi=\chi_{13}`$ the base has conductor 17 and the periods sum to $`P-\lambda`$. Since $`17e^{2(P-\lambda)}=e^{2P}=D/13`$, this gives the stated conductor dependence in that case as well. The standard error in the Dirichlet zero count is $`O(\log(3q(T+2)))`$, and counting the grids adds $`O(k)`$. The base $`L(s,\chi_{13})`$ has a central gap. For its special twist, $`0.7216<L(1/2,\chi_{17})<0.7218`$ and the shifted grids avoid zero. [Quadratic zero count](https://arxiv.org/abs/2005.02989) · [Base gap](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-positive-averages-5-13/PROOF.md) · [Conductor 17 check](CHECKS.md)

## Positive averages and small secondary correlations

Write $`u=\log y`$ and

```math
 S_C(u)=\sum_{t_n\ge u} C_n e^{-(t_n-u)/2}(1-e^{-(t_n-u)})u/t_n .
```

Uniformly in $`y,\theta,H`$ as $`k\to\infty`$,

```math
 N_y(F_\xi-F_\eta)=2S_A(u)+o(1),\qquad V_\xi(y)-V_\eta(y)=-2S_A(u)+o(1).
 \tag{6}
```

For the twisted prime sum replace $`A`$ by the appropriate $`B`$ or $`E`$ if the contributing packets are captured. This includes all $`y\ge2`$ for a fixed $`\psi`$ and sufficiently large $`k`$, and all sufficiently large $`y`$ with $`q\le(\log y)/2`$ for all sufficiently large $`k`$. A packet meeting the future then has $`t_n\ge u-O(e^{-t_n/4})`$. Each flipped prime contributes its old sign times $`2\ell(p)b_y(p)-\ell(p^2)b_y(p^2)`$ to the change of $`F`$. The prime-tail change instead uses $`-2p^{-1}b_y(p)`$. The linear functions are $`O(X^{-1})`$-Lipschitz in $`\log p`$ and have $`N_y\ll t_n\sqrt X`$ on their support. Collapsing the packet costs $`O(PX^{-1/4})`$, replacing $`\ell(X)`$ by $`1/X`$ costs $`O(P/X)`$, and rounding costs $`O(t_nh/\sqrt X)`$. The square term costs $`O(P/\sqrt X)`$ since it vanishes for $`y>(X+X^{3/4})^2`$. Summing from $`n\ge\ell_1-1`$ makes the errors $`o(1)`$, including cutoffs inside packets. [Earlier single-period calculation](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/quadratic-prime-disagreement-model/PROOF.md)

At $`\theta=0`$ all terms of $`S_A`$ are nonnegative. Below the asserted near-pair horizon, the first two cosines from $`j_0=\lceil u/P\rceil`$ on the $`P`$ grid are both at least $`1/2`$. Relative to the unsigned weight at $`j_0+1`$, the absolute tail from $`j_0+2`$ is bounded by $`e^{-P/2}/[(1-e^{-P/2})(1-e^{-P})]<1/2`$. Thus $`S_A\ge0`$ there also. The fixed base margin proves the claim. Given $`a>0`$ take $`0<\theta<\pi/[3(2a+3)]`$. At $`u=P-\log3`$ the first term of $`S_A`$ is $`2(P-\log3)\cos\theta/(3\sqrt3)`$ and the rest costs $`O(Pe^{-P/2})`$. The bounded base tail yields the untwisted value.

In the postponed version, $`|B_n|,|E_n|\le P`$ and either vanishes for $`t_n<2H`$. Therefore on $`u\le H`$ both corresponding $`|S_C(u)|`$ are at most $`Pe^{-H/2}/(1-e^{-\lambda/2})`$. Combined with the base estimate, this proves the fixed-character and uniform small-conductor bounds.

In the immediate version, for $`n<\ell_1^2`$ at most one prime in $`I`$ divides $`n`$. In $`I'`$ at most one of $`\ell_2,\ldots,\ell_k`$ and the additional $`\ell_1-1`$ can divide $`n`$. Hence both absolute coefficients are bounded by $`2\lambda\ell_k`$ there and by $`P`$ everywhere. For $`u\le\lambda\ell_1^2/2`$ their respective $`|S_C(u)|`$ are at most $`(2\lambda\ell_k+Pe^{-\lambda\ell_1^2/4})/(1-e^{-\lambda/2})`$. This proves the uniform $`O(\sqrt{P\log P})`$ contribution through the stated range.

Finally a smooth bump $`\varphi`$ supported in $`(1,2)`$ can meet only a bounded number of packets on a dyadic prime interval $`(x,2x)`$. Replacing $`\log p\,\varphi(p/x)`$ by its value at $`e^{t_n}`$ costs $`O_\varphi(Px^{1/4})`$ and rounding costs $`O_\varphi(h\log x)`$. The signed main change per packet in a captured nonprincipal twist is $`O_\varphi(P\sqrt x)`$ at all scales. With the base estimate, each fixed nonprincipal twist has weighted smooth prime sum $`O_{\psi,\varphi}(P\sqrt x)`$ for each fixed assignment. Smooth approximation and the ordinary prime number theorem therefore give zero mean for sharp prime counts as well.

The finite change in the twisted coefficients is permitted because the model only prescribes a continuation and its zeros. A genuine field ties the continuation to its Euler factors by a full functional equation. The model can reproduce the conductor term in the zero count and still lacks that identity. Different secondary twists also share many added zeros here.
