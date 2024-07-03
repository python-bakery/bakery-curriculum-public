---
waltz:
  title: bakery_structures_mutability_code_wrong_return
  display title: 4B3.4) Wrong Return
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    start_view: text
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 6
    created: June 28 2022, 0300 PM
    modified: September 09 2022, 0951 AM
  files:
    path: bakery_structures_mutability_code_wrong_return
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The function <code>get_front_of_weekdays</code> consumes a string representing a day of the week, and returns <code>"weekend"</code> if it is a Sunday or Saturday, or returns the day without the <code>"day"</code> part at the end. However, it does not seem to be returning the right values. Diagnose the issue and fix the function.