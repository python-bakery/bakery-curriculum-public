---
waltz:
  title: bakery_time_while_patterns_code_double_down
  display title: 9A2.2) Doubling Down
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
    created: September 19 2022, 1107 PM
    modified: September 19 2022, 1120 PM
  files:
    path: bakery_time_while_patterns_code_double_down
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `double_down` that consumes a positive integer `n` and produces an integer representing the number of times that `n` can be divided by `2` using integer division (`//`) until `1` is produced.

So, for instance, the integer `10` would produce `3`, since it can be divided three times like so:

```
10
5
2
1
```