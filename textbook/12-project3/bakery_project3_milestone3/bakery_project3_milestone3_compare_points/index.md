---
waltz:
  title: bakery_project3_milestone3_compare_points
  display title: 3.3) Compare Points
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    disable_tifa: true
    hide_files: false
    preload_files: '{"course": {"37": {"canvas_data.json": true}}}'
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 216
    created: November 25 2022, 0457 PM
    modified: November 29 2022, 1259 PM
  files:
    path: bakery_project3_milestone3_compare_points
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
If assignment A is worth 100 points and assignment B is worth 100 points, does that mean they are worth the same amount? Not necessarily! You need to consider the assignment's group weight. After all, some instructors might weigh exams more heavily than homeworks. How often do assignments' points possible match their *actual* amount in the overall course? Let's make a plot that will show us.

Define a function `plot_points` that consumes a `user_token` (a string) and a `course_id` (an integer) and returns nothing but creates a graph comparing the points possible for each assignment with the *weighted* points possible for that assignment. The weighted points possible for a given assignment is calculated by multiplying the assignment's points possible by the assignment's group's weight and dividing by the *total weighted points*. The total weighted points can be calculated by adding together all of the assignment's points possible multiplied by their respective group's weight divided by `100`. Note that you will need to calculate the *total weighted points* BEFORE you can calculate the *weighted points possible* for each assignment. If the total weighted points is zero, then do not plot anything (just `return` early).

As an example of the, consider the following three assignments (with their associated group weights):

<table class="table table-condensed table-bordered table-striped" style="max-width:400px">
    <tr><th>Assignment</th><th>Points Possible</th><th>Group Weight</th></tr>
    <tr><td>Homework 1</td><td>100</td><td>20%</td></tr>
    <tr><td>Midterm 1</td><td>20</td><td>80%</td></tr>
    <tr><td>Homework 2</td><td>20</td><td>20%</td></tr>
</table>

In the example data above, the total points possible is `140`, but the *total weighted points* is `(20*100 + 80*20 + 20*20) / 100`, or `40.0`. So the *weighted points possible* for each assignment are:

* Homework 1: `100*20/40.`, or `50.0`
* Midterm 1: `80*20/40.`, or `40.0`
* Project 2: `20*20/40.`, or `10.0`

The function does not need a `return` statement, but must call the appropriate plotting function, the `plt.show()` function, the `plt.title(text)` function, and both `plt.xlabel(text)` and `plt.ylabel(text)`.