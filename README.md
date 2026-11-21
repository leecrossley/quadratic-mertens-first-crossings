# How long can a prime product stay above its predicted curve?

In the field $\mathbb Q(\sqrt{5004173})$, the prime-ideal Mertens product stays ahead until just past 201,402. Two calculations check every interval from 2 to that first crossing.

The theorem concerns the whole family. Write $d=m^2+4$ with $m$ positive and odd and $d$ squarefree. Let $S_d$ be the first crossing, the infimum of the points where the product is strictly below its main term. Define $M(D)$ as the largest $S_d$ among these fields with $d\le D$. For some absolute $c>0$ and every sufficiently large $D$,

$$
M(D)>\exp\!\big(c(\log D)^{1/5}\big).
$$

Any fixed power of the number of digits in $d$ will underestimate the wait for infinitely many fields. The older lower bound was of order $\log D / ((\log\log D)^2\log\log\log D)$. The exponent $1/5$ comes from the cost of biasing the primes enough to keep the product ahead at **every** point in a growing interval. The constant and starting discriminant are implicit. [Proof](PROOF.md) · [Earlier lower bound, §5](https://github.com/leecrossley/yokoi-mertens-crossing-bounds/blob/v1.0.0/PROOF.md) · [Literature and scope](PRIOR-WORK.md)

## The field with first crossing near 201,402

The product jumps when a prime ideal enters. Between jumps the product stays constant while its predicted curve increases. Checking just after a jump can miss the first crossing.

For $d=2237^2+4=5{,}004{,}173$, each calculation checks the limit from the left at every successive jump. Both find interval 8,901, beginning at 201,337 and ending at 201,403, and give

$$
201402.091859<S_d<201402.091860 .
$$

The first calculation derives the residue from a complete character period, a rigorous tail bound, and the real quadratic class number formula. The fundamental unit is $(2237+\sqrt d)/2$, by the minimum-unit argument for this family. The class number comes out as 48. Prime splitting is computed by Euler's criterion and the local factors are multiplied. The second calculation obtains the residue directly from a Dirichlet $L$-function and sums the logarithms of independently generated local factors. Both use Arb interval arithmetic. This is a worked example from a search, with no claim that it is the largest below a given discriminant. [Example code](example.py) · [Certified output](evidence/example.txt) · [Fundamental unit and class formula, §6](https://github.com/leecrossley/yokoi-mertens-crossing-bounds/blob/v1.0.0/PROOF.md)

## Checking the result

The family theorem has a written analytic proof. Its ordinary prime estimate uses Schoenfeld's theorem and the Riemann zeta zero-location result. Dahl and Kala's moment estimate transfers the weighted calculation to genuine fields. The lower bound uses Granville and Soundararajan's unconditional character approximation with its exceptional fields counted. [Proof and references](PROOF.md) · [Zero-location verification](https://math.mit.edu/~drew/grh/)

~~~sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
./verify-release.sh
~~~

The script verifies the manifest, enumerates a finite model using exact fractions, and reproduces the numerical example. The separate Lean file checks the one-prime bias inequality for all inputs satisfying its hypotheses. To reproduce that check, set `REPO` to the absolute checkout path and run the following from a Mathlib v4.33.1 checkout using Lean v4.33.1. [Finite model checks](evidence/check.txt) · [Lean source](Tilt.lean) · [Lean output](evidence/lean.txt) · [Mathlib revision](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474)

~~~sh
lake env lean -R "$REPO" "$REPO/Tilt.lean"
~~~
