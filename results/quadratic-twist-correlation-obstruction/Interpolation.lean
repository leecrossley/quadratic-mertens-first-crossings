import Mathlib

namespace QuadraticTwistModel

/-- Both equations of the two-moment interpolation problem. -/
theorem gram_solution (n u v a b : ℝ) (h : n*v-u^2 ≠ 0) :
    let A := (a*v-b*u)/(n*v-u^2)
    let B := (b*n-a*u)/(n*v-u^2)
    n*A+u*B=a ∧ u*A+v*B=b := by
  dsimp
  constructor <;> simp only [← mul_div_assoc, ← add_div] <;> apply (div_eq_iff h).mpr <;> ring

/-- Total mass assigned by the identity-class adjustment. -/
theorem quota_mass (A B h : ℝ) (hh : h ≠ 0) :
    (h-1)*((A-B)/h)+((A-B)/h+B)=A := by
  field_simp
  ring

/-- The special reference contributes exactly its prescribed correction. -/
theorem special_quota (B E h : ℝ) (hh : h ≠ 0) : B+((E-B)/h)*h = E := by
  field_simp
  ring

/-- An orthogonal nonprincipal character has zero sum on all square classes. -/
theorem quota_twist (A B h sum : ℝ) (hz : sum=0) :
    (A-B)/h*sum+B=B := by simp [hz]

/-- Two different prime periods cannot meet below the squared lower cutoff. -/
theorem periods_disjoint {n p q small : ℕ} (hn : 0<n) (hp : Nat.Prime p)
    (hq : Nat.Prime q) (hne : p≠q) (hlp : small≤p) (hlq : small≤q)
    (horizon : n<small^2) : ¬(p∣n ∧ q∣n) := by
  rintro ⟨h₁,h₂⟩
  have hmul : p*q ∣ n := ((Nat.coprime_primes hp hq).mpr hne).mul_dvd_of_dvd_of_dvd h₁ h₂
  have hbound := Nat.le_of_dvd hn hmul
  have : small*small ≤ p*q := Nat.mul_le_mul hlp hlq
  nlinarith

end QuadraticTwistModel

#print axioms QuadraticTwistModel.gram_solution
#print axioms QuadraticTwistModel.quota_mass
#print axioms QuadraticTwistModel.quota_twist
#print axioms QuadraticTwistModel.special_quota
#print axioms QuadraticTwistModel.periods_disjoint

