import Mathlib

namespace PowerDelays

/-- The fourth-moment transfer only needs the energy, while truncation uses the length-weighted sum. -/
theorem truncation_budget (n cost divisor requested : ℝ) (hd : 0 < divisor)
    (hb : cost + requested*divisor ≤ n) :
    (-n+cost)/divisor ≤ -requested := by
  apply (div_le_iff₀ hd).mpr
  linarith

/-- A weight that increases between zero and one has total variation bounded by one. -/
theorem abel_step (a b upper lower : ℝ) (h0 : 0 ≤ a) (hab : a ≤ b) (hb : b ≤ 1)
    (hU : |upper| ≤ 1) (hL : |lower| ≤ 1) :
    |a*upper+(b-a)*lower| ≤ 1 := by
  calc
    |a*upper+(b-a)*lower| ≤ |a*upper|+|(b-a)*lower| := abs_add_le _ _
    _ = a*|upper|+(b-a)*|lower| := by rw [abs_mul, abs_mul, abs_of_nonneg h0, abs_of_nonneg (sub_nonneg.mpr hab)]
    _ ≤ a*1+(b-a)*1 := add_le_add (mul_le_mul_of_nonneg_left hU h0)
      (mul_le_mul_of_nonneg_left hL (sub_nonneg.mpr hab))
    _ ≤ 1 := by linarith

/-- When the full tail already has positive sign, attaching an earlier positive interval preserves it. -/
theorem extend_left (head factor tail : ℝ) (hh : 0 ≤ head) (hf : 0 < factor) (ht : 0 < tail) :
    0 < head+factor*tail := by positivity

end PowerDelays

#print axioms PowerDelays.truncation_budget
#print axioms PowerDelays.abel_step
#print axioms PowerDelays.extend_left
