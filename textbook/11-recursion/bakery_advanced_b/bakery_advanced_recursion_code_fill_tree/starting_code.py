from dataclasses import dataclass
from bakery import assert_equal

@dataclass
class Corgi:
    name: str
    height: int
    coat_color: str

@dataclass
class Tree:
    pass

EMPTY = Tree()

@dataclass
class FamilyTree:
    corgi: Corgi
    mother: Tree
    father: Tree

def stack_yellow_corgis(family: Tree) -> int:
    if ___ == ___:
        return ___
    mother_height_total = ___(___.___)
    father_height_total = ___(___.___)
    total_height_from_parents = ___ + ___
    if ___.___.___ == "___":
        return total_height_from_parents + ___.___.___
    else:
        return total_height_from_parents

assert_equal(stack_yellow_corgis(EMPTY), 0)
ada = Corgi("Ada", 20, "yellow")
grace = Corgi("Grace", 30, "yellow")
alan = Corgi("Alan", 25, "yellow")
don = Corgi("Don", 15, "brown")
assert_equal(stack_yellow_corgis(FamilyTree(ada, EMPTY, EMPTY)), 20)
assert_equal(stack_yellow_corgis(FamilyTree(ada, FamilyTree(grace, EMPTY, EMPTY), EMPTY)), 50)
assert_equal(stack_yellow_corgis(FamilyTree(ada, FamilyTree(grace, EMPTY, EMPTY), FamilyTree(alan, EMPTY, EMPTY))), 75)
assert_equal(stack_yellow_corgis(FamilyTree(ada, FamilyTree(grace, EMPTY, EMPTY), FamilyTree(don, EMPTY, EMPTY))), 50)