# What prolonged positivity would require of split and inert primes

Let $L=\log(3d)$ and use the [definitions and hypotheses of the nearest-zero theorem](NEAREST-ZERO.md). For every $\varepsilon>0$ there are $A_\varepsilon$ and $d_\varepsilon$ such that, for $d\ge d_\varepsilon$ and $H\ge A_\varepsilon L$, positivity $F_d(y)\ge0$ throughout $2\le y\le e^{2H}$ requires

$$
 \frac1H\sum_{p\le e^H}\frac{\chi_d(p)\log p}{\sqrt p}
       \left(1-\frac{\log p}{H}\right)\le-\frac12+\varepsilon .
 \tag{1}
$$

Thus a field that keeps the average nonnegative throughout the window must have a definite weighted excess of inert primes. This *initial* prime sum differs from the signed *tail* $T_d(y)$.

Write $S(t)=\sum_{\lambda\ {\rm quadratic}}\mathrm{sinc}^2(H(\lambda-t)/2)$. For bounded $|t|\le1$, the Guinand–Weil formula gives

$$
 S(t)=\frac{\log(d/\pi)}H+G_H(t)
 -\frac2H\sum_{n\le e^H}\frac{\Lambda(n)\chi_d(n)}{\sqrt n}
       \left(1-\frac{\log n}{H}\right)\cos(t\log n),
 \tag{2}
$$

where $\Lambda(n)$ is the von Mangoldt function and

$$
 G_H(t)=\frac1{2\pi}\int_{\mathbb R}\mathrm{sinc}^2(H(v-t)/2)
       \Re\psi(1/4+iv/2)\thinspace dv=O(1/H).
$$

Here $\psi=\Gamma'/\Gamma$. The last bound follows by using boundedness of the digamma function on the central compact interval and $O(\log(2+|v|))$ in the tails. With the Fourier convention $e^{-2\pi i x\xi}$, the transform of the centred square sinc is $(2\pi/H)(1-2\pi|\xi|/H)_+$, fixing both factors in (2). The shifted test introduces the cosine by pairing the two sides. The quadratic factor is even and primitive and has no pole. [Carneiro, Chandee and Milinovich, formula (4.6)](https://arxiv.org/pdf/1503.00955#page=8)

For every fixed small $r>0$ there is a quadratic zero $\tau\in(r/2,r)$ for every sufficiently large $d$, by the fixed-interval argument. Its weight $w_\tau$ approaches $4/3$ uniformly as $r\to0$. Under the assumed positivity, inequality (6) in the main proof gives $D(0)\ge 4/3-b-O(r+L/H+1/(Hr))-o(1)$, where $b=2/3$. At zero the ordinary contribution to $D(0)$ is $O(H^{-2})$ by its fixed central gap and the summability of its weights. All quadratic weights are at most $4/3$. Choose $r$ small, $A_\varepsilon$ large, then $d$ large. This gives $S(0)\ge1/2-O(\varepsilon)$, with arbitrarily small error.

At $t=0$ the square terms inside the sum in (2) are $H/4+O(\log(2+L))$. Indeed $\sum_{p\le x}(\log p)/p=\log x+O(1)$ by Mertens' first theorem. Integrate its partial sums against the linear weight up to $\log x=H/2$. The ramified primes cost $O(\log(2+L))$ by splitting at $p=L$ and using $\sum_{p\mid d}\log p\le\log d$. Powers of order at least three are absolutely bounded. Substitution in (2), including the conductor term of size $L/H$, proves (1) by taking the errors sufficiently small. A double central zero would already give $S(0)\ge2$ for every $H$. The sign of the prime sum at frequency zero alone therefore cannot remove that case. [Mertens' prime sums](https://doi.org/10.1215/ijm/1255631807)

## A test using several frequencies entirely on the prime side

Formula (2) also makes the several-frequency argument available without individual zero data. Fix an absolute $r_0\in(0,1/4)$ whose double lies in the ordinary central zero-free interval. For $0 < r\le r_0$, choose any $t_1,\ldots,t_n\in[0,r]$ and real $v_1,\ldots,v_n$. Define the even function

$$
 E(t)=w_t S(t)+b\mathrm{sinc}^2(Ht/2).
$$

If $F_d$ stays nonnegative throughout the same interval and $H\ge L$, then

$$
 \sum_{i,j}v_i v_j E(t_i-t_j)
 \ge -C\left(\sum_i|v_i|\right)^2
 \left(\frac LH+r(1+S(0))+o(1)\right).
 \tag{3}
$$

The constant is absolute for fixed $r_0$ and the remainder tends to zero uniformly in $H\ge L$ as $d\to\infty$. All entries can be expressed through finite prime-power sums, the conductor and an explicit gamma integral by (2).

For $|t|\le r_0$ one has $D(t)=w_t S(t)+O(L/H)$. Within $|\lambda-t|\le1$ the derivative of $w$ is bounded, $w_\lambda$ is bounded below, and $|\lambda-t|\mathrm{sinc}^2(H(\lambda-t)/2)\ll1/H$. Sum against the total mass $V\ll L$. Outside this interval the squared sinc is $O(H^{-2}(1+\lambda^2)^{-1})$ and the sum of $(1+\lambda^2)^{-1}$ is $O(L)$. The ordinary contribution is $O(H^{-2})$ because of the fixed central gap. Under positivity, (3)–(5) of the main proof give $|M(t)|\ll1+S(0)$. Removing the phase $\theta_t$ from the left side of (4) there and from the bias costs $O(r(1+S(0)))$ for $|t|\le r$. Thus $\Re M(t)=E(t)+O(L/H+r(1+S(0))+o(1))$. Finally integrate $Z(u)|\sum v_j e^{it_j u}|^2$ against the triangular measure. It is bounded below by $-(\sum |v_j|)^2\langle Z_-\rangle$. Substituting the preceding estimate in the expanded square proves (3).

To settle the exceptional fields by this route one would need a violation of (3), with a margin larger than its error, for every field that escapes the nearest-zero bound. No such uniform prime estimate is established here.
