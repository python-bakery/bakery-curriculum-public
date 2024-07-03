---
waltz:
  title: bakery_project3_milestone1_count_courses
  display title: 1.2) Count Courses
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
    version downloaded: 77
    created: November 03 2022, 0219 AM
    modified: November 08 2022, 0604 PM
  files:
    path: bakery_project3_milestone1_count_courses
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The first function you will need to implement is `count_courses`, which consumes a `user_token` (a string value) and produces an integer representing the number of courses that user is taking.

Your `count_courses` function will need to use the `get_courses` function from the `bakery_canvas` library. We have already provided the import statements and unit tests. However, it is up to you to define the body!