# Verification

The analytic theorem is proved in [the paper](PROOF.md). The following are independent checks on its finite arithmetic example and on portions of the argument.

For $d=533$, let $C_k=\sum_p a_d(p)/p^k$ for $k=1,2$. To evaluate $C_k$, start with $\tfrac12\log(L(k,\chi_d)/L(k,\chi_5))$, remove the three ramified factors, and subtract the terms of prime-power index at least two. Away from ramification the even powers cancel and the first omitted term beyond a prime cutoff $M$ is cubic in $p^{-k}$. A bound $2/M^{3k-1}$ suffices by a geometric series and the integral test. Subtracting the two finite prefixes at $y$ gives $W(\log y)$ with its entire future tail. The first program uses Arb's Dirichlet functions and local logarithms; the second computes the special values from finite quadratic Fourier series and sums the odd powers with explicit remainders. [First calculation](scripts/verify.py) · [Second calculation](scripts/independent.py)

For the value of $F_{533}(30)$, the first program sums the correction to $\log\zeta_K(2)$ through norm $10^5$. If $x=1/q$, the two terms $-x\log(1-x)$ and $-\log(1-x^2)$ each differ from $x^2$ by at most $x^3$. There are at most two ideals at a given norm. The tail bound $4/M^2$ and the integrated logarithm yield the narrow interval. The second program directly sums averaged prime-ideal jumps through one million. The remaining unnormalised positive contribution is at most $2y/M$, giving a coarser independent certificate of the sign. No zero values are inputs to either finite example. [Numerical results](evidence/check.txt)

The exact sign test in the last section of the proof is checked a second way. The first program computes its two sides from the two independent field products. The second starts with the oriented prime tail and adds the square-norm, local-log and ramified-prime corrections directly, with error at most $2N_y/M$ from primes beyond its cutoff. It obtains a strict crossing from the resulting lead and a separately computed threshold.

## Replay the Lean lemmas

Use the Lean toolchain named in [lean-toolchain](lean-toolchain). In a checkout of the [pinned mathlib revision](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474), run `lake exe cache get` once. Then, from this repository, run

```sh
sh check-lean.sh /path/to/mathlib4
```

The script runs the source file, checks its printed axiom lists against [the recorded output](evidence/lean.txt) and checks the toolchain version. The public arithmetic workflow runs the two numerical programs and verifies the file hashes.

[Window.lean](Window.lean) checks the positive diagonal lower bound with arbitrary finite multiplicities, the orientation identity, the two taper identities and the deduction of an adverse endpoint from a ceiling and a displacement. The numerical programmes and these lemmas do not formalise the explicit formula, the limiting zero count or the Fourier estimates in the paper.
