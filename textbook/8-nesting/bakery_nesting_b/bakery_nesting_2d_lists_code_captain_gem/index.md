---
waltz:
  title: bakery_nesting_2d_lists_code_captain_gem
  display title: 8B1.3) Captain Sails Again!
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
    version downloaded: 141
    created: September 19 2022, 0338 PM
    modified: October 18 2022, 1145 AM
  files:
    path: bakery_nesting_2d_lists_code_captain_gem
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The dread pirate **Captain the Cat** is once again sailing the seas looking for treasure. The seas are, of course, a 2D list of strings where each string is one character long (mostly just `"🌊"` emoji). However, one of the elements will be a `"💎"` character, representing the treasure that Captain is looking for.

First, define a dataclass `Position` with the fields `x` (`int`) and `y` (`int`).

Then, define a function `find_gem` that consumes a 2D list of strings and produces a `Position` representing the x/y coordinate of the treasure character. Remember, the outer list is the `y` coordinate and the inner lists represent the `x` coordinate! You can trust that there is only one treasure per 2D list, and if the treasure is not found then just return the origin (`0, 0`) position.