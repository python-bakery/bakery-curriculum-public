---
waltz:
  title: bakery_project3_milestone3_score_distribution
  display title: 3.1) Score Distribution
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
    version downloaded: 171
    created: November 25 2022, 0457 PM
    modified: November 29 2022, 0414 PM
  files:
    path: bakery_project3_milestone3_score_distribution
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `plot_scores` that consumes a `user_token` (a string) and a `course_id` (an integer) and returns nothing but creates a graph representing the distribution of the fractional scores in the course. The fractional score can be calculated by dividing each `score` by the `points_possible` for that assignment and then multiplying by `100`. Make sure to skip assignments that do not have a grade or that are worth zero points.

The function does not need a `return` statement, but must call the appropriate plotting function, the `plt.show()` function, the `plt.title(text)` function, and both `plt.xlabel(text)` and `plt.ylabel(text)`.

We have not taught you how to unit test functions that plot, so you do NOT need unit tests for this function. However, if you would like to have the function return the data you plot, you are free to write unit tests for debugging purposes. The autograder does not care what your function returns, just that it generates the correct plot data. Either way, we strongly recommend calling your function yourself so you can see the output.