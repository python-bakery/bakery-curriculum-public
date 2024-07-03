---
waltz:
  title: bakery_nesting_list_dataclasses_code_wish_for_wings
  display title: 8A1.3) Wish for Wings
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
    version downloaded: 119
    created: September 17 2022, 0427 PM
    modified: October 16 2022, 0445 PM
  files:
    path: bakery_nesting_list_dataclasses_code_wish_for_wings
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define the dataclass `Bird` with the fields `name` (str), `can_fly` (bool), and `region` (str). Some example birds are provided below.

Then, define the function `first_land_bird` that consumes a list of `Bird` and produces the `name` of the first `Bird` in the list that cannot fly. If there are no birds that cannot fly, then return `"Flew the coop"` instead.