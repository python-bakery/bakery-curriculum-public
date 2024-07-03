---
waltz:
  title: bakery_project3_milestone2_total_points
  display title: 2.2) Total Points
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
    version downloaded: 30
    created: November 11 2022, 1113 AM
    modified: November 11 2022, 0354 PM
  files:
    path: bakery_project3_milestone2_total_points
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define the function `total_points` that consumes a `user_token` (a string) and a `course_id` (an integer), and produces an integer representing the total number of points possible in the course (NOT adjusted by group weights).

Your `total_points` function will need to use the `get_submissions` function from the `bakery_canvas` library. We have already provided the import statements and unit tests. However, it is up to you to define the function!

