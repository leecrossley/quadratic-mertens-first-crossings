# A certificate that withholds all central zero data

Use RH for the ordinary factor and GRH for the stated quadratic character, as in the main theorem. Take the prime discriminant $d=1543^2+4=2{,}380{,}853$, $u=36359/25=1454.36$, $y=e^u$ and $N_y=u e^{u/2}$. For the [prime-ideal average](NEAREST-ZERO.md) and the signed reciprocal-prime tail $T_d(y)=\sum_{p>y}(1-y/p)\chi_d(p)/p$, the certificate proves

$$
 N_y F_d(y) < -1/20,\qquad N_y T_d(y)>1/10,\qquad y < d^{100}.
$$

The input lists 151 positive quadratic zero brackets, all above height $1/2$. They are the earlier calculation's 152 brackets without the lowest one. No central value, individual ordinary zeta zero, completeness of the list or spacing between the missing zeros enters either inequality. Every rearrangement of the remaining quadratic zero mass consistent with the single trace bound below satisfies the same sign estimates. This discriminant already has a negative start below $d^{7/3}$. The purpose of this later witness is to test the effect of withholding the hardest data. [Earlier first-start bounds](../fixed-weight-delay-2380853/PROOF.md) · [The 151 input intervals](brackets-above-half.txt) · [The earlier brackets and their check](../fixed-weight-delay-2380853/QUADRATURE.md)

## Bounding all unobserved ordinates

For the completed even quadratic function $\Lambda_\chi$ set

$$
 R=\frac{2}{3}\frac{\Lambda_\chi'(2)}{\Lambda_\chi(2)}
   -\sum_{\text{151 brackets}}\frac{2}{9/4+\lambda^2}.
$$

Choose one enclosed zero per bracket and its conjugate. By the paired Hadamard product at 2 the residual is exactly $\sum_{\rm unobserved}(9/4+\lambda^2)^{-1}$, counting both signs and multiplicity. At every real $\lambda$, including zero,

$$
 |h_\lambda(u)|\le |c_\lambda|
 =\frac1{9/4+\lambda^2}\sqrt{\frac{9/4+\lambda^2}{1/4+\lambda^2}}
 \le\frac{3}{9/4+\lambda^2}.
$$

Consequently the missing terms cost at most $3R$, even if they combine with the worst possible phases. The calculation certifies $8/9 < R < 0.984$. A hypothetical double central zero would use exactly $8/9$ of this budget. This tests the sign against both possibilities for the centre. It supplies no evidence for an actual central zero.

The bracket endpoint signs are checked against the theta integral with the certified trapezoidal error from the earlier field calculation. For $s=2$ its numerator for $2\Lambda_\chi'(2)$ inserts $x\sinh(3x/4)$, and its denominator for $\Lambda_\chi(2)$ inserts $\cosh(3x/4)$. The strip-edge absolute integral of $zG(z)e^{3z/4}$ is bounded by $100d^2$ since $|G(z)|\le d^2e^{-7|\Re z|/4}$ there. The spatial tail beyond 22 obeys the same bound as the previously treated weights. This gives the $10^{-48}$ quadrature allowance for both integrals. [Theta integral, edge and tail bounds](../fixed-weight-delay-2380853/QUADRATURE.md)

An independent determination at 2 uses

$$
 \frac{2}{3}\frac{\Lambda_\chi'(2)}{\Lambda_\chi(2)}
 =\frac{\log(d/\pi)-\gamma_E+2L'(2,\chi_d)/L(2,\chi_d)}{3}.
$$

Sum $-\chi_d(p)\log(p)/(p^2-\chi_d(p))$ over $p\le300{,}000$ for the logarithmic derivative. The remaining absolute tail at cutoff $M$ is at most $2(\log M+1)/M$ by summing $2\log n/n^2$ over all integers $n>M$. Both traces enclose the same value.

## Evaluating the observed terms

The first calculation expands $1/(\alpha+t/u)-1/(1+\alpha+t/u)$ through degree two in $t/u$ and integrates against $e^{-t}dt$, where $\alpha=1/2-i\lambda$. The absolute remainder for one zero is at most $6u^{-3}(|\alpha|^{-4}+|1+\alpha|^{-4})$. The second integrates the original Laplace kernel directly using eight-point Gauss–Legendre quadrature on 24 unit intervals. On radius-one disks about real points in those intervals the integrand has absolute value at most 5 since $u>1400$. On each interval the error in each component is at most $5/[17{16\choose8}^2]$ by the Hermite interpolation remainder. Each component of the remaining tail is at most $4e^{-24}$. Both routines enclose the full ordinate intervals, including their occurrence in the phase.

For the ordinary factor use its entire inverse-square mass $2+\gamma_E-\log(4\pi)$. For the archimedean term use $e^{-u/2}/(2\tanh u)$. For the upper bounds on prime powers use $(2/3)(1+3\delta_{n,\Delta})+(39/5)e^{-u/6}$ with the degree and discriminant $(2,d)$ for the field and $(1,1)$ for the character square upper bound. The ramified squares are omitted in the character sum and can only lower its upper bound. The signed tail has the opposite sign from the sum of its quadratic zero terms and corrections. [Prime-power and archimedean bounds](PROOF.md) · [Two interval calculations](packets.py) · [Replay output](evidence/packets.txt)
