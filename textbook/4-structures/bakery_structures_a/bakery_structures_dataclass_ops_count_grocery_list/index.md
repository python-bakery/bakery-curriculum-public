---
waltz:
  title: bakery_structures_dataclass_ops_count_grocery_list
  display title: 4A2.1) Count Grocery List Items
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    start_view: text
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 58
    created: August 15 2022, 0241 PM
    modified: September 09 2022, 0301 PM
  files:
    path: bakery_structures_dataclass_ops_count_grocery_list
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The function `count_items` consumes a `GroceryList` instance and produces the total number of items that are in the grocery list. A `GroceryList` is a dataclass with three integer fields: `eggs`, `bread`, and `milk`.

When counting up the items of a grocery list, you need to multiply the `eggs` by 12 (since one package contains a dozen eggs) and the `bread` by 20 (since one loaf contains about 20 slices).

One unit test is provided to you, but you should write another!