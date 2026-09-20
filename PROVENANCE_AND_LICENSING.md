# Data Provenance and Licensing (L0 Clearance)

## 1. Upstream Dataset
- **Title**: Data for "Quantum error correction below the surface code threshold"
- **Author / Creator**: Google Quantum AI (2024)
- **Repository**: Zenodo
- **DOI**: [10.5281/zenodo.13273331](https://doi.org/10.5281/zenodo.13273331)
- **Archive File**: `google_105Q_surface_code_d3_d5_d7.zip`
- **Archive Size**: 5,716,907,033 bytes
- **Archive MD5**: `21fa6ad35b395d838ebcdbc92e364a12`
- **License**: Creative Commons Attribution 4.0 International ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/))
- **Access Date**: 2026-09-20

## 2. Third-Party Analysis Under Reproduction
- **Title**: The Rotation Gap Is Not An Error
- **Author**: Selina Stenberg (2026)
- **Preprint**: [arXiv:2604.11963v1](https://arxiv.org/abs/2604.11963)
- **Estimator Code**: `willow/willow_fano_analysis.py` in [SelinaAliens/The_Rotation_Gap_Is_Not_An_Error](https://github.com/SelinaAliens/The_Rotation_Gap_Is_Not_An_Error) (MIT License)

## 3. Derived Sufficient Statistics (`W2D7_INPUT.json`)
The array of 30 triples `[n_j, S_j, Q_j]` contained in `W2D7_INPUT.json` constitutes derived summary statistics computed from raw detector bitstreams in the Google Quantum AI d=7 dataset patch (`d7_at_q6_7`).
- Extraction rule: $n_j$ = shots, $S_j = \sum c_i$, $Q_j = \sum c_i^2$, where $c_i$ is the popcount of detector events in shot $i$.
- Under CC BY 4.0 terms, attribution is hereby provided to Google Quantum AI (2024).

## 4. Certificate Software License
All Lean 4 formal certificates, verification harnesses, extraction scripts, and documentation in this repository are released under the [MIT License](LICENSE) (Copyright (c) 2026 VolMax Studio Lab / Ivan Nestorov).
