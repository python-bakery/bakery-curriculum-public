---
waltz:
  title: bakery_nesting_2d_dataclasses_code_event_difference
  display title: 8A2.1) A Different Event
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
    version downloaded: 77
    created: September 19 2022, 0207 PM
    modified: September 19 2022, 0216 PM
  files:
    path: bakery_nesting_2d_dataclasses_code_event_difference
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The `Time` dataclass has two fields: `hour` (int, from `0` to `23`) and `minute` (int, from `0` to `60`). This represents a specific time in a day.

The `Event` dataclass has three fields: `name` (`str`), `start` (`Time`), and `stop` (`Time`). This represents a specific Event. The `start` and `stop` times are considered to be the same day.

Define a function `event_duration` that consumes an `Event` and produces an `int` representing how long the event is in minutes, by subtracting appropriate fields of the `start` time from the `stop` time. For example, if the start time was `Time(4, 30)` and the end time was `Time(12, 15)` then the result would be `465`.

**Hint**: You will need to convert the hours to minutes. There are 60 minutes in an hour.