---
waltz:
  title: bakery_nesting_heavy_code_total_rainfall
  display title: 8B2.1) Total Rainfall
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
    version downloaded: 132
    created: September 19 2022, 0500 PM
    modified: October 17 2022, 0423 PM
  files:
    path: bakery_nesting_heavy_code_total_rainfall
    hidden but accessible files:
    - bakery_nesting_heavy_code_total_rainfall\images.blockpy
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The following diagram is meant to model the dataclasses `Forecast`, `Report`, `Measurement`, and `WeatherOptions`. Define each dataclass based on the diagram.

![Forecast, Report, WeatherOptions, Measurement UML diagram](https://i.imgur.com/erKteB0.png)

Then, define a function `total_rainfall` that consumes a list of `Forecast` and produces an integer representing the total `amount` of `rainfall` over all the `reports` in each provided `Forecast`. 