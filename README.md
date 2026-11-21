# First Mertens crossings in two real quadratic fields

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24410876.svg)](https://doi.org/10.5281/zenodo.24410876)

Daniel R. Johnston asked where the Mertens product over prime ideals first falls below its main term in the fields $\mathbb Q(\sqrt 5)$ and $\mathbb Q(\sqrt{13})$. He posed the question during Ethan Lee’s talk at the University of British Columbia in June 2024. The answer depends on whether the real argument starts at 2 or at the smallest prime-ideal norm $q_d$. [Problem 8, pp. 4–5](https://arxiv.org/pdf/2407.03530#page=4)

| Field | $q_d$ | Infimum from 2 | Infimum from $q_d$ | First negative integer | First negative ideal norm |
| --- | ---: | ---: | ---: | ---: | ---: |
| $\mathbb Q(\sqrt5)$ | 4 | 3.685768810486 | 8.794547206824 | 28 | 8,581 |
| $\mathbb Q(\sqrt{13})$ | 3 | 2.333070011802 | 12.699403270703 | 16 | 101 |

The real boundaries are rounded to twelve decimal places. In each case the error equals zero at the boundary and becomes strictly negative immediately afterwards. For the infima from 2 the product is still 1. After the first ideal enters, the first negative intervals end at 9 and 13 respectively. Each next jump occurs before an integer sample can detect the negative interval. [Strict enclosures](evidence/check.txt)

The same argument gives a result for Yokoi’s family. Among squarefree discriminants $d=m^2+4$ with $m$ positive and odd, a limiting proportion greater than 7% have their first real crossing in $(2.005,2.99]$. The product is empty throughout this interval, so the proportion concerns the distribution of $L(1,\chi_d)$. Here the fields are ordered by discriminant. The bound uses Dahl and Kala’s distribution theorem for $L(1,\chi_d)$. [Proof and prior work](PROOF.md) [Dahl and Kala, Theorem 2](https://arxiv.org/pdf/1611.02424#page=4)

## Reproduce the calculation

Use Python 3.10 or later. The first two checks use the standard library. The third uses Arb interval arithmetic through python-flint. It calculates the zeta residues by a different formula, factors primes independently, and counts the local classes for the family bound directly.

~~~sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
./verify-release.sh
~~~

The script checks the SHA-256 manifest, runs all three calculations, and compares their output with the recorded results. [Verification output](evidence/check.txt) · [SHA-256 manifest](SHA256SUMS)
