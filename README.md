# A positive prime model that passes every fixed quadratic twist test

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24417499.svg)](https://doi.org/10.5281/zenodo.24417499)

The field of discriminant 13 exposed the earlier prime model because that model still copied its splitting pattern. This construction changes the signs on ordinary primes so that testing against 13 gives the prime sums of a nonprincipal character. The same assignment handles every other fixed quadratic reference.

The untwisted prime bias grows in proportion to $`\log D`$, where $`D`$ is the scale of the construction. Its decreasing Mertens average stays positive at every start in the central-zero case. At the same time, the normalised correlation with each fixed secondary character stays bounded through **any prescribed finite cutoff**. With a close pair of zeros in place of the central zero, positivity can last through any prescribed power of $`D`$. The statement uses RH and quadratic Dirichlet GRH. [Proof](PROOF.md)

The continued products even have the degree-one zero counts with the expected change in the conductor term when twisting an odd discriminant whose only possible common prime factor with the reference conductor is 13. Adjusting when finitely many secondary coefficients begin leaves their zeros fixed. There is also a version where the added coefficients start immediately and each fixed secondary bias is $`O(\sqrt{\log D\,\log\log D})`$ through every fixed power of $`D`$. These are statements about a constructed prime assignment. The implication at a polynomial scale in genuine Yokoi fields remains open. [Comparison with earlier results](PRIOR-WORK.md)

To replay the finite prime construction and the arithmetic checks, install [requirements.txt](requirements.txt) and run

```sh
sh verify-release.sh
```

Two programs verify the interpolated moments and period bounds. The release includes the Lean source for five supporting lemmas. [Verification](CHECKS.md) · [File hashes](SHA256SUMS)
