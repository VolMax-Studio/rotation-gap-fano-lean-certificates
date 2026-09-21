> [!WARNING]
> **HISTORICAL PROJECT CHAT GATE RECORD**
> This document is a transcription by assistant Ananke of a gate response produced by Claude within the VolMax Observatory Project chat session during post-extraction verification of commit `bc7c76e`.
> It was NOT issued or endorsed by Anthropic as an institutional review and was NOT independent of the operator.
> Preserved for audit history. See [`PROVENANCE_CORRECTION_2026-09-21.md`](PROVENANCE_CORRECTION_2026-09-21.md) and [`GATE_PROVENANCE_CORRECTION.md`](GATE_PROVENANCE_CORRECTION.md).

# Historical Project Chat Gate Record (FABLE-005)

Evaluated: origin/feat/w2-d7-post-extraction @ bc7c76e1d12062ba036d9ecddc4f2257928148d6  
Anchor:    origin/main @ 2de083e8c1887e57a2b507465915c18e75bdb3c4  
Toolchain: Lean 4.34.0 (293d5d0c0c3f3dded4688b3ccd6a33939ac5102b)  

---

```text
GATE RESULT — W2-d7 post-extraction (FABLE-005)

Evaluated: origin/feat/w2-d7-post-extraction @ bc7c76e1d12062ba036d9ecddc4f2257928148d6
Anchor:    origin/main @ 2de083e8c1887e57a2b507465915c18e75bdb3c4
Toolchain: Lean 4.34.0 (293d5d0c0c3f3dded4688b3ccd6a33939ac5102b)

BLOCKERS (on the ratification step, not on the artifact):

- B1 — The commit SHA in the handover does not exist.
  Handover: "Commit SHA za evaluaciju: bc7c76e10ba8e7f1e73778216183df5745484aa7"
  Actual:    bc7c76e1d12062ba036d9ecddc4f2257928148d6
  Only the 8-character prefix matches; the remaining 32 are not this commit's.
  git rev-parse on the branch returns the second. I gated the real one.
  The other two SHAs in the handover are correct in full: 2de083e8c1887e57a2b507465915c18e75bdb3c4
  and 1c366f7ef45362d6dc4b63302c73698153200808. A ratification instruction that pins a
  nonexistent 40-character identifier cannot be acted on, and a fabricated full hash next to
  two correct ones is the catalogued pattern, not a typo class I can wave through.

- B2 — The PR head Ivan would merge is two commits behind the package.
  git ls-remote origin 'refs/pull/*', queried twice:
      refs/pull/1/head -> bdeda47d94adba5a2c8691b542429b33525ff191   (merged, = main's second parent)
      refs/pull/2/head -> 1c366f7ef45362d6dc4b63302c73698153200808
  The branch tip is bc7c76e. Missing from that PR head ref: 8e6f05b (binding's extraction
  commit/timestamp record) and bc7c76e (PROVENANCE_AND_LICENSING.md + POST_EXTRACTION_RECORD_v3.sha256).
  Merging PR #2 as the ref currently stands puts an incomplete package on main: no L0
  document, no post-extraction record, and a binding missing the extractor identity it is
  supposed to carry.
  Open the PR page before clicking merge and confirm the head commit reads bc7c76e1d120….
  If it does, this is a stale ref and B2 dissolves; if it still reads 1c366f7, push the
  branch again or repoint the PR.

FIXES (should fix, not blocking):

- F1 — The determinism check is weaker than the binding implies. extract_w2d7.py calls
  run_extraction() twice inside one process, and sorted_dirs is computed once, outside the
  function. The second pass re-reads the files but does not re-derive the ordering and does
  not test a process restart. The binding records "STATUS: PASSED. Two successive extraction
  runs were executed off disk" — accurate as written, but it cannot catch an ordering or
  environment nondeterminism, which is the exact thing the order convention exists to guard.
  A second run as a separate process invocation closes it. (Not blocking: I re-derived the
  order independently — see CLEAN.)
- F2 — The binding's gloss of the detector count is wrong even though the code is right.
  §Extraction rule says "n_det = number of DETECTOR tokens … (same method as reproduce.py's
  count_detectors: parse the circuit, count DETECTOR instructions)". reproduce.py:346-348 is
  z.read(stim_path).decode().count("DETECTOR"), documented there as "Author line 28:
  substring count". extract_w2d7.py does the substring count, so it matches the authoritative
  clause and contradicts the gloss. A reimplementer following the gloss would tokenise and
  could land on a different n_det.
- F3 — The popcount equivalence check is narrower than its name. Both paths in
  extract_w2d7.py take the same n_det, so it compares two bit-summing implementations, not
  two determinations of the detector count. The tiling HALT also cannot see an n_det
  over-count of up to 7 (same ceil). The binding's "30/30 … (PASS)" is true; it just does not
  cover that gap.
- F4 — Identity block composed rather than copied. LICENSE:3 "Copyright (c) 2026 VolMax
  Studio Lab (Ivan Nestorov)" and PROVENANCE_AND_LICENSING.md §4 "VolMax Studio Lab / Ivan
  Nestorov". The pinned block is "Nestorov, Ivan / VolMax Studio Lab / ORCID
  0009-0006-7940-9539" — the ORCID is absent from both, and the name order differs.
- F5 — extract_w2d7.py hardcodes MANIFEST_PATH as /home/volmax-studio/volmax-projects/…
  It is committed as the authoritative extractor but cannot run anywhere else unedited.
- F6 — Carried forward, still open: FABLE-004 F1 (FABLE-002 does not record which v1
  revision it read), F2 (scalability numbers not produced by the report that prints them),
  F3 (supersession record calls a BLOCKER a "minor reporting defect"), F6 (README gate
  history omits B3 and B5). All in frozen or committed files; correct in the next document.

CLEAN (checked, held, with the proof):

- FABLE-004 B1 is closed the way the doctrine asks. origin/main is 2de083e, a GitHub merge
  commit — committer GitHub <noreply@github.com>, two parents 5beb2f2 and bdeda47, subject
  "Merge pull request #1 from VolMax-Studio/feat/w2-d7-v3-ratify". The agent-direct push is
  not erased: 717acc1 is preserved on branch history/agent-direct-main-20260920.
- The frozen pre-extraction artifacts are untouched since the anchor. Against
  git show 2de083e:<file>, byte-identical: FORMAL_TARGET_W2_D7_v3.md 02c9f057…,
  generate_W2D7_lean_v3.py 1a2644c2…, FEASIBILITY_REPORT_v3.md 78e04150…,
  FREEZE_RECORD_v3.sha256 270d11d3….
- POST_EXTRACTION_RECORD_v3.sha256 verifies 9/9 against the branch bytes.
  W2D7_INPUT.sha256 matches the measured file: 3dd3a86624b53f3aead8972fd902cee7431c11d1f42199e05f9a055e08892b5f.
- The custody chain closes independently. I parsed all 90 rows of the binding: for every row,
  expected_sha256 == measured_sha256 == the value in rotation-gap-fano-s1/data_manifest.json,
  0 mismatches, 0 not-in-manifest. The 90 paths are exactly the 90 d=7 members in that
  manifest (30 each of circuit_ideal.stim, detection_events.b8, metadata.json).
- The order convention was actually followed, and I can show it from the data rather than
  from the binding's word. Re-deriving the byte-lexicographic order from data_manifest.json
  gives X/r01, r10, r110, r13, r130, r150, r170, r190, r210, r230, r250, r30, r50, r70, r90,
  then Z identically. S_j/n_j in W2D7_INPUT.json, in file order, is 1.98, 35.2, 415.2, 46.3,
  505.8, 563.4, 654.6, 731.9, 770.3, 884.8, 935.5, 114.9, 183.7, 265.0, 337.0 — roughly
  3.7-3.9 detections per shot per round at every position except r01, which is the
  single-round boundary case the source paper itself describes. That non-monotone sequence is
  the fingerprint of lexicographic order, and it is the right fingerprint.
- The extractor reproduces the audit's own code rather than paraphrasing it. n_det,
  bytes_per_shot = (n_det + 7) // 8, the author loop and the unpackbits path follow
  reproduce.py:346-370 as written, substring-count convention included. Guards are enforced
  at extraction and proved again in Lean.
- The certificate proves on real data: 'w2_d7_certificate' does not depend on any axioms,
  all five #eval true, exit 0, 0.31s warm. Regenerating from the frozen generator yields a
  byte-identical file; rename → regenerate recreates it byte-identically. The header carries
  -- Input SHA-256: 3dd3a866…, matching W2D7_INPUT.sha256.
- The number. Recomputed from W2D7_INPUT.json in Python Fraction, independently of Lean:
      exact-rational W2,d=7 = 2.7978273252888646
      float64 in rotation-gap-fano-s1/results/results.json = 2.7978273252888646
      difference = 0.0 at double precision
      |x − 2.80| = 0.0021726747…, inside the R5 band of 0.005, 43% of it consumed
  Guards hold on all 30 triples; per-experiment Fano spans 1.785 to 3.597; n_j = 50,000
  uniformly, matching the source paper's stated shot count.
- L0 verified at the source, not from the document. zenodo.org/records/13273331, Rights:
  Creative Commons Attribution 4.0 International, with the record stating the license permits
  re-distribution and re-use provided the creator is credited; creator Google Quantum AI;
  listed md5 for google_105Q_surface_code_d3_d5_d7.zip is 21fa6ad35b395d838ebcdbc92e364a12,
  matching the pin. PROVENANCE_AND_LICENSING.md separates the 2024 dataset creator from the
  2026 third-party analysis correctly. FABLE-002 F7 closed.
- Archive identity re-measured at extraction: MD5 and size both equal the pinned values.
  Tiling and popcount checks recorded as run. No <FILL> remains in the binding.
- No raw data in the repository — only the 30 derived (n, S, Q) sufficient statistics.

VERDICT: the artifact at bc7c76e1d12062ba036d9ecddc4f2257928148d6 SURVIVES-REVIEW.
The merge to main is BLOCKED until B2 is resolved and B1 is corrected in whatever text is
used to authorise it. Nothing here is ratified; that remains yours.
```
