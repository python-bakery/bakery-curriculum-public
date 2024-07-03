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

data = ___
print(data)