import Mathlib

namespace CrossingDensity

/-- The two local conditions on p force switching from inert to split to decrease the full area. -/
theorem switch_decreases (a b lp lh : ℝ) (hl : 0 < lp) (ha : 0 ≤ a)
    (hb : 2*b < a) (hh : lp/2 ≤ lh) : -a*lh + b*lp < 0 := by
  nlinarith [mul_nonneg ha (sub_nonneg.mpr hh), mul_pos (sub_pos.mpr hb) hl]

/-- The folded area at a recovery endpoint strictly short of the limiting width is insufficient. -/
theorem short_recovery (width deficit : ℝ)
    (hd : 0 < deficit) (hs : deficit < width) :
    (width - deficit)^2 / 4 < width^2 / 4 := by
  nlinarith [mul_pos hd (by linarith : 0 < 2*width-deficit)]

theorem conditional_cost (cost loss : ℝ) (hl : loss ≤ cost/2) :
    cost/2 ≤ cost-loss := by linarith

end CrossingDensity

#print axioms CrossingDensity.switch_decreases
#print axioms CrossingDensity.short_recovery
#print axioms CrossingDensity.conditional_cost
