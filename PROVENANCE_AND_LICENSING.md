# Data Provenance and Licensing (L0 Clearance)

## 1. Upstream Dataset
- **Title**: Quantum Error Correction with 105 Qubits on Willow (Surface Code d=3, d=5, d=7 experiment dataset)
- **Authors**: Google Quantum AI / Willow Team (Stenberg et al., 2026; arXiv:2604.11963v1)
- **Repository**: Zenodo
- **DOI**: [10.5281/zenodo.13273331](https://doi.org/10.5281/zenodo.13273331)
- **Archive File**: `google_105Q_surface_code_d3_d5_d7.zip`
- **Archive Size**: 5,716,907,033 bytes
- **Archive MD5**: `21fa6ad35b395d838ebcdbc92e364a12`
- **License**: Creative Commons Attribution 4.0 International ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/))
- **Access Date**: 2026-09-20

## 2. Derived Sufficient Statistics (`W2D7_INPUT.json`)
The array of 30 triples `[n_j, S_j, Q_j]` contained in `W2D7_INPUT.json` constitutes derived aggregate summary statistics computed from raw detector bitstreams in the d=7 patch (`d7_at_q6_7`).
- Extraction rule: $n_j$ = shots, $S_j = \sum c_i$, $Q_j = \sum c_i^2$, where $c_i$ is the popcount of detector events in shot $i$.
- Under CC BY 4.0 terms, attribution is hereby provided to Google Quantum AI / Stenberg et al. (2026).

## 3. Certificate Software License
All Lean 4 formal certificates, verification harnesses, extraction scripts, and documentation in this repository are released under the [MIT License](LICENSE) (Copyright (c) 2026 VolMax Studio Lab / Ivan Nestorov).
