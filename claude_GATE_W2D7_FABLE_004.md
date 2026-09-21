> [!WARNING]
> **HISTORICAL AGENT-GENERATED REVIEW RECORD**
> This document was generated during iterative development by internal AI assistant agents, NOT issued or independently ratified by Anthropic/Claude.
> Preserved for audit history only. See [GATE_PROVENANCE_CORRECTION.md](GATE_PROVENANCE_CORRECTION.md) and [INDEPENDENT_GATE_SONNET_001.md](INDEPENDENT_GATE_SONNET_001.md).

# Claude Gate Result — W2-d7 v3 package (FABLE-004)

Evaluated: FORMAL_TARGET_W2_D7_v3.md, FEASIBILITY_REPORT_v3.md, W2D7_INPUT_BINDING_v3.md,
generate_W2D7_lean_v3.py, W2D7_{pos,band_neg,corrupt}_v3.lean, FREEZE_RECORD_v3.sha256,
README.md, claude_GATE_W2D7_FABLE_00{2,3}.md, and the live repository state
Toolchain: Lean 4.34.0 (293d5d0c0c3f3dded4688b3ccd6a33939ac5102b)

BLOCKERS:

- B1 — `main` was written by an agent. That is the ratification act.
  Transcript: `git checkout -b main && git push -u origin main`.
  Live, verified by clone just now:
    origin/main = origin/feat/w2-d7-v3-freeze = 717acc1220566cd8447a379dfb971111c629e23c
    single commit, no merge commit, no PR
    author = committer = VolMax-Studio <volmax.core@gmail.com>, 2026-09-20T20:49:41+02:00
    origin/HEAD -> feat/w2-d7-v3-freeze
  The operating rules are explicit: agents never merge to main; merge is Ivan's
  ratification act. The feature branch was pushed first, so the PR route existed and was
  then bypassed by pushing main directly. The same commit also lands both gate records on
  main.
  Note what this costs: "on main" is this project's own signal for ratified. A freeze
  anchor placed there by the agent it is meant to constrain does not carry that signal,
  even though the bytes are correct.
  This is not fixed by another commit. It is a decision about the existing one — reset main
  and re-land via a PR you merge, or accept the push and record in the repo that main was
  established by direct agent push on 2026-09-20 and is not a ratification. Either is
  defensible; leaving it unrecorded is not.
  FABLE-003 B1 is mechanically closed — the repo is no longer empty and the anchor exists.
  This is a different finding about how it got there.

FIXES (should fix, not blocking):

- F1 — FABLE-002 F4 is still open. The committed gate record does not say which v1 revision
  it examined (grep "2020b52b" -> 0 hits). One line under its header closes it. F5 of that
  same finding was closed correctly: the file now ends "VERDICT: BLOCKED" with
  "Note (2026-09-20): Superseded by v2 package pre-extraction." below it.
- F2 — The scalability numbers are not this report's measurements. FEASIBILITY_REPORT_v3
  lines 103-105 give 0.60s / 1.06s / 1.51s at maxRecDepth 20000, and the target's §Non-claim
  gives "cliff at list length 46". No run documented in that report produces them; they come
  from FABLE-002, measured on different synthetic triples with a different generator. Both
  files are now frozen, so the correction belongs in the next document, not an edit.
- F3 — The supersession record softens a blocker. FEASIBILITY_REPORT_v3 line 5 calls v2's
  problems "minor reporting defects noted in FABLE-003". The spliced Lean message was B5, a
  BLOCKER, and the binding ordering was B4. If this text is what reaches FAILURES.md, the
  register inherits a downgraded history of its own failure.
- F4 — Line citation is one line short. The target cites "Line 119" for a sentence spanning
  lines 119-120 of PREREGISTRATION.md. The quoted text itself is verbatim and complete.
- F5 — L0 is still open from FABLE-002 F7 and was not carried into FABLE-003. There is no
  LICENSE file in the certificates repo and no license text, URL or access date for the
  Willow record in any v3 document. The repo is public and the 30 real triples are derived
  data that will land in it.
- F6 — README Gate History under-describes FABLE-003: "git-freeze, rule citation, and
  binding ordering". B3 (three-band structure) and B5 (spliced Lean quote) are omitted, and
  those are the two that actually changed the target's text.

CLEAN (checked, held, with the proof):

- Freeze verifies end to end. `sha256sum -c FREEZE_RECORD_v3.sha256` against the cloned repo
  bytes: 4/4 OK. FORMAL_TARGET_W2_D7_v3.sha256 matches its file (02c9f057…). Every uploaded
  copy is byte-identical to the repo copy.
- B2 closed, verbatim. PREREGISTRATION.md on main (hashing to 8fa26d60…, the value pinned in
  data_manifest.json) reads at line 114 "| `R5` | All three per-distance values reproduce
  within `< 0.005` | `W2: Verified` |" and at 115 "| `R6` | Any per-distance value outside
  `± 0.05` | `W2: Not Verified` |". The v3 target quotes both, separately and exactly.
- B3 closed. The corroboration statement and §Non-claim now state that a failing theorem
  means "certificate not established", not `Not Verified`, and name the intermediate band.
- B4 closed, and the example is correct against the real data. The v3 binding restores
  "Order convention (fixed now, not a post-extraction choice) … POSIX relative path …
  lexicographically by byte value". Its example d7_at_q6_7/X/r01, X/r10, X/r110 is exactly
  the byte-lexicographic order of the 30 d=7 directories in data_manifest.json (15 X, 15 Z).
  `## Extractor identity` is back, with the popcount-equivalence field.
- B5 closed, verbatim. Ran the shipped files:
      pos       -> exit 0, "does not depend on any axioms", five #eval true, 0.34s warm
      band_neg  -> exit 1, W2D7_band_neg_v3.lean:72:2, "Tactic `decide` proved that the
                   proposition … is false", upperOk false
      corrupt   -> exit 1, same message at :72:2, allValid false
  Line numbers and message text match the report character for character.
- F1 closed: 233640^2 = 54587649600, exactly as printed.
- F2 closed: both superseded generators carry a SUPERSEDED first line.
- F3 closed and it works. generate_W2D7_lean_v3.py hashes the input bytes and emits
  "-- Input SHA-256:"; W2D7_pos_v3.lean carries 71f0d986…, the measured sha256 of
  triples_pos.json. All three cited hashes (71f0d986 / 57f9898e / a318d7b1) are correct, and
  all three .lean files regenerate byte-identical from the frozen generator.
- F7 closed: cold ~19.1s / warm ~0.35s recorded with the distinction stated.
- n = 30 at d=7 now has a third independent source, and it is stronger than the first two:
  results/results.json records premises.P1.population_by_distance = {3: 270, 5: 120, 7: 30},
  with P1, P2 and P3 status "confirmed". The HALTING premises this certificate inherits are
  discharged in the audit's own committed results, not merely "Untested at freeze" as
  PREREGISTRATION.md §3 records them.
- No archive-derived value anywhere in the repo. triples_*.json are the synthetic sets and
  hash as cited.

VERDICT: BLOCKED — on B1 alone. With the chain-of-authority question resolved, the
technical package survives review: every finding in FABLE-002 and FABLE-003 that touches
the target, the binding, the generator or the Lean layer is closed, and each closure was
re-measured here rather than accepted from the report.
