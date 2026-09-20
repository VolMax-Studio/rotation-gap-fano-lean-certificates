# Input binding — W2, d=7

Status: SKELETON — not yet filled. Ananke completes every field below from
the actual archive extraction and commits this file alongside
`W2D7_INPUT.json` / `W2D7_INPUT.sha256`. Nothing here is filled by
inference, by the float64 pipeline's already-known result, or by Claude —
only by re-running the extraction against the archive.

## HALT conditions (summary — each is fail-closed, detailed in its own section below)

    1. archive MD5/size mismatch          -> HALT  (Archive identity)
    2. any measured member SHA mismatch   -> HALT  (Source members)
    3. packed-size tiling mismatch        -> HALT  (Extraction rule)
    4. second extraction output differs   -> HALT  (Determinism check)

Any one of these firing means: do not write W2D7_INPUT.json (or, if it was
already written under condition 4, discard it) and do not fill in the
remaining fields as if the binding were valid. Record which condition
fired and stop; this file does not get completed around a HALT.

## Answers to (target identity)

    FORMAL_TARGET_W2_D7.md sha256: 2020b52bf1ec12d3c3fde0748e16c6113260bd78b5719a5cfdac9c0c5bbcca09

This binding is void if it does not match the file's current sha256 at
extraction time. If FORMAL_TARGET_W2_D7.md ever needs to change, this
binding does not get edited to follow it — a new target file and a new
binding are created instead.

## Archive identity

    DOI:            10.5281/zenodo.13273331
    Archive member:  google_105Q_surface_code_d3_d5_d7.zip
    MD5 (pinned):    21fa6ad35b395d838ebcdbc92e364a12   <- must match reproduce.py ARCHIVE_MD5
    Size (pinned):   5716907033 bytes                    <- must match reproduce.py ARCHIVE_SIZE_BYTES
    MD5 (measured at this extraction): <FILL>
    Size (measured at this extraction): <FILL>

HALT this binding (do not write W2D7_INPUT.json) if either measured value
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

HALT this binding (do not write W2D7_INPUT.json) if any single
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
    per FORMAL_TARGET_W2_D7.md)

    HALT condition (mirrors reproduce.py's P2): if len(detection_events.b8)
    != shots * ceil(n_det/8) for any of the 30 experiments, do not write
    W2D7_INPUT.json — the packed record does not tile exactly and no triple
    may be derived from it.

## Extractor identity

    Tool / script: <FILL — e.g. commit hash of the extraction script used>
    Run by: <FILL — Ananke, with model/version if relevant>
    Run at: <FILL — UTC timestamp>
    Popcount equivalence check run: <FILL — yes/no, and result, mirroring
      reproduce.py --verify-popcount practice>

## Output

    W2D7_INPUT.json sha256: <FILL>

    Order convention (fixed now, not a post-extraction choice):
    Sort the 30 experiment directories by their POSIX relative path
    (as given in data_manifest.json, e.g.
    "google_105Q_surface_code_d3_d5_d7/d7_at_q6_7/X/r01/") lexicographically
    by byte value; emit (n, S, Q) in that exact order. The certificate's
    fold does not depend on order (it is a sum), but the *bytes* of
    W2D7_INPUT.json do — this is what makes the determinism check below a
    real test of the extractor rather than of an unstated tie-break.

## Determinism check (mandatory before this binding is considered valid)

    Rerun the extraction a second time from the same archive.
    W2D7_INPUT.json must be byte-identical (same sha256) on rerun.
    Rerun sha256: <FILL>
    Match: <FILL — yes/no; a "no" HALTS this binding>
