---
waltz:
  title: bakery_structures_dataclass_ops_next_door
  display title: 4A2.6) Next Door
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 51
    created: August 15 2022, 0834 PM
    modified: August 28 2022, 0235 PM
  files:
    path: bakery_structures_dataclass_ops_next_door
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `next_door` that consumes an `Address` and produces a new `Address` representing the house that is next door.

An `Address` has a `number` (integer), `street` (string), `city` (string), and `state` (string).

You can determine the house next door by increasing the `number` by 1; if the `number` becomes `10` or greater, than wrap it back around to `0`.

Hint: You can do this without an `if` statement! Think about what math operators we've taught you...