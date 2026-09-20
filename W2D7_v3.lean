-- W2-d7 component formal certificate. No Rat. No native_decide.
-- Input file: W2D7_INPUT.json
-- Input SHA-256: 3dd3a86624b53f3aead8972fd902cee7431c11d1f42199e05f9a055e08892b5f
-- Pure Nat/Int, kernel `decide`. Strict interval: 559/200 < x < 561/200
-- (2.795 < exact-rational W2,d=7 < 2.805), positive corroboration band matching R5.
-- Theorem is a strict conjunction; never an implication.

def triples : List (Nat × Nat × Nat) := [
  (50000, 98916, 372294),
  (50000, 1759810, 66344048),
  (50000, 20759483, 8676985925),
  (50000, 2315086, 113133374),
  (50000, 25288691, 12862957093),
  (50000, 28170889, 15949659425),
  (50000, 32732057, 21523447829),
  (50000, 36596627, 26891401861),
  (50000, 38514193, 29776371753),
  (50000, 44240422, 39282477592),
  (50000, 46774458, 43925233994),
  (50000, 5746174, 675739636),
  (50000, 9184797, 1712722641),
  (50000, 13249450, 3547539852),
  (50000, 16850726, 5724865826),
  (50000, 103626, 407116),
  (50000, 1763845, 66611491),
  (50000, 20558118, 8507732124),
  (50000, 2347082, 116053710),
  (50000, 24167226, 11746559984),
  (50000, 28497247, 16343524699),
  (50000, 32064703, 20651376875),
  (50000, 36970491, 27467986555),
  (50000, 39530523, 31363282905),
  (50000, 43384864, 37792203870),
  (50000, 46082695, 42610442423),
  (50000, 5725329, 670644755),
  (50000, 9197872, 1717040414),
  (50000, 13216577, 3529752173),
  (50000, 17853344, 6428008654)
]

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

#print axioms w2_d7_certificate
#eval lenOk
#eval allValid
#eval denomPositive
#eval lowerOk
#eval upperOk
