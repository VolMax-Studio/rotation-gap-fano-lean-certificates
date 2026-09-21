# Post-Gate Limitations and Operational Notes

**Date**: 2026-09-21  
**Scope**: Technical findings, historical project chat notes, and operational observations across review iterations

---

## 1. Authentic Independent Findings from Claude (Anthropic, Sonnet)

Documented in [`INDEPENDENT_GATE_SONNET_001.md`](INDEPENDENT_GATE_SONNET_001.md) (evaluating `cdcfc21`) and [`INDEPENDENT_GATE_SONNET_002.md`](INDEPENDENT_GATE_SONNET_002.md) (evaluating `e670ff7`):

### Lean 4 Kernel Execution
- A 26.95 s execution was observed in one independent fresh environment.
- A later independent run found real and synthetic inputs near the same runtime after environment initialization, indicating that the slow first run was environment/startup-related rather than demonstrated arithmetic scaling.
- The 60 s verification budget was satisfied in either case.

### Integrity Record Lifecycle Distinction
- **`FREEZE_RECORD_v3.sha256`**: Pre-extraction freeze anchor (pins initial target specification and unpopulated binding template prior to opening raw archives).
- **`POST_EXTRACTION_RECORD_v3.sha256`**: Authoritative post-extraction record (pins all 9 completed artifacts: target, extractor, generator, input triples, input hash, Lean proof, completed binding, licensing, and MIT license).

---

## 2. Historical Project Chat Gate Findings (FABLE-002 through FABLE-005)

The following findings originated during project chat gate evaluations (FABLE-002 through FABLE-005) transcribed by Ananke; they were **not** issued or endorsed by Anthropic as an institutional review and were **not** part of the separate independent Sonnet review sessions:

### Project Chat Note 1 (ex-F1) — Determinism check scope
- In `extract_w2d7.py`, two extraction passes were executed sequentially within a single process. A separate process restart provides stricter isolation against environment state retention. (Verified independently during audit).

### Project Chat Note 2 (ex-F2) — Detector count gloss vs code implementation
- The binding text glosses $n_{\text{det}}$ as parsed instructions, whereas `extract_w2d7.py` implements substring matching (`stim_data.decode().count("DETECTOR")`), reproducing line 28 of the original author script.

### Project Chat Note 3 (ex-F3) — Popcount equivalence check scope
- Both paths in `extract_w2d7.py` take the same $n_{\text{det}}$, verifying arithmetic equivalence between two bit-summing algorithms. Record tiling verifies record boundaries ($L_{\text{bytes}} \pmod n = 0$).

### Project Chat Note 4 (ex-F4) — Identity block formatting
- Author identity strings differed slightly in ordering and format across license headers; unified in human authorization records.

### Project Chat Note 5 (ex-F5) — Extractor local path dependency
- `extract_w2d7.py` hardcodes `MANIFEST_PATH` as an absolute path pointing to the pre-existing committed audit manifest in `rotation-gap-fano-s1` (`data_manifest.json`). External users must set this path to their local checkout.

### Project Chat Note 6 (ex-F6) — Carried forward documentation notes
- Historical drafting references from earlier development checkpoints.
