---
waltz:
  title: bakery_if_patterns_get_course_area
  display title: 3B2.3) Unknown Course
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
    version downloaded: 32
    created: September 09 2022, 0922 AM
    modified: September 14 2022, 0550 PM
  files:
    path: bakery_if_patterns_get_course_area
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `get_course_area` that consumes a string representing a course (e.g., `"CISC101"`) and produces a string. Normally, the result should just be the first part of the string (e.g., `"CISC"`, by removing the last three characters). However, if the first part of the string is `"UNKW"` then instead return `"Unknown"`. These represent specific kinds of invalid class codes.