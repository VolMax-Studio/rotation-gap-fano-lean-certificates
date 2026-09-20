# Input binding — W2-d7 component certificate (v3)

Status: COMPLETED AND VERIFIED.
Extracted on 2026-09-20T19:24:51Z by extract_w2d7.py against verified archive.
All 90 member hashes verified; tiling and popcount equivalence verified; determinism passed.

Supersedes:
- `W2D7_INPUT_BINDING.md` (v1, bound to superseded target v1 SHA `2020b52...`)
- `W2D7_INPUT_BINDING_v2.md` (v2, bound to superseded target v2 SHA `f0c4048...`)

## HALT conditions (summary — each is fail-closed, detailed in its own section below)

    1. archive MD5/size mismatch          -> HALT  (Archive identity)
    2. any measured member SHA mismatch   -> HALT  (Source members)
    3. packed-size tiling mismatch        -> HALT  (Extraction rule)
    4. second extraction output differs   -> HALT  (Determinism check)

Any one of these firing means: do not write `W2D7_INPUT.json` (or, if it was
already written under condition 4, discard it) and do not fill in the
remaining fields as if the binding were valid. Record which condition
fired and stop; this file does not get completed around a HALT.

## Answers to (target identity)

    FORMAL_TARGET_W2_D7_v3.md sha256: 02c9f057f3c80636a9287e4265f83e8d6e649f895f8268de7d4291ed16dbdb50

This binding is void if it does not match the file's current sha256 at
extraction time. If `FORMAL_TARGET_W2_D7_v3.md` ever needs to change, this
binding does not get edited to follow it — a new target file and a new
binding are created instead.

## Extractor identity

    Script:              extract_w2d7.py
    Git commit:          2de083e8c1887e57a2b507465915c18e75bdb3c4 (ratification merge commit on main)
    Execution timestamp: 2026-09-20T19:24:51Z
    Command line:        python3 extract_w2d7.py
    Popcount equivalence check run: YES — 30/30 experiments match vectorised vs author loop exactly (PASS)

## Archive identity

    DOI:            10.5281/zenodo.13273331
    Archive member:  google_105Q_surface_code_d3_d5_d7.zip
    MD5 (pinned):    21fa6ad35b395d838ebcdbc92e364a12   <- must match reproduce.py ARCHIVE_MD5
    Size (pinned):   5716907033 bytes                    <- must match reproduce.py ARCHIVE_SIZE_BYTES
    MD5 (measured at this extraction): 21fa6ad35b395d838ebcdbc92e364a12
    Size (measured at this extraction): 5716907033 bytes

HALT this binding (do not write `W2D7_INPUT.json`) if either measured value
disagrees with the pinned value above.

## Source members (30 experiments, d=7 patch)

Bind every source byte stream actually read by extraction, and no
fictitious dependency — nothing is listed here "just in case". Per the
Extraction rule below, that is exactly three files per experiment:
`metadata.json` (n_j), `circuit_ideal.stim` (n_det, needed to decode the
packed bits), and `detection_events.b8` (the raw counts S_j/Q_j are
computed from). If the extractor implementation ends up not reading one of
these for some experiment, that row must say so explicitly rather than
cite a hash for a file that was not actually opened.

Two hashes per file, not one — "looked up from the manifest" and "looked up
from the manifest" can never disagree with each other, so a single column
would make the HALT rule vacuous:

    expected_sha256 = value already committed in
                       rotation-gap-fano-s1/data_manifest.json (look up,
                       never recompute)
    measured_sha256 = sha256 of the actual bytes this extraction run read
                       off disk for that member, computed fresh, after
                       unpacking, right before those bytes are used
    require measured_sha256 == expected_sha256

This is what actually closes the custody chain: the archive MD5 pins the
5.7 GB zip as a whole at download time; this pins the specific bytes the
extractor opened, after unpacking, against that same commitment — it is
what catches local corruption or a wrong/stale extracted copy that the
whole-archive MD5 cannot see because it never re-touches the archive.

| Experiment | File | Path | Expected SHA-256 (manifest) | Measured SHA-256 (this run) |
| :--- | :--- | :--- | :--- | :--- |
| r01 (X)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r01/detection_events.b8 | 9254f4266633527f56c75287fb4be49f899cc01509e8c9393ebddeae5b551a75 | 9254f4266633527f56c75287fb4be49f899cc01509e8c9393ebddeae5b551a75 |
| r01 (X)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r01/metadata.json | 931f0e7af7e888d0fa80e340895f73567ea46ecac7398e080321bf343cca51ac | 931f0e7af7e888d0fa80e340895f73567ea46ecac7398e080321bf343cca51ac |
| r01 (X)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r01/circuit_ideal.stim | a28f50988b0d5c54c5089dcf00c9beddd5d534fb3adc148486cf59d39cc973c3 | a28f50988b0d5c54c5089dcf00c9beddd5d534fb3adc148486cf59d39cc973c3 |
| r10 (X)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r10/detection_events.b8 | cc93bb4db704dc0fbb4abb67c776adf208403fe3d8d634a27d25d639ea915362 | cc93bb4db704dc0fbb4abb67c776adf208403fe3d8d634a27d25d639ea915362 |
| r10 (X)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r10/metadata.json | 3fbcbadb6751d83f9717b0747371b1ff6413f770aea814621bb7a14c5ac3315e | 3fbcbadb6751d83f9717b0747371b1ff6413f770aea814621bb7a14c5ac3315e |
| r10 (X)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r10/circuit_ideal.stim | 4a613e12cc042f31e582a769fdefd560aa0565ae6744df6905b1b63de4cb54d2 | 4a613e12cc042f31e582a769fdefd560aa0565ae6744df6905b1b63de4cb54d2 |
| r110 (X) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r110/detection_events.b8 | 90dfc8ad450722d4f05acb3deb674b9da740461711cdf6ecae6f8242e0801867 | 90dfc8ad450722d4f05acb3deb674b9da740461711cdf6ecae6f8242e0801867 |
| r110 (X) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r110/metadata.json | c97686902e627a7cb861caf605a4f4ce962e84445002f3b5a804c01f9a85e610 | c97686902e627a7cb861caf605a4f4ce962e84445002f3b5a804c01f9a85e610 |
| r110 (X) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r110/circuit_ideal.stim | c88934dc3e8be8a23a7a463986d9ea58bec67e72130f8c7bc1523f3b187ad445 | c88934dc3e8be8a23a7a463986d9ea58bec67e72130f8c7bc1523f3b187ad445 |
| r13 (X)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r13/detection_events.b8 | 75fb18c1ae9c8abf40fce2a6cb8f4d703673e09dc02c6d8d4fe7e011ea15ccef | 75fb18c1ae9c8abf40fce2a6cb8f4d703673e09dc02c6d8d4fe7e011ea15ccef |
| r13 (X)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r13/metadata.json | a9a9f1754d952c15b662bab3f2236fccbc878912f67955875edec751194c2cf8 | a9a9f1754d952c15b662bab3f2236fccbc878912f67955875edec751194c2cf8 |
| r13 (X)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r13/circuit_ideal.stim | 3a1cb5a1b952ee92623862f17ad3d5d688c706f1365ba2be8f25bf5f6e8ec8ae | 3a1cb5a1b952ee92623862f17ad3d5d688c706f1365ba2be8f25bf5f6e8ec8ae |
| r130 (X) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r130/detection_events.b8 | 7dd42bf0691cb83cc55014b835475a30a64e40d025e8a0fbfd69df22f9e1e397 | 7dd42bf0691cb83cc55014b835475a30a64e40d025e8a0fbfd69df22f9e1e397 |
| r130 (X) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r130/metadata.json | c83cfbed6aed32edaae7eb18f2867cbbb6bea81c1abcdc530526b3b0b94c9e56 | c83cfbed6aed32edaae7eb18f2867cbbb6bea81c1abcdc530526b3b0b94c9e56 |
| r130 (X) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r130/circuit_ideal.stim | 9e3e85e92161f5fe549d41d1dc03cce190e55f18a01f4fffb42452a60aa29a0a | 9e3e85e92161f5fe549d41d1dc03cce190e55f18a01f4fffb42452a60aa29a0a |
| r150 (X) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r150/detection_events.b8 | 5f78a758371829455b355cce8000a697124d75464f17f297a8e31306084cbe2d | 5f78a758371829455b355cce8000a697124d75464f17f297a8e31306084cbe2d |
| r150 (X) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r150/metadata.json | 366a6977c5d2b76ccd0f17bf3577e06e48f8ab7b50f8ead72c0086d7bcb5c6a4 | 366a6977c5d2b76ccd0f17bf3577e06e48f8ab7b50f8ead72c0086d7bcb5c6a4 |
| r150 (X) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r150/circuit_ideal.stim | 5f69efaaca2dfee5d1dd65d62aee5dbeab6a7ae04f3483fdbd96c63300b89434 | 5f69efaaca2dfee5d1dd65d62aee5dbeab6a7ae04f3483fdbd96c63300b89434 |
| r170 (X) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r170/detection_events.b8 | f72870a5cd28b832939d0c4c15f10ff6ff4760eb3d5ddb7a00b0b854e23bbc73 | f72870a5cd28b832939d0c4c15f10ff6ff4760eb3d5ddb7a00b0b854e23bbc73 |
| r170 (X) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r170/metadata.json | 0584f6172948eb5c1556f1fab952bb7e533283e2da2db69d7d64c302a5e1cc68 | 0584f6172948eb5c1556f1fab952bb7e533283e2da2db69d7d64c302a5e1cc68 |
| r170 (X) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r170/circuit_ideal.stim | fd11114ddea325892894ab56a8c6c71b4dbf4eb68557fd0ded06affa023b3648 | fd11114ddea325892894ab56a8c6c71b4dbf4eb68557fd0ded06affa023b3648 |
| r190 (X) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r190/detection_events.b8 | d61f5a3a49f105dbbda0c8db1968d053983a756246176b8824c85f725dacebae | d61f5a3a49f105dbbda0c8db1968d053983a756246176b8824c85f725dacebae |
| r190 (X) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r190/metadata.json | 8d62506db05d76ee38033c00f1285a58e8505114002a6a07d5795eebdd7343fb | 8d62506db05d76ee38033c00f1285a58e8505114002a6a07d5795eebdd7343fb |
| r190 (X) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r190/circuit_ideal.stim | faae92e2d9f2c15fc8dfc32aa64be8da7440756db2262da5df2a29437ce9f6a5 | faae92e2d9f2c15fc8dfc32aa64be8da7440756db2262da5df2a29437ce9f6a5 |
| r210 (X) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r210/detection_events.b8 | 11bc815d62b307833ac5c04a045e941b284df718dc1a13ac189960ae10ea8089 | 11bc815d62b307833ac5c04a045e941b284df718dc1a13ac189960ae10ea8089 |
| r210 (X) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r210/metadata.json | a089f56ff54cadbd920c369ec25935c0135b51b15272735ebae24a852c1fd4e0 | a089f56ff54cadbd920c369ec25935c0135b51b15272735ebae24a852c1fd4e0 |
| r210 (X) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r210/circuit_ideal.stim | 1a0e8ca7947f7a653835cc5c6a211b752e9042f38007f9771fa01dd0567d8bd2 | 1a0e8ca7947f7a653835cc5c6a211b752e9042f38007f9771fa01dd0567d8bd2 |
| r230 (X) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r230/detection_events.b8 | 5145e48fc896a97a2079eb176c28a2f9fd7f5007b0ad81e198104b9588da22be | 5145e48fc896a97a2079eb176c28a2f9fd7f5007b0ad81e198104b9588da22be |
| r230 (X) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r230/metadata.json | e9ffb8aae7949958a0704fab01047ee314811301e7e1802343fab26cb351727e | e9ffb8aae7949958a0704fab01047ee314811301e7e1802343fab26cb351727e |
| r230 (X) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r230/circuit_ideal.stim | 887d65d765996c3d67cd0ebabeeb573a78b99837cbcdd5b3073a4b5f5a827bcd | 887d65d765996c3d67cd0ebabeeb573a78b99837cbcdd5b3073a4b5f5a827bcd |
| r250 (X) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r250/detection_events.b8 | 1d2b54cac0125a221e94cd00239705b43ebb91da7c954ee81705b86eb5d678b2 | 1d2b54cac0125a221e94cd00239705b43ebb91da7c954ee81705b86eb5d678b2 |
| r250 (X) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r250/metadata.json | 75486da00d7151f0b720c3e46e45d2836690a754f4e4baa1f942a5f9098a24f5 | 75486da00d7151f0b720c3e46e45d2836690a754f4e4baa1f942a5f9098a24f5 |
| r250 (X) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r250/circuit_ideal.stim | 06af4df6d46b4c26775567027534af77f10c28acb6cc20e53eaf542361f49731 | 06af4df6d46b4c26775567027534af77f10c28acb6cc20e53eaf542361f49731 |
| r30 (X)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r30/detection_events.b8 | c6de334aa5e44d0b7d40ba5b80c685860699cfbe6a8e13189e4fb0ebc8f63622 | c6de334aa5e44d0b7d40ba5b80c685860699cfbe6a8e13189e4fb0ebc8f63622 |
| r30 (X)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r30/metadata.json | 099518060c724abcbf69b20834b02365f4b7d54048c27ec7c235a40e8011b8ff | 099518060c724abcbf69b20834b02365f4b7d54048c27ec7c235a40e8011b8ff |
| r30 (X)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r30/circuit_ideal.stim | 4465aa8cc9fe69be42d4e765ca80ae5a22931e33584cb3c161b7b645d78861d3 | 4465aa8cc9fe69be42d4e765ca80ae5a22931e33584cb3c161b7b645d78861d3 |
| r50 (X)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r50/detection_events.b8 | 5610d2b471749b11e78e0ec4193810f1c63be65e08802c26936aed535bb49848 | 5610d2b471749b11e78e0ec4193810f1c63be65e08802c26936aed535bb49848 |
| r50 (X)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r50/metadata.json | 18a0c73d6cfb1be486101bb75fdf120470e2754b45d950cc94c6b4e24ed8d2b5 | 18a0c73d6cfb1be486101bb75fdf120470e2754b45d950cc94c6b4e24ed8d2b5 |
| r50 (X)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r50/circuit_ideal.stim | a4e2d7c0b1f47c51742b971311168da07c82fa9c3470e8ac64ef520025cfc27d | a4e2d7c0b1f47c51742b971311168da07c82fa9c3470e8ac64ef520025cfc27d |
| r70 (X)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r70/detection_events.b8 | 4e32da079cf73b5e9721bb859665a082f4a5a65f753ec469971b3b300c68bb7c | 4e32da079cf73b5e9721bb859665a082f4a5a65f753ec469971b3b300c68bb7c |
| r70 (X)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r70/metadata.json | 9b3edfa229950f98771cee6ca6514d3c8eb8444aefe43336a7b5b22db234be54 | 9b3edfa229950f98771cee6ca6514d3c8eb8444aefe43336a7b5b22db234be54 |
| r70 (X)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r70/circuit_ideal.stim | 0fe1cc3af4f714108d98ed3500bbe5c9e131160e86478ff8d5e4e95ed78690b4 | 0fe1cc3af4f714108d98ed3500bbe5c9e131160e86478ff8d5e4e95ed78690b4 |
| r90 (X)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r90/detection_events.b8 | 56660c6f8b5d1bd267fbda9d135055545bf9b2471e52ae67a600089c1b94a82f | 56660c6f8b5d1bd267fbda9d135055545bf9b2471e52ae67a600089c1b94a82f |
| r90 (X)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r90/metadata.json | 9dae4b4f6d00510f5d4f7f03e07ec7e8c9880d30021429cd9ffb474120723f40 | 9dae4b4f6d00510f5d4f7f03e07ec7e8c9880d30021429cd9ffb474120723f40 |
| r90 (X)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r90/circuit_ideal.stim | 8ea8e2cd12aa49c0082e1578285fde21b213884e796cbf849546cba7d7c7a5bf | 8ea8e2cd12aa49c0082e1578285fde21b213884e796cbf849546cba7d7c7a5bf |
| r01 (Z)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r01/detection_events.b8 | 24808c115ce985ae9fe69cf04a9b5bac89bb429156facee3981b96feb8e9b2a1 | 24808c115ce985ae9fe69cf04a9b5bac89bb429156facee3981b96feb8e9b2a1 |
| r01 (Z)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r01/metadata.json | ab38c25d95ecc7879e434b1b81d9ea7560d0793ab27c193bcd5b6bba22c18589 | ab38c25d95ecc7879e434b1b81d9ea7560d0793ab27c193bcd5b6bba22c18589 |
| r01 (Z)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r01/circuit_ideal.stim | 4319f420b7aec5267a495e8d2728874cf1c31601f2948b0753f24a73373deb3d | 4319f420b7aec5267a495e8d2728874cf1c31601f2948b0753f24a73373deb3d |
| r10 (Z)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r10/detection_events.b8 | 93cbe7d6fbad6d9667aeb910ace29d8283dc5e74d94401c824ae9bb76f2cbf48 | 93cbe7d6fbad6d9667aeb910ace29d8283dc5e74d94401c824ae9bb76f2cbf48 |
| r10 (Z)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r10/metadata.json | a8cf92b20c74fdb6b06f3c04f49a772a4e3e046f61cdd124c15930d7901a9db1 | a8cf92b20c74fdb6b06f3c04f49a772a4e3e046f61cdd124c15930d7901a9db1 |
| r10 (Z)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r10/circuit_ideal.stim | 83c3b6123651c13a2b9294b8539cccb26fc6f5eb0752f38de70e61e4a1d6e070 | 83c3b6123651c13a2b9294b8539cccb26fc6f5eb0752f38de70e61e4a1d6e070 |
| r110 (Z) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r110/detection_events.b8 | da682f42c0ddf48e51d3b19373d0b044ff1261dc103a5885b8f8bdeee23b1b8c | da682f42c0ddf48e51d3b19373d0b044ff1261dc103a5885b8f8bdeee23b1b8c |
| r110 (Z) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r110/metadata.json | e433dabfd7268e753d40d736aaca0af300b31bc1a5b338ad1c8a4d90966ffe08 | e433dabfd7268e753d40d736aaca0af300b31bc1a5b338ad1c8a4d90966ffe08 |
| r110 (Z) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r110/circuit_ideal.stim | 332a744340867258f957fd689c31b282f38eef32b17c2ddab20eb7510a42214b | 332a744340867258f957fd689c31b282f38eef32b17c2ddab20eb7510a42214b |
| r13 (Z)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r13/detection_events.b8 | f86765fa0e4a95a45ad3a16ec9a28b44a6f32656c6aa3c6897eae3391e3a9a2d | f86765fa0e4a95a45ad3a16ec9a28b44a6f32656c6aa3c6897eae3391e3a9a2d |
| r13 (Z)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r13/metadata.json | c42ff5a6538a762c514586fcebe4036bd989484995d1c110009e104e8e689f7a | c42ff5a6538a762c514586fcebe4036bd989484995d1c110009e104e8e689f7a |
| r13 (Z)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r13/circuit_ideal.stim | 572112a07ae0167fd7745c0c1d85f7cf00b513d92161c374ac05f2032184534e | 572112a07ae0167fd7745c0c1d85f7cf00b513d92161c374ac05f2032184534e |
| r130 (Z) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r130/detection_events.b8 | b7c285479c34d5366ab90d6f4a37fc2e4025d2940f579a8a7bfb386639731dfb | b7c285479c34d5366ab90d6f4a37fc2e4025d2940f579a8a7bfb386639731dfb |
| r130 (Z) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r130/metadata.json | 4ed3bae6bfff3b4f2de1c521d37946e16e792cfeecbd5659dfa1523e9cafa55e | 4ed3bae6bfff3b4f2de1c521d37946e16e792cfeecbd5659dfa1523e9cafa55e |
| r130 (Z) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r130/circuit_ideal.stim | 8ad0752b410072b432126a4994dedda4c17a2b90aaf0d9e2bffda5bf0bf94f5c | 8ad0752b410072b432126a4994dedda4c17a2b90aaf0d9e2bffda5bf0bf94f5c |
| r150 (Z) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r150/detection_events.b8 | d5cdf4e534005a39595b3c13348a2465b9ea720185ae2b8f82c182556c6ff126 | d5cdf4e534005a39595b3c13348a2465b9ea720185ae2b8f82c182556c6ff126 |
| r150 (Z) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r150/metadata.json | 899934f78a9b5ad458528600bdf203c95b4e33634ced083d2b232415af50d5d3 | 899934f78a9b5ad458528600bdf203c95b4e33634ced083d2b232415af50d5d3 |
| r150 (Z) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r150/circuit_ideal.stim | 13ab9d03d5ef9cfbe4391f493593eafc9d2fcaf0749f8551dc5db9f5f3c2a532 | 13ab9d03d5ef9cfbe4391f493593eafc9d2fcaf0749f8551dc5db9f5f3c2a532 |
| r170 (Z) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r170/detection_events.b8 | d730c284647a4c8f485716dbd9b7ac9fce9a3f98490f0df3827533c4ae1eff21 | d730c284647a4c8f485716dbd9b7ac9fce9a3f98490f0df3827533c4ae1eff21 |
| r170 (Z) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r170/metadata.json | 71a3f3e1d230888400f6619a5dded1f46e49058f66f9c7740a773e297dfec261 | 71a3f3e1d230888400f6619a5dded1f46e49058f66f9c7740a773e297dfec261 |
| r170 (Z) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r170/circuit_ideal.stim | 2e3b585e0dced5de3c859147f4ee08c60fae6cdedf302ed95a7a027ed68787aa | 2e3b585e0dced5de3c859147f4ee08c60fae6cdedf302ed95a7a027ed68787aa |
| r190 (Z) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r190/detection_events.b8 | 02ad0eacfc818950f8364f84ffba9fe886081df39eff14a2382ac3d35955e536 | 02ad0eacfc818950f8364f84ffba9fe886081df39eff14a2382ac3d35955e536 |
| r190 (Z) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r190/metadata.json | 8fc6cc1a43165c087951e045f2c481906358a3df3998a9960cf37bfad179de33 | 8fc6cc1a43165c087951e045f2c481906358a3df3998a9960cf37bfad179de33 |
| r190 (Z) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r190/circuit_ideal.stim | a4c362df31c2c3ee11af645216a7c758af4e37559fd46c0cebfaf115ed301af0 | a4c362df31c2c3ee11af645216a7c758af4e37559fd46c0cebfaf115ed301af0 |
| r210 (Z) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r210/detection_events.b8 | 2ad4abd116edfe088a53774ce5e038a9ab4baf948d4c5938784cbb3678e16a7c | 2ad4abd116edfe088a53774ce5e038a9ab4baf948d4c5938784cbb3678e16a7c |
| r210 (Z) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r210/metadata.json | 5005ac09226f17e61e4cdd638cdd6f0ed5b98cc6b88be1074edd5dadeca76a5b | 5005ac09226f17e61e4cdd638cdd6f0ed5b98cc6b88be1074edd5dadeca76a5b |
| r210 (Z) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r210/circuit_ideal.stim | d7544ef9b8102a35c7ef50611283577497980a79822520306ffbec7d6ef45095 | d7544ef9b8102a35c7ef50611283577497980a79822520306ffbec7d6ef45095 |
| r230 (Z) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r230/detection_events.b8 | 7218c69e0172584b341b132865fa9c5bc6698ee82ec3143c4f110f813441d56e | 7218c69e0172584b341b132865fa9c5bc6698ee82ec3143c4f110f813441d56e |
| r230 (Z) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r230/metadata.json | 43516ae7e5cf66bfa46f2cc5fbcfc2fcd7dd2fa5da546f140a053b6ba312eb45 | 43516ae7e5cf66bfa46f2cc5fbcfc2fcd7dd2fa5da546f140a053b6ba312eb45 |
| r230 (Z) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r230/circuit_ideal.stim | f23d284c79b4b27daf42fbbbe8d4f4c0ca307a31068ca50665f2398c4b44db72 | f23d284c79b4b27daf42fbbbe8d4f4c0ca307a31068ca50665f2398c4b44db72 |
| r250 (Z) | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r250/detection_events.b8 | 94d93fa22433eade021bb010177f9d70c2d7c5e872cd1755a5e962cdc1aa8ebf | 94d93fa22433eade021bb010177f9d70c2d7c5e872cd1755a5e962cdc1aa8ebf |
| r250 (Z) | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r250/metadata.json | 7d56aed516968150878420e0264a5a0712978af5d694e6ee027ac1df5a7ea02e | 7d56aed516968150878420e0264a5a0712978af5d694e6ee027ac1df5a7ea02e |
| r250 (Z) | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r250/circuit_ideal.stim | 210972fa5225f81c63db662b899cfa5ab799958b95ef341aa8c3b20d01bc7218 | 210972fa5225f81c63db662b899cfa5ab799958b95ef341aa8c3b20d01bc7218 |
| r30 (Z)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r30/detection_events.b8 | b2b37c8fe2d816ec280c834fcb66d02b7bb6782943ace03b846d87702a6e12b9 | b2b37c8fe2d816ec280c834fcb66d02b7bb6782943ace03b846d87702a6e12b9 |
| r30 (Z)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r30/metadata.json | 9280a03b612493ae75c9fe697c578ddd2493fd42dbf3ea3cd47d36c1a7ffe691 | 9280a03b612493ae75c9fe697c578ddd2493fd42dbf3ea3cd47d36c1a7ffe691 |
| r30 (Z)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r30/circuit_ideal.stim | 045c79e973eabc493197949dd92544dcc1880a85365b80eb956ea5a6e745e4b0 | 045c79e973eabc493197949dd92544dcc1880a85365b80eb956ea5a6e745e4b0 |
| r50 (Z)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r50/detection_events.b8 | 98e92ad4e895e2009ae6c470d236b72446457a61f7dea299ca52502b92cdabe8 | 98e92ad4e895e2009ae6c470d236b72446457a61f7dea299ca52502b92cdabe8 |
| r50 (Z)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r50/metadata.json | c2552b25213c5d20d802d8dd26d094c1dfd6c9525560b90ca99cc4aa3b5c5a65 | c2552b25213c5d20d802d8dd26d094c1dfd6c9525560b90ca99cc4aa3b5c5a65 |
| r50 (Z)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r50/circuit_ideal.stim | 3aab740adac3d515e60d3ad7d106d075573e56ade3a1ede1f52f663023a5148b | 3aab740adac3d515e60d3ad7d106d075573e56ade3a1ede1f52f663023a5148b |
| r70 (Z)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r70/detection_events.b8 | 713cf8d551f92cbe723268ea43b1ec67e39bf1427772eb15a04f817d7d82aef7 | 713cf8d551f92cbe723268ea43b1ec67e39bf1427772eb15a04f817d7d82aef7 |
| r70 (Z)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r70/metadata.json | fdd381cfd02f8eeebc9012fcd0a4eed438fc1220f670719a9d90f415411bc91c | fdd381cfd02f8eeebc9012fcd0a4eed438fc1220f670719a9d90f415411bc91c |
| r70 (Z)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r70/circuit_ideal.stim | 965c734102a78e63cfb0a7f7828e738fd262c0d82ada329fba1fbf0bf05bd5cf | 965c734102a78e63cfb0a7f7828e738fd262c0d82ada329fba1fbf0bf05bd5cf |
| r90 (Z)  | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r90/detection_events.b8 | 10b5dea45d1eb3626b0a94770f5916cd10a1074266e7bbbec6ce47b436a965bc | 10b5dea45d1eb3626b0a94770f5916cd10a1074266e7bbbec6ce47b436a965bc |
| r90 (Z)  | metadata.json       | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r90/metadata.json | 87c5dcc20197bc8aa6d333e1e9338cc864c11fa7140de0589fde80510e0d97c3 | 87c5dcc20197bc8aa6d333e1e9338cc864c11fa7140de0589fde80510e0d97c3 |
| r90 (Z)  | circuit_ideal.stim  | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/Z/r90/circuit_ideal.stim | b58234aaa12cb62e7fe3945d57942155af017f509d9fd46b4127fb6b403e4198 | b58234aaa12cb62e7fe3945d57942155af017f509d9fd46b4127fb6b403e4198 |

HALT this binding (do not write `W2D7_INPUT.json`) if any single
measured_sha256 != expected_sha256, for any of the 90 rows.

## Extraction rule

    n_j    = shots (from metadata.json)
    n_det  = number of DETECTOR tokens in circuit_ideal.stim (same method
             as reproduce.py's count_detectors: parse the circuit, count
             DETECTOR instructions — this is what fixes bytes_per_shot for
             decoding, it is not a free parameter)
    c_i    = popcount of packed detector bits per shot, decoded from
             detection_events.b8 with bytes_per_shot = ceil(n_det / 8),
             per PREREGISTRATION.md (author line 44-59 reduction: no
             preprocessing beyond decoding the packed detector records)
    S_j    = sum_i c_i
    Q_j    = sum_i c_i^2
    (ddof=1 is not invoked here; S_j, Q_j are raw sufficient statistics —
    ddof=1 enters only in the Lean-side derivation of the Fano ratio,
    per FORMAL_TARGET_W2_D7_v3.md)

    HALT condition (mirrors reproduce.py's P2): if len(detection_events.b8)
    != n_j * ceil(n_det / 8), stop immediately; the stream is malformed or
    the shot count is inconsistent with the detector layout. Do not write
    W2D7_INPUT.json.

## Generated output and order convention

    Output file:        W2D7_INPUT.json
    SHA-256:            3dd3a86624b53f3aead8972fd902cee7431c11d1f42199e05f9a055e08892b5f (and recorded in W2D7_INPUT.sha256)

Order convention (fixed now, not a post-extraction choice):
Sort the 30 experiment directories by their POSIX relative path within the
unpacked archive (relative to `google_105Q_surface_code_d3_d5_d7/`),
lexicographically by byte value:

    e.g. d7_at_q6_7/X/r01, d7_at_q6_7/X/r10, d7_at_q6_7/X/r110, ...

This is what makes the determinism check a real test of the extractor rather
than of an unstated tie-break.

Format of `W2D7_INPUT.json` — array of exactly 30 integer triples:

    [
      [n_1, S_1, Q_1],
      ...
      [n_30, S_30, Q_30]
    ]

## Determinism check

A second extraction run is mandatory:
1. Re-run the extraction from the unpacked files into a temporary file
   `W2D7_INPUT_check.json`.
2. Compute its SHA-256.
3. Assert byte-identity: `diff W2D7_INPUT.json W2D7_INPUT_check.json`.
4. Delete the temporary check file.

STATUS: PASSED. Two successive extraction runs were executed off disk.
`diff W2D7_INPUT.json W2D7_INPUT_check.json` confirmed 0 byte difference.
Temporary check file deleted.

## Code generation rule

The final Lean file `W2D7_v3.lean` MUST be generated mechanically from
`W2D7_INPUT.json` using `generate_W2D7_lean_v3.py`:

    python3 generate_W2D7_lean_v3.py W2D7_INPUT.json W2D7_v3.lean w2_d7_certificate

Zero manual transcription of the 30 triples is permitted. The generator
shall record `W2D7_INPUT.json`'s measured SHA-256 directly in the generated
Lean source comments.
