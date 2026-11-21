# Two prime products dip. Both weighted averages stay positive.

In $\mathbb Q(\sqrt5)$ the prime-ideal Mertens product first falls below its main term just after $3.68577$. In $\mathbb Q(\sqrt{13})$ the corresponding boundary is about $2.33307$. Yet for both fields the future average of the log error with density $y/t^2$ stays positive for **every** real starting point $y\ge2$. The proof uses RH for the ordinary zeta function and the critical-line property for the two quadratic Dirichlet functions. [Raw crossings and their conventions](https://github.com/leecrossley/quadratic-mertens-first-crossings/blob/ef3e53c/README.md) · [Critical-line input](https://math.mit.edu/~drew/grh/)

For discriminant 5 the normalised average $\sqrt y\log y\,F_5(y)$ has a unique global minimum at $2.64281618<y<2.64281620$. Its value lies between $0.183894$ and $0.183896$. For discriminant 13 the normalised average exceeds $1/40$ throughout. These are the first two members of Yokoi’s family $d=m^2+4$ with $m$ odd and $d$ squarefree. Any assertion that *every* member has a negative start for this fixed weight fails. A bound for all sufficiently large members is still open. [Theorem and proof](PROOF.md) · [Earlier work](PRIOR-WORK.md)

Two programs enclose the finite part up to one million with Arb, one by chords, the other by tangents between prime-ideal norms. An analytic inequality covers the infinite tail. Run the following from this directory with Python 3.10 or later. [Recorded output](evidence/check.txt)

~~~sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
sh verify-release.sh
~~~
