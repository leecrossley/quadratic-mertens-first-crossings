import Mathlib

set_option exponentiation.threshold 1024

namespace ConductorBound

/-- The signed coefficient of the product after the bounded primitive is added. -/
theorem product_coefficient (r s : ℂ) (h : r + s = 1) (hr : r ≠ 0) (hs : s ≠ 0) :
    -(1/r) + 1/(r*s) = 1/s := by
  field_simp
  linear_combination -h

/-- The derivative used when integrating the signed correction by parts. -/
theorem weighted_derivative (W : ℝ → ℝ) (u v : ℝ) (h : HasDerivAt W v u) :
    HasDerivAt (fun t => Real.exp (-t/2) * W t)
      (Real.exp (-u/2) * (v - W u/2)) u := by
  have he := (((hasDerivAt_id u).neg.div_const 2).exp).mul h
  convert he using 1 <;> (first | rfl | (dsimp; ring))

/-- The discarded high-frequency tail is strictly below one in these units. -/
theorem tail_budget (L k m T : ℕ) (hk : L ≤ 2^k) (hm : m = 1024 + 16*k)
    (hsmall : m ≤ 2^(11+k)) (hT : T = 2^257*m*L^2) : 6*L*T < 2^m := by
  calc
    6*L*T ≤ 2^3 * 2^257 * m * L^3 := by rw [hT]; ring_nf; omega
    _ ≤ 2^3 * 2^257 * 2^(11+k) * (2^k)^3 := by gcongr
    _ = 2^(271+4*k) := by
      rw [← pow_mul, ← pow_add, ← pow_add, ← pow_add]
      congr 1
      omega
    _ < 2^m := Nat.pow_lt_pow_right (by decide) (by omega)

theorem smoothing_order (k : ℕ) : 1024 + 16*k ≤ 2^(11+k) := by
  induction k with
  | zero => decide
  | succ k ih =>
    rw [show 11+(k+1) = (11+k)+1 by omega, pow_succ]
    omega

end ConductorBound

#print axioms ConductorBound.product_coefficient
#print axioms ConductorBound.weighted_derivative
#print axioms ConductorBound.tail_budget
#print axioms ConductorBound.smoothing_order
