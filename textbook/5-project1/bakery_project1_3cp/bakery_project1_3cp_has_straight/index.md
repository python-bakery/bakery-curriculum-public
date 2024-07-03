---
waltz:
  title: bakery_project1_3cp_has_straight
  display title: 5.5) has_straight
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    start_view: text
  forked:
    id: 683
    version: 26
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 50
    created: October 05 2021, 0845 PM
    modified: September 28 2022, 1029 AM
  files:
    path: bakery_project1_3cp_has_straight
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function **has_straight** that accepts a list of three integers (*hand*) as described in the 3-card poker assignment, and returns **True** if and only if the list is in direct consecutive order from largest to smallest. You may assume that the *hand* has already been sorted from largest to smallest.

"Direct, consecutive order" means that `3, 2, 1` works but `4, 2, 1` does not.

Define at least three **assert_equal** tests for your function.