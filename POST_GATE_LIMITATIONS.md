# Post-Gate Limitations and Operational Notes

**Date**: 2026-09-21  
**Reference Gate**: [`INDEPENDENT_GATE_SONNET_001.md`](INDEPENDENT_GATE_SONNET_001.md)  
**Evaluated Commit**: `cdcfc21`

This document records the technical observations, limitations, and operational distinctions identified during independent review.

---

## 1. Lean 4 Kernel Execution Scaling (Finding F1)

In [`FEASIBILITY_REPORT_v3.md`](FEASIBILITY_REPORT_v3.md), the feasibility benchmark reported:
- Synthetic sample execution time: **~0.35s** (using `triples_pos.json`, where $\max S = 264,667$ and $\max Q = 2,140,774$).

On the actual experimental Willow dataset ([`W2D7_INPUT.json`](W2D7_INPUT.json)):
- Real values are significantly larger: $\max S = 46,774,458$ and $\max Q = 43,925,233,994$ (an increase of ~175× for $S$ and ~20,000× for $Q$).
- The exact unreduced denominator product over 30 experiments and numerator cross-multiplications involve multi-precision integer arithmetic (`Nat`/`Int`) with numbers exceeding $10^{150}$.
- On a clean independent benchmark environment (Anthropic/Sonnet audit execution), `lean W2D7_v3.lean` completed in **26.95 seconds** (compared to sub-second timings on local development machines with warm kernel caches).
- **Assessment**: The execution time remains safely under the 60.0-second formal verification budget, but the ~75× scaling factor under cold evaluation is an important operational property of Lean 4's kernel reducer on large numeric literals.

---

## 2. Integrity Record Lifecycle Distinction (Finding F2)

The repository maintains two distinct SHA-256 verification records representing distinct stages of the protocol:

1. **`FREEZE_RECORD_v3.sha256`** (Pre-Extraction Anchor):
   - Created before unpacking raw experimental archives.
   - Pins the pre-extraction specification [`FORMAL_TARGET_W2_D7_v3.md`](FORMAL_TARGET_W2_D7_v3.md), generator [`generate_W2D7_lean_v3.py`](generate_W2D7_lean_v3.py), and the unpopulated binding template [`W2D7_INPUT_BINDING_v3.md`](W2D7_INPUT_BINDING_v3.md).
   - Expected status: Passes before data extraction; does not match post-extraction binding files once real archive SHA-256 hashes and shot statistics are populated.

2. **`POST_EXTRACTION_RECORD_v3.sha256`** (Post-Extraction Authoritative Record):
   - Created following extraction and proof generation.
   - Pins all 9 authoritative technical artifacts: target v3, extractor, generator, input triples, input hash, Lean proof, populated binding, licensing, and MIT license.
   - Expected status: Evaluates to `OK` on all 9 artifacts on post-extraction branches and `main`.

---

## 3. Data Ingestion and Tiling Observations (Findings F3–F4)

1. **Record Tiling and Popcount Equivalence**:
   - For all 30 Willow $d=7$ experiments, `extract_w2d7.py` verifies that `detection_events.b8` file sizes divide evenly by $n = 50,000$ shots with zero remainder.
   - The bytes per shot scale linearly as $6 \times \text{rounds}$ (representing 48 detectors packed into 6 bytes per round).
   - Ingestion popcounts were verified using two independent implementations (`numpy.unpackbits` fold vs bitwise shift mask loop), producing identical sums ($S$) and squared sums ($Q$) across all 1.5 million shots.

2. **Upstream Manifest Paths**:
   - In `extract_w2d7.py`, archive member SHA-256 hashes are verified against `data_manifest.json` from the Google Quantum AI dataset.
   - Users running independent extraction should ensure `data_manifest.json` is located in the archive unpacking directory or update the manifest path argument accordingly.

---

## 4. Epistemic Scope and Authority Separation

- The Lean 4 certificate proves the exact-rational bounds over the 30 integer triples $(n_j, S_j, Q_j)$.
- Custody, parsing, and bit-level integrity are verified by Python scripts at L1 and cross-checked against the published Google Quantum AI manifest.
- All governance authority is consolidated in [`HUMAN_RATIFICATION.md`](HUMAN_RATIFICATION.md).
