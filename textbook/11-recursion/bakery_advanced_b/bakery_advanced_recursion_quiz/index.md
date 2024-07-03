---
waltz:
  title: bakery_advanced_recursion_quiz
  display title: 11B1) Recursion and Trees
  resource: problem
  type: quiz
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: true
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 2
    created: June 28 2022, 0300 PM
    modified: November 14 2022, 0222 PM
  files:
    path: bakery_advanced_recursion_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_advanced_recursion_read"
  },
  "questions": {
    "DefineTreeVocabulary": {
      "type": "matching_question",
      "points": 2,
      "body": "Match each term to the best definition.",
      "answers": [
        "node",
        "edge",
        "root",
        "leaf",
        "parent",
        "child",
        "tree"
      ],
      "statements": [
        "The top node in a tree, without any parents.",
        "A bottom node in a tree, without any children.",
        "A given element in a tree.",
        "The connection between elements in a tree.",
        "A data structure holding elements with parent and child relationships.",
        "A node that has one or more nodes under it.",
        "A node that is subordinate to another node."
      ]
    },
    "DefineRecursionVocabulary": {
      "type": "matching_question",
      "points": 2,
      "body": "Match each term from the reading to the best explanation.",
      "answers": [
        "base case",
        "recursive case",
        "simplification",
        "branch",
        "combination",
        "recursive call",
        "dataclass",
        "Accumulate pattern",
        "modulo"
      ],
      "statements": [
        "When the function being defined is used in its own definition.",
        "A logical decision in the code to do different things based on a condition.",
        "To bring together the results of the recursive calls and the current element.",
        "The process of reducing down the original argument before the recursive call.",
        "The simpler branch of a recursive function, where the recursion terminates with a simple value.",
        "The other branch of a recursive function, where the recursive call and combination happens."
      ]
    },
    "RecallRecursionLoopEquivalency": {
      "type": "true_false_question",
      "points": 1,
      "body": "Anything you can do with recursion, you can do with a `while` loop (and vice versa), since they are both looping constructs."
    },
    "DetermineRecursiveExpressionTypes": {
      "type": "matching_question",
      "points": 3,
      "body": "Given the following code, determine the *most accurate* type for each expression on its line.\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Tree:\n    pass\n\n@dataclass\nclass BinaryTree(Tree):\n    value: int\n    left: Tree\n    right: Tree\n\nEMPTY = Tree()\n\ndef sum_tree(tree: Tree) -> int:\n    if tree == EMPTY:\n        return 0\n    left_side = sum_tree(tree.left)\n    right_side = sum_tree(tree.right)\n    result = tree.value + left_side + right_side\n    return result\n```",
      "retainOrder": true,
      "answers": [
        "int",
        "float",
        "bool",
        "str",
        "list[int]",
        "list[float]",
        "list[str]",
        "list[bool]",
        "Tree",
        "BinaryTree",
        "No way of knowing anything about the type"
      ],
      "statements": [
        "<code>tree</code> in the branch's condition",
        "<code>tree</code> inside the base case",
        "<code>tree</code> inside the recursive case",
        "<code>tree.left</code> inside the recursive case",
        "<code>left_side</code>",
        "<code>tree.value</code> inside the recursive case",
        "<code>result</code>"
      ]
    }
  }
}