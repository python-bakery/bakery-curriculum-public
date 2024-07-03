from dataclasses import dataclass

@dataclass
class Tree:
    pass

@dataclass
class BinaryTree(Tree):
    value: int
    left: Tree
    right: Tree

EMPTY = Tree()

data = BinaryTree(1, BinaryTree(5, BinaryTree(7, EMPTY, EMPTY),
                                   BinaryTree(9, EMPTY, EMPTY)),
                     BinaryTree(3, BinaryTree(6, EMPTY, EMPTY),
                                   BinaryTree(4, EMPTY, EMPTY)))
print(data)