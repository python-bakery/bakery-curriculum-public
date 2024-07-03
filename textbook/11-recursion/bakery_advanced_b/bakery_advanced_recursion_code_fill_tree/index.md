---
waltz:
  title: bakery_advanced_recursion_code_fill_tree
  display title: 11B1.3) Fill Tree
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
    version downloaded: 110
    created: June 28 2022, 0300 PM
    modified: November 14 2022, 0117 PM
  files:
    path: bakery_advanced_recursion_code_fill_tree
    hidden but accessible files: []
    instructor only files:
    - bakery_advanced_recursion_code_fill_tree\correct.py
    extra starting files: []
    read-only files: []
---
A `Corgi` is a short-legged dog represented by a dataclass with the fields:
* `name` (a string)
* `height` (an integer)
* `coat_color` (a string, either `'yellow'` or `'mixed'`)

A `Tree` is an empty dataclass, and the instance `EMPTY` represents an empty tree.

A `FamilyTree` is a dataclass inheriting from `Tree` that represents the known lineage of a Corgi, with the fields:
* `corgi` (a `Corgi`)
* `mother` (a `Tree`)
* `father` (a `Tree`)

The function `stack_yellow_corgis` below is meant to calculate the total height of the *yellow* Corgis in a lineage. Fill in the blanks inside the function definition to complete the code.