---
waltz:
  title: bakery_lecture_code_coverage_split_pay
  display title: 4) Split Pay
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
    version downloaded: 201
    created: July 25 2022, 0425 PM
    modified: September 14 2022, 1229 PM
  files:
    path: bakery_lecture_code_coverage_split_pay
    hidden but accessible files: []
    instructor only files:
    - bakery_lecture_code_coverage_split_pay\correct.py
    extra starting files: []
    read-only files: []
---
In the code below, you need to write unit tests to evaluate a function named `split_pay`.

* `split_pay(amount: str, people: int) -> float`: Consumes an `amount` representing an amount in dollars (e.g., `"$2.50"`) and a positive number of `people`, and determines how much money each person should get (as a float) such that everyone gets the same amount. The dollar amounts will always be strings. They may or may not start with a dollar sign, and they may or may not end in a decimal plus two digits. Otherwise, however, they should be proper numbers. If the arguments are invalid, then the float `0.0` should be returned.

**Remember: You should not implement the `split_pay` function yourself! Write the tests!**