---
waltz:
  title: bakery_lab_monster_mash_code_get_party_ratio
  display title: 1) Get Party Ratio
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    hide_files: false
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 45
    created: August 17 2022, 1235 PM
    modified: October 18 2022, 0102 PM
  files:
    path: bakery_lab_monster_mash_code_get_party_ratio
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files:
    - bakery_lab_monster_mash_code_get_party_ratio\monster_mash.py
---
Define a function `get_party_ratio` that consumes a `Party` and calculates the party's ratio by dividing the head count by the capacity of the venue. If the capacity of the event is `0`, then return `0.0` instead.