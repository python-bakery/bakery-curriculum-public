---
waltz:
  title: bakery_project3_milestone2_render_all
  display title: 2.9) Render All
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
    version downloaded: 59
    created: November 11 2022, 1116 AM
    modified: November 11 2022, 0518 PM
  files:
    path: bakery_project3_milestone2_render_all
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `render_all` that consumes a `user_token` (a string) and a `course_id` (an integer), and produces a single string that describes all of the submissions in the course. Each submission should be separate by a newline character. For each submission, include its **assignment `id`**, `name`, and whether it was `"graded"` or `"ungraded"`, like so:

`"12345: Chapter 1.5 Problems (graded)\n5738: Chapter 2.3 Problems (ungraded)"`