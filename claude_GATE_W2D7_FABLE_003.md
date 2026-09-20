# Claude Gate Result — W2-d7 v2 package (FABLE-003)

Evaluated: FORMAL_TARGET_W2_D7_v2.md, FEASIBILITY_REPORT_v2.md, W2D7_INPUT_BINDING_v2.md,
generate_W2D7_lean_v2.py, W2D7_{pos,band_neg,corrupt}.lean, triples_*.json,
FREEZE_RECORD_v2.sha256, FORMAL_TARGET_W2_D7{,_v2}.sha256, claude_GATE_W2D7_FABLE_002.md
Toolchain: Lean 4.34.0 (293d5d0c0c3f3dded4688b3ccd6a33939ac5102b)

BLOCKERS (must fix before this counts as frozen):

- B1 — Nothing is frozen. The freeze has no Git anchor and the two live claims are false.
  Proof, opened just now:
    git ls-remote https://github.com/VolMax-Studio/rotation-gap-fano-lean-certificates
      -> returns no refs.
    GitHub contents API on that repo -> {"message": "This repository is empty."}
    git clone --depth 1 rotation-gap-fano-s1 (HEAD bb5e68b, "Merge pull request #3 from
      VolMax-Studio/feat/rescience-manuscript") -> no `formal/` directory on main.
  The session summary states the package is "zamrznut u novom namenskom repozitorijumu …
  (i sinhronizovan u rotation-gap-fano-s1/formal/)". The transcript shows clone -> cp ->
  `git status`; there is no add, commit or push anywhere in it. Both artifacts exist only
  in a local working copy.
  Doctrine requires the criteria frozen *in Git* before download. A SHA-256 written into a
  local file is a checksum, not a freeze: nothing outside that machine can prove the target
  predates the extraction. Until the commit exists and Ivan merges it, extraction must not
  start. Check 9, and the catalogued self-report pattern.

- B2 — The v2 target attributes a non-verbatim, two-rule merge to Rule R5, and it is frozen
  under a recorded hash.
  Location: FORMAL_TARGET_W2_D7_v2.md §Claim, "Preregistration origin: Rule R5 at commit
  ff84608 defines 'Claim W2 (Per-Distance Fano): All 3 distances within < 0.005 => Verified
  (any > 0.05 => Not Verified)'."
  Actual PREREGISTRATION.md on main (sha256 8fa26d609e3c4cbe9b1681ca05c8cfbcadb09a64b83b5546a054e703a098098f,
  which is exactly the value pinned in data_manifest.json.preregistration_sha256):
      line 114  R5: "All three per-distance values reproduce within `< 0.005`"  -> W2: Verified
      line 115  R6: "Any per-distance value outside `± 0.05`"                   -> W2: Not Verified
  R5 is one rule. The parenthetical is R6. What the target quotes is the README's compressed
  paraphrase of both, presented as the definition of one. Check 4.

- B3 — W2 has three bands in the pre-registration; the certificate encodes two, and the
  frozen §Non-claim does not say so.
  Proof: PREREGISTRATION.md line 119 — "Values falling between the Verified and Not Verified
  bands in `R5`/`R6` receive `Verified with Limitations`."
  So the real structure is |Δ| < 0.005 Verified / 0.005 ≤ |Δ| ≤ 0.05 Verified with
  Limitations / |Δ| > 0.05 Not Verified. A Lean theorem is binary: outside 0.005 it emits
  sorryAx and exit 1, which is not a verdict in the controlled vocabulary. If the exact
  rational lands in the middle band, a failing certificate will be read as a defect while
  the note's own rules say the claim stands with limitations. That reading has to be
  pre-empted in the target text, and the target is already frozen.

- B4 — The v2 binding loosened a rule that v1 had deliberately fixed, with no changelog.
  v1 W2D7_INPUT_BINDING.md:117-121 — "Order convention (fixed now, not a post-extraction
  choice): Sort the 30 experiment directories by their POSIX relative path … lexicographically
  by byte value", with the stated reason that this is "what makes the determinism check … a
  real test of the extractor rather than of an unstated tie-break."
  v2 W2D7_INPUT_BINDING_v2.md:121-123 — "Sorted in canonical experiment order (stable sort by
  (patch, basis, round); record the exact sort key used …)". The key is now chosen at
  extraction time.
  Measured on the real directory set from data_manifest.json (30 d=7 dirs, patch d7_at_q6_7):
      byte-lexicographic   -> X/r01, X/r10, X/r110, X/r13, X/r130, X/r150, …
      numeric (basis,round)-> X/r01, X/r10, X/r13,  X/r30, X/r50,  X/r70,  …
  Different order -> different W2D7_INPUT.json bytes -> different sha256. The determinism
  check then proves only that the extractor used the same key twice.
  Also silently removed in v2: the "## Extractor identity" section, and the
  "Popcount equivalence check run: <FILL — yes/no, and result>" control (grep 1 -> 0).
  A hardening pass that removes controls is exactly what the Parametric Changelog is for.

- B5 — FEASIBILITY_REPORT_v2 §2 quotes a Lean message Lean does not emit.
  Report: "error: Tactic `decide` failed for proposition / lenOk = true ∧ … / is false".
  Measured on the shipped file, same toolchain:
      W2D7_band_neg.lean:70:2: error: Tactic `decide` proved that the proposition
        lenOk = true ∧ allValid = true ∧ denomPositive = true ∧ lowerOk = true ∧ upperOk = true
      is false
  "failed for proposition …" and "proved that the proposition … is false" are two different
  Lean messages; §2 splices them. §3 quotes the same message correctly, so the two adjacent
  blocks disagree about what Lean says. This is F9 from the previous gate, reappearing in the
  file that was written to close it — and this one is hash-frozen.

FIXES (should fix, not blocking):

- F1 — FEASIBILITY_REPORT_v2 §3: "50000 · 1 < 225000^2". triples_corrupt.json[0] is
  [50000, 233640, 1]; S_0 is 233640.
- F2 — The superseded generator is still in the package. generate_W2D7_lean.py still emits
  11/4 and 57/20 and no lenOk — running it produces a clean-looking certificate carrying the
  rejected band. It is not in FREEZE_RECORD_v2.sha256, so nothing pins it either. Delete it
  or put SUPERSEDED in its first line.
- F3 — Generated Lean carries no provenance. generate_W2D7_lean_v2.py writes no reference to
  the input file or its sha256, so W2D7_v2.lean alone cannot be traced to a W2D7_INPUT.json.
  One emitted comment line closes the gap that F5 of the previous gate was about.
- F4 — claude_GATE_W2D7_FABLE_002.md cites v1 text that is absent from the file with the
  recorded hash. In the file hashing to 2020b52b…: grep "0.31-0.85" -> 0 hits;
  grep "Input provenance" -> 0 hits; it reads "sub-second wall clock" and points to
  scratch/feasibility/FEASIBILITY_REPORT.md. So the gate examined a different v1 revision than
  the one now frozen. The gate artifact should record the sha256 of the file it actually read.
  (Its W2D7_v2.lean:58-59 citation does check out — verified by line number.)
- F5 — The verdict line of that gate file was edited to "BLOCKED (Superseded by v2 package
  pre-extraction)". Supersession is a later fact about the gate, not part of its verdict.
  Put it in a dated note under the verdict line.
- F6 — R5's 0.005 governs |F_rec − published| for the float64 recomputation. The v2
  certificate applies the same tolerance to the exact-rational quantity that the same
  document insists is a different quantity. Defensible, but the transfer should be stated
  rather than inherited silently.
- F7 — 0.35s and ~475 MB are warm-cache figures. Cold first invocation of W2D7_pos.lean in a
  fresh directory measured 19.1s here; warm re-runs 0.35-0.38s. The report does say "warm
  cache" — just note it so a cold CI run is not read as a regression.

CLEAN (checked, held, with the proof):

- Freeze record is internally sound: all four digests in FREEZE_RECORD_v2.sha256 recompute
  byte-for-byte against the uploaded files. FORMAL_TARGET_W2_D7.sha256 also matches its file
  (2020b52b…; see F4 for which revision that is).
- The three v2 Lean runs reproduce exactly as reported:
      pos       -> exit 0, "does not depend on any axioms", all five #eval true, 0.35s warm
      band_neg  -> exit 1, lenOk/allValid/denomPositive/lowerOk true, upperOk false
      corrupt   -> exit 1, allValid false
  The conjunction shape is non-vacuous under a falsified guard. B3 of the previous gate is
  closed, by measurement, on the actual shipped files.
- Exact averages recomputed in Python Fraction: pos 2.797799660 (inside 559/200 … 561/200),
  band-neg 2.819841308 (outside). Both match the report to every printed digit.
- Generator is deterministic and does what the binding claims: regenerating all three .lean
  files from their .json byte-diffs identical to the shipped files; the len==30 assert fires
  on a 29-triple input.
- n = 30 at d=7 is now verified at member level rather than from a percentage:
  data_manifest.json (member_count 1260) contains exactly 30 d=7 experiment directories, all
  under patch d7_at_q6_7, with 90 files — circuit_ideal.stim / detection_events.b8 /
  metadata.json, 30 each. That is precisely the 90-row table the binding requires, and the
  example path in the binding is correct.
- PREREGISTRATION.md on main hashes to the value pinned inside data_manifest.json — the
  custody chain the binding relies on is intact at that link.
- R5 and R6 labels in the v2 supersession header are correct against PREREGISTRATION.md
  lines 114-115. My previous session could not see the rule numbers; they check out.
- F1, F2, F3 and F6 of the previous gate are closed in the v2 target: citation is now
  "Sec. II F and FIG. 4 caption"; published 2.80 and float64 2.7978273252888646 are kept
  apart; the artifact is renamed W2-d7 component with explicit non-certification of full W2;
  lenOk is present and proved.
- No archive-derived value appears anywhere in the package. I cannot verify the archive was
  never opened — only that nothing in these files came from it.

VERDICT: BLOCKED
