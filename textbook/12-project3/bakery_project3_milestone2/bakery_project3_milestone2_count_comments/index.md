---
waltz:
  title: bakery_project3_milestone2_count_comments
  display title: 2.3) Count Comments
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
    version downloaded: 21
    created: November 11 2022, 1113 AM
    modified: November 11 2022, 0355 PM
  files:
    path: bakery_project3_milestone2_count_comments
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `count_comments` that consumes a `user_token` (a string) and a `course_id` (an integer), and produces an integer representing the number of comments across all the submissions for that course. 

Write at least two unit tests. You may find it helpful to explore the data in Thonny or in the reading at the start of this Part.