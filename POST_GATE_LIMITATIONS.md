# Post-Gate Limitations and Operational Notes

**Date**: 2026-09-21  
**Scope**: Technical findings, internal notes, and operational observations across review iterations

---

## 1. Authentic Independent Findings from Claude (Anthropic, Sonnet)

Documented in [`INDEPENDENT_GATE_SONNET_001.md`](INDEPENDENT_GATE_SONNET_001.md) (evaluating `cdcfc21`):

### Lean 4 Kernel Execution Scaling
- **Observation**: In [`FEASIBILITY_REPORT_v3.md`](FEASIBILITY_REPORT_v3.md), synthetic sample execution completed in ~0.35s ($\max S \approx 2.6 \times 10^5$, $\max Q \approx 2.1 \times 10^6$).
- On the real experimental dataset ([`W2D7_INPUT.json`](W2D7_INPUT.json)), numbers are multi-precision integers ($\max S = 46,774,458$, $\max Q = 43,925,233,994$).
- Under cold independent verification by Claude (Anthropic, Sonnet), `lean W2D7_v3.lean` completed in **26.95 seconds**.
- While well within the 60.0-second formal budget, this execution scaling is noted as an intrinsic property of kernel reduction over large arithmetic literals.

### Integrity Record Lifecycle Distinction
- **`FREEZE_RECORD_v3.sha256`**: Pre-extraction freeze anchor (pins initial target specification and unpopulated binding template prior to opening raw archives).
- **`POST_EXTRACTION_RECORD_v3.sha256`**: Authoritative post-extraction record (pins all 9 completed artifacts: target, extractor, generator, input triples, input hash, Lean proof, completed binding, licensing, and MIT license).

---

## 2. Internal Historical Findings (Agent-Generated / Not Independently Attributed to Sonnet)

The following findings originated during internal development checkpoints (formerly denoted F1–F6 in historical record [`HISTORICAL_AGENT_GENERATED_FABLE_005.md`](HISTORICAL_AGENT_GENERATED_FABLE_005.md)); they were **not** issued by Anthropic/Sonnet:

### Internal Note 1 (ex-F1) — Determinism check scope
- In `extract_w2d7.py`, two extraction passes were executed sequentially within a single process. A separate process restart provides stricter isolation against environment state retention. (Verified independently during audit).

### Internal Note 2 (ex-F2) — Detector count gloss vs code implementation
- The binding text glosses $n_{\text{det}}$ as parsed instructions, whereas `extract_w2d7.py` implements substring matching (`stim_data.decode().count("DETECTOR")`), reproducing line 28 of the original author script.

### Internal Note 3 (ex-F3) — Popcount equivalence check scope
- Both paths in `extract_w2d7.py` take the same $n_{\text{det}}$, verifying arithmetic equivalence between two bit-summing algorithms. Record tiling verifies record boundaries ($L_{\text{bytes}} \pmod n = 0$).

### Internal Note 4 (ex-F4) — Identity block formatting
- Author identity strings differed slightly in ordering and format across license headers; unified in human authorization records.

### Internal Note 5 (ex-F5) — Extractor local path dependency
- `extract_w2d7.py` hardcodes `MANIFEST_PATH` as an absolute path pointing to the pre-existing committed audit manifest in `rotation-gap-fano-s1` (`data_manifest.json`). External users must set this path to their local checkout.

### Internal Note 6 (ex-F6) — Carried forward documentation notes
- Historical drafting references from earlier development checkpoints.
