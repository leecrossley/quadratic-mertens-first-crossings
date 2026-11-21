import Mathlib

namespace PrescribedCrossings

/-- A signed tilt can reach half the requested coefficient on either side of zero. -/
theorem tilt_factor (a v m : ℝ) (ha : |a| ≤ 1/16) (hv : 1/2 ≤ v)
    (hv' : v ≤ 1) (hm : |m| ≤ 2*v) :
    1/2 ≤ (2*v+a*m)/(1+a^2*v) := by
  have hv0 : 0 ≤ v := by linarith
  have h1 : |a*m| ≤ (1/16)*(2:ℝ) := by
    rw [abs_mul]
    exact mul_le_mul ha (by linarith : |m| ≤ 2) (abs_nonneg m) (by norm_num)
  have hm' := (abs_le.mp h1).1
  have h2 : |a| * |a| ≤ (1/16:ℝ)*(1/16) :=
    mul_le_mul ha ha (abs_nonneg a) (by norm_num)
  rw [← sq, sq_abs] at h2
  have h3 : a^2*v ≤ a^2 := by nlinarith [mul_nonneg (sq_nonneg a) (sub_nonneg.mpr hv')]
  have hpos : 0 < 1+a^2*v := by positivity
  apply (le_div_iff₀ hpos).mpr
  nlinarith

/-- Cauchy--Schwarz changes a good weighted mass into an ordinary counting bound. -/
theorem counting_bound (p good mass fourth : ℝ) (hm : 0 ≤ mass) (hf : 0 < fourth)
    (hg : 3*mass/4 ≤ good) (hcs : good^2 ≤ p*fourth) :
    (3*mass/4)^2/fourth ≤ p := by
  apply (div_le_iff₀ hf).mpr
  have h : (3*mass/4)^2 ≤ good^2 := by
    nlinarith [mul_nonneg (sub_nonneg.mpr hg)
      (show 0 ≤ good+3*mass/4 by linarith)]
  linarith

/-- The negative part exceeds the worst positive area for both measures. -/
theorem profile_margins (r η K : ℝ) (hr : 0 < r)
    (hk : K*(r*η)=16) :
    2/r < 3*K*η/5 ∧ 1 < 12*r*K*η/25 := by
  constructor
  · apply (div_lt_iff₀ hr).mpr
    nlinarith
  · nlinarith

end PrescribedCrossings

#print axioms PrescribedCrossings.tilt_factor
#print axioms PrescribedCrossings.counting_bound
#print axioms PrescribedCrossings.profile_margins
