import Mathlib

open MeasureTheory

namespace RoughCharacterSums

/-- A nearly constant cosine cannot cancel positive mass without negative mass. -/
theorem cosine_mass {α : Type*} [MeasurableSpace α] {μ : Measure α}
    {p n phase : α → ℝ} {radius err : ℝ}
    (hp : Integrable p μ) (hn : Integrable n μ)
    (hw : Integrable (fun x => Real.cos (phase x) * (p x - n x)) μ)
    (hpos : ∀ᵐ x ∂μ, 0 ≤ p x ∧ 0 ≤ n x)
    (hphase : ∀ᵐ x ∂μ, (phase x)^2 ≤ radius^2)
    (herr : (∫ x, Real.cos (phase x) * (p x - n x) ∂μ) ≤ err) :
    (1 - radius^2 / 2) * (∫ x, p x ∂μ) - err ≤ ∫ x, n x ∂μ := by
  have hcompare : ∀ᵐ x ∂μ,
      (1-radius^2/2)*p x - n x ≤ Real.cos (phase x)*(p x-n x) := by
    filter_upwards [hpos, hphase] with x hx hy
    have hc : 1-radius^2/2 ≤ Real.cos (phase x) := by
      have ht := Real.one_sub_sq_div_two_le_cos (x := phase x)
      linarith
    have ha := mul_le_mul_of_nonneg_right hc hx.1
    have hb := mul_le_mul_of_nonneg_right (Real.cos_le_one (phase x)) hx.2
    linarith
  have h := (integral_mono_ae ((hp.const_mul _).sub hn) hw hcompare).trans herr
  change (∫ x, (1 - radius^2 / 2) * p x - n x ∂μ) ≤ err at h
  rw [integral_sub (hp.const_mul _) hn, integral_const_mul] at h
  linarith

/-- A finite weighted average below its proposed lower bound has a witness. -/
theorem prefix_witness {ι : Type*} (s : Finset ι) (weight value bound : ι → ℝ)
    (hw : ∀ i ∈ s, 0 ≤ weight i)
    (hlt : ∑ i ∈ s, weight i * value i < ∑ i ∈ s, weight i * bound i) :
    ∃ i ∈ s, value i < bound i := by
  by_contra! h
  exact (not_lt_of_ge (Finset.sum_le_sum (fun i hi =>
    mul_le_mul_of_nonneg_left (h i hi) (hw i hi)))) hlt

/-- The two wrong-sign contributions cannot exhaust the initial positive mass. -/
theorem ordered_budget (first left right tail scale b tau c₀ c₁ c₂ : ℝ)
    (hτ : 0 < tau) (hscale : 0 < scale) (hcap : tau ≤ b * scale)
    (hc : 0 ≤ c₁)
    (hfirst : c₀ * tau ≤ first)
    (hleft : left ≤ c₁ * tau^2 / (2 * scale))
    (hright : right ≤ c₂ * b^2 * tau / 2)
    (htail : tail < c₀ * tau / 2)
    (hbudget : c₁ * b / 2 + c₂ * b^2 / 2 < c₀ / 2) :
    0 < first - left - right - tail := by
  have hprod := mul_le_mul_of_nonneg_left hcap (mul_nonneg hc hτ.le)
  have hsmall : c₁ * tau^2 / (2 * scale) ≤ c₁ * b * tau / 2 := by
    apply (div_le_iff₀ (by positivity : 0 < 2 * scale)).mpr
    nlinarith [hprod]
  have hroom := mul_lt_mul_of_pos_right hbudget hτ
  linarith

theorem exponent_eight_margins :
    (33/80 : ℝ) < 1/2 ∧ 11/4 - (27/4)/2 + 1/2 < (-1/16 : ℝ)
    ∧ (1/2 : ℝ) + (27/4 - 8)/2 = -1/8 := by norm_num

/-- A negative prefix after nonnegative dilation forces an earlier negative prefix. -/
theorem negative_prefix_of_dilates {ι : Type*} (terms : Finset ι)
    (weight : ι → ℝ) (index : ι → ℕ) (count : ℕ → ℝ) (limit : ℕ)
    (hw : ∀ i ∈ terms, 0 ≤ weight i) (hi : ∀ i ∈ terms, index i ≤ limit)
    (h : ∑ i ∈ terms, weight i * count (index i) < 0) :
    ∃ j ≤ limit, count j < 0 := by
  obtain ⟨i, hit, hneg⟩ := prefix_witness terms weight (fun i => count (index i))
    (fun _ => 0) hw (by simpa using h)
  exact ⟨index i, hi i hit, hneg⟩

/-- A positive convolution contracts the mass ratio when its signed mass is nonnegative. -/
theorem mass_ratio_order {p n pStar nStar k : ℝ}
    (hp : 0 < p) (hStar : 0 < pStar) (hsign : n ≤ p)
    (hpos : pStar ≤ k * p) (hs : pStar - nStar = k * (p - n)) :
    nStar / pStar ≤ n / p := by
  apply (div_le_div_iff₀ hStar hp).mpr
  have hbound := mul_le_mul_of_nonneg_right hpos (sub_nonneg.mpr hsign)
  have heq := congrArg (fun v : ℝ => v * p) hs
  nlinarith only [hbound, heq]

end RoughCharacterSums

#print axioms RoughCharacterSums.cosine_mass
#print axioms RoughCharacterSums.prefix_witness
#print axioms RoughCharacterSums.ordered_budget
#print axioms RoughCharacterSums.exponent_eight_margins
#print axioms RoughCharacterSums.negative_prefix_of_dilates
#print axioms RoughCharacterSums.mass_ratio_order
