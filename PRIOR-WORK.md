# Prior work and scope

**Question.** Daniel R. Johnston (UNSW Canberra at ADFA) asked for the first negative value of the prime-ideal Mertens error in two fields and an upper bound on the first sign change in a family. Alia Hamieh, Habiba Kadiri, Greg Martin and Nathan Ng recorded the question as Problem 8 in their 2024 list. The two fields named there are $\mathbb Q(\sqrt5)$ and $\mathbb Q(\sqrt{13})$. The earlier prime-window work chose the larger Yokoi family and supplied a density-one upper bound, arbitrarily late first crossings and a finite census. Its §6 also explains how a search terminates for a field once oscillation is known. [Problem 8](https://arxiv.org/pdf/2407.03530#page=4) [Earlier family release](https://github.com/leecrossley/yokoi-mertens-crossing-bounds/releases/tag/v1.0.0)

**Oscillation.** Harold Diamond and János Pintz proved oscillation for the rational prime product. Jan Büthe located a negative value for the rational prime reciprocal sum, giving the rational product bound quoted in the problem list. Shehzad Hathi and Ethan Lee proved arbitrarily large oscillations of the scaled number-field product error if a nonreal zero lies at least as far right as every other nontrivial zero. The critical-line theorem supplies that condition here, since the Riemann zeta factor has nonreal zeros. Qualitative finiteness of the first crossing therefore already follows from their theorem. [Diamond and Pintz](https://doi.org/10.5802/jtnb.687) · [Büthe](https://arxiv.org/abs/1503.01277) · [Hathi and Lee, Theorem 1](https://arxiv.org/pdf/2112.02166#page=3)

**Explicit estimates.** Grenié and Molteni supply the integrated prime ideal explicit formula used in the proof, including the gamma-factor terms and the finite part at zero. Révész studied effective oscillations of the prime ideal counting error. His 1983 Part I, Theorem (3.1)–(3.3), bounds the absolute size of that error in an interval associated with a zero. Garcia and Lee bound errors in number-field Mertens formulas. Broadbent, Fiori, Kadiri, Ng and Wilk give recent estimates and an explicit formula for rational prime Mertens sums. These papers supply context for using explicit formulas and smoothing in this problem. The triangle kernel and simultaneous approximation are classical. [Grenié and Molteni](https://arxiv.org/abs/1312.4465) · [Révész, p. 59](https://users.renyi.hu/~revesz/irregprimeidi.pdf#page=3) · [Garcia and Lee](https://arxiv.org/abs/2007.10313) · [Broadbent et al.](https://arxiv.org/abs/2608.01498)

Hathi and Lee already use the integrated Chebyshev error and integration by parts in §§2.4 and 4.3. They refer to Ingham's presentation of Littlewood's argument for the large positive and negative values. The constants in that oscillation calculation are given asymptotically for each field. [Hathi and Lee, §2.4](https://arxiv.org/pdf/2112.02166#page=7) · [Product comparison in §4.3](https://arxiv.org/pdf/2112.02166#page=11)

**What this note adds.** It gives a fully specified bound before looking at a single prime or zero of the input field. The main steps are the uniform signed comparison (6), the cancellation forced near $x=1$, and an explicit upper bound on when the smoothed zero sum can return sufficiently close to its initial value. The argument applies to every real quadratic fundamental discriminant. It supplies the requested family bound in Problem 8 for this whole class. The numerical example $d=9413$ is reproduced from the earlier census.

**Priority check, 21 November 2026.** Searches covered arXiv, the workshop list, the comparative-prime-number-theory bibliography and searches combining first negative value, first sign change, Skewes number, prime-ideal Mertens product, discriminant, real quadratic and Yokoi. The OpenAlex query for citations to the list or Hathi–Lee returned ten records, including work on integrated errors, prime races and explicit Mertens constants. I found no earlier published upper bound specified in terms of the discriminant for the first negative prime-ideal Mertens product error in every real quadratic field. Unindexed papers and unpublished arguments can escape such a search. [Citation query](https://api.openalex.org/works?filter=cites%3AW4400433728%7CW4200631075&per_page=100) · [Comparative prime number theory bibliography](https://doi.org/10.1016/j.exmath.2024.125644)

## The zero-location input

The formal result used here is LFunction_eq_zero_re, whose type is DirichletLZerosOnLine. It quantifies over all nonzero moduli, all Dirichlet characters and all zeros in the open strip. The standard identity with the Riemann zeta function at modulus one means this single theorem supplies both factors. In a built copy of the upstream project the specialization reads

~~~lean
import Main
import FirstCrossing

example (d : ℕ) [NeZero d] (χ : DirichletCharacter ℂ d) (s : ℂ)
    (h₀ : 0 < s.re) (h₁ : s.re < 1)
    (hz : riemannZeta s * DirichletCharacter.LFunction χ s = 0) : s.re = 1 / 2 :=
  FirstCrossing.product_zero LFunction_eq_zero_re d χ s h₀ h₁ hz
~~~

Andrew Sutherland's audit reports kernel replay on 175,187 modules, acceptance of the full export by nanoda and con-leche, and a con-leche comparison matching the five headline declarations. The axiom report for LFunction_eq_zero_re lists propext, Classical.choice and Quot.sound. The audit page gives the status of the other runs separately. [Source statement](https://github.com/Deicyde/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Statements.lean) · [Definition of the theorem](https://github.com/Deicyde/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean) · [Independent audit](https://math.mit.edu/~drew/grh/) · [Comparison log](https://math.mit.edu/~drew/grh/con-leche-compare.log)

For this release I matched the author's original source archive to the audit hash and compared the extracted statement and theorem declaration files byte for byte with the pinned public mirror. I checked the axiom and comparison log hashes against Sutherland's manifest. The local Lean replay used the exact statement as a hypothesis for the product lemma. It also checked finite simultaneous recurrence for arbitrary real frequencies and the integer cutoff estimates. The full upstream kernel replay is Sutherland's. The passage through the explicit formula, partial summation and smoothing is the written proof in this repository. [Axiom log](https://math.mit.edu/~drew/grh/audit.log) · [Upstream manifest](https://math.mit.edu/~drew/grh/SHA256SUMS) · [Local Lean reports](evidence/lean.txt)

| File checked | SHA-256 |
| --- | --- |
| Original source archive | 9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc |
| Statements.lean | 79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf |
| Main.lean | 017645ca448f2fd1f6fd5c4c2cb2c6e96e472725be13f6e180ca6e1574360939 |
| Axiom log | 0a1473fce6eed840011f4a76b1c51558fc6f03edd1e6bd1ee542e6c738d87a62 |
| Comparison log | 5a068bf55f24904eea9f05eda947c63d43bdee3c6ab0490e43943a3bd9af1f6e |
