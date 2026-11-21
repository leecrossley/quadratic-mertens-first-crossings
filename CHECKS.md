# Verification

The construction of an infinite assignment and its analytic continuation are proved in [the paper](PROOF.md). The finite checks verify the interpolation, rounding, exceptional twist and period calculations on actual primes.

* The adjacent bins $`(20000,30000]`$ and $`(30000,40000]`$ contain 1,941 primes in total. The four square classes use the characters of 5 and 13. For the four tests $`1,\chi_5,\chi_{13},\chi_{65}`$ the targets are respectively $`\chi_{13},\chi_{65},\chi_{17},\chi_5`$. Both the constant and linear moments are matched exactly in each bin. One rounding sequence for each class runs across the shared boundary. Each fractional sign comes from a solution with $`|A|+|B|<1/2`$, and every rounded class prefix differs from its fractional sum by less than 2.
* With $`k=32`$ the 32 prime periods start at 223 and end at 401 and their integer sum is 9,850. Every positive index below $`223^2=49{,}729`$ is checked. At most one ordinary prime period divides such an index. The special list replaces 223 by 222 and at most two of its periods can divide an index. Dropping one unit in the period sum cancels the factor 17 contributed by changing the base of the special twist. The example also tests projection of the signed class quotas in both versions.
* Arb encloses $`L(1/2,\chi_{17})`$ in $`(0.7216,0.7218)`$. For a separate check the second program directly sums the periodic character through 34,000 and bounds the remainder by partial summation. It obtains an enclosure inside $`(0.70,0.75)`$.

The first program uses exact rational numbers for interpolation, the Jacobi symbol for prime signs and Arb for the central value. The second uses integer-scaled normal equations, square-residue tables, trial division and a carry in $`[0,1)`$ for rounding. It uses only Python's standard library. [First program](scripts/verify.py) · [Second program](scripts/independent.py) · [Recorded output](evidence/check.txt)

```sh
python3 -m pip install -r requirements.txt
sh verify-release.sh
sh check-lean.sh /path/to/mathlib4
```

Use the toolchain in [lean-toolchain](lean-toolchain) and the [pinned mathlib revision](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474) for the last command. Its five lemmas check the Gram equations, total quota, orthogonal quota, special-class correction and disjointness of prime periods below the cutoff. Analytic continuation, uniform error estimates and the positivity bound are written arguments. [Lean source](Interpolation.lean) · [Axiom lists](evidence/lean.txt)
