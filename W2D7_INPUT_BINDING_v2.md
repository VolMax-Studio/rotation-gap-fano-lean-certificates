# Input binding — W2-d7 component certificate (v2)

Status: SKELETON — not yet filled. Ananke completes every field below from
the actual archive extraction and commits this file alongside
`W2D7_INPUT.json` / `W2D7_INPUT.sha256`. Nothing here is filled by
inference, by the float64 pipeline's already-known result, or by Claude —
only by re-running the extraction against the verified archive.

Supersedes: `W2D7_INPUT_BINDING.md` (v1, which was bound to superseded target v1 SHA `2020b52...`).

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

    FORMAL_TARGET_W2_D7_v2.md sha256: f0c404862acacfff83b563fea37830d947a74127cdfc34d2f91b801d45e11980

This binding is void if it does not match the file's current sha256 at
extraction time. If `FORMAL_TARGET_W2_D7_v2.md` ever needs to change, this
binding does not get edited to follow it — a new target file and a new
binding are created instead.

## Archive identity

    DOI:            10.5281/zenodo.13273331
    Archive member:  google_105Q_surface_code_d3_d5_d7.zip
    MD5 (pinned):    21fa6ad35b395d838ebcdbc92e364a12   <- must match reproduce.py ARCHIVE_MD5
    Size (pinned):   5716907033 bytes                    <- must match reproduce.py ARCHIVE_SIZE_BYTES
    MD5 (measured at this extraction): <FILL>
    Size (measured at this extraction): <FILL>

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

    <FILL: 90 rows, three per experiment>
    experiment | file            | path                        | expected_sha256 (manifest) | measured_sha256 (this run)
    r01 (X)    | detection_events.b8 | google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r01/detection_events.b8 | <FILL> | <FILL>
    r01 (X)    | metadata.json       | .../r01/metadata.json       | <FILL> | <FILL>
    r01 (X)    | circuit_ideal.stim  | .../r01/circuit_ideal.stim  | <FILL> | <FILL>
    ... (30 experiments x 3 files = 90 rows total — all 15 rounds x 2 bases
         for the d7_at_q6_7 patch, or whichever patch id(s)
         data_manifest.json actually shows for d=7)

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
    per FORMAL_TARGET_W2_D7_v2.md)

    HALT condition (mirrors reproduce.py's P2): if len(detection_events.b8)
    != n_j * ceil(n_det / 8), stop immediately; the stream is malformed or
    the shot count is inconsistent with the detector layout. Do not write
    W2D7_INPUT.json.

## Generated output

    Output file:        W2D7_INPUT.json
    SHA-256:            <FILL> (and recorded in W2D7_INPUT.sha256)
    Extraction runner:  <FILL: commit, timestamp, command line>

Format of `W2D7_INPUT.json` — array of exactly 30 integer triples:

    [
      [n_1, S_1, Q_1],
      ...
      [n_30, S_30, Q_30]
    ]

Sorted in canonical experiment order (stable sort by (patch, basis, round);
record the exact sort key used so recreation does not depend on directory
iteration order).

## Determinism check

A second extraction run is mandatory:
1. Re-run the extraction from the unpacked files into a temporary file
   `W2D7_INPUT_check.json`.
2. Compute its SHA-256.
3. Assert byte-identity: `diff W2D7_INPUT.json W2D7_INPUT_check.json`.
4. Delete the temporary check file.

If the check output differs by even one byte, HALT: the extraction is
non-deterministic. Discard `W2D7_INPUT.json`, do not commit it, do not
complete this file.

## Code generation rule

The final Lean file `W2D7_v2.lean` MUST be generated mechanically from
`W2D7_INPUT.json` using `generate_W2D7_lean_v2.py`:

    python3 generate_W2D7_lean_v2.py W2D7_INPUT.json W2D7_v2.lean w2_d7_certificate

Zero manual transcription of the 30 triples is permitted.
