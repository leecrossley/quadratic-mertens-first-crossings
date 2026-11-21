import Mathlib

namespace RealAxisCrossings

/-- The three real traces used for the one-sided transform, before pairing zeros. -/
theorem three_resolvents (q a z : ℂ) (hq : q ≠ z) (ha : a ≠ z)
    (hb : a + 1 ≠ z) (hqa : a ≠ q) (hqb : a + 1 ≠ q) :
    1 / ((q-z)*(a-z)*(a+1-z)) =
        1 / ((a-q)*(a+1-q)*(q-z)) - 1 / ((a-q)*(a-z))
        + 1 / ((a+1-q)*(a+1-z)) := by
  field_simp [sub_ne_zero.mpr hq, sub_ne_zero.mpr ha, sub_ne_zero.mpr hb,
    sub_ne_zero.mpr hqa, sub_ne_zero.mpr hqb]
  ring

/-- The conductor and square contributions after the endpoints tend to 1/2. -/
theorem conductor_offset (x p : ℝ) (hx : x ≠ 0) :
    (2/3)/x + p/((1/2)*(3/2)) - (1/2)/(1/2) + (1/2)/(3/2) =
      (4/3)*(p + 1/(2*x) - 1/2) := by
  field_simp
  ring

/-- A strict excess after paying for both portions is attained on the window. -/
theorem window_margin (p mean inside outside peak target : ℝ) (hp : 0 ≤ p)
    (hp1 : p ≤ 1) (ht : 0 ≤ target)
    (hb : mean ≤ p*(peak+inside)+(1-p)*outside)
    (hg : target < mean - p*inside - (1-p)*outside) :
    target < peak := by
  by_contra! h
  have h₁ := mul_le_mul_of_nonneg_left h hp
  have h₂ := mul_le_mul_of_nonneg_right hp1 ht
  nlinarith

/-- The lattice of density 1/(2π) supplies a positive geometric series. -/
theorem double_grid (r : ℝ) (hr : 1 < r) :
    (1/2)*((r+1)/(r-1)) - 1/2 = 1/(r-1) ∧ 0 < 1/(r-1) := by
  have hd : 0 < r-1 := by linarith
  constructor
  · field_simp
    ring
  · positivity

/-- Two real samples control inverse-square mass outside the central interval. -/
theorem crowding_ratio (t : ℝ) :
    4*(1+t^2)/(4+t^2)-1 = 3*t^2/(4+t^2) := by
  have hd : 0 < 4+t^2 := by positivity
  field_simp
  ring

/-- The quadratic square contribution cancels the arithmetic bias. -/
theorem prime_square_bias (m s : ℝ) :
    (2/3)*m+(4/3)*(-s-m/2) = -(4/3)*s := by ring

#print axioms three_resolvents
#print axioms conductor_offset
#print axioms window_margin
#print axioms double_grid
#print axioms crowding_ratio
#print axioms prime_square_bias

end RealAxisCrossings
