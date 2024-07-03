---
waltz:
  title: bakery_advanced_recursion_code_evaluate_operator
  display title: 11B1.4) Evaluate Operator
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    disable_tifa: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 101
    created: June 28 2022, 0300 PM
    modified: November 15 2022, 0144 PM
  files:
    path: bakery_advanced_recursion_code_evaluate_operator
    hidden but accessible files: []
    instructor only files:
    - bakery_advanced_recursion_code_evaluate_operator\correct.py
    extra starting files: []
    read-only files: []
---
Math expressions can be represented as trees. We will rename the empty parent dataclass as `Expression`.

Then, we will have a `BinaryExpression` dataclass:
* `operator` (a string, either `'+'` or `'*'`)
* `left` (an `Expression`)
* `right` (an `Expression`)

To actually make this work, we need one further twist: instead of an `EMPTY` instance, we'll instead have a `IntegerExpression` dataclass with a single field:
* `value` (an integer)

The function `evaluate_math` is meant to process these complex Expression trees, and we have already written the logic that will separate out the base case from the recursive case. However, you will need to fill in the rest such that the code correctly evaluates the mathematical expressions.

**Note**: This problem is different from the other ways we've used recursion so far, and it's meant to highlight how much variety you can see with these problems. It is not something we would put on our exam, but it is still worth looking closely at!