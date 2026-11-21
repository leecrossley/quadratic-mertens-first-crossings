import Statements

namespace FirstCrossing

/-- Applied to the quadratic Euler factorization in the open critical strip. -/
theorem product_zero (h : DirichletLZerosOnLine) (d : ℕ) [NeZero d]
    (χ : DirichletCharacter ℂ d) (s : ℂ) (hs₀ : 0 < s.re) (hs₁ : s.re < 1)
    (hz : riemannZeta s * DirichletCharacter.LFunction χ s = 0) :
    s.re = 1 / 2 := by
  rcases mul_eq_zero.mp hz with hzeta | hchi
  · apply h 1 (1 : DirichletCharacter ℂ 1) s hs₀ hs₁
    simpa only [DirichletCharacter.LFunction_modOne_eq] using hzeta
  · exact h d χ s hs₀ hs₁ hchi

/-- The box count used in simultaneous recurrence, including repeated ordinates. -/
theorem box_collision (Q n : ℕ) (box : Fin (Q ^ n + 1) → (Fin n → Fin Q)) :
    ∃ i j, i < j ∧ box i = box j := by
  have hc : Fintype.card (Fin n → Fin Q) < Fintype.card (Fin (Q ^ n + 1)) := by simp
  obtain ⟨i, j, hij, hbox⟩ := Fintype.exists_ne_map_eq_of_card_lt box hc
  rcases lt_or_gt_of_ne hij with hlt | hgt
  · exact ⟨i, j, hlt, hbox⟩
  · exact ⟨j, i, hgt, hbox.symm⟩

/-- One positive shift brings every real frequency back to within one box of an integer. -/
theorem simultaneous_return (Q n : ℕ) (hQ : 0 < Q) (a : Fin n → ℝ) :
    ∃ q : ℕ, 0 < q ∧ q ≤ Q ^ n ∧
      ∀ k, ∃ m : ℤ, |(q : ℝ) * a k - m| ≤ 1 / (Q : ℝ) := by
  have hQr : (0 : ℝ) < Q := by exact_mod_cast hQ
  let v (j : Fin (Q ^ n + 1)) (k : Fin n) := (Q : ℝ) * Int.fract ((j.val : ℝ) * a k)
  have hv j k : 0 ≤ v j k := mul_nonneg hQr.le (Int.fract_nonneg _)
  let box (j : Fin (Q ^ n + 1)) (k : Fin n) : Fin Q :=
    ⟨⌊v j k⌋₊, (Nat.floor_lt (hv j k)).2 (mul_lt_of_lt_one_right hQr (Int.fract_lt_one _))⟩
  obtain ⟨i, j, hij, hijbox⟩ := box_collision Q n box
  have hijval : i.val < j.val := hij
  refine ⟨j.val - i.val, by omega, by have := j.isLt; omega, ?_⟩
  intro k
  have heq : ⌊v i k⌋₊ = ⌊v j k⌋₊ := congrArg Fin.val (congrFun hijbox k)
  have hi := Nat.floor_le (hv i k)
  have hi' := Nat.lt_floor_add_one (v i k)
  have hj := Nat.floor_le (hv j k)
  have hj' := Nat.lt_floor_add_one (v j k)
  rw [heq] at hi hi'
  have hdiff : |v j k - v i k| ≤ 1 := by rw [abs_le]; constructor <;> linarith
  refine ⟨⌊(j.val : ℝ) * a k⌋ - ⌊(i.val : ℝ) * a k⌋, ?_⟩
  have hprod : (((j.val : ℝ) - i.val) * a k -
      ((⌊(j.val : ℝ) * a k⌋ : ℝ) - (⌊(i.val : ℝ) * a k⌋ : ℝ))) * Q = v j k - v i k := by
    simp only [v, Int.fract]
    ring
  rw [Nat.cast_sub hijval.le, Int.cast_sub, le_div_iff₀ hQr, ← abs_of_pos hQr, ← abs_mul]
  rwa [hprod]

theorem polynomial_envelope (h : ℕ) (hh : 64 ≤ h) :
    3 + 512 * h * (32 * h + 9) ≤ 2 ^ h := by
  induction h, hh using Nat.le_induction with
  | base => decide
  | succ k hk ih =>
    rw [pow_succ]
    have hsq := Nat.mul_le_mul_right k hk
    nlinarith

/-- The size of log₂ log₂ of the cutoff constructed by recurrence. -/
theorem recurrence_exponent (h : ℕ) (hh : 64 ≤ h) :
    3 + h * (32 * h + 9) * 2 ^ (64 * h + 9) ≤ 2 ^ (65 * h) := by
  have hpos : 1 ≤ (2 : ℕ) ^ (64 * h) := Nat.one_le_two_pow
  have hpoly := Nat.mul_le_mul_right (2 ^ (64 * h)) (polynomial_envelope h hh)
  rw [show 65 * h = h + 64 * h by omega, pow_add, pow_add]
  norm_num only [Nat.reducePow] at *
  nlinarith

set_option exponentiation.threshold 40000 in
/-- For the ceiling binary logarithm, the hypothesis on ℓ follows from rounding. -/
theorem discriminant_envelope (d ℓ : ℕ) (hd : 4 ≤ d) (hℓ : 2 ^ ℓ ≤ 2 * d) :
    (2 : ℕ) ^ (65 * (512 + 128 * ℓ)) ≤ d ^ 30000 := by
  calc
    (2 : ℕ) ^ (65 * (512 + 128 * ℓ)) = 2 ^ 33280 * (2 ^ ℓ) ^ 8320 := by
      rw [← pow_mul, ← pow_add]
      congr 1
      omega
    _ ≤ 2 ^ 33280 * (2 * d) ^ 8320 := by gcongr
    _ = 4 ^ 20800 * d ^ 8320 := by
      rw [mul_pow, ← mul_assoc, ← pow_add, show (4 : ℕ) = 2 ^ 2 by decide, ← pow_mul]
    _ ≤ d ^ 20800 * d ^ 8320 := by gcongr
    _ = d ^ 29120 := by rw [← pow_add]
    _ ≤ d ^ 30000 := Nat.pow_le_pow_right ((show 0 < 4 by decide).trans_le hd) (by decide)

end FirstCrossing

#print axioms FirstCrossing.product_zero
#print axioms FirstCrossing.box_collision
#print axioms FirstCrossing.simultaneous_return
#print axioms FirstCrossing.polynomial_envelope
#print axioms FirstCrossing.recurrence_exponent
#print axioms FirstCrossing.discriminant_envelope
