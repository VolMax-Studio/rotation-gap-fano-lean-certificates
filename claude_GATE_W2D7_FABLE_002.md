# Claude Gate Result — W2 d=7 Formal Target (FABLE-002)

Date: 2026-09-20
Evaluated: FORMAL_TARGET_W2_D7.md, FEASIBILITY_REPORT.md, W2D7_v2.lean, W2D7Scratch{,Neg,Stress}.lean, gen.py
Toolchain: Lean 4.34.0 (commit 293d5d0c0c3f3dded4688b3ccd6a33939ac5102b)

## Gate Findings

### BLOCKERS (must fix before freeze/publish):

- B1 — Certificate band is the note's Not-Verified threshold, not its Verified threshold.
  Location: FORMAL_TARGET_W2_D7.md §Claim ("2.75 < W2,d=7^exact < 2.85"), encoded in
  W2D7_v2.lean:58-59.
  Proof: rotation-gap-fano-s1 README §2, opened live today, pre-registers
  "Claim W2 (Per-Distance Fano): All 3 distances within < 0.005 => Verified
   (any > 0.05 => Not Verified)". The Lean band is ±0.05 — the *rejection* edge.
  A value satisfying this certificate can still fail W2 by a factor of 10.
  Per Check 6 this is PARAMS-vs-code divergence regardless of which is "better".
  Measured fix (not proposed — compiled): band 2.795 < x < 2.805 encodes in the same
  Nat/Int form as
      lowerOk := decide (559 * (30 * BigDenom) < 200 * BigNumer)
      upperOk := decide (200 * BigNumer < 561 * (30 * BigDenom))
  Ran on 30 triples at n=50,000 tuned to exact avg 2.797832904: zero axioms, 0.34s.

- B2 — The band is misdescribed in the same paragraph that states it.
  Location: §Claim, "the one-decimal neighborhood centered at the reported printed
  value 2.80".
  Proof: 2.80 is printed to two decimals. The one-decimal neighborhood of a
  two-decimal literal is ±0.005, not ±0.05. ±0.05 is the neighborhood of "2.8".
  The margin sentence that follows (~0.048 / ~0.052) is internally consistent with
  ±0.05 and inconsistent with the label. Check 7, numeric layer.

- B3 — The feasibility precedent measures a different theorem than the one frozen.
  Location: FORMAL_TARGET §Feasibility precedent cites "0.31-0.85s, zero axioms,
  negative control correctly rejected"; the source is FEASIBILITY_REPORT.md, whose
  theorem (W2D7Scratch.lean:68-72, identically in Neg and Stress) is
      allValid = true -> denomPositive = true -> lowerOk /\ upperOk
  with lowerOk using `<=` (line 65). §Certificate shape forbids implication premises
  and mandates strict `<`.
  Proof that this is not cosmetic — measured, Lean 4.34.0 commit 293d5d0c…:
  I corrupted triple 1 to (11802, 43286, 1) so n*Q < S^2, then ran both shapes.
      implication shape  -> compiles, exit 0, "does not depend on any axioms",
                            while lowerOk actually evaluates false.
      conjunction shape  -> "decide proved that the proposition ... is false", exit 1.
  The implication form green-lights corrupted input with a clean axiom line.
  FEASIBILITY_REPORT's "not vacuous-true" claim holds only because both guards
  happened to be true in the negative-control set; W2D7ScratchNeg.lean varies the
  Fano level only and never falsifies a guard. The vacuity trap was never tested.
  Consequence: the 0.32s/0.35s/zero-axiom numbers cannot be cited as precedent for
  w2_d7_certificate. W2D7_v2.lean has no published measurement at all.

- B4 — The stress test varied the wrong axis; there is a hard cliff at list length 46.
  Location: FEASIBILITY_REPORT §Stress run and its closing recommendation
  ("should be for any later W1/W3/W4 pass too").
  Proof (measured, default settings, n_j = 50,000):
      length 45 -> passes.  length 46 -> "maximum recursion depth has been reached",
      theorem picks up sorryAx.
  Cost is flat in bignum magnitude (the axis the stress run varied: 10-20x, no
  measurable change) and cliff-edged in list length (the axis it did not).
  d=7 at 30 is 16 below the wall. W2 d=5 (120), W2 d=3 (270) and W1 (420) are all
  above it and would fail as written. With `set_option maxRecDepth 20000`:
      120 -> 0.60s,  270 -> 1.06s,  420 -> 1.51s, no recursion error.

### FIXES (should fix, not blocking):

- F1 — 2.80 is not in Table III. Opened arxiv.org/html/2604.11963: Table III carries
  the Fano row 0.856 / 2.42 and a qualitative "F grows with d" row. The numbers
  2.29 / 2.59 / 2.80 appear in §II F body text and the FIG. 4 caption. The
  "Table III / Sec. II F" attribution is inherited from rotation-gap-fano-s1
  README §1, so the mis-citation is already live in a ratified, Zenodo-deposited
  artifact (10.5281/zenodo.22309777) — fix both, not just this file.
- F2 — Published vs recomputed conflated. §Claim: "the reported printed value 2.80
  (arXiv…, via rotation-gap-fano-s1's independent recomputation)". Those are two
  quantities: PUBLISHED 2.80, RECOMPUTED 2.7978. The repo's own results table keeps
  them in separate columns; this sentence merges them.
- F3 — Name collision. The note's W2 is the conjunction over d ∈ {3,5,7}. This target
  certifies one component while its §Non-claim lists only W1/W3/W4 as out of scope,
  implying W2 is covered. Rename to W2-d7 and state it does not certify W2.
- F4 — gen.py:8-9 states "shots order ~10^4" and draws n ∈ [8000,12000], citing
  archive byte-size analysis. arXiv §II F states 50,000 shots per experiment. The
  stress set brackets it, so feasibility is unaffected, but the justification is
  wrong by ~5x. Bind n_j to metadata.json at extraction instead.
- F5 — The triples are transcribed, not generated. W2D7_v2.lean:5-36 are literals.
  I diffed them against triples.json: identical for the synthetic case. For the real
  run this must be a generator + byte-diff against W2D7_INPUT.json — the project's
  "generated from the source of truth, zero transcription" rule applies here more
  than anywhere, because the entire epistemic weight of the certificate sits on this
  one unproven binding.
- F6 — No length guard. The literal 30 in lines 58-59 is unbound to triples.length.
  Measured: adding `def lenOk : Bool := decide (triples.length = 30)` as a first
  conjunct compiles with zero axioms at 0.34s — no cost, closes the class.
- F7 — L0 not documented. The target pins archive MD5 and size but carries no verbatim
  license text, URL or access date for the Willow record. The 30 triples are derived
  data headed for a public repo.
- F8 — Claim-scope, for §Non-claim. Measured discriminating power: corrupting one of
  30 experiments' Q by ±20% leaves the certificate true with all guards satisfied
  (2.8057 -> 2.8479 / 2.7634). The certificate bounds the aggregate; it does not
  detect a per-experiment extraction error. [L2] At the 0.005 band that tolerance
  should shrink to roughly ±2% — verify on the real triples, not from this estimate.
- F9 — The quoted Rat error in FEASIBILITY_REPORT §Finding to log is not what Lean
  4.34.0 emits. Running the report's own example verbatim gives:
      "Tactic `decide` failed for proposition 1 / 2 < 3 / 4 because its `Decidable`
       instance (1 / 2).instDecidableLt (3 / 4) did not reduce to `isTrue` or
       `isFalse`."
  The report quotes a `Rat.blt` match-stuck message instead. Substance holds; the
  quoted block is headed for FAILURES.md and must be actual output (Check 4).

### CLEAN (checked, held, with the proof):

- Toolchain identity: independently fetched lean 4.34.0 reports commit
  293d5d0c0c3f3dded4688b3ccd6a33939ac5102b — matches the report's claim.
- W2D7_v2.lean compiles: "does not depend on any axioms", all four #eval true, 0.36s.
  Stricter than p10-core's [propext, Quot.sound] bar, as claimed.
- No Rat, no native_decide anywhere in the four .lean files. The Rat/decide trap
  reproduces (see F9 for the wording).
- Fold semantics: (Na*D + N*Da, Da*D) from (0,1) computes sum of N_j/D_j exactly;
  cross-multiplication is valid under denomPositive, which is a proved conjunct.
  Recomputed all four datasets in Python Fraction against the Lean #eval results —
  agree.
- n = 30 at d=7 traces to a source, not to an agent sentence: README §4.2 gives the
  archive composition 64.3% / 28.6% / 7.1% of 420 = 270 / 120 / 30.
- Archive pin verified live: Zenodo 13273331 lists google_105Q_surface_code_d3_d5_d7.zip
  at md5 21fa6ad35b395d838ebcdbc92e364a12 — matches the target.
- Determinism proof performed as doctrine requires (recreation, not identity alone):
  rename output -> rerun -> olean recreated byte-identical,
  sha256 e8092b290676d65eb89614c1a973aef32790469fe2325f33fff80bcc9c48ff40.
- Exit codes discriminate: pass -> 0, false proposition -> 1. A failed proof does not
  emit "does not depend on any axioms", so a grep-based CI check is not the trap here.
  The trap is B3's shape, which exits 0 on corrupted input.

VERDICT: BLOCKED

Note (2026-09-20): Superseded by v2 package pre-extraction.
