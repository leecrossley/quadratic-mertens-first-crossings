# Verification

The infinite construction and its quantifiers are proved in [the paper](PROOF.md). The finite example uses $X_1=2^{24}$ and ordinary primes through $X_1+2^{18}$. The two choices $(\cos\theta,\cos\beta)=(1,0)$ and $(3/5,-4/5)$ check independent sign choices, floor rounding and both directions of the fixed reference table. The second packet parameter choice here illustrates signed allocation; the near-central all-start theorem uses $\theta$ small enough for the interval specified in its statement.

The first program sieves a single packet and evaluates the change of the weighted discrepancy and the exact change of the prime-ideal log average for that packet, at $X_1/3$ and $X_1$. Arb interval arithmetic encloses its contribution to the rise. A Dirichlet-function evaluation encloses the central value for the base twist. The second program uses a different prime sieve, modular exponentiation and rational intervals. It bounds $\log2,\log3$ by the series for $\operatorname{atanh}$ and bounds square roots by integer square roots. A direct sum of the periodic series at $s=1/2$, with its Abel remainder, independently proves that the base twist has positive central value. [First calculation](scripts/verify.py) · [Standard-library calculation](scripts/independent.py) · [Outputs](evidence/check.txt)

The reported numerical rises are contributions of the first finite packet. The estimates for every subsequent packet and the positive all-start bound are analytic. The base bound for field 13 has its own two interval verifiers. [Base certificate](https://github.com/leecrossley/yokoi-mertens-positive-averages-5-13/releases/tag/v1.0.0)

## Replay the Lean lemmas

Use the Lean toolchain named in [lean-toolchain](lean-toolchain). In a checkout of the [pinned mathlib revision](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474), run `lake exe cache get` once. Then, from this repository, run

```sh
sh check-lean.sh /path/to/mathlib4
```

The script runs the source file, checks its printed axiom lists against [the recorded output](evidence/lean.txt) and checks the toolchain version. The public arithmetic workflow runs the two numerical programs and verifies the file hashes.

[Packets.lean](Packets.lean) checks both sign allocations, their total absolute mass, the rounded sums, the quadratic zero factor and the signed-tail inequality. The complex continuations, prime counts and the all-start average are proved in prose.
