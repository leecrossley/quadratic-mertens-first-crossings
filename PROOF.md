# How far beyond the first dip must a negative average reach?

Let $K=\mathbb Q(\sqrt d)$ with $d=m^2+4$ squarefree and $m$ odd and positive. Put $c_d=e^\gamma L(1,\chi_d)$, let $P_d(t)$ be the product of $(1-1/N\mathfrak p)^{-1}$ over all prime ideals with norm at most $t$, and put
$$
 B_d(t)=\log(P_d(t)/(c_d\log t)),\qquad J_d(T)=\int_2^T B_d(t)\,dt/t.
$$
The first crossing is $S_d=\inf\{t\ge2:B_d(t)<0\}$. Write $W_d=\inf\{T\ge2:J_d(T)<0\}$, with the empty infimum taken as infinity. A bounded nonnegative nonincreasing weight on $[2,\infty)$ gives a negative integral against $B_d(t)dt/t$ exactly when $W_d$ is finite. An indicator gives one direction. For the other, decompose the weight into its superlevel intervals and apply Fubini. A negative integral with constant weight on the full half-line also has a finite negative prefix. The absolute convergence needed here follows from the quadratic prime ideal theorem quoted in §2. [Decreasing weights, §1](https://github.com/leecrossley/yokoi-mertens-optimal-starts/blob/v1.0.0/PROOF.md)

Let $A_*$ denote the least possible integral $\int_2^\infty B(t)\,dt/t$ over everywhere nonnegative errors obtained from admissible local splitting patterns and positive benchmarks. This finite strictly positive constant is the increasing limit of the analogous minima $A_X$ on $[2,X]$. Any pattern positive through $X$ has built up at least that much area. For every $\eta>0$ there is a fixed infinite positive pattern with area below $A_*+\eta$ and $0\le B(e^v)\ll_\eta v^{-2}$ for all large $v$. Indeed, truncate a near-minimiser at a good point with small endpoint error, lower its benchmark as in the positive continuation proof, and extend it. Only a fixed finite initial set of primes can be ramified in this extension. [Definition and compactness](https://github.com/leecrossley/mertens-power-average-deadlines/blob/v1.0.0/SLOW-WEIGHTS.md) · [Positive continuation](https://github.com/leecrossley/mertens-power-average-deadlines/blob/v1.0.0/PATHS.md)

**Theorems.** The following statements concern actual fields.

1. As $S_d\to\infty$ over fields with $W_d<\infty$, the lower limit of $\log(W_d/S_d)/\sqrt{\log S_d}$ is exactly $\sqrt{2A_*}$. For each individual such field with $S_d>2$ there is the finite inequality $\log(W_d/S_d)\ge\sqrt{2A_{S_d}\log S_d}$.
2. Put $L=\log\log d$. For every $\kappa<2\sqrt{2A_*}$ and all sufficiently large fields with $W_d<\infty$,
$$
 S_d\le(\log d)^2\exp(-\kappa\sqrt L).
 \tag{1}
$$
In particular the finite certificate $A_*>0.4829182931$ permits $\kappa=1.965$. This improves the previous $O((\log d/\log\log d)^2)$ bound for fields admitting a decreasing average at 2.
3. Conversely, for every $\kappa>2\sqrt{A_*}$, set $L=\log\log D$ and $N=(\log D)\exp(-\kappa\sqrt L)$. In each sufficiently large shell $D/2<d\le D$ there are at least $D^{1/2-o(1)}$ such fields with $N<S_d=N(1+O_\kappa(1/\log N))$ and $W_d<\infty$. In these fields all power averages starting at 2 with $0<s\le\lambda_\kappa/L$ are strictly negative, for some $\lambda_\kappa>0$. Thus the earliest possible start works in a large set of examples with a first crossing this late. The exponents one and two on $\log d$ in the lower and upper statements are distinct.

The first assertion and the finite-prefix construction in the third use classical results on primes and residues in the family. The upper conductor bound and the estimate for the infinite tail of the simultaneous power averages use the ordinary and quadratic critical-line estimates indicated below.

## 1. A one-sided bound and its sharpness

Suppress the field index. Up to $S$ the error is nonnegative, including the limiting benchmark at $S$. Thus $J(S)\ge A_S$, and monotonicity of $P$ gives
$$
 B(Se^w)\ge-\log(1+w/u)\ge-w/u,\qquad u=\log S,\quad w\ge0 .
$$
Consequently $J(Se^h)\ge A_S-h^2/(2u)$ for $h\ge0$. Taking the infimum over negative endpoints gives the stated finite inequality. Its limiting coefficient is at least $\sqrt{2A_*}$.

For sharpness choose any $b>\sqrt{2A_*}$ and a positive infinite pattern with benchmark $c$ and total area $A<b^2/2$, as above. For each large $u$ retain this pattern through $N=e^u$ and set all new primes inert through $T=e^{u+b\sqrt u}$. At $N$ the original error is $O(u^{-2})$. The total log jump over the new interval is $O(e^{-u/2})$ because only inert prime squares can arrive. Uniformly on $0\le w\le b\sqrt u$ the error is
$$
 O(u^{-2})-\log(1+w/u)+O(e^{-u/2}).
$$
The signed area on this interval tends to $-b^2/2$, by integrating the expansion $\log(1+w/u)=w/u+O(w^2/u^2)$. Condition the benchmark to lie between $c\exp(-2/u^2)$ and $c\exp(-1/u^2)$. This keeps the whole prefix strictly positive and perturbs its integral through $T$ by $O(1/u)$. The error is strictly negative by $w=C/u$ for some fixed sufficiently large $C$. The area up to $T$ is negative. Every prescribed sign pattern through the finite $T$ together with this open benchmark interval occurs in infinitely many actual fields, by the joint local support theorem. In these fields $N<S\le Ne^{C/u}$ and $W\le T$. Sending $u$ to infinity and $b$ down to $\sqrt{2A_*}$ proves sharpness. [Family support with the residue, §3](https://github.com/leecrossley/mertens-power-average-deadlines/blob/v1.0.0/PROOF.md)

## 2. A smaller worst case in terms of the discriminant

Put $R=(\log d)^2 L^4$ with $L=\log\log d$. For $R$ sufficiently large the real quadratic bounds
$$
 |B_d(R)|\ll(\log d+\log R)/\sqrt R,\qquad
 J_d(t)-J_d(R)\ge-2(9+3\log d)/(\sqrt R\log R)\quad(t\ge R)
 \tag{2}
$$
give $|B_d(R)|\ll L^{-2}$ and a possible future loss $O(L^{-3})$. The first estimate follows by partial summation of the prime ideal theorem. The second follows by integrating the quadratic explicit formula. Its constant is uniform in $d$. [Derivation, §2](https://github.com/leecrossley/yokoi-mertens-optimal-starts/blob/v1.0.0/PROOF.md) · [Grenié and Molteni](https://arxiv.org/abs/1312.4463) · [Critical-line verification](https://math.mit.edu/~drew/grh/)

Suppose $W_d<\infty$. Some endpoint has negative $J_d$. Truncating it at $R$ gives an endpoint $T\le R$ with $J_d(T)\le O(L^{-3})$. If $S_d\ge R$, a negative endpoint would be beyond $R$ and $J_d(R)\ge A_R$ would contradict (2). Hence $S_d<R$. If the negative endpoint lies before $R$ it lies after $S_d$. In all cases we may use a $T$ in $[S_d,R]$ with the asserted upper bound.

Write $S=S_d$, $u=\log S$ and $h=\log R-u$. To prove (1) it suffices to treat sequences failing the proposed bound, for which $u\sim2L$ and $h=O(\sqrt u)$. For $0\le w\le h$ we have
$$
 B_d(Se^w)\ge-w/u,\qquad
 B_d(Se^w)\ge -(h-w)/u-O(L^{-2})-O(e^{-c_1\sqrt u})
 \tag{3}
$$
with an absolute $c_1>0$. The first inequality was proved in §1. For the second, an upper bound for the log growth of $P_d$ between $t=Se^w$ and $R$ consists of two factors at every rational prime in $(t,R]$ and all possible delayed inert squares after $t$. The latter cost $O(t^{-1/2})$. Partial summation of the effective ordinary prime number theorem bounds the former by $2\log(\log R/\log t)+O(e^{-c_1\sqrt u})$, reducing $c_1$ if needed. Subtract the growth of the benchmark and use $B_d(R)=O(L^{-2})$. Finally $\log(\log R/\log t)\le(h-w)/u$. [Ordinary prime number theorem with error](https://arxiv.org/abs/2204.01980)

Integrating the negative part of (3) over any subset of this interval costs at most
$$
 \int_0^h \min(w,h-w)\,dw/u+o(1)=h^2/(4u)+o(1).
$$
At least $A_S-o(1)$ must be lost by the endpoint $T$. Hence $h\ge(2\sqrt{A_*}-o(1))\sqrt u$. As $\log R=2L+4\log L$ this proves (1).

## 3. Many fields with a late first dip and a successful start at 2

The construction and count are given in [FAMILY.md](FAMILY.md). It first keeps a positive pattern through $N$, then leaves all new primes inert, then makes all new primes split until the benchmark is recovered. A successful average requires enough negative area to absorb the positive prefix. The two parts of the dip together provide $b^2+o(1)$ of negative area with a log length of $2b\sqrt{\log N}+O(1)$. The count keeps the residue within $o((\log N)^{-2})$ of its predicted value even after fixing every prime through that recovery point.
