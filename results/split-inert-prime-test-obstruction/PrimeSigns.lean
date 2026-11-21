import Mathlib

open scoped BigOperators

namespace SplitInert

/-- A cosine difference matrix is positive semidefinite for any sample points. -/
theorem cosine_form {ι : Type*} [Fintype ι] (a x : ι → ℝ) :
    0 ≤ ∑ i, ∑ j, a i * a j * Real.cos (x i - x j) := by
  have h (i j : ι) :
      a i * a j * Real.cos (x i - x j) =
        (a i * Real.cos (x i)) * (a j * Real.cos (x j)) +
        (a i * Real.sin (x i)) * (a j * Real.sin (x j)) := by
    rw [Real.cos_sub]
    ring
  simp_rw [h, Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.sum_mul]
  exact add_nonneg (mul_self_nonneg _) (mul_self_nonneg _)

/-- Multiplying any positive difference kernel by a cosine preserves positivity. -/
theorem cosine_times_kernel {ι : Type*} [Fintype ι] (K : ι → ι → ℝ)
    (hK : ∀ v : ι → ℝ, 0 ≤ ∑ i, ∑ j, v i * v j * K i j)
    (a x : ι → ℝ) :
    0 ≤ ∑ i, ∑ j, a i * a j * (K i j * Real.cos (x i - x j)) := by
  have h (i j : ι) :
      a i * a j * (K i j * Real.cos (x i - x j)) =
        (a i * Real.cos (x i)) * (a j * Real.cos (x j)) * K i j +
        (a i * Real.sin (x i)) * (a j * Real.sin (x j)) * K i j := by
    rw [Real.cos_sub]
    ring
  simp_rw [h, Finset.sum_add_distrib]
  exact add_nonneg (hK (fun i => a i * Real.cos (x i)))
    (hK (fun i => a i * Real.sin (x i)))

#print axioms cosine_form
#print axioms cosine_times_kernel

end SplitInert
