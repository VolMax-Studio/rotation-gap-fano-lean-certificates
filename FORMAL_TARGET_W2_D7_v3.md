# Formal target — W2-d7 component certificate (v3)

Supersedes pre-extraction targets:
- `FORMAL_TARGET_W2_D7.md` (SHA-256: `2020b52bf1ec12d3c3fde0748e16c6113260bd78b5719a5cfdac9c0c5bbcca09`)
  Reason: Gate finding B1 (FABLE-002) — v1 encoded outer R6 rejection boundary (±0.05) instead of R5 (<0.005).
- `FORMAL_TARGET_W2_D7_v2.md` (SHA-256: `f0c404862acacfff83b563fea37830d947a74127cdfc34d2f91b801d45e11980`)
  Reason: Gate findings B2, B3, F6 (FABLE-003) — v2 conflated R5 and R6 into a single paraphrase, omitted the note's three-band structure, and did not explicitly define the corroboration transfer from float64 R5 to exact-rational.

No real d=7 archive member was read before this supersession.

Status: Git-frozen before extraction and before reading any real d=7 archive member.
This document is immutable from the moment its SHA-256 is recorded
(`FORMAL_TARGET_W2_D7_v3.sha256`, computed against this exact file) and committed to Git.
No field in this document is completed after that point, ever — there is no
`<PENDING>` here and none may be added. A later change of any kind is a new
target under a new filename, never an edit to this one.

## Target

Exact-rational W2-d7 component statistic, computed from (n, S, Q) sufficient statistics
per experiment (n = shots, S = sum of per-shot detection-event counts,
Q = sum of squared per-shot detection-event counts), for the 30 experiments
at code distance d=7 in the Google Willow archive (10.5281/zenodo.13273331),
under the estimator pre-registered in rotation-gap-fano-s1/PREREGISTRATION.md
(ddof=1 sample variance per experiment; mean over the 30 per-experiment
Fano ratios).

Per-experiment exact Fano ratio: F_j = (n_j Q_j - S_j^2) / ((n_j - 1) S_j)
W2,d=7^exact = (1/30) * sum_{j=1}^{30} F_j

## Preregistration Origin and Corroboration Claim

Actual rules in `PREREGISTRATION.md` on main (SHA-256: `8fa26d609e3c4cbe9b1681ca05c8cfbcadb09a64b83b5546a054e703a098098f`):
- Line 114, Rule R5: "All three per-distance values reproduce within `< 0.005`" -> W2: `Verified`
- Line 115, Rule R6: "Any per-distance value outside `± 0.05`" -> W2: `Not Verified`
- Line 119: "Values falling between the Verified and Not Verified bands in `R5`/`R6` receive `Verified with Limitations`."

### Exact Corroboration Statement:
> If the theorem succeeds, Lean 4 kernel-checks that the exact-rational W2-d7
> component derived from the bound 30 sufficient-statistic triples lies within
> the same ±0.005 numerical band used by preregistered Rule R5 around the published
> value 2.80. This is a derived exact-rational corroboration certificate, not a
> re-execution of the original float64 R5 verdict rule. Failure of the theorem
> alone carries no controlled W2 verdict.

The Lean theorem is binary: it either proves containment within ±0.005 or fails.
If the exact rational lands in the intermediate band (0.005 <= |Delta| <= 0.05),
the theorem fails (`sorryAx` / exit 1), which means "certificate not established",
NOT a verdict of `Not Verified` (since under the note's three-band structure,
such an outcome receives `Verified with Limitations`).

## Formal Claim

    2.795 < W2,d=7^exact < 2.805

i.e. the exact-rational statistic lies strictly inside the ±0.005 numerical band
centered at the published value 2.80 (arXiv:2604.11963v1, Sec. II F and FIG. 4 caption).

The bound is strict on both sides (< not <=), so no unverified rounding
convention (banker's rounding, round-half-up, etc.) is assumed for how "2.80"
was printed from upstream data.

The published comparator "2.80" and the historical float64 recomputation
2.7978273252888646 (rotation-gap-fano-s1/results/results.json) are kept
strictly as separate quantities and are never conflated.

## Non-claim (explicit epistemic boundary)

- Scope: W2-d7 component only. This target certifies one component; it
  explicitly does NOT certify full W2 (which requires the conjunction over
  all three distances d in {3, 5, 7}). W1, W3, W4, and distances d=3, d=5
  are out of scope.
- Corroboration certificate vs verdict engine: Lean does not execute
  PREREGISTRATION.md's three-band verdict logic; it verifies only the positive
  corroboration condition (< 0.005).
- Aggregate certificate vs member custody: Lean bounds the aggregate arithmetic
  mean over the 30 bound triples; it does NOT detect an individual single-experiment
  extraction or decoding error (discriminating power at aggregate level). Custody,
  single-member data integrity, popcount correctness, and stimulus decoding are
  exclusively the responsibility of the L1 custody layer (archive MD5, 90 member
  SHA-256 hashes against data_manifest.json, tiling checks, second-run byte identity).
- Lean does NOT prove IEEE-754/NumPy float64 execution equivalence. The
  exact-rational recomputation is a separate quantity from the float64
  pipeline in reproduce.py; the two are compared, never conflated.
- Lean does NOT verify popcount/decoding correctness of the raw
  detection_events.b8 records; that is rotation-gap-fano-s1's own P2
  (HALTING) premise and --verify-popcount equivalence check, both already
  gated at Note level.
- Scalability: The 30 triples at d=7 evaluate well within default limits.
  Lean 4.34.0 default recursion depth encounters a cliff at list length 46.
  Future passes for d=5 (120 triples), d=3 (270 triples), and W1 (420 triples)
  must explicitly supply `set_option maxRecDepth 20000` or refactor the fold
  strategy.

## Validity guards (proved, not assumed, in the final certificate)

    lenOk         : triples.length = 30
    allValid      : forall j, n_j > 1 AND S_j > 0 AND n_j * Q_j >= S_j^2
    denomPositive : the accumulated cross-multiplication denominator is > 0

All three are conjuncts of the single certificate theorem, never premises of an
implication — a false guard fails the theorem (kernel decide proved false, exit 1);
it cannot vacuously pass.

## Formalization pattern (mandatory, per feasibility finding)

No `Rat` type. Core Lean 4.34.0's `Rat` `/` operator and its `<`/`<=`
`Decidable` instances do not reduce under kernel `decide`. All arithmetic
here is `Nat`/`Int` only, with denominators cleared by explicit
cross-multiplication (unreduced fraction fold), never by gcd-based normalization.

## Certificate shape (pure conjunction, no implication premises)

    theorem w2_d7_certificate :
        lenOk = true ∧
        allValid = true ∧
        denomPositive = true ∧
        lowerOk = true ∧
        upperOk = true := by
      decide

where lowerOk/upperOk encode the strict cross-multiplied form:

    lowerOk := decide (559 * (30 * BigDenom) < 200 * BigNumer)
    upperOk := decide (200 * BigNumer < 561 * (30 * BigDenom))

## Feasibility precedent

Verified via FEASIBILITY_REPORT_v3.md on exact theorem conjunction shape across
three synthetic test cases (positive at n=50,000, band-negative, guard-corrupted).
Sub-second warm wall clock, zero axioms, exact discrimination.

## Input binding and generation rule

The real-data input bundle is not part of this target freeze. After
extraction, it SHALL be recorded in `W2D7_INPUT_BINDING_v3.md`, which must cite
the SHA-256 of this frozen target (`FORMAL_TARGET_W2_D7_v3.sha256`).
The final Lean file SHALL be mechanically generated from `W2D7_INPUT.json`
using `generate_W2D7_lean_v3.py`, with zero manual transcription and explicit
input SHA-256 recorded in the generated source.
