# What a grid of ordinates permits

The sign in the [nearest-zero theorem](NEAREST-ZERO.md) uses the oscillating sum with coefficients $c_\lambda$ and bias $b=2/3$. In the original average the oscillating coefficients are $h_\lambda(u)$. The following model works with both kernels. It shows why a proof covering every Yokoi field needs more information about its primes or zeros than a functional equation, a critical line and a macroscopic zero count.

Fix $P\ge4$ and $0\le\theta < \pi/3$. Take the two shifted lattices

$$
 \lambda=(2\pi k+\theta)/P,\quad (2\pi k-\theta)/P,\qquad k\in\mathbb Z ,
$$

retaining their multiplicities. Their contribution to the sum with $h_\lambda$ is

$$
 2P\sum_{jP\ge u}\cos(j\theta)\thinspace
       e^{-(jP-u)/2}(1-e^{-(jP-u)})\thinspace \frac{u}{jP},\qquad u>0 .
 \tag{1}
$$

For $c_\lambda$ the same expression holds with the final fraction replaced by one. To verify this, apply periodization with period $P$ to the function supported on $v\ge0$ given by $e^{-v/2}(1-e^{-v})u/(u+v)$. Modulation supplies the two phases at $u+v=jP$. Equivalently, expand the periodization in its Fourier series. The coefficient tails are absolutely summable since the function is continuous, with integrable second derivative on the open half-line and a finite first derivative jump at zero. The value at an endpoint $jP=u$ is zero.

For $\theta=0$ each sum is strictly positive for every $u>0$, and the model has a double central zero. For $\theta>0$ each sum is nonnegative throughout

$$
 0 < u\le P\left(\frac{\pi}{3\theta}-2\right).
 \tag{2}
$$

In fact for $j_0=\lceil u/P\rceil$ the first two cosines are at least $1/2$. Divide the absolute tail beginning at $j_0+2$ by the positive weight at $j_0+1$ before its cosine is inserted. This ratio is at most $e^{-P/2}/[(1-e^{-P/2})(1-e^{-P})] < 1/2$. The factor $u/(jP)$ can only reduce this ratio. This proves (2) across the entire interval, including at the lattice points.

## Matching the growing zero count

Use the critical-line property for the ordinary and conductor-five factors. To include the higher zeros of an even degree-one function, take as the model's completed quadratic factor

$$
  \Lambda^{\sharp}(s)=2\big(\cosh(P(s-1/2))-\cos\theta\big)\Lambda(s,\chi_5),
$$

and use the ordinary zeta function for the other factor. This is an entire function of order one with symmetry $s\mapsto1-s$. It has the ordinary even gamma factor, a conductor parameter $D=5e^{2P}$ and the stated critical-line zeros alongside those of $\Lambda(s,\chi_5)$. In $0 < \Im s\le T$ the added lattices supply $PT/\pi+O(1)$ ordinates uniformly in $P,T,\theta$. This is precisely the change of the linear conductor term from 5 to $D$ in the degree-one zero count.

The ordinary and conductor-five zeros together contribute less than $1/4$ in absolute value for either kernel, uniformly in $u$. The sum of their inverse squared distances from 1 is

$$
 2+\log5-2\log\pi-4\log 2+2L'(1,\chi_5)/L(1,\chi_5) < 1/4 .
$$

Use the paired logarithmic derivatives at 1 and the ordinary zeta identity in the [explicit formula](PROOF.md). The interval check below evaluates $L(1)$ and $L'(1)$ by their Dirichlet series. At any multiple $N$ of 5, partial sums of $\chi_5$ over the tail have absolute value at most one. Abel summation bounds the tails by $1/N$ and $(\log N)/N$ for $N>e$. [Interval calculation](packets.py)

Thus $b$ plus the complete oscillating sum stays strictly positive on (2), and for all $u>0$ at $\theta=0$. Here $b$ is the limiting square contribution used in the model. The nearest added ordinates at $\theta>0$ are $\pm g$, $g=\theta/P$. As $\theta\to0$ the protected length is asymptotic to $\pi/(3g)$, which can exceed any fixed multiple of $\log D$. This is an obstruction at the reciprocal-height scale for these spectral data.

For $e^P=p$ prime, the Dirichlet factor after normalization is

$$
 L(s,\chi_5)\big(1-2\sqrt p\cos(\theta)\thinspace p^{-s}+p\thinspace p^{-2s}\big).
$$

Its coefficient at $p$ is $\chi_5(p)-2\sqrt p\cos\theta$, incompatible with a quadratic Dirichlet character for $p\ge e^4$. This calculation locates exactly where arithmetic distinguishes the model from an actual field. It leaves the family-wide polynomial question open.
