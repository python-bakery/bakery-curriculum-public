---
waltz:
  title: bakery_lecture_code_coverage_str_average
  display title: 2) Sum Digits
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    disable_instructor_run: true
    disable_student_run: true
    disable_tifa: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 126
    created: August 12 2022, 0737 PM
    modified: September 13 2022, 0606 PM
  files:
    path: bakery_lecture_code_coverage_str_average
    hidden but accessible files: []
    instructor only files:
    - bakery_lecture_code_coverage_str_average\correct.py
    extra starting files: []
    read-only files: []
---
In the code below, you need to write unit tests to evaluate a function named `add_three_digits`.

* `add_three_digits(digits: str) -> int`: Consumes a string of three digits (e.g., `"123"`), converts each digit to an integer, and produces their sum. If any characters are not digits, or if there are not three digits, then the integer `0` should be returned instead.

**You should not implement the `add_three_digits` function yourself!**

Instead, your job is to write a collection of unit tests that:
* will all pass when provided a *correct* implementation of the function ("Valid Tests", or "Accept Wheat")
* at least one will fail when provided an *incorrect* implementation of the function ("Thorough Tests", or "Reject Chaff")

You earn points for each of the wheats you correctly accept and each of the chaffs you correctly reject.