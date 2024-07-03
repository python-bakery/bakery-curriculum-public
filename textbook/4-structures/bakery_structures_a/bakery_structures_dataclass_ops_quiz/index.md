---
waltz:
  title: bakery_structures_dataclass_ops_quiz
  display title: 4A2) Using Dataclasses
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
    version downloaded: 1
    created: June 28 2022, 0300 PM
    modified: August 10 2022, 0458 PM
  files:
    path: bakery_structures_dataclass_ops_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_structures_dataclass_ops_read"
  },
  "questions": {
    "ListDataclassOperators": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "Which of the following operators work with dataclass instances?",
      "answers": [
        "Addition (`+`)",
        "Subtraction (`-`)",
        "Indexing (square brackets, `[]`)",
        "Equality (`==`)",
        "Comparison (`<`)",
        "Modulo (`%`)"
      ]
    },
    "DescribeDataclassInstanceEquivalency": {
      "type": "multiple_choice_question",
      "points": 3,
      "body": "When are two instances equivalent?",
      "answers": [
        "Two instances are equivalent if they have the same values in their fields, even if the instances come from different dataclasses.",
        "Two instances are equivalent if they come from the same dataclass and have the same values for their fields.",
        "Two instances are equivalent if at least one value is the same in each",
        "Two instances can never be equivalent; using `==` with instances will cause an error",
        "Two instances can never be equivalent, but it does not cause an error to check"
      ]
    },
    "ConnectFunctionDataclasses": {
      "type": "multiple_answers_question",
      "points": 2,
      "body": "Which of the following statements is true?",
      "answers": [
        "A function can return an instance of a dataclass",
        "A function can consume an instance of a dataclass",
        "The attribute of an instance can be used as an argument to a function",
        "The attribute of an instance can be used as the return value for a function"
      ]
    },
    "AnnotateDataclassTypes": {
      "type": "fill_in_multiple_blanks_question",
      "points": 3,
      "body": "Given the code below...\n\n```python\nfrom dataclasses import dataclass\nfrom bakery import assert_equal\n\n@dataclass\nclass Fruit:\n    kind: str\n    sweetness: __1__\n\ndef is_sweet(fruit: __2__) -> __3__:\n    return fruit.sweetness > 10\n\nassert_equal(is_sweet(Fruit(\"Orange\", 15)), True)\nassert_equal(is_sweet(Fruit(\"Lemon\", 5)), False)\n```\n\nWhat type should be put in the `__1__` blank? [fieldType]\n\nWhat type should be put in the `__2__` blank? [parameterType]\n\nWhat type should be put in the `__3__` blank? [returnType]"
    },
    "UseAttributeAccessInFunction": {
      "type": "fill_in_multiple_blanks_question",
      "points": 3,
      "body": "Given the code below...\n\n```python\nfrom dataclasses import dataclass\nfrom bakery import assert_equal\n\n@dataclass\nclass Wallet:\n    cash: int\n    cards: int\n\ndef add_wallets(left: Wallet, right: Wallet) -> __1__:\n    return Wallet(\n        left.cash + right.cash,\n        __2__ + __3__\n    )\n\nassert_equal(add_wallets(Wallet(5, 10), Wallet(3, 2)), Wallet(8, 12))\n```\n\nWhat type should be put in the `__1__` blank? [returnType]\n\nWhat code should be put in the `__2__` blank? [leftOperand]\n\nWhat code should be put in the `__3__` blank? [rightOperand]"
    }
  }
}