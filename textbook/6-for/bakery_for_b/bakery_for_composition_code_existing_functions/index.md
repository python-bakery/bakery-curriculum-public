---
waltz:
  title: bakery_for_composition_code_existing_functions
  display title: 6B2.2) Existing Functions
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
    version downloaded: 9
    created: June 28 2022, 0300 PM
    modified: September 09 2022, 0311 PM
  files:
    path: bakery_for_composition_code_existing_functions
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
There are three functions below that filter, map, and sum lists:
* `remove_xs` consumes a list of strings and removes any `"x"`s
* `map_strs_to_ints` consumes a list of strings and produces a list of integers
* `summate` consumes a list of integers and adds all the numbers together

Compose the functions in a new function named `total_values` such that they are applied correctly. This function should consume a list of strings (numbers and `"x"`s) and produces an integer representing the total ignoring the `"x"`s. You do not need to modify the existing functions.