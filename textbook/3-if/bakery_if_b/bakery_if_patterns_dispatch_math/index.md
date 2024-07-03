---
waltz:
  title: bakery_if_patterns_dispatch_math
  display title: 3B2.4) Dispatch the Math
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
    version downloaded: 49
    created: September 09 2022, 0922 AM
    modified: September 09 2022, 0930 AM
  files:
    path: bakery_if_patterns_dispatch_math
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `dispatch_math` that consumes a string and two integers, and produces an integer. The first argument (the string) represents an operator: either `"+"`, `"-"`, or `"*"`. The second and third arguments (the integers) are meant to represent the operands for the given operator. The result will be the addition, subtraction, or product of the two operands based on the first parameter. If any other operator is given, just return `0`.