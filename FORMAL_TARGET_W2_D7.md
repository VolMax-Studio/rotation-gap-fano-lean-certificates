# Formal target — W2, d=7

Status: FROZEN. This document is immutable from the moment its SHA-256 is
recorded (`FORMAL_TARGET_W2_D7.sha256`, computed against this exact file).
No field in this document is completed after that point, ever — there is no
`<PENDING>` here and none may be added. A later change of any kind is a new
target under a new filename, never an edit to this one.

## Target

Exact-rational W2,d=7 statistic, computed from (n, S, Q) sufficient statistics
per experiment (n = shots, S = sum of per-shot detection-event counts,
Q = sum of squared per-shot detection-event counts), for the 30 experiments
at code distance d=7 in the Google Willow archive (10.5281/zenodo.13273331),
under the estimator frozen in rotation-gap-fano-s1/PREREGISTRATION.md
(ddof=1 sample variance per experiment; mean over the 30 per-experiment
Fano ratios).

Per-experiment exact Fano ratio: F_j = (n_j Q_j - S_j^2) / ((n_j - 1) S_j)
W2,d=7^exact = (1/30) * sum_{j=1}^{30} F_j

## Claim

    2.75 < W2,d=7^exact < 2.85

i.e. the exact-rational statistic lies strictly inside the one-decimal
neighborhood centered at the reported printed value 2.80 (arXiv:2604.11963v1,
Table III / Sec. II F, via rotation-gap-fano-s1's independent recomputation).
The bound is strict on both sides (not <=), so no unverified rounding
convention (banker's rounding, round-half-up, etc.) is assumed for how "2.80"
was printed from a float64 upstream. Given the already-measured float64 value
2.7978273252888646 (rotation-gap-fano-s1/results/results.json), both margins
are wide (~0.048 and ~0.052) relative to that float value; this claim does
not depend on how close to the boundary the true exact value falls.

## Non-claim (explicit epistemic boundary)

- Lean does NOT prove IEEE-754/NumPy float64 execution equivalence. The
  exact-rational recomputation is a separate quantity from the float64
  pipeline in reproduce.py; the two are compared, never conflated.
- Lean does NOT verify popcount/decoding correctness of the raw
  detection_events.b8 records; that is rotation-gap-fano-s1's own P2
  (HALTING) premise and --verify-popcount equivalence check, both already
  gated at Note level.
- Lean does NOT re-derive the printed value "2.80" itself, nor any rounding
  rule Stenberg (2026) may have used; it only checks strict containment in
  the printed digit's one-decimal neighborhood.
- This target covers W2, d=7 only. W1, W3, W4 are explicitly out of scope
  until this one clears end to end. W4 in particular must not reuse this
  file's ddof assumptions without re-deriving them (ddof=1 for Fano,
  ddof=0 for population std/SE — see rotation-gap-fano-s1/reproduce.py
  lines 429-430 vs 474-476).

## Validity guards (proved, not assumed, in the final certificate)

    allValid      : forall j, n_j > 1 AND S_j > 0 AND n_j * Q_j >= S_j^2
    denomPositive : the accumulated cross-multiplication denominator is > 0

Both are conjuncts of the single certificate theorem, never premises of an
implication — a false guard fails the theorem, it cannot vacuously pass one.

## Formalization pattern (mandatory, per feasibility scratch test finding)

No `Rat` type. Core Lean 4.34.0's `Rat` `/` operator and its `<`/`<=`
`Decidable` instances (`Rat.blt`) do not reduce under kernel `decide` — this
was measured directly (see scratch/feasibility/FEASIBILITY_REPORT.md, "Rat"
finding) and would silently require `native_decide` if used, which this
project's trust boundary excludes. All arithmetic here is `Nat`/`Int` only,
with denominators cleared by explicit cross-multiplication (unreduced
fraction fold), never by gcd-based normalization.

## Certificate shape (no implication premises)

    theorem w2_d7_certificate :
        allValid = true ∧
        denomPositive = true ∧
        lowerOk = true ∧
        upperOk = true := by
      decide

where lowerOk/upperOk encode the strict cross-multiplied form:

    lowerOk := decide (11 * (30 * BigDenom) < 4 * BigNumer)
    upperOk := decide (20 * BigNumer < 57 * (30 * BigDenom))

## Feasibility precedent

Scratch test on 30 synthetic (n,S,Q) triples of representative magnitude
(and a 10-20x stress variant): sub-second wall clock, zero axioms, negative
control correctly rejected. Full measurement in
scratch/feasibility/FEASIBILITY_REPORT.md. Not evidence about the real data —
only that the proof strategy is computationally and trust-boundary feasible.

## Input binding

The real-data input bundle is not part of this target freeze. After
extraction, it SHALL be recorded in `W2D7_INPUT_BINDING.md`, which must cite
the SHA-256 of this frozen target (`FORMAL_TARGET_W2_D7.sha256`). This file
is never edited to record that binding; the binding document points to this
file, not the reverse.
