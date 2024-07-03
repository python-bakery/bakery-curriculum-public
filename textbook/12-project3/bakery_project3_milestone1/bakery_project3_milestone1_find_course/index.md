---
waltz:
  title: bakery_project3_milestone1_find_course
  display title: 1.4) Find Course
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
    modified: November 08 2022, 0604 PM
  files:
    path: bakery_project3_milestone1_find_course
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `find_course` that consumes a `user_token` (a string) and a `course_id` (an integer), and produces a string representing the full `name` of the course with the given `id`. If no course is found, then return `"no course found"` instead.