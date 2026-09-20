import hashlib
import json
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "W2D7_INPUT.json"
outfile = sys.argv[2] if len(sys.argv) > 2 else "W2D7_v3.lean"
theorem_name = sys.argv[3] if len(sys.argv) > 3 else "w2_d7_certificate"

raw_bytes = open(infile, "rb").read()
input_sha256 = hashlib.sha256(raw_bytes).hexdigest()
triples = json.loads(raw_bytes.decode("utf-8"))
assert len(triples) == 30, f"expected 30 triples, got {len(triples)}"

def fmt_triple(t):
    n, S, Q = t
    return f"({n}, {S}, {Q})"

lean = []
lean.append("-- W2-d7 component formal certificate. No Rat. No native_decide.")
lean.append(f"-- Input file: {infile}")
lean.append(f"-- Input SHA-256: {input_sha256}")
lean.append("-- Pure Nat/Int, kernel `decide`. Strict interval: 559/200 < x < 561/200")
lean.append("-- (2.795 < exact-rational W2,d=7 < 2.805), positive corroboration band matching R5.")
lean.append("-- Theorem is a strict conjunction; never an implication.")
lean.append("")
lean.append("def triples : List (Nat x Nat x Nat) := [".replace("x", "×"))
for i, t in enumerate(triples):
    comma = "," if i < len(triples) - 1 else ""
    lean.append(f"  {fmt_triple(t)}{comma}")
lean.append("]")
lean.append("")
lean.append("def lenOk : Bool := decide (triples.length = 30)")
lean.append("")
lean.append("def validTriple (t : Nat × Nat × Nat) : Bool :=")
lean.append("  let (n, S, Q) := t")
lean.append("  decide (n > 1) && decide (S > 0) && decide (n * Q >= S * S)")
lean.append("")
lean.append("def allValid : Bool := triples.all validTriple")
lean.append("")
lean.append("def stepFrac (acc : Int × Int) (t : Nat × Nat × Nat) : Int × Int :=")
lean.append("  let (Na, Da) := acc")
lean.append("  let (n, S, Q) := t")
lean.append("  let D : Int := ((n : Int) - 1) * (S : Int)")
lean.append("  let N : Int := (n : Int) * (Q : Int) - (S : Int) * (S : Int)")
lean.append("  (Na * D + N * Da, Da * D)")
lean.append("")
lean.append("def bigFrac : Int × Int := triples.foldl stepFrac (0, 1)")
lean.append("def BigNumer : Int := bigFrac.1")
lean.append("def BigDenom : Int := bigFrac.2")
lean.append("")
lean.append("def denomPositive : Bool := decide (BigDenom > 0)")
lean.append("")
lean.append("-- strict: 559/200 < avg and avg < 561/200 (i.e. 2.795 < avg < 2.805)")
lean.append("def lowerOk : Bool := decide (559 * (30 * BigDenom) < 200 * BigNumer)")
lean.append("def upperOk : Bool := decide (200 * BigNumer < 561 * (30 * BigDenom))")
lean.append("")
lean.append(f"theorem {theorem_name} :")
lean.append("    lenOk = true ∧")
lean.append("    allValid = true ∧")
lean.append("    denomPositive = true ∧")
lean.append("    lowerOk = true ∧")
lean.append("    upperOk = true := by")
lean.append("  decide")
lean.append("")
lean.append(f"#print axioms {theorem_name}")
lean.append("#eval lenOk")
lean.append("#eval allValid")
lean.append("#eval denomPositive")
lean.append("#eval lowerOk")
lean.append("#eval upperOk")

with open(outfile, "w") as f:
    f.write("\n".join(lean) + "\n")
print(f"wrote {outfile} (input SHA-256: {input_sha256})")
