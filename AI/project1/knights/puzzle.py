from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

common_knowledge = And(
    # A is either a knight or a knave
    Or(AKnight, AKnave),
    # A cannot be both a knight and a knave
    Not(And(AKnight, AKnave)),
    # B is either a knight or a knave
    Or(BKnight, BKnave),
    # B cannot be both a knight and a knave
    Not(And(BKnight, BKnave)),
    # C is either a knight or a knave
    Or(CKnight, CKnave),
    # C cannot be both a knight and a knave
    Not(And(CKnight, CKnave))
)
# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave))),
    common_knowledge
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
    common_knowledge
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
    common_knowledge
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
   Implication(AKnight, Or(AKnight, AKnave)),
   Implication(AKnave, Not(Or(AKnight, AKnave))),
   Implication(BKnight, AKnave),
   Implication(BKnave, Not(AKnave)),
   Implication(BKnight, CKnave),
   Implication(BKnave, Not(CKnave)),
   Implication(CKnight, AKnight),
   Implication(CKnave, Not(AKnight)),
   common_knowledge
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
