-- W2-d7 component formal certificate. No Rat. No native_decide.
-- Input file: triples_corrupt.json
-- Input SHA-256: a318d7b178a1415f72e0d2896f99ad191e757fc6472231ecbcd1678c840273d6
-- Pure Nat/Int, kernel `decide`. Strict interval: 559/200 < x < 561/200
-- (2.795 < exact-rational W2,d=7 < 2.805), positive corroboration band matching R5.
-- Theorem is a strict conjunction; never an implication.

def triples : List (Nat × Nat × Nat) := [
  (50000, 233640, 1),
  (50000, 187773, 1230972),
  (50000, 215998, 1537080),
  (50000, 218816, 1569177),
  (50000, 247275, 1914734),
  (50000, 222047, 1607949),
  (50000, 261682, 2101086),
  (50000, 193762, 1292894),
  (50000, 193503, 1290237),
  (50000, 222777, 1616404),
  (50000, 207300, 1439635),
  (50000, 227318, 1669453),
  (50000, 221681, 1603125),
  (50000, 237009, 1785900),
  (50000, 210697, 1477427),
  (50000, 228153, 1679539),
  (50000, 242422, 1853272),
  (50000, 194474, 1300257),
  (50000, 243236, 1863188),
  (50000, 196948, 1327350),
  (50000, 201868, 1380039),
  (50000, 264667, 2140774),
  (50000, 175811, 1109827),
  (50000, 219870, 1581455),
  (50000, 243494, 1867106),
  (50000, 204275, 1406250),
  (50000, 195322, 1309725),
  (50000, 181364, 1165525),
  (50000, 177473, 1126761),
  (50000, 222864, 1616886)
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

theorem w2_d7_certificate_corrupt :
    lenOk = true ∧
    allValid = true ∧
    denomPositive = true ∧
    lowerOk = true ∧
    upperOk = true := by
  decide

#print axioms w2_d7_certificate_corrupt
#eval lenOk
#eval allValid
#eval denomPositive
#eval lowerOk
#eval upperOk
