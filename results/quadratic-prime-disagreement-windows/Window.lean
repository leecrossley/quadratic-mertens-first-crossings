import Mathlib

open scoped BigOperators

namespace QuadraticDisagreement

/-- Keeping the diagonal in a positive square allows arbitrary multiplicities. -/
theorem diagonal_energy {ι : Type*} [DecidableEq ι] (f : ι → ℝ)
    (hf : ∀ i, 0 ≤ f i) (s : Finset ι) :
    (∑ i ∈ s, (f i)^2) ≤ (∑ i ∈ s, f i)^2 := by
  induction s using Finset.induction_on with
  | empty => simp
  | @insert a s ha ih =>
    simp only [Finset.sum_insert ha]
    have hs : 0 ≤ ∑ i ∈ s, f i := Finset.sum_nonneg (fun i _ => hf i)
    nlinarith [mul_nonneg (hf a) hs]

/-- The orientation of the two unramified disagreement classes. -/
theorem orientation (a b : ℝ) :
    ((1+a)*(1-b) - (1-a)*(1+b))/4 = (a-b)/2 := by ring

/-- On the last part of the finite prime window, t = Ky/p, r = 1/K. -/
theorem taper_middle (r t : ℝ) :
    (1-r*t) - (2-r)*(1-t) = (1-r)*(2*t-1) := by ring

theorem taper_ends (r t : ℝ) :
    (1-r*t) - (2-r)*(1-t) + (1-r)*(1-2*t) = 0 := by ring

theorem adverse_endpoint (x y ceiling gap : ℝ) (hx : x ≤ ceiling) (hy : y ≤ ceiling)
    (hd : gap ≤ |y-x|) : x ≤ ceiling-gap ∨ y ≤ ceiling-gap := by
  by_contra! hn
  obtain ⟨h₁, h₂⟩ := hn
  have h : |y-x| < gap := abs_lt.mpr ⟨by linarith, by linarith⟩
  exact (not_lt_of_ge hd) h

end QuadraticDisagreement

#print axioms QuadraticDisagreement.diagonal_energy
#print axioms QuadraticDisagreement.orientation
#print axioms QuadraticDisagreement.taper_middle
#print axioms QuadraticDisagreement.taper_ends
#print axioms QuadraticDisagreement.adverse_endpoint
