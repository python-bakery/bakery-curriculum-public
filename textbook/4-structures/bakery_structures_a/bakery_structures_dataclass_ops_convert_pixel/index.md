---
waltz:
  title: bakery_structures_dataclass_ops_convert_pixel
  display title: 4A2.4) Convert Pixels
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
    version downloaded: 52
    created: August 15 2022, 0833 PM
    modified: August 28 2022, 0235 PM
  files:
    path: bakery_structures_dataclass_ops_convert_pixel
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `make_pixel` that consumes a string (representing one of four possible colors) and produces a `Pixel`.

A `Pixel` is a dataclass with three float fields: `red`, `green`, and `blue`. These float will go from `0.0` (dark) to `1.0` (light).

The four possible colors are `"yellow"` (full red and green, zero blue), `"cyan"` (full green and blue, zero red), `"magenta"` (full red and blue, zero green), or `"black"` (zero red, green, and blue). Any other string should produce the a Pixel with all fields set to `1` (aka, white).