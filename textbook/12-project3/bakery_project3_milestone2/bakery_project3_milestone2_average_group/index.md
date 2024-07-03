---
waltz:
  title: bakery_project3_milestone2_average_group
  display title: 2.7) Average Group
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
    version downloaded: 78
    created: November 11 2022, 1115 AM
    modified: November 29 2022, 0403 PM
  files:
    path: bakery_project3_milestone2_average_group
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `average_group` that consumes a `user_token` (a string), a `course_id` (an integer), and a `group_name` (a string). The function returns a float representing the average, unweighted grade ratio for all the graded submissions with that `group_name`. (The "grade ratio" of an assignment is the score divided by the points possible, so a score of 8 on an assignment worth 10 points would have a grade ratio of 0.8).

When testing group names, ignore capitalization by using the `.lower()` or `.upper()` string methods. If there are no assignments in that group, then return `0.0`.