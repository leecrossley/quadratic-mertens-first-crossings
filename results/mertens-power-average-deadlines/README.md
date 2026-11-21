# A sharp deadline for a negative prime-product average

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24412091.svg)](https://doi.org/10.5281/zenodo.24412091)

Across Yokoi's real quadratic fields, suppose the average logarithmic error of the prime-ideal Mertens product is negative when the averaging starts at 2 with weight $2/t$ against $dt/t$. How long can the product stay above its main term? The exact supremum for its first dip is **3.461332112486105…**. Every qualifying field dips earlier, and infinitely many get arbitrarily close to that number. In those extremal fields 3 and all primes up to a large bound are inert, so the product is still 1 on $[2,4)$ and the dip comes before any prime ideal enters.

The family consists of $\mathbb Q(\sqrt d)$ with squarefree $d=m^2+4$ and odd positive $m$. For each fixed start $y\ge 2$ and exponent $s>0$, the proof gives a finite maximisation formula for the sharp family deadline. Each candidate is evaluated from its prime splitting pattern and an absolutely convergent series. For any number field, a negative average with weight $(y/t)^s$ forces a dip before $C y^{1+1/s}/(\log y)^{1/s}$ for all sufficiently large $y$, whenever $C>(2/s)^{1/s}$. [Definitions, proof and sharp value](PROOF.md)

At start 2 the deadline grows without bound as $s$ decreases to zero. If $M(s)$ is that sharp deadline, then

$$
s\log M(s)=\log(1/s)-\log\log(1/s)-\log A_\ast+o(1).
$$

Here $A_\ast$ is the least area under an admissible nonnegative error curve in log coordinates. It is positive, finite, attained and approximable by finite patterns. Exhausting 46,656 assignments through 43 gives $A_\ast>0.4829182931$. The proof gives the rate at which finite minima converge. [Small-exponent theorem](SLOW-WEIGHTS.md) · [Construction and convergence](PATHS.md) · [Finite minima](evidence/areas.txt)

For the original all-field question the sign at the start remains to be proved. If a real quadratic field has a negative $y/t$ average at some $y\le d^a$, its first crossing is $O_a(d^{4a/3})$, using the one-sided critical-line estimate in §2. The sharp family deadline and its small-exponent law use the family residue distribution and the ordinary prime number theorem. [Discriminant-dependent bound](PROOF.md) · [Prior work and scope](PRIOR-WORK.md)

## Reproducing the checks

Run these commands in the release directory with Python 3.10 or later and the dependency in [requirements.txt](requirements.txt).

~~~sh
python3 -m pip install -r requirements.txt
shasum -a 256 -c SHA256SUMS
python3 -B deadlines.py
python3 -B independent.py
python3 -B zeta_check.py
python3 -B area.py
~~~

The first program computes ten comparison deadlines by recurrence. The second certifies both ends of each interval by integrating constant windows directly, and calculates the Yokoi extremum by summing primes and enclosing the remaining tail. Its quadrature for the exponential integral uses a finite expansion on 60 unit panels and bounds the remainder on every panel. The third independently calculates the extremum by Möbius inversion of integer zeta values. The fourth exhausts all admissible signs for six finite minima, with a second integral calculation on every pattern through 37. [Deadline brackets](evidence/deadlines.txt) · [Direct integration](evidence/independent.txt) · [Integer-zeta check](evidence/zeta.txt)

The main theorems have written proofs. [Four auxiliary inequalities](Deadline.lean) were checked with Lean 4.33.1. Set `NOTE` to the absolute release directory and run the following from the [pinned Mathlib checkout](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).

~~~sh
lake env lean -R "$NOTE" "$NOTE/Deadline.lean"
~~~

The kernel reports its axioms for each lemma. [Lean output](evidence/lean.txt)
