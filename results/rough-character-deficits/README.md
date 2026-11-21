# What a late prime average requires after the small primes are removed

Lee Crossley

In a real quadratic field, give each split prime a score of $`+1`$, each inert prime $`-1`$, and each ramified prime zero. Multiply these scores to score an integer, with 1 scoring $`+1`$. Throw out all multiples of any selected primes up to $`(\log d)^2`$, where $`d`$ is the field discriminant. Then keep a running total over the integers that remain.

Suppose the future Mertens average over the field's prime ideals stays nonnegative at every start from 2 through $`d^A`$, for a sufficiently large absolute constant $`A`$. For every sufficiently large $`d`$ the running total must go negative and then positive again, **both by $`d^8`$**, for every selection of the small primes. The theorem gives a minimum size for each change of sign. Periodicity alone gives both signs by one more than the period of the sieved character, which can exceed every fixed power of $`d`$. It includes all sufficiently large Yokoi discriminants $`d=m^2+4`$ with $`m`$ odd and $`d`$ squarefree. The analytic proof uses RH and quadratic Dirichlet GRH. Alpöge's announced Dirichlet GRH theorem supplies this input. [Theorem and proof](PROOF.md) · [Announcement](https://alpo.ge/remark.pdf) · [Independent formal checks](https://math.mit.edu/~drew/grh/)

At an exact central zero the functional equation forces two signed integrals to vanish. For a zero very close to the centre a sine weight gives the same two changes of sign. A field that misses either required change has a negative prime average by a fixed power of $`d`$. Whether such an exponent works for every sufficiently large Yokoi field remains open.

For $`d=2{,}380{,}853`$, remove all 47 primes through 215. The count first reaches $`-1`$ at 331 and first recovers to $`+1`$ at 367. Up to 367 only 1 and primes survive this sieve. Under field GRH, the original prime-ideal average stays positive past 222 trillion in this same field. Two programs reproduce the integer counts. [Checks and numerical results](CHECKS.md) · [Earlier prime-average certificate](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/cae0113ded2504f0f29857045ca2a3028ddaab55/results/fixed-weight-delay-2380853/PROOF.md)

For any fixed $`K>0`$ the proof also permits a deletion modulus as large as $`\exp(K(\log d)^2)`$ with a witness exponent depending on $`K`$. It gives a second test using the relative positive and negative mass of a signed sum. [Related work and novelty search](PRIOR-WORK.md)

## Verification

Install the dependency in [requirements.txt](requirements.txt) in a Python environment and run

```sh
sh verify-release.sh
```

Lean checks four supporting lemmas, `cosine_mass`, `prefix_witness`, `ordered_budget` and `exponent_eight_margins`, through `sh check-lean.sh /path/to/mathlib4`. The complete number-theoretic argument is in the written proof. [What each check covers](CHECKS.md) · [File hashes](SHA256SUMS)
