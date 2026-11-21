import Mathlib

open MeasureTheory

namespace QuadraticMertens

/-- A nonnegative function dominates each of its unit-modulus Fourier averages. -/
theorem positive_weight_bounds_frequency
    {X : Type*} [MeasurableSpace X] {μ : Measure X}
    (weight : X → ℝ) (phase : X → ℂ) (hi : Integrable weight μ)
    (hp : 0 ≤ᵐ[μ] weight) (hu : ∀ᵐ x ∂μ, ‖phase x‖ ≤ 1) :
    ‖∫ x, (weight x : ℂ) * phase x ∂μ‖ ≤ ∫ x, weight x ∂μ := by
  apply norm_integral_le_of_norm_le hi
  filter_upwards [hp, hu] with x hx hphase
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hx]
  exact mul_le_of_le_one_right hx hphase

/-- A coefficient exceeding the mean forces values below the chosen level. -/
theorem coefficient_forces_negative_set
    {X : Type*} [MeasurableSpace X] {μ : Measure X}
    (f : X → ℝ) (phase : X → ℂ) (level : ℝ)
    (hi : Integrable (fun x => f x + level) μ)
    (hu : ∀ᵐ x ∂μ, ‖phase x‖ ≤ 1)
    (gap : (∫ x, f x + level ∂μ) <
      ‖∫ x, ((f x + level : ℝ) : ℂ) * phase x ∂μ‖) :
    ¬ (∀ᵐ x ∂μ, -level ≤ f x) := by
  intro h
  have hnon : 0 ≤ᵐ[μ] (fun x => f x + level) := by
    filter_upwards [h] with x hx
    change 0 ≤ f x + level
    linarith
  exact (not_lt_of_ge
    (positive_weight_bounds_frequency (fun x => f x + level) phase hi hnon hu)) gap

#print axioms positive_weight_bounds_frequency
#print axioms coefficient_forces_negative_set

end QuadraticMertens
