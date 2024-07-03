---
waltz:
  title: bakery_project3_milestone2_ratio_graded
  display title: 2.4) Ratio Graded
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
    version downloaded: 32
    created: November 11 2022, 1113 AM
    modified: November 11 2022, 0507 PM
  files:
    path: bakery_project3_milestone2_ratio_graded
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `ratio_graded` that consumes a `user_token` (a string) and a `course_id` (an integer), and produces a string value representing the number of assignments that have been graded compared to the number of total assignments in the course. The two numbers should be separated by a `'/'` character. For example, `"5/10"` would mean that there are five graded assignments out of ten assignments in the course.