# Extending a positive finite pattern

This construction supplies a finite-area admissible path using the ordinary prime number theorem. It also controls how accurately the finite minima approximate the variational constant in the [small-exponent law](SLOW-WEIGHTS.md). The signs are freely chosen among the permitted Yokoi local signs. Their transfer to actual fields is a separate finite-pattern argument.

Put $u=\log t$. Suppose that all signs at primes through $e^U$ have been fixed, that the error $B_{\sigma,c}$ is nonnegative up to that point, and that $U$ is sufficiently large. By lowering $c$ by the factor $\exp(-2/U^2)$ the error on the whole prefix increases by $2/U^2$. Its area increases by at most $2/U$. Let $b_0$ be the new terminal error. Thus $b_0\ge 2/U^2$.

On a grid $u'=u+1/u$, beginning at $U$, maintain $B(e^u)\ge b(u)=2/u^2$. The drop in the log benchmark on a jump-free block is $d_u=\log(u'/u)=\log(1+1/u^2)\sim u^{-2}$. New split primes in $(e^u,e^{u'}]$ can supply a log jump of total size $(2+o(1))d_u$ if all are used. Indeed the effective ordinary prime number theorem $\vartheta(x)=x+O(x\exp(-c_1\sqrt{\log x}))$ gives $\vartheta(e^{u'})-\vartheta(e^u)\sim e^u/u$. Throughout the interval $p\log p\sim e^u u$ and $\log(1-1/p)^{-1}=1/p+O(p^{-2})$. Both signs $+1,-1$ are admissible at all these primes. The inert squares arriving in the block are already determined because their underlying primes are below $e^u$. Their total log jump $r_u$ is $O(e^{-u/2})$, using even the sum over all integers past $e^{u/2}$ of their reciprocal squares. [Johnston and Yang, explicit estimates for the prime number theorem](https://arxiv.org/abs/2204.01980)

If choosing no new split primes ends the block at or above $b(u')$, choose all its primes inert. Otherwise split primes until the end height reaches $b(u')$, and leave the others inert. The deficit before choosing splits is at most $d_u$, since $b(u')\le b(u)$ and $r_u\ge0$. Enough primes are available, and the excess above $b(u')$ is at most $O(e^{-u})$, the size of a single split jump. The error stays positive at all intermediate times even if the chosen splits occur last in the block, because $b(u)>d_u$.

There is a finite first block where splits are required. Before then the error is at most $b_0-\log(u/U)+O(e^{-U/2})$, as the total contribution of every possible later inert square is $O(e^{-U/2})$. This expression eventually becomes negative. When $b_0\le1$, the initial blocks with no splits have total log length $O(U(b_0+e^{-U/2})+1/U)$ and error at most $b_0+O(e^{-U/2})$. The first block with splits itself has length at most $1/U$ and total new jumps $O(U^{-2})$ in addition to inert squares. Their combined area is $O(U b_0^2+1/U)$. For any fixed larger $b_0$ the initial length and area are still finite by the same logarithmic drop.

After the first block with splits, the error at its endpoint is $b(u')+O(e^{-u})$. Subsequent blocks starting that close to the buffer always require some splits, since $b(u)-b(u')=O(u^{-4})$, $r_u=O(e^{-u/2})$ and $d_u\asymp u^{-2}$. Thus the error is $O(u^{-2})$ everywhere on the remaining tail, including the intervening points by the bound on total jumps per block. Its area is $O(1/U)$. This proves the extension estimate.

In particular, begin with all signs inert through some fixed sufficiently large $e^{U_0}$ and $c=1/(2U_0)$. The error is positive on this prefix and the preceding construction gives a positive path of finite area. This proves that $A_\ast$ is finite with no zero-location assumption. With an explicit rational-prime error bound one can fix the starting threshold and give a computable coarse upper bound for its area.

There is also a rate of convergence to $A_\ast$. Choose a minimiser for $A_L$ and take $U\in[\tfrac12\log L,\log L]$ where its error is at most $4A_L/\log L$, avoiding jumps. Such a point exists by the area bound. Keep its prefix only through $e^U$ and use the extension above. The adjustment to the prefix costs $O(1/U)$ and the new tail costs $O(Ub_0^2+1/U)$ with $b_0\ll (1+A_L)/U$ for large $L$. The discarded part of the original prefix had nonnegative area. Therefore

$$
 0\le A_\ast-A_L\ll (1+A_\ast^2)/\log L.
$$

The finite minima and this approximation refer to ideal splitting patterns in the variational problem. They do not assert that a single real quadratic field stays above its main term forever.
