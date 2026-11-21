import Mathlib

open MeasureTheory Set
open scoped Interval

namespace CrossingLookahead

/-- The maximal loss when only the starting height is fixed. -/
theorem one_sided_area (length : ℝ) :
    (∫ x in (0 : ℝ)..length, x) = length ^ 2 / 2 := by
  simp [integral_id]

/-- The two halves of the extremal dip when the terminal height is also controlled. -/
theorem recovered_area (length : ℝ) :
    (∫ x in (0 : ℝ)..(length / 2), x) +
    (∫ x in (length / 2)..length, length - x) = length ^ 2 / 4 := by
  have hsub : (∫ x in (length / 2)..length, length - x) =
      (∫ _ in (length / 2)..length, length) - (∫ x in (length / 2)..length, x) :=
    intervalIntegral.integral_sub (f := fun _ : ℝ => length) (g := fun x : ℝ => x)
      (continuous_const.intervalIntegrable _ _) (continuous_id.intervalIntegrable _ _)
  rw [hsub]
  simp only [integral_id, intervalIntegral.integral_const, smul_eq_mul]
  ring

theorem accessible_constant :
    (1965/1000 : ℝ)^2 < 8*(4829182931/10000000000 : ℝ) := by norm_num

end CrossingLookahead

#print axioms CrossingLookahead.one_sided_area
#print axioms CrossingLookahead.recovered_area
#print axioms CrossingLookahead.accessible_constant
