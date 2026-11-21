# Enough fields remain above their benchmark through X

The lower bound needed to condition on $S_d\ge X$ is $\Pr_D(S_d\ge X)\ge\exp[-C(\log X)^4]$ for $\log X\le c(\log D)^{1/5}$, with $c$ small and $D,X\to\infty$. It assumes RH for the Riemann zeta function, but no hypothesis on $L(s,\chi_d)$. We give the changes of parameters in the earlier signed-profile estimate since the cutoff can grow very slowly here. [Signed-profile proof, §§1–2](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-prescribed-crossings/PROOF.md)

Replace $X$ temporarily by the next dyadic integer $X'$ (so $X\le X'<2X$ except equality). Choose first a sufficiently large amplitude $A$ and then a sufficiently large fixed dyadic $B$. Force all primes through $B$ inert. On $B<p\le2X'$ set

$$
 \Delta_p=-A(\log p)^2/\sqrt p .
$$

In the Euler model tilt by the square of $\prod_{B<p\le2X'}(1+a_p(T_p-\mu_p))$ with $|a_p|\le2|\Delta_p|$ to change each mean by $\Delta_p$. This is possible by continuity of the mean in $a_p$ and the uniform variance lower bound. The sum of $a_p^2$ is $O_A((\log X')^4)$ by the prime number theorem. Truncate the expanded product at squarefree indices $n\le N=\lfloor D^{1/1000}\rfloor$ and denote it by $R_N$.

Here take $V=(X')^{128}(\log D)^{128}$, rounded upwards to a power of two for dyadic subdivision. Orthogonality of the centred monomials and Markov's inequality as in the cited proof give for the relative discarded squared norm at most

$$
 \exp[-\log N/\log(2X')+O_A((\log X')^4)] .
$$

Its square root is at most $V^{-100}$ on reducing $c$: $\log D/\log(2X')$ dominates a sufficiently large multiple of $(\log X')^4+\log V$. In the case $\log X'<\log\log D$ this follows directly from growth with $D$. Thus the same normalised tilted moments transfer to the shell for every prime interval through this larger $V$. More explicitly, if $I$ is the fixed initial sign indicator, the fourth moment of a centred sum of signs divided by $p$ over any interval through $V$, weighted by $I R_N^2$, has numerator comparison error

$$
 O_B\big(N^4(2V)^4(N^2V^4)^{2/3}D^{-1/6}\log D\big)\ll D^{-1/8}
$$

for sufficiently large $D$. The normalised model truncation costs $O_B(V^4V^{-100})$ and $\mathbb E_{\rm shell}IR_N^2\gg_B1$. These errors are smaller than $V^{-10}$. A dyadic maximal fourth-moment estimate then gives, with positive probability in the tilted shell, **simultaneously** for $B\le t\le X'$,

$$
 \left|\sum_{t < p\le V}(\chi_d(p)-\mu_p-\Delta_p)/p\right|
 \ll \log t/\sqrt t.
$$

Here $\Delta_p=0$ off its support. To see the maximal bound, on $(z,2z]$ the fourth moment on a subinterval of $h$ integers is $O(h^2/z^4)$ by independent centring and transfer. Each prefix consists of at most one dyadic block per subdivision level. Summing the fourth powers at each level and applying Minkowski gives $L^4$ norm $O(z^{-1/2})$ for the maximum. The sum of failure probabilities $O(\sum_{z=2^j\ge B}(\log z)^{-4})$ is small. Sum the successful dyadic bounds to obtain the display. All error constants in this display are absolute once $B$ is large.

The second moment of the weight is at most $\exp(O_A((\log X')^4))$ in the shell. This follows by expanding $R_N^4$, vanishing of singleton centred factors in the independent model, and the comparison error $O_B(N^{32/3}D^{-1/6}\log D)=o(1)$. Cauchy–Schwarz converts the positive weighted probability to unweighted proportion at least $\exp[-O_A((\log X')^4)]$. Removing the exceptional characters of the short Euler product costs $O(D^{-1/4})$. Its truncation error for the others is now $O((\log D)V^{-1/32})=O((X')^{-4})$. Norm factorisation and the rational Mertens estimate under RH consequently give

$$
 B_d(t)=-\sum_{t < p\le 2X'}\Delta_p/p+O(\log t/\sqrt t)\qquad(B\le t\le X').
$$

The dyadic subinterval $(t,2t]$ alone contributes $\gg A\log t/\sqrt t$ with positive sign. Choose $A$ large enough to dominate the absolute error, in particular to ensure $B_d(B)>2/\sqrt B$. The choices of $B,c$ then satisfy the previous conditions. On $2\le t\le B$ the forced inert product satisfies $P_d(t)\ge\zeta(2)(1-t^{-1/2})$ by comparison with the telescoping product over all integers past $\sqrt t$, and $P_d(B)\le\zeta(2)$. The ratio $(1-t^{-1/2})/\log t$ decreases for $t>1$, as follows by differentiating and using $1+x<e^x$ for $x>0$. Since $e^{-2/\sqrt B}<1-1/\sqrt B$ for large $B$, the lower bound for $B_d(B)$ gives $P_d(t)>c_d\log t$ on the entire remaining prefix. Thus $S_d\ge X$, with the desired count. No estimate for the integral above $(X')^2$ is needed for this denominator.
