# The sharp small-exponent law for the Yokoi family

Fix the earliest possible start $y=2$. Let $M(s)=\mathcal S(2,s)$ be the supremum of the first crossing over actual squarefree Yokoi fields with $F_{d,s}(2)<0$, using the normalisation and strict inequalities in the [main proof](PROOF.md). As $s\downarrow0$ this supremum grows without bound. Its logarithm satisfies

$$
 s\log M(s)=\log(1/s)-\log\log(1/s)-\log A_\ast+o(1).
 \tag{6}
$$

Here $A_\ast$ is a positive finite extremal area specified below, independent of $s$. Thus even the sign of an average starting at 2 allows very late fields when the exponent is allowed to approach zero. The asymptotic in (6) lets the field vary with $s$. It gives no upper bound for an individual field whose average at 2 has positive sign.

## 1. An extremal area

For an assignment $\sigma$ of allowed Yokoi local signs at every prime, form the product $P_\sigma$ using the prime-ideal norm rule. For $c>0$ put $B_{\sigma,c}(t)=\log(P_\sigma(t)/(c\log t))$. Define

$$
 A_\ast=\inf_{\sigma,c:\ B_{\sigma,c}(t)\ge0\text{ for every }t\ge2}
           \int_2^\infty B_{\sigma,c}(t)\thinspace dt/t .
 \tag{7}
$$

The definition refers to local patterns. It permits an assignment that is not itself the full character of any one field. The local-support argument in §3 below transfers the needed finite portions to genuine fields.

No family product has a jump on $[2,3)$. Nonnegativity implies $1\ge c\log3$ by taking the left limit. Consequently $A_\ast\ge\int_2^3\log(\log3/\log t)\thinspace dt/t>0$.

To see that a positive path of finite area exists, work in the log coordinate $u=\log t$. On intervals from $u$ to $u+1/u$, choosing which new primes split can keep the error just above $2/u^2$. The effective ordinary prime number theorem supplies enough primes in every such interval, and the forced later jumps at inert squares cost an exponentially small amount. The resulting error is integrable. The construction also proves $0\le A_\ast-A_L\ll (1+A_\ast^2)/\log L$ for the finite minima below. [Positive continuation and the convergence rate](PATHS.md)

In fact the infimum is a minimum. Along a minimising sequence the same compactness applies. The upper bound on $c$ follows from $t<3$, and bounded area on $[2,3]$ keeps $c$ away from zero. Extract the finite-sign limits and a converging $c$, then apply Fatou's lemma to nonnegative errors. Equivalently $A_\ast$ is the increasing limit of finite minima $A_L$ for the same constrained area on $[2,L]$. For each finite pattern through $L$ the optimal $c$ is the largest compatible benchmark, the infimum of $P_\sigma(t)/\log t$ on that interval. It is computed by the left limits at jumps and the last endpoint. Monotonicity and $A_L\le A_\ast$ are immediate by restriction. Applying the same compactness to minimisers as $L\to\infty$ proves the reverse limiting inequality.

## 2. Upper bound from the future loss

Define

$$
 k(v)=\int_0^\infty e^{-w}/(v+w)\thinspace dw,\qquad k(v)\sim1/v\quad(v\to\infty).
$$

For $N>2$ put $v=s\log N$. The weighted mean of $\log(\log t/\log N)$ on $[N,\infty)$ equals $(2/N)^s k(v)$, by the substitution $w=s\log(t/N)$ and integration by parts. Suppose $F_{d,s}(2)<0$ while there is no negative point on $[2,N)$. The product is nondecreasing, so for $t\ge N$ its error is at least $-\log(\log t/\log N)$. Therefore

$$
 s A_{s,N}<2^s e^{-v} k(v),\qquad
 A_{s,N}=\int_2^N (2/t)^s B_d(t)\thinspace dt/t\ge0.
 \tag{8}
$$

Write $q=\log(1/s)$. For $s\le1$, $N\ge3$, the area $A_{s,N}$ is at least a positive absolute constant by the first interval in §1 and $(2/3)^s\ge2/3$. Thus if $v\to\infty$, (8) gives $v+\log v\le q+O(1)$. For an upper limit in (6) it suffices to consider sequences with $v\ge q-\log q-C$ for a fixed $C$. All other sequences with the centred expression tending to minus infinity satisfy the required upper bound directly. Here $v/q\to1$ and (8) gives $A_{s,N}=O(1)$.

Along each such sequence, $\liminf A_{s,N}\ge A_\ast$. To see this take a subsequence attaining the lower limit. The first interval again keeps $c_d$ both bounded and bounded away from zero. Extract a limit of the benchmarks and local signs. On any fixed $[2,L]$, eventually $N>L$, $(2/t)^s\to1$ uniformly, and the products agree with the limiting pattern. The limiting error is nonnegative, and its integral on $[2,L]$ is at most $\liminf A_{s,N}$. Send $L$ to infinity and use (7). Now (8), $vk(v)\to1$ and $\log v=\log q+o(1)$ imply

$$
 \limsup (v-q+\log q)\le-\log A_\ast .
$$

For each $s$ the supremum $M(s)$ is finite by the integer comparison. Taking fields and survival endpoints approaching that supremum gives the same bound for $v=s\log M(s)$. Small bounded $N$ cannot affect this upper limit.

## 3. Matching lower bound in actual fields

Choose a minimising path $\sigma,c$ from §1. Fix $\delta>0$, take $s$ small and set $v=q-\log q-\log A_\ast-\delta$. There exists a regular point $N$ with

$$
 v/s\le\log N\le v/s+s^{-1/2},\qquad
 B_{\sigma,c}(N)\le2A_\ast\sqrt s .
$$

Indeed the integral over this log interval is at most $A_\ast$. The points with larger values occupy at most half the interval, and jumps form a countable set. Set $v'=s\log N=v+o(1)$.

Keep every local sign up to $N$ and make all later primes inert. The modified product agrees with $P_\sigma$ through $N$, so the unnormalised positive area up to $N$, even before discounting, is at most $A_\ast$. The only new factors after $N$ come from inert primes of norm $p^2>N$, including those already assigned inert below $N$. Their total log contribution is at most $\sum_{p>\sqrt N}-\log(1-p^{-2})\ll N^{-1/2}$. Thus the normalised full average for this modified product, with the same $c$, is bounded above by

$$
 s A_\ast+2^s e^{-v'}\lbrace B_{\sigma,c}(N)+O(N^{-1/2})-k(v')\rbrace.
$$

Because $v'\sqrt s\to0$ and $2^s e^{-v'}k(v')/s\to e^\delta A_\ast$, this is strictly negative. The modified product remains nonnegative in its error through $N$.

For this fixed $s$ and its finite $N$, decrease the benchmark $c$ by a sufficiently small relative amount. This leaves the full mean negative and makes the error strictly positive up to $N$. Prescribe the modified pattern through an arbitrarily large finite $Q>N$. Changes above $Q$ cost at most $(4/s)(2/Q)^s$ in the average. Choose $Q$ so this cost fits inside the strict negative margin. Local support supplies actual Yokoi fields with this pattern and benchmark in a small open interval just below $c$. They retain both strict signs, including a right neighbourhood at $N$. [Local support and the uniform approximation of the tail](PROOF.md)

Consequently $s\log M(s)\ge v+o(1)$. Taking $\delta\downarrow0$ proves (6). For each fixed sufficiently small $s$ in this argument the finite local conditions have positive lower density, which may depend on $s$. The constant in (6) is characterised by (7). Its numerical value has not been determined here.
