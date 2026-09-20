# Formal target — W2-d7 component certificate (v2)

Supersedes pre-extraction target:
FORMAL_TARGET_W2_D7.md
SHA-256: 2020b52bf1ec12d3c3fde0748e16c6113260bd78b5719a5cfdac9c0c5bbcca09

Reason:
Gate finding B1 — v1 encoded the outer R6 rejection boundary (±0.05)
instead of the preregistered R5 verification criterion (<0.005).

No real d=7 archive member was read before this supersession.

Status: FROZEN-PRE-EXTRACTION. This document is immutable from the moment its SHA-256 is
recorded (`FORMAL_TARGET_W2_D7_v2.sha256`, computed against this exact file).
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

## Claim

    2.795 < W2,d=7^exact < 2.805

i.e. the exact-rational statistic lies strictly inside the pre-registered R5
verification band (< 0.005) centered at the reported published value 2.80
(arXiv:2604.11963v1, Sec. II F and FIG. 4 caption).

Preregistration origin: Rule R5 at commit ff84608 defines
"Claim W2 (Per-Distance Fano): All 3 distances within < 0.005 => Verified
(any > 0.05 => Not Verified)".
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
- Lean does NOT re-derive the printed value "2.80" itself, nor any rounding
  rule Stenberg (2026) may have used; it only checks strict containment in
  the pre-registered R5 verification band.
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

Verified via FEASIBILITY_REPORT_v2.md on exact theorem conjunction shape across
three synthetic test cases (positive at n=50,000, band-negative, guard-corrupted).
Sub-second wall clock, zero axioms, exact discrimination.

## Input binding and generation rule

The real-data input bundle is not part of this target freeze. After
extraction, it SHALL be recorded in `W2D7_INPUT_BINDING_v2.md`, which must cite
the SHA-256 of this frozen target (`FORMAL_TARGET_W2_D7_v2.sha256`).
The final Lean file SHALL be mechanically generated from `W2D7_INPUT.json`
using `generate_W2D7_lean_v2.py`, with zero manual transcription.
