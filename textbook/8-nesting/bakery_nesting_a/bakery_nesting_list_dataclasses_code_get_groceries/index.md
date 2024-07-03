---
waltz:
  title: bakery_nesting_list_dataclasses_code_get_groceries
  display title: 8A1.1) Get Groceries
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
    version downloaded: 192
    created: September 17 2022, 0426 PM
    modified: September 19 2022, 1034 AM
  files:
    path: bakery_nesting_list_dataclasses_code_get_groceries
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The dataclass `Grocery` represents an item at a grocery store, and is defined below with the fields `item` (str), `cost` (int), and `on_sale` (boolean).

Define a function `sum_groceries` that consumes a list of `Grocery` and produces an integer representing the sum of all their costs.
Unit test this function a suitable number of times.