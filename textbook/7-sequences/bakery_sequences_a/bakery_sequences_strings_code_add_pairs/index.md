---
waltz:
  title: bakery_sequences_strings_code_add_pairs
  display title: 7A1.3) Add Pairs
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
    version downloaded: 40
    created: September 09 2022, 1222 PM
    modified: September 09 2022, 0332 PM
  files:
    path: bakery_sequences_strings_code_add_pairs
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `add_pairs` that consumes a list of numbers and produces a new list with each number added to the previous element of the list. So `[1, 4, 7]` would become `[8, 5, 11]`. Use the `range` and `len` functions or the `enumerate` function. The first element will be naturally added to the last element.

**Hint:** One of the quiz questions achieves a similar effect of getting the previous element from the current index.