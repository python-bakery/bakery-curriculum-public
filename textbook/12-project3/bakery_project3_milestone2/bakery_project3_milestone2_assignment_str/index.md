---
waltz:
  title: bakery_project3_milestone2_assignment_str
  display title: 2.8) Assignment String
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
    version downloaded: 152
    created: November 11 2022, 1115 AM
    modified: November 16 2022, 0330 PM
  files:
    path: bakery_project3_milestone2_assignment_str
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `render_assignment` that consumes a `user_token` (a string), a `course_id` (an integer), and an `assignment_id` (an integer). The function produces a string representing the assignment and its submission details. If the assignment cannot be found in the user's submissions, then return the string `"Assignment not found: "` followed by the `assignment_id`.

The string needs to include the following data on separate lines (i.e., separated by newline characters `"\n"`):

* Assignment `id`, a colon, and the assignment `name`
* The text `Group: `, and the group's name
* The text `Module: `, and the module's name
* If the assignment is graded, then:
    * The text `Grade: `, submission `score`, a `'/'` character, the `points_possible`, open parentheses, the `grade`, and then a closed parentheses
    * Otherwise, the last line should just be the text `Grade: (missing)`

Here is an example:
```
12345: Chapter 2.5 Problems
Group: Homeworks
Module: Week 1
Grade: 9/10 (A-)
```

Or on one line: `"12345: Chapter 2.5 Problems\nGroup: Homeworks\nModule: Week 1\nGrade: 9/10 (A-)"`

Later on, you may choose to include additional fields in this string, but for now please limit it to these fields and this format.

**NOTE:** This function is *not* `print`ing. Do not do any kind of printing!