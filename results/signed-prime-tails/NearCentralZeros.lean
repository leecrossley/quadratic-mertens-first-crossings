import Mathlib

open Finset Filter Topology
open scoped BigOperators

namespace NearCentralZeros

/-- The cost of moving a conjugate pair to the centre is nonnegative and
    quadratic in its ordinate before the positive kernel is integrated. -/
theorem central_pair_cost (u v g : ℝ) (hu : 0 < u) (hv : 0 ≤ v) :
    0 ≤ 2 * (u / (u + v)) * (1 - Real.cos (g * (u + v))) ∧
      2 * (u / (u + v)) * (1 - Real.cos (g * (u + v))) ≤ g^2 * u * (u + v) := by
  have huv : 0 < u + v := by linarith
  have factor : 0 ≤ 2 * (u / (u + v)) := by positivity
  constructor
  · exact mul_nonneg factor (sub_nonneg.mpr (Real.cos_le_one _))
  · calc
      _ ≤ 2 * (u / (u + v)) * ((g * (u + v))^2 / 2) := by
        apply mul_le_mul_of_nonneg_left _ factor
        linarith only [Real.one_sub_sq_div_two_le_cos (x := g * (u + v))]
      _ = _ := by field_simp

/-- Errors of size e in the six real Fourier moments retain the sign margin. -/
theorem six_height_margin {m0 m1 m2 m3 m4 m5 e : ℝ}
    (h0 : m0 ≤ 5/2 + e) (h1 : 1-e ≤ m1) (h2 : m2 ≤ e)
    (h3 : 1-e ≤ m3) (h4 : m4 ≤ e) (h5 : -e ≤ m5) :
    6*m0 - 10*m1 + 8*m2 - 6*m3 + 4*m4 - 2*m5 ≤ -1 + 36*e := by
  linarith

/-- One signed difference cannot cover two points more than two radii apart. -/
theorem unique_neighbor {x y z t r : ℝ} (hy : |(x - y) - t| ≤ r)
    (hz : |(x - z) - t| ≤ r) (hsep : 2 * r < |y-z|) : False := by
  rw [abs_le] at hy hz
  have h : |y-z| ≤ 2*r := abs_le.mpr ⟨by linarith, by linarith⟩
  exact (not_lt_of_ge h) hsep

/-- A finite symmetric conflict relation has an independent set whose closed
    neighborhoods cover all vertices, with the stated degree bound. -/
theorem independent_cover {α : Type*} [DecidableEq α]
    (v : Finset α) (adj : α → α → Prop) [DecidableRel adj]
    (symm : ∀ {i j}, adj i j → adj j i) (D : ℕ)
    (degree : ∀ i ∈ v, (v.filter (adj i)).card ≤ D) :
    ∃ s ⊆ v, (∀ i ∈ s, ∀ j ∈ s, i ≠ j → ¬ adj i j) ∧
      v.card ≤ s.card * (D + 1) := by
  classical
  let good (s : Finset α) := ∀ i ∈ s, ∀ j ∈ s, i ≠ j → ¬ adj i j
  let choices := v.powerset.filter good
  have nonempty : choices.Nonempty := ⟨∅, by simp [choices, good]⟩
  obtain ⟨s, hs, maximal⟩ := choices.exists_maximal nonempty
  have hs' : s ⊆ v ∧ good s := by simpa [choices] using hs
  let hood (i : α) := insert i (v.filter (adj i))
  have cover : v ⊆ s.biUnion hood := by
    intro x hx
    by_contra h
    have outside : x ∉ s := fun hxs => h (mem_biUnion.mpr ⟨x, hxs, mem_insert_self ..⟩)
    have noedge : ∀ i ∈ s, ¬ adj i x := by
      intro i hi hadj
      exact h (mem_biUnion.mpr ⟨i, hi, mem_insert_of_mem (mem_filter.mpr ⟨hx, hadj⟩)⟩)
    have extended : good (insert x s) := by
      intro i hi j hj hij
      rcases mem_insert.mp hi with hix | his
      · subst i
        rcases mem_insert.mp hj with hjx | hjs
        · exact (hij hjx.symm).elim
        · exact fun he => noedge j hjs (symm he)
      · rcases mem_insert.mp hj with hjx | hjs
        · subst j
          exact noedge i his
        · exact hs'.2 i his j hjs hij
    have memchoices : insert x s ∈ choices := by
      apply mem_filter.mpr
      exact ⟨mem_powerset.mpr (insert_subset hx hs'.1), extended⟩
    exact outside (maximal memchoices (subset_insert x s) (mem_insert_self x s))
  refine ⟨s, hs'.1, hs'.2, (card_le_card cover).trans ?_⟩
  apply card_biUnion_le.trans
  calc
    ∑ i ∈ s, (hood i).card ≤ ∑ _i ∈ s, (D + 1) := by
      apply sum_le_sum
      intro i hi
      exact (card_insert_le ..).trans (Nat.add_le_add_right (degree i (hs'.1 hi)) 1)
    _ = _ := by simp

/-- Entrywise limits of real quadratic forms with vanishing lower errors
    are nonnegative. The Fourier analysis supplies the entrywise limits. -/
theorem limit_of_square_tests {ι : Type*} (s : Finset ι) (p : ι → ℝ)
    (X : ℕ → ι → ι → ℝ) (B : ι → ι → ℝ) (err : ℕ → ℝ)
    (entries : ∀ i j, Tendsto (fun n => X n i j) atTop (𝓝 (B i j)))
    (vanish : Tendsto err atTop (𝓝 0))
    (lower : ∀ n, -err n ≤ ∑ i ∈ s, ∑ j ∈ s, (p i * p j) * X n i j) :
    0 ≤ ∑ i ∈ s, ∑ j ∈ s, (p i * p j) * B i j := by
  have h := tendsto_finsetSum s (fun i _ =>
    tendsto_finsetSum s (fun j _ => (entries i j).const_mul (p i * p j)))
  simpa using le_of_tendsto_of_tendsto' vanish.neg h lower

#print axioms central_pair_cost
#print axioms six_height_margin
#print axioms unique_neighbor
#print axioms independent_cover
#print axioms limit_of_square_tests

end NearCentralZeros
