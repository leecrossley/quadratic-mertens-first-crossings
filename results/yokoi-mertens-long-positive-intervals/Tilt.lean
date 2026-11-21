import Mathlib

namespace YokoiTilt

/-- A squared linear weight forces a negative mean of at least half its slope. -/
theorem negative_mean (a v m₃ μ : ℝ)
    (ha : 0 ≤ a) (ha' : a ≤ 1/16) (hv : 1/2 ≤ v) (hv' : v ≤ 1)
    (h₃ : m₃ ≤ 2*v) (hμ : μ ≤ 0) :
    μ + (-2*a*v + a^2*m₃)/(1 + a^2*v) ≤ -a/2 := by
  have vpos : 0 ≤ v := by linarith
  have hd : 0 < 1+a^2*v := by positivity
  have ha₂ : a^2 ≤ a/16 := by nlinarith [mul_nonneg ha (sub_nonneg.mpr ha')]
  have ha₂v : a^2*v ≤ (a*v)/16 := by nlinarith [mul_le_mul_of_nonneg_right ha₂ vpos]
  have hav : a/2 ≤ a*v := by nlinarith [mul_le_mul_of_nonneg_left hv ha]
  have hle : a^2*v ≤ 1/2 := by
    nlinarith [mul_le_mul_of_nonneg_left hv' (sq_nonneg a)]
  have hnum : -2*a*v + a^2*m₃ ≤ -(3*a/4) := by
    nlinarith [mul_le_mul_of_nonneg_left h₃ (sq_nonneg a)]
  have hmul := mul_le_mul_of_nonneg_left hle ha
  have hratio : (-2*a*v + a^2*m₃)/(1 + a^2*v) ≤ -a/2 := by
    apply (div_le_iff₀ hd).2
    nlinarith
  linarith

end YokoiTilt

#print axioms YokoiTilt.negative_mean
