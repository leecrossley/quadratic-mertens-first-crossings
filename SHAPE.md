# The shape conditional on a late first crossing

Set $E_X=\{S\ge X,\ W<\infty\}$, $u=\log X$ and $\Lambda=2\sqrt{A_*}$. We prove the shape statement of the [frequency theorem](PROOF.md). Every deterministic estimate here applies to the independent model and to the true quadratic fields.

Fix a small $\eta>0$. Put $a=\Lambda+\eta$, $R=X\exp(a\sqrt u)$, and call the endpoint good when
$$
 |B(R)|\le1/u,\qquad \int_R^\infty |B(t)|\,dt/t\le1/u .
$$
The conditional probability that it is bad, given $E_X$, tends to zero. The unconditioned bad probability is $O(\exp[-cR/u^2])$ in the model. The lower bound in the frequency proof gives $\Pr(E_X)\ge\frac12\exp[-CQ/\log Q]$ with $\log Q=u+2b\sqrt u+O(1)$ and $\Lambda<2b<\Lambda+\eta/2$. Thus $R/u^2$ exceeds $Q$ by a factor tending to infinity. In moving shells first choose $\eta<\epsilon/2$ in (2). The additional exceptional probability $O(D^{-1/4})$ divided by the lower probability also tends to zero since $Q=o(\log D)$. The same estimates with a limit superior in $D$ work for the successive limits. For fixed $X$, the integrated tail bound on actual fields follows by taking $D\to\infty$ at fixed $R,k$ in the moment proof.

On a good endpoint and $E_X$, write $f(w)=\sqrt u\,B(Xe^{w\sqrt u})$, $g(w)=\max(0,-f(w))$, $T_a(w)=\min(w,a-w)$ for $0\le w\le a$. The deterministic two-sided prime bound gives
$$
 0\le g(w)\le T_a(w)+o(1),\qquad
 |f(w)-f(z)|\le |w-z|+o(1) .
 \tag{9}
$$
All error terms are uniform on this fixed compact interval. For the second estimate, between any two points monotonicity of the product bounds the downward change by the log growth of the benchmark. The upper change is bounded by using two split factors at every rational prime and all possible delayed squares. The ordinary prime estimate gives the same log growth plus $O(e^{-c\sqrt u})$ for the log error. After scaling, this proves (9) even across prime jumps. The first bound uses the nonnegative starting height and the terminal estimate at $R$.

Because a negative endpoint exists and the absolute tail after $R$ is small, $\int_0^a g(w)\,dw\ge J(X)-1/u\ge A_X-1/u$. On the other hand $\int_0^a T_a(w)\,dw=a^2/4$. Consequently
$$
 A_X\le J(X)\le a^2/4+o(1),\qquad
 \int_0^a|T_a(w)-g(w)|\,dw\le a^2/4-A_X+o(1)=O(\eta)+o(1).
 \tag{10}
$$
In the last estimate the negative part of $T_a-g$ is $o(1)$ uniformly. By (9) and the Lipschitz property of $T_a$, an absolute gap of size $v$ at one point forces a gap at least $v/2-o(1)$ on an adjacent subinterval of length at least $\min(v/4,a/2)$. Thus $\|g-T_a\|_\infty=O(\sqrt\eta)+o(1)$ for small $\eta$. On $[0,\Lambda]$, $\|T_a-T_\Lambda\|_\infty\le\eta$. On every compact subinterval of $(0,\Lambda)$, for small $\eta$ and large $X$, $g$ is positive, so $f=-g$. At either endpoint the second part of (9) controls $f$ by its value at a nearby interior point. First let $X$ grow, then $\eta$ decrease to zero and the interior points tend to the two endpoints. This proves uniform convergence in conditional probability of $f$ to $-T_\Lambda$, together with $J(X)\to A_*$ from (10).

In particular the cumulative errors $J(Xe^{w\sqrt u})$ converge conditionally and uniformly on the same interval to $A_*-\int_0^wT_\Lambda(z)\,dz$. The limit reaches zero at $\Lambda$. This uniform approximation alone does not determine which side of zero a finite field occupies at that last point.
