# What a late prime average requires after the small primes are removed

Lee Crossley

In a real quadratic field, give each split prime a score of $`+1`$, each inert prime $`-1`$, and each ramified prime zero. Multiply these scores to score an integer, with 1 scoring $`+1`$. Throw out all multiples of any selected primes up to $`(\log d)^2`$, where $`d`$ is the field discriminant. Then keep a running total over the integers that remain.

Suppose the future Mertens average over the field's prime ideals stays nonnegative at every start from 2 through $`d^A`$, for a sufficiently large absolute constant $`A`$. For every sufficiently large $`d`$ the running total must go negative and then positive again, **both by $`d^8`$**, for every selection of the small primes. The theorem gives a minimum size for each change of sign. Periodicity alone gives both signs by one more than the period of the sieved character, which can exceed every fixed power of $`d`$. It includes all sufficiently large Yokoi discriminants $`d=m^2+4`$ with $`m`$ odd and $`d`$ squarefree. The analytic proof uses RH and quadratic Dirichlet GRH. Alpöge's announced Dirichlet GRH theorem supplies this input. [Theorem and proof](PROOF.md) · [Announcement](https://alpo.ge/remark.pdf) · [Independent formal checks](https://math.mit.edu/~drew/grh/)

At an exact central zero the functional equation forces two signed integrals to vanish. For a zero very close to the centre a sine weight gives the same two changes of sign. A field that misses either required change has a negative prime average by a fixed power of $`d`$. Whether such an exponent works for every sufficiently large Yokoi field remains open.

For $`d=2{,}380{,}853`$, remove all 47 primes through 215. The count first reaches $`-1`$ at 331 and first recovers to $`+1`$ at 367. Up to 367 only 1 and primes survive this sieve. Under field GRH, the original prime-ideal average stays positive past 222 trillion in this same field. Two programs reproduce the integer counts. [Checks and numerical results](CHECKS.md) · [Earlier prime-average certificate](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/cae0113ded2504f0f29857045ca2a3028ddaab55/results/fixed-weight-delay-2380853/PROOF.md)

For any fixed $`K>0`$ the proof also permits a deletion modulus as large as $`\exp(K(\log d)^2)`$ with a witness exponent depending on $`K`$. It gives a second test using the relative positive and negative mass of a signed sum. [Related work and novelty search](PRIOR-WORK.md)

Among all choices an exact rule delays the first negative count as long as possible. Remove the multiples of every eligible inert prime and keep the split primes. In $`d=2{,}380{,}853`$ all $`2^{47}`$ choices go negative by 49,937 and recover by $`d^6`$, with no zero-location hypothesis. The optimal choice for the first dip recovers six integers later. Keeping just one more prime, 43, moves the first recovery to **137,705,720,539**. The sharp and Gaussian mass tests have the same extremal choice when the central value is nonnegative. [Sieve comparison and proof](SIEVE-CHOICE.md) · [Independent checks](SIEVE-CHECKS.md)

## Verification

Install the dependency in [requirements.txt](requirements.txt) in a Python 3.11+ environment and run with a C++20 compiler available

```sh
sh verify-release.sh
```

Run `sh check-lean.sh /path/to/mathlib4` to check six supporting lemmas. The original four are `cosine_mass`, `prefix_witness`, `ordered_budget` and `exponent_eight_margins`. The sieve comparison adds `negative_prefix_of_dilates` and `mass_ratio_order`. The number-theoretic arguments are in the written proofs. [Original checks](CHECKS.md) · [Sieve-choice checks](SIEVE-CHECKS.md) · [File hashes](SHA256SUMS)
