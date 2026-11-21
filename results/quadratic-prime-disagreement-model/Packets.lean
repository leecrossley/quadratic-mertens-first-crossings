import Mathlib

namespace QuadraticPackets

theorem recover_signs (c b : ℝ) :
    (c+b)/2 + (c-b)/2 = c ∧ (c+b)/2 - (c-b)/2 = b := by
  constructor <;> ring

theorem allocation_mass (c b : ℝ) :
    |(c+b)/2| + |(c-b)/2| = max |c| |b| := by
  simp only [abs_eq_max_neg, max_def]
  split_ifs <;> linarith

theorem rounding (x y ex ey : ℝ) (hx : |x-ex| ≤ 1) (hy : |y-ey| ≤ 1) :
    |(x+y)-(ex+ey)| ≤ 2 ∧ |(x-y)-(ex-ey)| ≤ 2 := by
  obtain ⟨hx₁, hx₂⟩ := abs_le.mp hx
  obtain ⟨hy₁, hy₂⟩ := abs_le.mp hy
  constructor <;> apply abs_le.mpr <;> constructor <;> linarith

theorem two_zero_factors (z w v : ℂ) (h : w*v = 1) :
    (1-w*z)*(1-v*z) = 1-(w+v)*z+z^2 := by
  linear_combination z^2 * h

theorem signed_tail (a b tail c₁ c₂ : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (h₁ : 1/2 ≤ c₁) (h₂ : 1/2 ≤ c₂) (ht : -(b/2) ≤ tail) :
    0 ≤ a*c₁ + b*c₂ + tail := by
  nlinarith [mul_nonneg ha (sub_nonneg.mpr h₁), mul_nonneg hb (sub_nonneg.mpr h₂)]

end QuadraticPackets

#print axioms QuadraticPackets.recover_signs
#print axioms QuadraticPackets.allocation_mass
#print axioms QuadraticPackets.rounding
#print axioms QuadraticPackets.two_zero_factors
#print axioms QuadraticPackets.signed_tail
