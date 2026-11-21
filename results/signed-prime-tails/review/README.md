# Review the 51 real values for discriminant 2,380,853

The [review packet](https://github.com/leecrossley/quadratic-mertens-first-crossings/releases/download/real-axis-prime-test-v1/real-axis-review.zip) includes the proof, its hypotheses, the proof sources and replay outputs. The [five-page handout](https://github.com/leecrossley/quadratic-mertens-first-crossings/releases/download/real-axis-prime-test-v1/real-axis-review.pdf) includes a printable copy of every interval.

The [machine-readable table](real-values.json) encloses the completed logarithmic derivative divided by $L=\log(3d)$. The first 49 rows use $s=1/2+j/(16L)$, the final two $s=1,2$. All endpoints are exact decimal strings and each interval has width $3\times10^{-42}$.

From this directory, check the four signed witnesses in the [finite proof](../REAL-AXIS-FIELD.md) with a standard Python installation.

~~~sh
python3 -B from_table.py
~~~

The checker uses rational polynomials and outward-rounded decimal intervals. Its lower bounds on the four signed margins are 1.364038, 1.828247, 0.518515 and 0.273694. The signs of the average use RH for the ordinary zeta function and GRH for this field's primitive quadratic Dirichlet function. The 51 derivative enclosures themselves follow unconditionally from the theta integral. [Table-only replay](table-only.txt)

To check the enclosures, install the package in the repository's [requirements file](../../../requirements.txt) and run the following command with assertions enabled.

~~~sh
python3 -B recompute.py
~~~

This recomputes every measurement twice, checks that the two Arb enclosures overlap, and verifies that the published decimal endpoints contain both full enclosures. The trapezoidal and Gaussian programs in the original release also replay the four signs end to end. [Enclosure replay](real-values-replay.txt) · [Tagged release](https://github.com/leecrossley/quadratic-mertens-first-crossings/releases/tag/real-axis-prime-test-v1)

The [general real-axis proof](../REAL-AXIS.md) gives a sufficient condition for a negative start by a power of the discriminant. Whether every sufficiently large Yokoi field has such a start for one common exponent remains open. Two synthetic zero patterns satisfy the limiting positivity tests. Excluding these possibilities for genuine quadratic Euler products requires further arithmetic.
