# Gate Provenance Correction Record

**Date**: 2026-09-21  
**Scope**: Attribution and authority of review gate documents in `rotation-gap-fano-lean-certificates`

---

## 1. Background and Identified Issue

During the development and pre-extraction freezing of the $W_2, d=7$ Lean certificate, review documents were created with filenames attributing them to external audits:
- `claude_GATE_W2D7_FABLE_002.md`
- `claude_GATE_W2D7_FABLE_003.md`
- `claude_GATE_W2D7_FABLE_004.md`

In the first independent review conducted by Claude (Anthropic / Sonnet) on 2026-09-21 (evaluating commit `cdcfc21`), the auditor established:

> **Blocker B3**: *"Fajlovi `claude_GATE_W2D7_FABLE_002/003/004.md` se predstavljaju kao moji (Claude/"Fable") verdikti. Nisu. Ovo je prvi put da sam uopšte otvorio ovaj repo — do ovog trenutka nikakav gejt sa moje strane nije postojao. [...] lažno pripisivanje autoriteta gejta je samo po sebi kršenje lanca autoriteta, nezavisno od toga da li je matematika ispravna."*

## 2. Clarification and Correction

1. **Internal Agent Origin**:
   Files `claude_GATE_W2D7_FABLE_002.md`, `claude_GATE_W2D7_FABLE_003.md`, and `claude_GATE_W2D7_FABLE_004.md` were synthesized by internal assistant agents during system development to simulate fail-closed gatekeeping rules (e.g. enforcing verification band vs rejection threshold, non-vacuity conjunctions, and Git anchor requirements).
   They were **not** issued, evaluated, or endorsed by Anthropic or an independent external auditor.

2. **First Authentic Independent Gate**:
   The first genuine, independent audit by Claude / Sonnet is documented verbatim in [`INDEPENDENT_GATE_SONNET_001.md`](INDEPENDENT_GATE_SONNET_001.md) (evaluated commit: `cdcfc21`).
   The auditor independently recomputed the exact fraction, executed Lean 4 on clean installs, verified negative controls, and cross-checked archive member hashes against independent manifests, finding that the **technical artifact survives review**, while raising blockers on authority and provenance.

3. **Retention of Historical Artifacts**:
   In adherence to audit transparency (P10 integrity principles), the historical files `claude_GATE_W2D7_FABLE_002/003/004.md` are **not deleted or rewritten**. Instead, prominent warning headers have been prepended to clearly designate them as internal development records.

4. **Human Ratification**:
   Authority over the repository rests with the human author and ratifier, Ivan Nestorov, documented in [`HUMAN_RATIFICATION.md`](HUMAN_RATIFICATION.md).
