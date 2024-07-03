---
waltz:
  title: bakery_project3_milestone2_average_weighted
  display title: 2.6) Average Weighted
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
    version downloaded: 50
    created: November 11 2022, 1114 AM
    modified: November 29 2022, 0355 PM
  files:
    path: bakery_project3_milestone2_average_weighted
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `average_weighted` that consumes a `user_token` (a string) and a `course_id` (an integer), and produces a float representing the average, **weighted** score of all the graded assignments in the course. To calculate this, add up the scores and points possible for all graded submissions multiplying each by their respective assignment weights, and then divide the total weighted scores by the total weighted points possible.

Feel free to copy and modify your submission from the last question.