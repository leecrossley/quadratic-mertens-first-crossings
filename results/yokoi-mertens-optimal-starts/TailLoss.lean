import Mathlib

namespace MertensStart

/-- A decreasing nonnegative correction can only help the lower bound on a future increment. -/
theorem future_loss (hT ht zT zt cT ct eT et : ℝ)
    (h : ht - hT = (zT + cT) - (zt + ct)) (hc : ct ≤ cT)
    (hzT : |zT| ≤ eT) (hzt : |zt| ≤ et) :
    -(eT+et) ≤ ht-hT := by
  have h1 := (abs_le.mp hzT).1
  have h2 := (abs_le.mp hzt).2
  linarith

/-- The kernel denominator on the critical line only increases for positive shifts. -/
theorem kernel_denominator (s t : ℝ) (hs : 0 ≤ s) :
    (1/2:ℝ)^2 + t^2 ≤ (1/2+s)^2+t^2 := by
  nlinarith [sq_nonneg s]

/-- The gap area protects the accumulated integral at every later endpoint. -/
theorem positive_area (initial change loss reserve : ℝ)
    (h1 : reserve ≤ initial) (h2 : -loss ≤ change) (h3 : loss < reserve) :
    0 < initial+change := by linarith

end MertensStart

#print axioms MertensStart.future_loss
#print axioms MertensStart.kernel_denominator
#print axioms MertensStart.positive_area
