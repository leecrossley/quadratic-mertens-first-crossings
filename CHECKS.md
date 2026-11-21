# Verification

The asymptotic family result has a written analytic proof. The numerical programs check finite illustrations in a field whose first negative average was already bounded. All intervals in the table enclose the complete infinite quantity

```math
 \sqrt y\log y\sum_{p>y}\frac{\chi_d(p)\psi(p)}p(1-y/p),\qquad d=2{,}380{,}853.
```


| Start | Untwisted | Character of 5 | Character of 13 |
|---:|---:|---:|---:|
| 163 | (−1.755, −1.754) | (0.249, 0.250) | (−0.013, −0.012) |
| 2,380,853 | (−1.139, −1.138) | (1.677, 1.678) | (−1.683, −1.682) |
| 7,142,559 | (−2.997, −2.996) | (1.046, 1.047) | (−0.912, −0.911) |

On the finite interval $`(33698,67396]`$ the untwisted log-weighted sum lies in $`(-1740.81,-1740.80)`$. There are 3,103 primes. The largest absolute twisted sum over the 20 nontrivial primitive quadratic characters of conductor at most 31 is attained by discriminant $`-11`$ and lies in $`(879.94,879.95)`$. The starts are illustrative choices, including a small start with weak secondary signals and the round multiples $`d,3d`$. [Exact output](evidence/check.txt)

## Complete future tails

For each of the three positive fundamental conductors $`q=d,5d,13d`$, the primitive even character has positive root number. Write $`x=\pi n^2/q`$ and $`J_s(x,r)=\int_r^\infty e^{-xt}t^{s/2-1}dt`$. Splitting the theta integral at $`r`$ gives

```math
 (q/\pi)^{s/2}\Gamma(s/2)L(s,\chi_q)=
 \sum_{n\ge1}\chi_q(n)[J_s(x,r)+J_{1-s}(x,1/r)].
```

The first calculation uses $`r=1`$ and the exponential integral and complementary error function. The other uses $`r=2`$ and upper incomplete gamma functions. In both cases $`s=1,2`$. For $`x>1`$, $`r,1/r\ge1/2`$, each of the integrals past its lower endpoint is at most $`3e^{-x/2}`$. For an integer cutoff $`N`$ the residual after $`N`$ is at most $`6q e^{-\pi N^2/(2q)}/(\pi N)`$ by the Gaussian integral bound. The scripts enclose the special functions with Arb. [FLINT real ball arithmetic](https://flintlib.org/doc/arb.html)

In the first calculation, with $`C_s=\sum_p\chi_q(p)/p^s`$ one has

```math
 C_s=\log L(s,\chi_q)-\tfrac12\log\left(\zeta(2s)\prod_{p\mid q}(1-p^{-2s})\right)
       -\sum_p\chi_q(p)\bigl(\operatorname{atanh}(p^{-s})-p^{-s}\bigr).
```

Terms beyond $`M`$ in the last sum cost at most $`2/M^{3s-1}`$. Subtract the two finite prime prefixes from $`C_1,C_2`$ and form their tapered difference. The second calculation directly removes $`\log(1-\chi_q(p)/p^s)^{-1}-\chi_q(p)/p^s`$ with absolute tail at most $`1/((2s-1)M^{2s-1})`$ after $`M=3d`$. It uses Euler's criterion and an odd-only sieve. In the raw prime window it compares exact integer products by correctly rounded decimal logarithms. The secondary intervals from its different Euler remainder are coarser than the printed primary intervals and suffice to check all the strict magnitude comparisons. [First calculation](scripts/verify.py) · [Theta integral](scripts/weighted.py) · [Second calculation](scripts/independent.py)

## Replay

```sh
python3 -m pip install -r requirements.txt
sh verify-release.sh
sh check-lean.sh /path/to/mathlib4
```

The Lean script uses the toolchain in [lean-toolchain](lean-toolchain) and the [pinned mathlib revision](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474) with its compiled cache. The source checks the ratio inequality, the squared-tilt identity and conversion from weighted to unweighted mass. The analytic estimates and prior results are used in the written proof. [Lean source](Correlation.lean) · [Axiom lists](evidence/lean.txt)
