-- W2-d7 component formal certificate. No Rat. No native_decide.
-- Pure Nat/Int, kernel `decide`. Strict interval: 559/200 < x < 561/200
-- (2.795 < exact-rational W2,d=7 < 2.805), pre-registered R5 verification band.
-- Theorem is a strict conjunction; never an implication.

def triples : List (Nat × Nat × Nat) := [
  (50000, 219125, 1578338),
  (50000, 223619, 1631012),
  (50000, 259083, 2072718),
  (50000, 237326, 1796073),
  (50000, 183466, 1190509),
  (50000, 206119, 1431310),
  (50000, 227072, 1671187),
  (50000, 272561, 2254084),
  (50000, 202904, 1395544),
  (50000, 201042, 1375178),
  (50000, 268043, 2193255),
  (50000, 253401, 1999166),
  (50000, 207892, 1450737),
  (50000, 223716, 1631408),
  (50000, 244220, 1881381),
  (50000, 180689, 1162198),
  (50000, 212316, 1499923),
  (50000, 176637, 1122151),
  (50000, 236060, 1779903),
  (50000, 208798, 1460639),
  (50000, 196353, 1324985),
  (50000, 200715, 1371420),
  (50000, 216384, 1547012),
  (50000, 234994, 1766664),
  (50000, 227474, 1676385),
  (50000, 180274, 1158355),
  (50000, 240020, 1829409),
  (50000, 246409, 1908905),
  (50000, 257560, 2052732),
  (50000, 194820, 1308577)
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

theorem w2_d7_certificate_band_neg :
    lenOk = true ∧
    allValid = true ∧
    denomPositive = true ∧
    lowerOk = true ∧
    upperOk = true := by
  decide

#print axioms w2_d7_certificate_band_neg
#eval lenOk
#eval allValid
#eval denomPositive
#eval lowerOk
#eval upperOk
