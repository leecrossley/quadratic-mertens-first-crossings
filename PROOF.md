# Two positive Mertens averages and a global minimum

Let $d=5$ or $13$, $K=\mathbb Q(\sqrt d)$, and write $q=N\mathfrak p$ with one entry for each prime ideal. Put $\ell(q)=-\log(1-1/q)$, $\kappa=L(1,\chi_d)$, $u=\log y$ and $N_y=\sqrt y\log y$. The average considered here is

$$
 B_d(t)=\sum_{q\le t}\ell(q)-\gamma-\log\kappa-\log\log t,
 \qquad F_d(y)=\int_y^\infty B_d(t)\frac{y}{t^2}\,dt .
$$

**Theorem.** Use RH for $\zeta$ and the critical-line property for $L(s,\chi_d)$ for the two indicated characters. Then $N_y F_{13}(y)>1/40$ for every real $y\ge2$. For $d=5$, $N_yF_5(y)$ has a unique global minimum. Its argument lies in $(2.64281618,2.64281620)$ and its value in $(0.183894,0.183896)$. For $y\ge4$ it exceeds $1/5$. Thus neither field has a negative start for this weight. The critical-line input is the case of the announced Dirichlet GRH theorem specified here. [Alpöge](https://alpo.ge/remark.pdf) · [Sutherland’s verification record](https://math.mit.edu/~drew/grh/)

## The finite part

Put $E_1(u)=\int_u^\infty e^{-v}dv/v$ and $D=\sum_q\ell(q)/q$. Integrating each prime-ideal jump gives the weight $\min(1,y/q)$. Integrating $\log\log t$ by parts gives

$$
 F_d(y)=\sum_{q\le y}\ell(q)-\gamma-\log\kappa-\log u
        +y\left(D-\sum_{q\le y}\frac{\ell(q)}q-E_1(u)\right).
$$

The norm list has two copies of $p$ for split primes, one copy of $p^2$ for inert primes and one copy of $p$ for ramified primes. To enclose $D$, start with $\log(\zeta(2)L(2,\chi_d))$ and add $\ell(q)/q-\ell(q^2)$ for $q\le M=10^6$. With $x=1/q$, each of $x\ell(q)-x^2$ and $\ell(q^2)-x^2$ lies between $0$ and $x^3$ by the log series. There are at most two ideals of each norm, so $4/M^2$ more than bounds the absolute tail.

Both fields have class number one by the Minkowski bound. Their fundamental units are $(m+\sqrt d)/2$ with $m=1,3$ respectively, of norm $-1$. Minimality follows from the norm equation: a smaller unit $v>1$ would have positive integer coefficient $(v-v')/\sqrt d<1$ if its norm is $-1$; if its norm is $+1$, the same inequality follows from $v-1/v<v+1/v$. The class number formula gives $\kappa=2\log((m+\sqrt d)/2)/\sqrt d$. Equivalently one can evaluate the Dirichlet series itself. Expanding the Fourier series of $B_2(x)=x^2-x+1/6$ and summing with the quadratic Gauss sum gives $L(2,\chi_d)=\pi^2 d^{-1/2}\sum_{a=1}^{d}\chi_d(a)B_2(a/d)$. The constant and linear terms sum to zero.

Between prime-ideal norms $F_d''(y)=1/(y^2\log y)$. At each norm its first derivative jumps down by $\ell(q)/q$ per ideal. On $[a,b]$ the curve therefore lies above its endpoint chord minus $(b-a)^2/(8a^2\log a)$, by subtracting a quadratic of second derivative $1/(a^2\log a)$. Use the increasing factor $N_a$ for the lower bound once both endpoint bounds exceed the positive target. The first calculation covers $[4,M]$ for $d=5$ and $[2,M]$ for $d=13$. A second calculation uses the supporting tangent on each gap between successive norms, where $F_d$ is convex, subdividing any inconclusive gap. It obtains the two special values from the Dirichlet $L$ function in Arb and checks splitting by a separate primality and Jacobi-symbol calculation. [Chord calculation](verify.py) · [Tangent calculation](independent.py)

On the first gap for $d=5$ write $A=e^u(D-E_1(u))$, $C=\gamma+\log\kappa+\log u$. The formula $N_y F_5(y)=e^{u/2}u(A-C)$ holds up to $y=4$ by continuity. Its derivative with respect to $u$ has the sign of

$$
 W=(1+3u/2)A-(1+u/2)C,\qquad
 W'=1-C/2+(5+3u)A/2,\qquad
 W''=2/u+3/2+(4+3u/2)A .
$$

The chord calculation encloses $W''>0$ on 128 intervals and $W(\log 2)<0$. Strict convexity and opposite signs at the two stated endpoints for the minimiser give exactly one root on $[\,\log 2,\log 4\,]$. The other calculation encloses $W<0$ through $y=2.4$ and $W'>0$ thereafter, and encloses the value at the same root. The rest of the half-line lies above $1/5$.

## From one million to infinity

Write $\langle f\rangle=\int_y^\infty f(t)y\,dt/t^2$, $\psi_K(v)=\sum_{q^j\le v}\log q$ and $Q(t)=\sum_{q\le t,\ q^j>t}1/(jq^j)$. Separating the prime powers at their own cutoff gives $F_d=J+\langle Q\rangle$, where $J$ is the averaged error of $\sum_{q^j\le t}1/(jq^j)$. The integrated explicit formula gives $N_yJ\ge -V_d$ with

$$
 V_d=\sum_{\zeta_K(1/2+i\lambda)=0}^{*}\frac{1}{1/4+\lambda^2}
     =2+\log d-2\log\pi-4\log 2+2\frac{L'(1,\chi_d)}{L(1,\chi_d)}.
$$

The star counts nontrivial zeros of both signs with multiplicity. For clarity, test $-d(\psi_K(e^z)-e^z)$ against $(1-e^{u-z})e^{-z}/z$ on $z\ge u$. Each zero contributes, after normalisation, $e^{i\lambda u}u\int_0^\infty e^{-vu}[(1/2-i\lambda+v)(3/2-i\lambda+v)]^{-1}dv$, of absolute value at most $(1/4+\lambda^2)^{-1}$. The remaining density $\coth z$ for the real quadratic signature is positive. The displayed value of $V_d$ follows by pairing zeros in the completed logarithmic derivatives at 1. Smoothing the test and passing to the limit is justified by its summable $O_u((1+\lambda^2)^{-1})$ transform. [Detailed derivation](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/ef3e53c/results/signed-prime-tails/PROOF.md) · [Grenié and Molteni, integrated explicit formula](https://arxiv.org/pdf/1312.4465#page=2)

For every $v\ge1000$ one has $|\psi_K(v)-v|<\delta v$, with $\delta=0.05$ for $5$ and $0.037$ for $13$. Up to $M$ the two programs check both sides of every jump or every integer gap. Beyond $M$, Corollary 1.2 of Grenié and Molteni bounds the relative error by

$$
 e^{-h/2}\big[(h/(2\pi)+2)\log d+h^2/(4\pi)+4\big],\qquad h=\log v .
$$

This expression decreases for $h>4$, and at $M$ it is below the indicated $\delta$. Truncating the character series for $L(1)$ and $L'(1)$ at $65000$ bounds their tails by $b/65000$ and $b\log(65000)/65000$, where $b=\max_k|\sum_{n\le k}\chi_d(n)|$. Complete periods and Abel summation give these bounds. They imply $V_5<0.22$ and $V_{13}<0.445$. A separate power-series evaluation of the two $L$ functions gives $0.202<V_5<0.204$ and $0.442<V_{13}<0.444$. [Explicit prime-ideal theorem](https://arxiv.org/pdf/1312.4463#page=3)

Keep only the even indices in $Q(t)$. Adding the omitted $q>t$ costs at most $\sum_{n>t}1/(n^2-1)\le2/t$. With $z=\sqrt t$ and $h(v)=1/(v^2\log v)$, this gives

$$
 Q(t)\ \ge\ \frac12\int_{(z,\infty)}h(v)\,d\psi_K(v)-2/t .
$$

Replacing $d\psi_K$ by $dv$ costs at most $\tfrac12\delta(zh(z)+\int_z^\infty v|h'(v)|dv)\le3\delta/(2z\log z)$ by parts. After averaging and normalising this costs at most $2\delta$. The allowance $2/t$ costs $u e^{-u/2}$. Substitute $t=ye^r$, $v=\sqrt t\,e^s$ in the main integral. Its normalised value is $\int_0^\infty\int_0^\infty e^{-3r/2-s}u/(u+r+2s)\,ds\,dr$. The measure has mass $2/3$ and the mean of $r+2s$ under its probability normalisation is $8/3$. Jensen's inequality for the reciprocal now gives

$$
 N_y F_d(y)\ \ge\ \frac{2u}{3u+8}-2\delta-u e^{-u/2}-V_d .
$$

For $y\ge10^6$ this lower bound increases. At its left endpoint it exceeds $1/5$ for $d=5$ and $1/40$ for $d=13$, using even the coarser bounds on $V_d$. This completes the proof for every real start.
