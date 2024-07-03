---
waltz:
  title: bakery_time_while_patterns_code_rainfall_accumulates
  display title: 9A2.3) Rainfall Accumulates
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
    version downloaded: 45
    created: September 19 2022, 1108 PM
    modified: September 19 2022, 1131 PM
  files:
    path: bakery_time_while_patterns_code_rainfall_accumulates
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Write a program (not a function) that repeatedly takes in user `input` representing daily rainfall measurements (non-negative integers) until it encounters the integer `99999`. The program should output the average of the numbers encountered before `99999`. Ignore negative numbers and any user input that is not made up entirely of digits. If no valid numbers are entered, then print out 0 instead.