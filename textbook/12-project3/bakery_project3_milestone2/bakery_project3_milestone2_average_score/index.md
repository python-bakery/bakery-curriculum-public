---
waltz:
  title: bakery_project3_milestone2_average_score
  display title: 2.5) Average Score
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
    version downloaded: 45
    created: November 11 2022, 1114 AM
    modified: November 29 2022, 0357 PM
  files:
    path: bakery_project3_milestone2_average_score
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `average_score` that consumes a `user_token` (a string) and a `course_id` (an integer), and produces a float representing the average, unweighted score of all the **graded** assignments in the course. To calculate this, you will need to add up the scores for all **graded** submissions, then add up all the points possible for the **graded** submissions, and then divide the first total by the second total. Do NOT multiply anything by the assignment's group's weight.