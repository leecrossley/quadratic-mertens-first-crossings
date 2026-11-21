# Delayed Yokoi averages with small quadratic twist correlations

Can a long excess of inert primes be explained by the primes copying the splitting pattern of a second field? In many actual Yokoi fields the excess is larger than every such correlation, even when the comparison field is chosen after seeing the primes.

Let $`d=m^2+4`$ be squarefree with $`m`$ odd. Fix any $`K>0`$. In every sufficiently large discriminant interval $`(D/2,D]`$ there are $`D^{1/2-o(1)}`$ fields where the future Mertens average stays positive for every real start through

```math
 X=2^{\lfloor c_K(\log D/(\log\log D)^2)^{1/3}\rfloor}.
```

At each sufficiently large $`y\le X`$, the absolute weighted correlation with every nonprincipal primitive quadratic character of conductor at most $`y^K`$ is $`O_K(1/\log\log y)`$ times the untwisted prime bias. This includes the characters of 5 and 13. The cutoff exceeds every fixed power of $`\log D`$. Reaching $`d^a`$ for one fixed positive $`a`$ in every field remains open. The proof uses RH and quadratic Dirichlet GRH. [Proof](PROOF.md) · [Prior work](PRIOR-WORK.md)

In the field $`d=1543^2+4=2{,}380{,}853`$ the average was previously proved positive through $`d^{9/4}`$. For the complete prime tails at $`y=163`$, multiplying by $`\sqrt y\log y`$ gives values in $`(-1.755,-1.754)`$ without a twist, $`(0.249,0.250)`$ against 5 and $`(-0.013,-0.012)`$ against 13. At the later start $`y=d`$ both secondary tails are larger in magnitude than the untwisted one. Two calculations cover both starts and $`y=3d`$. [Numerical enclosures](CHECKS.md) · [Earlier positive interval](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/fa7ed4741f735e37fc3552f497952a57f02cbaa2/results/fixed-weight-delay-2380853/PROOF.md)

Install the dependency in [requirements.txt](requirements.txt), then run

```sh
sh verify-release.sh
```

The release contains the paper, verifiers, recorded output and the pinned Lean checks for three supporting lemmas. [How to replay the checks](CHECKS.md) · [File hashes](SHA256SUMS)
