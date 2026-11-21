# Realising the late fields in each discriminant shell

This proves the third assertion of the [main theorem](PROOF.md). The count in §2, with the location of $S_d$ and $W_d<\infty$, is unconditional. The power averages in §3 also assume the critical-line property for the Riemann zeta function and $L(s,\chi_d)$ (field GRH), through the pointwise bound beyond $V$. Write $L=\log\log D$, fix $\kappa>2\sqrt{A_\ast}$ and take $u=L-\kappa\sqrt L$, $N=e^u$. Choose $b$ and an admissible fixed positive pattern with area $A$ and benchmark $c$ so that

$$
 A_\ast \le A < b^2,\qquad 2b<\kappa,\qquad 0\le B(e^v)\ll v^{-2}\quad(v\to\infty).
$$

The construction quoted at the beginning of the main proof permits these choices. Implicit constants may depend on them. All primes past a fixed initial set have signs $-1$ or $+1$.

## 1. A dip with a prescribed negative area

Keep this positive pattern through $N$. Make all new primes inert until $e^{u+h}$, with $h=b\sqrt u$. After this point make all new primes split until the first return to height $-u^{-2}$ from below, measuring the error relative to $c$. Let $Q$ be the location of that return. This point exists and

$$
 \log Q=u+2b\sqrt u+O(1),\qquad
 \log(P(Q)/(c\log Q))=-u^{-2}+O(e^{-u}).
 \tag{1}
$$

Indeed, in the inert part at $v=\log t$ the error is $B(N)-\log(v/u)+O(e^{-u/2})$. Delayed squares are bounded by summing reciprocal squares of all integers above $e^{u/2}$. In the split part, the log product gains $2\log(v/(u+h))+O(e^{-c_1\sqrt u})$ relative to its value at the turn, using the ordinary prime number theorem. Thus its error is $B(N)+\log(uv/(u+h)^2)+O(e^{-c_1\sqrt u})$. At $v=(u+h)^2/u\pm C$ the latter has opposite signs relative to $-u^{-2}$ for fixed sufficiently large $C$. The same uniform upper estimate excludes an earlier return before the lower endpoint. The overshoot at first return costs only $O(e^{-u})$, since upward jumps have that size at most. This proves (1). In particular $Q=o(\log D)$ because $2b<\kappa$.

With $w=(\log t-u)/\sqrt u$, uniformly from $N$ to $Q$ the error multiplied by $\sqrt u$ converges to $-w$ on $[0,b]$ and to $w-2b$ on $[b,2b]$, allowing the endpoint displacement $O(1/\sqrt u)$. Its signed integral against $dt/t$ is therefore $-b^2+o(1)$, and its positive part has integral $o(1)$ there. Before $N$ its integral is at most $A$. These conclusions hold if $\log c$ changes by $O(u^{-2})$, since the whole log length through $Q$ is $O(u)$.

## 2. The field count and the residue

Let $I$ impose the chosen signs on all primes $p\le Q$. In the independent model for the Yokoi family both nonzero signs have probabilities bounded away from zero for odd primes. Every initially used ramified sign has fixed positive probability. Hence the model probability $p_I$ satisfies

$$
 p_I\ge \exp[-C Q/\log Q].
$$

Over the actual shell $D/2<d\le D$, the mean of $I$ is $p_I+O(D^{-1/7})$ for sufficiently large $D$. Here and below the fractions of powers of $D$ just absorb logarithms and $D^{o(1)}$ factors. To prove this, write a prescribed nonzero sign indicator as $(\chi(p)^2\pm\chi(p))/2$ and the zero indicator as $1-\chi(p)^2$. In the expansion the character indices are at most $\exp(2\vartheta(Q))=D^{o(1)}$ and the sum of absolute coefficients stays bounded since only a fixed finite set can ramify. Dahl and Kala's Proposition 14 has normalised moment error $O(n^{2/3}D^{-1/6}\log D)$, also on the shell by subtraction at its endpoints. There are $\asymp\sqrt D$ discriminants in the shell. This proves the comparison. The same reasoning applies after multiplication by two character values at primes up to $V=(\log D)^{128}$. [Squarefree family count and character moments](https://arxiv.org/pdf/1611.02424#page=11)

For $Q\le t\le V$ write $Z_t=\sum_{t<p\le V}\chi_d(p)/p$. The mean square over the conditioned shell is

$$
 \mathbb E(Z_t^2\mid I=1)\ll 1/t+D^{-1/8}.
 \tag{2}
$$

Indeed independence in the model gives the variance bound $\sum_{p>t}1/p^2\ll1/t$, and the mean is $O(1/t)$ since each model sign has mean $O(1/p)$. The two inserted primes increase the maximal index by at most $V^2$. The sum of absolute coefficients increases by at most $(\sum_{p\le V}1/p)^2$. Dividing the moment comparison by $p_I=D^{-o(1)}$ gives (2), uniformly in $t$. The implicit constant can absorb the bounded square of the model mean.

By Granville and Soundararajan's short Euler product, apart from $O(D^{1/4})$ primitive characters up to $D$, the log residue differs from the log Euler product through $V$ by $O((\log D)V^{-1/32})=O((\log D)^{-3})$. The exceptional proportion conditional on $I=1$ tends to zero. For all the remaining fields, multiplication of the ordinary Mertens product by the quadratic Euler factors through $t$ gives

$$
 B_d(t)=-Z_t+O\big(e^{-c_2\sqrt{\log t}}+t^{-1/2}+(\log D)^{-3}\big)
 \qquad (Q\le t\le V).
 \tag{3}
$$

The rational-prime error follows from the effective ordinary prime number theorem. Replacing the partial character factors above $t$ by their linear terms costs $O(1/t)$. A rational inert prime $p\le t$ contributes to the product of the two Euler factors as $(1-p^{-2})^{-1}$, and its ideal-norm factor is absent if $p^2>t$. Removing these excess factors costs $O(t^{-1/2})$. [Short Euler products, Proposition 2.2](https://arxiv.org/pdf/math/0206031#page=7) · [Effective ordinary prime number theorem](https://arxiv.org/abs/2204.01980)

Chebyshev's inequality in (2) at $Q$ and (3) give $|B_d(Q)|<u^{-3}$ for a proportion tending to one conditional on $I=1$. Since the actual and prescribed products agree through $Q$, this and (1) imply

$$
 \log c_d-\log c=-u^{-2}+O(u^{-3}).
 \tag{4}
$$

In particular, the actual error is positive through $N$. A log distance $C/u$ into the inert interval it is strictly negative, using the formula in §1 and the bound for $B(N)$. Positivity at $N$ extends to a right neighbourhood by monotonicity and the strict margin. Thus $N<S_d\le N\exp(C/u)$. By §1 the integral up to $Q$ is at most $A-b^2+o(1)<0$ for all these fields. This proves $W_d<\infty$ with the count in the theorem using only finite endpoints.

## 3. One start for an interval of slowly decaying powers

For the same conditioned shell the expected value of $|Z_t|$ is $O(t^{-1/2}+D^{-1/16})$ by (2). Integrating the absolute upper bound in (3) over its nonexceptional members gives

$$
 \mathbb E\left[\mathbf1_{\rm nonexceptional}\int_Q^V |B_d(t)|\thinspace dt/t\ \middle|\ I=1\right]=o(1).
$$

Indeed $\log V=128L$ while $Q=\exp((1+o(1))L)$. Beyond $V$ the pointwise real quadratic bound of (2) in the main proof, which assumes field GRH, gives a uniform absolute integral $O((\log D+\log V+1)/\sqrt V)=o(1)$. Markov's inequality now gives, simultaneously with (4), a proportion tending to one in the conditioned shell for which the entire absolute tail past $Q$ is $o(1)$. For example use the square root of the vanishing expectation as the cutoff on $[Q,V]$. [Quadratic pointwise estimate and its critical-line input](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/main/results/yokoi-mertens-optimal-starts/PROOF.md)

Choose a fixed $\lambda>0$ sufficiently small that $e^{-\lambda}b^2>A$. For all $0<s\le\lambda/L$ the weight $(2/t)^s$ lies between $e^{-\lambda-o(1)}$ and 1 throughout $[2,Q]$. The positive prefix to $N$ has area at most $A+o(1)$, the interval $[N,Q]$ contributes at most $-e^{-\lambda}b^2+o(1)$, and the whole tail past $Q$ costs $o(1)$, uniformly over this range of powers. Consequently

$$
 \int_2^\infty s(2/t)^s B_d(t)\thinspace dt/t <0\qquad(0 < s\le\lambda/L).
$$

The strict margin is for the integral divided by $s$. At least a fixed fraction of the conditioned fields meet all requirements. Their number is $\gg\sqrt D\thinspace p_I\ge\sqrt D\exp[-C Q/\log Q]=D^{1/2-o(1)}$, as claimed.
