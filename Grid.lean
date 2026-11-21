import Mathlib

namespace GeometricStarts

theorem polynomial_majorant (coeff x : ℝ) (hcoeff : 0 ≤ coeff) (hx : x ≤ 1/4) :
    1 ≤ (1 - coeff*((x-1/4)*(x+1)^2))^2 := by
  have h : coeff*((x-1/4)*(x+1)^2) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hcoeff (mul_nonpos_of_nonpos_of_nonneg (by linarith) (sq_nonneg _))
  nlinarith [sq_nonneg (coeff*((x-1/4)*(x+1)^2))]

theorem failed_tail (u t a : ℝ) (hu : 1/4 < u) (h : a ≤ 1/8-u-t) (ha : 0 ≤ a) :
    t < -(1/8) := by linarith

theorem contraction (coeff m v : ℝ) (hcoeff : 0 < coeff) (hm : 1 ≤ m) (hv : coeff*v ≤ 1) :
    1-2*coeff*m+coeff^2*v ≤ 1-coeff := by
  nlinarith [mul_nonneg (le_of_lt hcoeff) (sub_nonneg.mpr hm),
    mul_nonneg (le_of_lt hcoeff) (sub_nonneg.mpr hv)]

end GeometricStarts

#print axioms GeometricStarts.polynomial_majorant
#print axioms GeometricStarts.failed_tail
#print axioms GeometricStarts.contraction
