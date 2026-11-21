# A prime average that stays positive past 222 trillion

Assume the critical-line property for the Riemann zeta function and $L(s,\chi_d)$ for $d=2{,}380{,}853$ (field GRH). Alpöge's announced Dirichlet GRH theorem supplies this input. The proof uses it for the zero expansion, the bound for the remaining zero sum and the explicit prime estimates. [Announcement](https://alpo.ge/remark.pdf) [Independent formal checks](https://math.mit.edu/~drew/grh/)

For $d=2{,}380{,}853=1543^2+4$, the Mertens product over prime ideals first falls below its main term at about 143,054. How long does that dip take to show up in a fixed weighted average? The average here starts at $y$ and gives the future log error weight $y\thinspace dt/t^2$.

Every real start through $d^{9/4}$, more than **222 trillion**, gives a positive average. At $d^{7/3}$, less than **757 trillion**, the average is negative. The normalised weighted excess of split primes over inert primes in the finite range from that start through $10^{26}$ exceeds **0.23**, enough on its own to force the sign. The certificate bounds this prime sum analytically. [Proof](PROOF.md) · [Earlier raw crossing](https://github.com/leecrossley/yokoi-mertens-optimal-starts/blob/v1.0.0/PROOF.md)

A direct prime-ideal calculation covers the small starts. At large starts the proof uses 152 certified quadratic zero brackets and a bound for the entire remaining zero sum. Explicit contributions from split prime squares cover the intervals where the zero sum alone leaves the sign undecided. A second calculation checks every quadratic bracket and the final signed witness by Gaussian quadrature. [Quadrature bounds](QUADRATURE.md) · [Comparison with prior results](PRIOR-WORK.md)

## Replay

Run from this directory with Python 3.10 or later.

~~~sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -B verify.py
python -B witness.py
~~~

The first run checks the continuum of starts and both signs at the witness. The second evaluates the theta function and the zero kernels by a different integration method. Both use Arb's outward-rounded ball arithmetic. [Main output](evidence/verification.txt) · [Second output](evidence/witness.txt) · [File hashes](SHA256SUMS)
