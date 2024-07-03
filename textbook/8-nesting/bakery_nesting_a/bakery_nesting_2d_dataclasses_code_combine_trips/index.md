---
waltz:
  title: bakery_nesting_2d_dataclasses_code_combine_trips
  display title: 8A2.3) Combine Trips
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
    version downloaded: 95
    created: September 19 2022, 0207 PM
    modified: September 19 2022, 0259 PM
  files:
    path: bakery_nesting_2d_dataclasses_code_combine_trips
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a dataclass `Location` that has two fields: `city` (`str`) and `state` (`str`).

Define a dataclass `Trip` that has three fields: `origin` (`Location`), `target` (`Location`), and `duration` (`int`). The `duration` field represents how long the `Trip` takes in minutes, while the `origin` and `target` are the beginning and ending locations of the Trip.

Then, define a function `combine_trips` that consumes **two** `Trip` instances and produces one new `Trip`. The new trip will have the `origin` of the first `Trip` parameter and the `target` of the second `Trip` parameter. Its `duration` will be the sum of the two `Trip` parameter's `duration`s.