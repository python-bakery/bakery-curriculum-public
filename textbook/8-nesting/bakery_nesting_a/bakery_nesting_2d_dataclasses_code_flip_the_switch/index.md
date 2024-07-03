---
waltz:
  title: bakery_nesting_2d_dataclasses_code_flip_the_switch
  display title: 8A2.2) Flip the Switch
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
    version downloaded: 151
    created: September 19 2022, 0207 PM
    modified: September 19 2022, 0237 PM
  files:
    path: bakery_nesting_2d_dataclasses_code_flip_the_switch
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a dataclass `LightBulb` that has two fields: `status` (`bool`) and `color` (`str`).

Define a dataclass `Lamp` that has three fields: `light` (`LightBulb`), `material` (`str`), and `weight` (`float`).

Then, define a function `hit_switch` that consumes a `Lamp` and produces a `Lamp`. The new `Lamp` should have all the same fields as the original `Lamp`, except the `status` field should be negated (`True` becomes `False`, and `False` becomes `True`).