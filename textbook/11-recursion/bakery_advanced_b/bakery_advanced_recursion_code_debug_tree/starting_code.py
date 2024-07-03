from dataclasses import dataclass
from bakery import assert_equal

@dataclass
class Tree:
    pass

@dataclass
class BinaryTree:
    value: int
    left: ___
    right: Tree

EMPTY = BinaryTree()

def add_up_tree(tree: Tree) -> int:
    if tree == EMPTY:
        return 0
    left_side = tree.left
    right_side = add_up_tree(tree.right)
    combined = left_side + right_side
    return 'value' + combined

assert_equal(add_up_tree(BinaryTree(7, EMPTY, EMPTY)), 7)
assert_equal(add_up_tree(BinaryTree(7, BinaryTree(3, EMPTY, EMPTY), EMPTY)), 10)
assert_equal(add_up_tree(BinaryTree(7, BinaryTree(3, BinaryTree(1, EMPTY, EMPTY), EMPTY), BinaryTree(9, EMPTY, EMPTY))), 20)
assert_equal(add_up_tree(EMPTY), 0)