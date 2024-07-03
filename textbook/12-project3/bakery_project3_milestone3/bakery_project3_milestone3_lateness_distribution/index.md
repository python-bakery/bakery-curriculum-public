---
waltz:
  title: bakery_project3_milestone3_lateness_distribution
  display title: 3.2) Lateness Distribution
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 42
    created: November 25 2022, 0457 PM
    modified: November 29 2022, 0418 PM
  files:
    path: bakery_project3_milestone3_lateness_distribution
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `plot_earliness` that consumes a `user_token` (a string) and a `course_id` (an integer) and returns nothing but creates a graph representing the distribution of the lateness of each submission. 

The lateness can be calculated using the provided helper function `days_apart` that consumes two strings (representing two dates in ISO format) and produces an integer indicating how many days are between the two dates. You will need to use the `submitted_at` field of the submission and the `due_at` field of the assignment, and calculate their difference. The order matters - use `submitted_at` first, then `due_at` (so that we are plotting the *days early* rather than the *days late*). Make sure you check that both fields are not empty strings before you call the function!

The function does not need a `return` statement, but must call the appropriate plotting function, the `plt.show()` function, the `plt.title(text)` function, and both `plt.xlabel(text)` and `plt.ylabel(text)`.

We have not taught you how to unit test functions that plot, so you do NOT need unit tests for this function. However, if you would like to have the function return the data you plot, you are free to write unit tests for debugging purposes. The autograder does not care what your function returns, just that it generates the correct plot data. Either way, we strongly recommend calling your function yourself so you can see the output.