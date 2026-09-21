# Post-Gate Limitations and Operational Notes

**Date**: 2026-09-21  
**Reference Gate**: [`INDEPENDENT_GATE_SONNET_001.md`](INDEPENDENT_GATE_SONNET_001.md)  
**Evaluated Commits**: `bc7c76e` (post-extraction package) & `cdcfc21` (main branch)

This document maps and explains the specific non-blocking findings (F1–F6) and operational observations established during the independent reviews by Claude (Anthropic, Sonnet).

---

## 1. Mapped Findings from Post-Extraction Audit (F1–F6)

### F1 — Determinism check scope
- **Finding**: In `extract_w2d7.py`, two extraction passes are executed sequentially within a single Python process invocation, with `sorted_dirs` evaluated once prior to function execution.
- **Analysis**: While the two passes verify byte-identical output from disk re-reads, they do not test a separate process restart or re-derive the directory ordering independently.
- **Mitigation/Status**: Closed independently during audit by re-deriving the byte-lexicographical ordering directly from the manifest. Future extractors should execute separate process invocations.

### F2 — Detector count gloss vs code implementation
- **Finding**: The binding text notes that $n_{\text{det}}$ is determined by parsing the circuit, whereas `extract_w2d7.py` implements a substring search: `stim_data.decode().count("DETECTOR")`.
- **Analysis**: The substring search reproduces line 28 of the original author script (`reproduce.py:346-348`), so the code is authoritative and correct. However, a third-party reimplementer attempting AST tokenization could diverge if token semantics differed.
- **Status**: Code implementation matches authoritative upstream behavior.

### F3 — Popcount equivalence check scope
- **Finding**: Both popcount evaluation paths in `extract_w2d7.py` (`numpy.unpackbits` fold and manual bitwise shift/mask loop) take the same $n_{\text{det}}$.
- **Analysis**: This verifies arithmetic equivalence between two bit-summing implementations over identical data, rather than two independent determinations of detector count. The byte tiling check ($L_{\text{bytes}} \pmod n = 0$) guarantees packed record integrity, but could not detect an overcount within the same 8-bit ceiling (up to 7 bits).
- **Status**: Arithmetic popcount equivalence is verified 30/30 across all 1.5 million shots.

### F4 — Identity block formatting
- **Finding**: The author line in `LICENSE` ("Copyright (c) 2026 VolMax Studio Lab (Ivan Nestorov)") and `PROVENANCE_AND_LICENSING.md` ("VolMax Studio Lab / Ivan Nestorov") was composed slightly differently from the canonical identity string ("Nestorov, Ivan / VolMax Studio Lab / ORCID 0009-0006-7940-9539").
- **Status**: Reconciled and canonicalized in [`HUMAN_RATIFICATION.md`](HUMAN_RATIFICATION.md).

### F5 — Extractor local path dependency
- **Finding**: `extract_w2d7.py` hardcodes `MANIFEST_PATH` as an absolute path on the development machine (`/home/volmax-studio/...`).
- **Analysis**: This path points to **the pre-existing committed audit manifest in rotation-gap-fano-s1** (`data_manifest.json`).
- **Mitigation**: Users running independent extraction on external systems must provide the path to their local clone of the audit manifest or place `data_manifest.json` in the current working directory.

### F6 — Carried forward documentation notes
- **Finding**: Earlier developmental records (FABLE-002, 003, 004) contained historical drafting notes and reporting artifacts.
- **Status**: Formally superseded and placed in historical perspective by [`GATE_PROVENANCE_CORRECTION.md`](GATE_PROVENANCE_CORRECTION.md).

---

## 2. Operational Observations from Gate on `main @ cdcfc21`

### Lean 4 Kernel Execution Scaling
- In [`FEASIBILITY_REPORT_v3.md`](FEASIBILITY_REPORT_v3.md), synthetic sample execution completed in ~0.35s ($\max S \approx 2.6 \times 10^5$, $\max Q \approx 2.1 \times 10^6$).
- On the real experimental dataset ([`W2D7_INPUT.json`](W2D7_INPUT.json)), numbers are multi-precision integers ($\max S = 46,774,458$, $\max Q = 43,925,233,994$).
- Under cold independent verification by Claude (Anthropic, Sonnet), `lean W2D7_v3.lean` completed in **26.95 seconds**.
- While well within the 60.0-second formal budget, this execution scaling is noted as an intrinsic property of kernel reduction over large arithmetic literals.

### Integrity Record Lifecycle Distinction
- **`FREEZE_RECORD_v3.sha256`**: Pre-extraction freeze anchor (pins initial target specification and unpopulated binding template prior to opening raw archives).
- **`POST_EXTRACTION_RECORD_v3.sha256`**: Authoritative post-extraction record (pins all 9 completed artifacts: target, extractor, generator, input triples, input hash, Lean proof, completed binding, licensing, and MIT license).
