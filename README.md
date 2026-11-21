# First Mertens crossings in two real quadratic fields

Daniel R. Johnston asked where the Mertens product over prime ideals first falls below its main term in the fields $\mathbb Q(\sqrt 5)$ and $\mathbb Q(\sqrt{13})$. He posed the question during Ethan Lee’s talk at the University of British Columbia in June 2024. Both crossings happen before the first prime ideal enters the product. [Problem 8, pp. 4–5](https://arxiv.org/pdf/2407.03530#page=4)

| Field | First real crossing lies between | First negative integer argument | First negative prime-ideal norm |
| --- | --- | ---: | ---: |
| $\mathbb Q(\sqrt 5)$ | 3.685768810485 and 3.685768810486 | 28 | 8581 |
| $\mathbb Q(\sqrt{13})$ | 2.333070011801 and 2.333070011802 | 16 | 101 |

At the real crossing the error equals zero. It is strictly negative from just after that point until the next prime-ideal norm, respectively 4 and 3. At a norm the convention is to include every prime ideal of that norm. This accounts for the difference between the three columns.

The same argument gives a result for Yokoi’s family. Among squarefree discriminants $d=m^2+4$ with $m$ positive and odd, a limiting proportion greater than 7% have their first real crossing in $(2.005,2.99]$. Here the fields are ordered by discriminant. The bound uses Dahl and Kala’s distribution theorem for $L(1,\chi_d)$. [Proof and prior work](PROOF.md) · [Dahl and Kala, Theorem 2](https://arxiv.org/pdf/1611.02424#page=4)

## Reproduce the calculation

Use Python 3.10 or later. The first two checks use the standard library. The third uses Arb interval arithmetic through python-flint. It calculates the zeta residues by a different formula, factors primes independently, and counts the local classes for the family bound directly.

~~~sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
./verify-release.sh
~~~

The script checks the SHA-256 manifest, runs all three calculations, and compares their output with the recorded results. [Verification output](evidence/check.txt) · [SHA-256 manifest](SHA256SUMS)
