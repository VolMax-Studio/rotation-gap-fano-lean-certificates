#!/usr/bin/env python3
"""
Authoritative extraction script for W2-d7 component formal certificate.
Follows W2D7_INPUT_BINDING_v3.md protocol exactly:
1. Re-verifies archive size and MD5
2. Verifies 90 member SHA-256 hashes against data_manifest.json
3. Verifies packed-record tiling and popcount equivalence
4. Enforces byte-lexicographical ordering of the 30 d=7 experiments
5. Performs two extraction passes to guarantee determinism
6. Generates W2D7_INPUT.json and W2D7_INPUT.sha256
"""

import os
import sys
import json
import hashlib
from datetime import datetime, timezone
import numpy as np

ARCHIVE_PATH = os.path.expanduser("~/Downloads/willow-archive/google_105Q_surface_code_d3_d5_d7.zip")
UNPACKED_ROOT = os.path.expanduser("~/Downloads/willow-archive/unpacked/google_105Q_surface_code_d3_d5_d7")
MANIFEST_PATH = "/home/volmax-studio/volmax-projects/iot2/PORTFOLIO/rotation-gap-fano-s1/data_manifest.json"

PINNED_MD5 = "21fa6ad35b395d838ebcdbc92e364a12"
PINNED_SIZE = 5716907033

def halt(msg):
    print(f"HALT: {msg}", file=sys.stderr)
    sys.exit(1)

print("=== STEP 1: Archive Identity Check ===")
actual_size = os.path.getsize(ARCHIVE_PATH)
if actual_size != PINNED_SIZE:
    halt(f"Archive size mismatch: {actual_size} != {PINNED_SIZE}")
print(f"[OK] Archive size: {actual_size}")

h_md5 = hashlib.md5()
with open(ARCHIVE_PATH, "rb") as f:
    while chunk := f.read(65536 * 16):
        h_md5.update(chunk)
actual_md5 = h_md5.hexdigest()
if actual_md5 != PINNED_MD5:
    halt(f"Archive MD5 mismatch: {actual_md5} != {PINNED_MD5}")
print(f"[OK] Archive MD5: {actual_md5}")

print("\n=== STEP 2: Source Member Verification (90 files) ===")
manifest = json.load(open(MANIFEST_PATH))
d7_members = {p: info for p, info in manifest["members"].items() if "d7_at_q6_7" in p}
assert len(d7_members) == 90, f"Expected 90 d7 members, found {len(d7_members)}"

member_records = []
for p, info in sorted(d7_members.items()):
    rel = p.replace("google_105Q_surface_code_d3_d5_d7/", "")
    full_path = os.path.join(UNPACKED_ROOT, rel)
    if not os.path.exists(full_path):
        halt(f"Missing member on disk: {full_path}")
    raw = open(full_path, "rb").read()
    m_sha = hashlib.sha256(raw).hexdigest()
    exp_sha = info["sha256"]
    if m_sha != exp_sha:
        halt(f"Member SHA mismatch on {p}: measured {m_sha} != expected {exp_sha}")
    member_records.append({
        "path": p,
        "rel_path": rel,
        "expected_sha256": exp_sha,
        "measured_sha256": m_sha
    })
print(f"[OK] All 90 member SHA-256 hashes match data_manifest.json exactly.")

print("\n=== STEP 3: Ordered Extraction (Byte-lexicographic order) ===")
dirs = set()
for m in member_records:
    d = "/".join(m["rel_path"].split("/")[:-1])
    dirs.add(d)

sorted_dirs = sorted(list(dirs)) # Byte-lexicographical order
assert len(sorted_dirs) == 30, f"Expected 30 directories, got {len(sorted_dirs)}"

def run_extraction():
    triples = []
    popcount_verified = True
    for exp_dir in sorted_dirs:
        full_dir = os.path.join(UNPACKED_ROOT, exp_dir)
        meta_path = os.path.join(full_dir, "metadata.json")
        stim_path = os.path.join(full_dir, "circuit_ideal.stim")
        b8_path = os.path.join(full_dir, "detection_events.b8")

        meta = json.load(open(meta_path))
        shots = meta["shots"]

        stim_content = open(stim_path, "r", encoding="utf-8").read()
        n_det = stim_content.count("DETECTOR")
        bytes_per_shot = (n_det + 7) // 8

        b8_data = open(b8_path, "rb").read()
        if len(b8_data) != shots * bytes_per_shot:
            halt(f"Tiling mismatch on {exp_dir}: {len(b8_data)} != {shots * bytes_per_shot}")

        # Vectorised popcount
        data = np.frombuffer(b8_data, dtype=np.uint8).reshape(shots, bytes_per_shot)
        bits = np.unpackbits(data, axis=1, bitorder="little")[:, :n_det]
        counts_fast = bits.sum(axis=1, dtype=np.int32)

        # Author loop equivalence check
        counts_author = np.zeros(shots, dtype=np.int32)
        for byte_idx in range(bytes_per_shot):
            byte_col = data[:, byte_idx].astype(np.int32)
            for bit in range(min(8, n_det - byte_idx * 8)):
                counts_author += (byte_col >> bit) & 1

        if not np.array_equal(counts_fast, counts_author):
            halt(f"Popcount equivalence failure on {exp_dir}")

        c = counts_fast.astype(np.int64)
        S = int(np.sum(c))
        Q = int(np.sum(c * c))
        n = int(shots)

        if n <= 1 or S <= 0 or n * Q < S * S:
            halt(f"Guard condition failed on {exp_dir}: n={n}, S={S}, Q={Q}")

        triples.append([n, S, Q])
    return triples

triples_run1 = run_extraction()
print(f"[OK] Extraction Run 1 produced {len(triples_run1)} triples.")

out_json = "W2D7_INPUT.json"
with open(out_json, "w") as f:
    json.dump(triples_run1, f, indent=2)

print("\n=== STEP 4: Determinism Check (Run 2) ===")
triples_run2 = run_extraction()
out_check = "W2D7_INPUT_check.json"
with open(out_check, "w") as f:
    json.dump(triples_run2, f, indent=2)

bytes1 = open(out_json, "rb").read()
bytes2 = open(out_check, "rb").read()

if bytes1 != bytes2:
    os.remove(out_check)
    os.remove(out_json)
    halt("Non-deterministic extraction! Output files differed.")

os.remove(out_check)
print("[OK] Determinism check passed: byte-identical output across runs.")

input_sha256 = hashlib.sha256(bytes1).hexdigest()
sha_file = "W2D7_INPUT.sha256"
with open(sha_file, "w") as f:
    f.write(f"{input_sha256}  {out_json}\n")

print(f"[OK] W2D7_INPUT.json SHA-256: {input_sha256}")
