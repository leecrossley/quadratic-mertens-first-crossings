import Mathlib

namespace LateStarts

theorem interval_majorant (x shift scale : ℝ) (hscale : 0 ≤ scale)
    (hx : |x-shift| ≤ 1/2) :
    1 ≤ (1 - scale * (((x-shift)^2-1/4)/(1+shift^2)))^2 := by
  have hh := abs_le.mp hx
  have hsq : (x-shift)^2 ≤ 1/4 := by
    nlinarith [mul_nonneg (by linarith [hh.1] : 0 ≤ 1/2+(x-shift))
      (by linarith [hh.2] : 0 ≤ 1/2-(x-shift))]
  have hf : ((x-shift)^2-1/4)/(1+shift^2) ≤ 0 :=
    div_nonpos_of_nonpos_of_nonneg (by linarith) (by positivity)
  have hp := mul_nonpos_of_nonneg_of_nonpos hscale hf
  nlinarith [sq_nonneg (scale*(((x-shift)^2-1/4)/(1+shift^2)))]

theorem model_contraction (first second : ℝ) (h₁ : 3/4 ≤ first) (h₂ : second ≤ 89) :
    1-2*(1/256)*first+(1/256)^2*second ≤ 255/256 := by linarith

theorem aggregate_reserve (positive negative budget : ℝ)
    (h : positive + negative ≤ budget) (hn : 0 ≤ negative) : positive ≤ budget := by linarith

end LateStarts

#print axioms LateStarts.interval_majorant
#print axioms LateStarts.model_contraction
#print axioms LateStarts.aggregate_reserve
