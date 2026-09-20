# W2-d7 component formal-target feasibility report (v2) — RESULT: PASS

Supersedes: FEASIBILITY_REPORT.md (v1)
Reason: v1 documented the obsolete implication theorem shape (`allValid -> denomPositive -> ...`)
and ±0.05 band. This report measures the exact final v2 conjunction theorem shape with
the pre-registered R5 verification band (2.795 < x < 2.805) and lenOk guard.

## Environment
- Lean version: 4.34.0
- Toolchain commit: 293d5d0c0c3f3dded4688b3ccd6a33939ac5102b (matches p10-core's pinned lean-toolchain)
- Architecture: x86_64-unknown-linux-gnu (Release)

## Exact Theorem Statement (as compiled)
```lean
def triples : List (Nat × Nat × Nat) := [ ... 30 triples ... ]

def lenOk : Bool := decide (triples.length = 30)

def validTriple (t : Nat × Nat × Nat) : Bool :=
  let (n, S, Q) := t
  decide (n > 1) && decide (S > 0) && decide (n * Q >= S * S)

def allValid : Bool := triples.all validTriple

def stepFrac (acc : Int × Int) (t : Nat × Nat × Nat) : Int × Int :=
  let (Na, Da) := acc
  let (n, S, Q) := t
  let D : Int := ((n : Int) - 1) * (S : Int)
  let N : Int := (n : Int) * (Q : Int) - (S : Int) * (S : Int)
  (Na * D + N * Da, Da * D)

def bigFrac : Int × Int := triples.foldl stepFrac (0, 1)
def BigNumer : Int := bigFrac.1
def BigDenom : Int := bigFrac.2

def denomPositive : Bool := decide (BigDenom > 0)

-- strict: 559/200 < avg and avg < 561/200 (i.e. 2.795 < avg < 2.805)
def lowerOk : Bool := decide (559 * (30 * BigDenom) < 200 * BigNumer)
def upperOk : Bool := decide (200 * BigNumer < 561 * (30 * BigDenom))

theorem w2_d7_certificate :
    lenOk = true ∧
    allValid = true ∧
    denomPositive = true ∧
    lowerOk = true ∧
    upperOk = true := by
  decide
```

No `Rat`. No `native_decide`. Pure Nat/Int cross-multiplication, kernel GMP reduction only.

## Test Matrix

Three synthetic datasets were generated to test all discrimination axes of the v2 conjunction theorem:

### 1. Positive Synthetic Run (`triples_pos.json`)
- Shots: $n_j = 50,000$ (matching arXiv:2604.11963 §II F)
- Fano targets tuned to cluster near recomputed float value: exact rational average = $2.797799660$
- Interval check: $2.795 < 2.797799660 < 2.805$ (TRUE)
- Wall-clock time: ~0.35s (warm cache, Peak RSS: ~475 MB)
- Exit code: 0
- #print axioms output:
  `'w2_d7_certificate_pos' does not depend on any axioms`
- Evaluation results:
  `lenOk = true`, `allValid = true`, `denomPositive = true`, `lowerOk = true`, `upperOk = true`
- Status: **PASS**

### 2. Band-Negative Run (`triples_band_neg.json`)
- Valid inputs ($n_j = 50,000$, all $n_j Q_j \ge S_j^2$), but Fano targets tuned outside R5 band: exact rational average = $2.819841308$
- Interval check: $2.819841308 < 2.805$ is FALSE (`upperOk = false`)
- Exit code: 1
- Lean error output:
  ```text
  W2D7_band_neg.lean:70:2: error: Tactic `decide` failed for proposition
    lenOk = true ∧ allValid = true ∧ denomPositive = true ∧ lowerOk = true ∧ upperOk = true
  is false
  'w2_d7_certificate_band_neg' depends on axioms: [sorryAx]
  ```
- Evaluation results:
  `lenOk = true`, `allValid = true`, `denomPositive = true`, `lowerOk = true`, `upperOk = false`
- Status: **DISCRIMINATES (Correctly rejected)**

### 3. Guard-Corruption Run (`triples_corrupt.json`)
- Triple 0 corrupted to $Q=1$ such that $n_0 \cdot Q_0 < S_0^2$ ($50000 \cdot 1 < 225000^2$), violating `validTriple`
- Exit code: 1
- Lean error output:
  ```text
  W2D7_corrupt.lean:70:2: error: Tactic `decide` proved that the proposition
    lenOk = true ∧ allValid = true ∧ denomPositive = true ∧ lowerOk = true ∧ upperOk = true
  is false
  'w2_d7_certificate_corrupt' depends on axioms: [sorryAx]
  ```
- Evaluation results:
  `lenOk = true`, `allValid = false`, `denomPositive = true`, `lowerOk = false`, `upperOk = true`
- Non-vacuity proof: Unlike the deprecated implication form (`allValid -> denomPositive -> ...`) which exited 0 with zero axioms on corrupted input because the premise was false, the conjunction form fails with exit 1 and does not produce a valid certificate.
- Status: **DISCRIMINATES (Non-vacuous, fail-closed)**

## Scalability and Stack Limits (Gate Finding B4)
For the 30 triples of the $W2, d=7$ component, the reduction executes well within default limits in 0.35s.
Lean 4.34.0's kernel reduction stack has a recursion depth boundary at longer lists under default configuration. For future multi-experiment passes:
- $d=5$ (120 triples): requires `set_option maxRecDepth 20000` (runs in ~0.60s)
- $d=3$ (270 triples): requires `set_option maxRecDepth 20000` (runs in ~1.06s)
- $W1$ (420 triples): requires `set_option maxRecDepth 20000` (runs in ~1.51s)
Therefore, no claim of universal scalability beyond length 30 is made for this v2 certificate without setting `maxRecDepth`.

## Finding on Lean 4 `Rat` Reduction
Verbatim Lean 4.34.0 output on `example : (1:Rat)/2 < (3:Rat)/4 := by decide`:
```text
<stdin>:2:38: error: Tactic `decide` failed for proposition
  1 / 2 < 3 / 4
because its `Decidable` instance
  (1 / 2).instDecidableLt (3 / 4)
did not reduce to `isTrue` or `isFalse`.

After unfolding the instances `instDecidableEqBool`, `Bool.decEq`, `Int.decLt`, `Int.decNonneg`, and `Rat.instDecidableLt`, reduction got stuck at the `Decidable` instance
  match (1 / 2).blt (3 / 4), true with
  | false, false => isTrue ⋯
  | false, true => isFalse ⋯
  | true, false => isFalse ⋯
  | true, true => isTrue ⋯
```
Kernel `decide` cannot reduce `Rat` division. Pure `Nat`/`Int` unreduced fraction cross-multiplication is mandatory.

## PASS Criterion
- Wall clock time: 0.35s (< 60s threshold) — **PASS**
- Trust boundary: zero axioms, no `native_decide`, no `Rat` — **PASS**
- Discrimination: rejects out-of-band and invalid guards — **PASS**
- Non-vacuity: verified on corrupted guard test case — **PASS**
=> **GO for W2-d7 v2 Formal Certificate.**
