import Mathlib

namespace MertensDeadline

/-- A one-sided comparison suffices to exclude a negative average. -/
theorem survival_excludes_negative (reserve loss observed : ℝ)
    (h : reserve - loss ≤ observed) (hbound : loss ≤ reserve) : 0 ≤ observed := by
  linarith

/-- The weighted tail bound improves at larger exponents. -/
theorem tail_mass_mono (base s₀ s : ℝ) (hpos : 0 < base) (hone : base ≤ 1)
    (hs : s₀ ≤ s) : base ^ s ≤ base ^ s₀ := by
  exact Real.rpow_le_rpow_of_exponent_ge hpos hone hs

/-- In the positive continuation, a block remains positive even if every jump comes last. -/
theorem inside_block (start drop spent jumps : ℝ) (h : drop < start)
    (hspent : spent ≤ drop) (hjumps : 0 ≤ jumps) : 0 < start - spent + jumps := by
  linarith

/-- A small downward adjustment of a benchmark preserves a strict negative mean. -/
theorem adjust_margin (observed increment : ℝ) (h : increment < -observed) :
    observed + increment < 0 := by linarith

end MertensDeadline

#print axioms MertensDeadline.survival_excludes_negative
#print axioms MertensDeadline.tail_mass_mono
#print axioms MertensDeadline.inside_block
#print axioms MertensDeadline.adjust_margin
