---
waltz:
  title: bakery_structures_dataclass_ops_dark_pixels
  display title: 4A2.3) Dark Pixels
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
    version downloaded: 57
    created: August 15 2022, 0833 PM
    modified: August 28 2022, 0235 PM
  files:
    path: bakery_structures_dataclass_ops_dark_pixels
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `is_dark` that consumes a `Pixel` and returns a boolean indicating whether or not the `Pixel` is dark.

A `Pixel` is a dataclass with three float fields: `red`, `green`, and `blue`. These float will go from `0.0` (dark) to `1.0` (light).

To determine if a pixel is dark, calculate the average of the three fields and test if the result is less than or equal to `0.5`.