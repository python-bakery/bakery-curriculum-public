---
waltz:
  title: bakery_if_patterns_check_capacity
  display title: 3B2.1) Check Capacity
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
    version downloaded: 26
    created: September 09 2022, 0921 AM
    modified: September 14 2022, 0151 PM
  files:
    path: bakery_if_patterns_check_capacity
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `check_capacity` that consumes two integers and produces a float. The first integer represents the number of people attending an event, and the second integer represents the total number of people who could fit into the event's location (the capacity, or room load). The result should be the number of people attending the event divided by the capacity. If the location cannot fit any people (i.e., it has a capacity of `0`), return `0.0` instead. Note that the function can return more than `1.0` if the event has more people than capacity!