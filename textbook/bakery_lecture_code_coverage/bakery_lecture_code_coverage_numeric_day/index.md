---
waltz:
  title: bakery_lecture_code_coverage_numeric_day
  display title: 3) Numeric Day
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    start_view: text
    disable_instructor_run: true
    disable_student_run: true
    disable_tifa: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 135
    created: July 25 2022, 0426 PM
    modified: September 13 2022, 0548 PM
  files:
    path: bakery_lecture_code_coverage_numeric_day
    hidden but accessible files: []
    instructor only files:
    - bakery_lecture_code_coverage_numeric_day\correct.py
    extra starting files: []
    read-only files: []
---
In the code below, you need to write unit tests to evaluate a function named `numeric_day`.

* `numeric_day(day: str) -> int`: Consumes a `day` representing the current day of week (e.g., `"Wednesday"`) and returns the corresponding numeric version of that day. Monday is 0, Tuesday is 1, and so on. If the day is not a valid day, then return `-1` instead. Any capitalization should be ignored, but no abbreviations are allowed. 
**Remember: You should not implement the `numeric_day` function yourself! Write the tests!**