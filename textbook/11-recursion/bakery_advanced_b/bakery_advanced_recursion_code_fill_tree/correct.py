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
    if family == EMPTY:
        return 0
    mother_height_total = stack_yellow_corgis(family.mother)
    father_height_total = stack_yellow_corgis(family.father)
    total_height_from_parents = mother_height_total + father_height_total
    if family.corgi.coat_color == "yellow":
        return total_height_from_parents + family.corgi.height
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