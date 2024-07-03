---
waltz:
  title: bakery_project3_milestone1_find_cisc
  display title: 1.3) Find CISC
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    disable_tifa: true
    preload_files: '{"course": {"37": {"canvas_data.json": true}}}'
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 28
    created: November 03 2022, 0115 AM
    modified: November 09 2022, 0844 AM
  files:
    path: bakery_project3_milestone1_find_cisc
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `find_cs1` that consumes a `user_token` (a string) and produces an integer representing the `id` of the first `Course` that has the text `"CISC1"` in their `code` field. If no `Course` can be found that satisfies the criteria, then return `0` instead.

The body of this function is similar to the previous one - you will need to use the `get_courses` function to access the relevant data.