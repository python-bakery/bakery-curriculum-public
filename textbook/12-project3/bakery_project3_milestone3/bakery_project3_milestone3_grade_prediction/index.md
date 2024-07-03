---
waltz:
  title: bakery_project3_milestone3_grade_prediction
  display title: 3.4) Grade Prediction
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
    version downloaded: 203
    created: November 25 2022, 0458 PM
    modified: November 29 2022, 1055 PM
  files:
    path: bakery_project3_milestone3_grade_prediction
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Students often ask "what grade will I earn?" But that question is complicated because there are often many assignments still left to be graded and they are not all worth the same number of points. To help visualize the range of possibilites, you are going to make a **graph with three line plots**:

1. A running sum line of the maximum weighted points possible in the course (`max_points`).
2. A running sum line of the maximum possible weighted score in the course (`max_score`).
3. A running sum line of the minimum possible weighted score in the course (`min_score`).

If all assignments in the course were already graded, then the `max_score` and `min_score` lines would be the same; otherwise, the two lines show what happens if you scored perfect 100%s (`max_score`) and 0%s (`min_score`) on each assignment. Similarly, if you scored perfectly on *every* assignment in the entire course, then the `max_points` line would match exactly to the `max_score` line.

All of the lines need to be weighted appropriately, which means you will need to begin by calculating the *total weighted points* before the running sum lists (similar to the previous problem). The final result should have the values `0` to `100` on the Y-axis (representing the course grade), and each assignment on the X-axis.

Define a function `predict_grades` that consumes a `user_token` (a string) and a `course_id` (an integer) and returns nothing but creates a graph with the three running sums as described above. The function does not need a `return` statement, but must call the appropriate plotting function, the `plt.show()` function, the `plt.title(text)` function, and both `plt.xlabel(text)` and `plt.ylabel(text)`.

[This infographic](https://i.imgur.com/v7xUByq.png) gives an example of the calculations required to generate the grade predictions graph. In its final graph, you can see the students' range of possible final grades between the green and red lines. 