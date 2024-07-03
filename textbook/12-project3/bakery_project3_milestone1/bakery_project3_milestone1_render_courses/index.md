---
waltz:
  title: bakery_project3_milestone1_render_courses
  display title: 1.5) Render Courses
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
    version downloaded: 46
    created: November 03 2022, 0115 AM
    modified: November 08 2022, 0604 PM
  files:
    path: bakery_project3_milestone1_render_courses
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `render_courses` that consumes a `user_token` (a string) and produces a single string that combines all the available courses by joining together their IDs and codes, ending each course with a newline.

For example, a user with the courses CISC108 (ID 100167) and ENGL101 (ID 386814) would produce a string like: `"100167: CISC108\n386814: ENGL101\n"`

If the user has no courses, produce just the empty string.