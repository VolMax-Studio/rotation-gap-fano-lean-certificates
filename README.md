# Rotation-Gap Fano Lean Certificates

Formal Lean 4 exact-rational verification certificates for the Fano factor analysis of the Google Willow QEC dataset (arXiv:2604.11963v1, Zenodo: 10.5281/zenodo.13273331), supporting [rotation-gap-fano-s1](https://github.com/VolMax-Studio/rotation-gap-fano-s1).

## Scope: W2-d7 Component Certificate (v3)

- **Target Specification**: [`FORMAL_TARGET_W2_D7_v3.md`](FORMAL_TARGET_W2_D7_v3.md) (SHA-256: `02c9f057f3c80636a9287e4265f83e8d6e649f895f8268de7d4291ed16dbdb50`)
- **Corroboration Band**: $2.795 < W_{2,d=7}^{exact} < 2.805$ (derived positive corroboration matching preregistered Rule R5 `< 0.005` around published value 2.80)
- **Input Binding Skeleton**: [`W2D7_INPUT_BINDING_v3.md`](W2D7_INPUT_BINDING_v3.md)
- **Generator**: [`generate_W2D7_lean_v3.py`](generate_W2D7_lean_v3.py)
- **Feasibility Evidence**: [`FEASIBILITY_REPORT_v3.md`](FEASIBILITY_REPORT_v3.md)
- **Freeze Record**: [`FREEZE_RECORD_v3.sha256`](FREEZE_RECORD_v3.sha256)

## Gate History
- [`claude_GATE_W2D7_FABLE_002.md`](claude_GATE_W2D7_FABLE_002.md): Caught B1-B4 pre-extraction on v1.
- [`claude_GATE_W2D7_FABLE_003.md`](claude_GATE_W2D7_FABLE_003.md): Identified git-freeze, rule citation, and binding ordering requirements leading to v3.

## Epistemic Boundary
The Lean 4 certificate bounds the exact-rational aggregate mean over 30 sufficient-statistic triples without using floating-point arithmetic, `Rat` division, or `native_decide`. All raw byte custody, individual member SHA-256 validation, and detector decoding are verified at the L1 custody layer.
