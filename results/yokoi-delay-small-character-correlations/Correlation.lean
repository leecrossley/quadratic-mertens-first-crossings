import Mathlib

namespace YokoiCorrelations

/-- A field good for a common family of tests satisfies every ratio estimate. -/
theorem ratio_bound (t twist c b l root : ℝ) (ht : 0 < -t)
    (hr : 0 < root) (hb : 0 < b) (hl : 0 < l)
    (h₁ : b*l/root ≤ -t) (h₂ : |twist| ≤ c/root) :
    |twist| / (-t) ≤ c/(b*l) := by
  have h₃ : |twist| * root ≤ c := (le_div_iff₀ hr).mp h₂
  have h₄ : b*l ≤ (-t)*root := (div_le_iff₀ hr).mp h₁
  apply (div_le_div_iff₀ ht (mul_pos hb hl)).mpr
  calc
    |twist| * (b*l) ≤ |twist| * ((-t)*root) := mul_le_mul_of_nonneg_left h₄ (abs_nonneg _)
    _ = (|twist| * root) * (-t) := by ring
    _ ≤ c*(-t) := mul_le_mul_of_nonneg_right h₃ ht.le

/-- Denominator when a centred random variable is tilted by a squared linear weight. -/
theorem tilt_identity (a mu z : ℝ) :
    (1+a*(z-mu))^2*(z-mu) =
    (z-mu)+2*a*(z-mu)^2+a^2*(z-mu)^3 := by ring

/-- Turn weight and second-moment bounds into an ordinary positive mass. -/
theorem transfer_mass (fraction total weighted second : ℝ) (hs : 0 < second)
    (hw : 0 ≤ weighted) (hm : 0 ≤ total) (hgood : 3 * total / 4 ≤ weighted)
    (hcs : weighted^2 ≤ fraction * second) :
    (3 * total / 4)^2 / second ≤ fraction := by
  apply (div_le_iff₀ hs).mpr
  have h : (3 * total / 4)^2 ≤ weighted^2 := by
    apply sq_le_sq' <;> linarith
  exact h.trans hcs

end YokoiCorrelations

#print axioms YokoiCorrelations.ratio_bound
#print axioms YokoiCorrelations.tilt_identity
#print axioms YokoiCorrelations.transfer_mass

