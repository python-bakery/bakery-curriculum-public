---
waltz:
  title: bakery_for_composition_code_highest_filter
  display title: 6B2.4) Highest Filter
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
    path: bakery_for_composition_code_highest_filter
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define the function `high_score` that consumes a list of integers (representing scores in a game) and produces an integer representing the highest score in the list. Ignore scores less than `100`, and stop processing values if you encounter `-999`. If the list is empty, return the value `None` instead. It is up to you to decompose this function (or not) however you want.