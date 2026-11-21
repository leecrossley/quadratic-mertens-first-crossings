import Mathlib

open MeasureTheory

namespace CentralPackets

/-- The positive future convolution restores the factor removed by u/(u+s). -/
theorem convolution_identity (s : ℝ) :
    (∫ r in (0:ℝ)..s, (1 + Real.exp (-r)) * (1 - Real.exp (-(s-r)))) =
      s * (1 - Real.exp (-s)) := by
  let F : ℝ → ℝ := fun r => r * (1 - Real.exp (-s)) - Real.exp (-r) - Real.exp (r-s)
  have deriv (r : ℝ) : HasDerivAt F
      ((1 + Real.exp (-r)) * (1 - Real.exp (-(s-r)))) r := by
    have h₁ : HasDerivAt (fun x : ℝ => Real.exp (-x)) (-Real.exp (-r)) r := by
      simpa using ((hasDerivAt_id r).neg.exp)
    have h₂ : HasDerivAt (fun x : ℝ => Real.exp (x-s)) (Real.exp (r-s)) r := by
      simpa using (((hasDerivAt_id r).sub_const s).exp)
    have h₃ := (((hasDerivAt_id r).mul_const (1 - Real.exp (-s))).sub h₁).sub h₂
    have he : Real.exp (-r) * Real.exp (r-s) = Real.exp (-s) := by
      rw [← Real.exp_add]
      congr 1
      ring
    have eqn : (1 + Real.exp (-r)) * (1 - Real.exp (-(s-r))) =
        1 * (1 - Real.exp (-s)) - -Real.exp (-r) - Real.exp (r-s) := by
      rw [show -(s-r) = r-s by ring]
      nlinarith only [he]
    rw [eqn]
    exact h₃
  have cont : Continuous (fun r : ℝ => (1 + Real.exp (-r)) * (1 - Real.exp (-(s-r)))) := by
    fun_prop
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => deriv x)
    (cont.intervalIntegrable 0 s)]
  simp [F]
  ring

/-- A signed integral against a bounded square loses only the negative mass. -/
theorem square_test_lower {X : Type*} [MeasurableSpace X] {μ : Measure X}
    (f q : X → ℝ) (B : ℝ) (hn : Integrable (fun x => max 0 (-f x)) μ)
    (hi : Integrable (fun x => f x * q x) μ)
    (hb : ∀ᵐ x ∂μ, 0 ≤ q x ∧ q x ≤ B) :
    -B * (∫ x, max 0 (-f x) ∂μ) ≤ ∫ x, f x * q x ∂μ := by
  rw [← integral_const_mul]
  apply integral_mono_ae (hn.const_mul (-B)) hi
  filter_upwards [hb] with x hx
  by_cases hf : 0 ≤ f x
  · rw [max_eq_left (neg_nonpos.mpr hf), mul_zero]
    exact mul_nonneg hf hx.1
  · have hf' : f x ≤ 0 := le_of_not_ge hf
    rw [max_eq_right (neg_nonneg.mpr hf'), neg_mul_neg]
    simpa [mul_comm] using mul_le_mul_of_nonpos_left hx.2 hf'

/-- An upper bound involving the unknown central mass can be absorbed. -/
theorem absorb_mass {M C ε : ℝ} (hε : ε < 1) (h : M ≤ ε * (M + C)) :
    M ≤ ε * C / (1 - ε) := by
  apply (le_div_iff₀ (by linarith : 0 < 1 - ε)).2
  linarith only [show M ≤ ε*M + ε*C by simpa [mul_add] using h,
    show M*ε = ε*M by ring]

/-- The seven-frequency choice clears the double-central-zero bias by more than 1/3. -/
theorem seven_frequency_margin :
    2 * ((2:ℝ)/3 + 4*2/3) - (8/3) * Real.sqrt 7 < -(1/3) := by
  have h : (21:ℝ)/8 < Real.sqrt 7 := Real.lt_sqrt_of_sq_lt (by norm_num)
  linarith

#print axioms convolution_identity
#print axioms square_test_lower
#print axioms absorb_mass
#print axioms seven_frequency_margin

end CentralPackets
