---
waltz:
  title: bakery_nesting_list_dataclasses_code_grocery_sales
  display title: 8A1.2) Check for Sales
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
    version downloaded: 26
    created: September 17 2022, 0427 PM
    modified: October 15 2022, 0959 PM
  files:
    path: bakery_nesting_list_dataclasses_code_grocery_sales
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The dataclass `Grocery` represents an item at a grocery store, and is defined below with the fields `item` (str), `cost` (int), and `on_sale` (boolean).

Define a function `sum_sale` that consumes a list of `Grocery` and produces an integer representing the sum of all their costs, but only include items that are on sale.
Unit test this function a suitable number of times.