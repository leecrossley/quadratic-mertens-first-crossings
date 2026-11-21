# High moments for the absolute future error

This proves (4) in the [starting-point theorem](PROOF.md). Use $V=X^{128}(\log D)^{128}$ and $k=\lceil H(\log X)^4\rceil$ for a fixed $H>0$. Choose the upper-range constant $c$ in $\log X\le c(\log D)^{1/5}$ sufficiently small after $H$ is chosen. Then $V<D/2$ for large $D$.

In the independent model, a centred sign has log moment-generating function at most $v^2/2$ at real argument $v$, since its tilted variance is at most one. Independence, exponential Markov and integration of the resulting Gaussian tail give for $t\ge X$
$$
 \left\|\sum_{t<p\le V}T_p/p\right\|_{2k}
 \ll \sqrt{k/(t\log t)}+1/t .
$$
Here the sum of squared coefficients is $O(1/(t\log t))$ by the ordinary prime number theorem, and the contribution of model means is $O(1/t)$. The $L^{2k}$ norm on the real family adds at most $D^{-1/(16k)}$. In fact the error in the $2k$th moment is
$$
 O\left(D^{-1/6}\log D\,V^{4k/3}\big(\sum_{p\le V}1/p\big)^{2k}\right)\le D^{-1/8}.
$$
The inequality follows because $k\log V\ll H u^4(u+\log\log D)$ with $u=\log X$. If $u\ge\log\log D$, reduce $c$, and if $u<\log\log D$ this is $o(\log D)$. [Family moment comparison](https://arxiv.org/pdf/1611.02424#page=11) · [Moment argument in detail](https://github.com/leecrossley/yokoi-mertens-late-crossing-density/blob/v1.0.0/MOMENTS.md)

Outside $O(D^{1/4})$ primitive characters, throughout $X\le t\le V$,
$$
 |B_d(t)|\le \left|\sum_{t<p\le V}\chi_d(p)/p\right|
  +O\left(\log t/\sqrt t+(\log D)V^{-1/32}\right).
$$
Use the ordinary critical-line prime number theorem and partial summation for the rational Mertens product. Delayed inert squares cost $O(t^{-1/2})$. The short Euler product gives the residue error in this display. Beyond $V$ the total absolute integral is $O((\log D+\log V+1)/\sqrt V)$ by the pointwise quadratic estimate. [Ordinary and quadratic error bounds](https://github.com/leecrossley/yokoi-mertens-prescribed-crossings/blob/v1.0.0/PROOF.md) · [Short Euler products](https://arxiv.org/pdf/math/0206031#page=7) · [Critical-line verification](https://math.mit.edu/~drew/grh/)

Apply Minkowski's integral inequality after restricting to nonexceptional fields. The $L^{2k}$ norm of their absolute tail from $X$ is at most
$$
 C\left(\sqrt{k/(X\log X)}+u/\sqrt X\right)
 +O\left[(1+\log V)\big(D^{-1/(16k)}+(\log D)V^{-1/32}\big)
       +(\log D+\log V+1)/\sqrt V\right].
$$
The last error is $o(X^{-1/2})$. For the moment-comparison term, if $u\ge\log\log D$ reduce $c$ until $\log D/(16k)\ge 4u$. If $u<\log\log D$, this quotient grows faster than $u+\log\log V$. All other terms follow from the definition of $V$. The norm is therefore at most $C_Hu^{3/2}/\sqrt X$ for large $X$. At twice this bound Markov gives probability at most $2^{-2k}$. The exceptional proportion is $O(D^{-1/4})$. Choose $H$ sufficiently large in terms of $K_0$ and absorb fixed factors to obtain (4).
