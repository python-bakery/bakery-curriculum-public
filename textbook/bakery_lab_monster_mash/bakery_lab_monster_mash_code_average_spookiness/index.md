---
waltz:
  title: bakery_lab_monster_mash_code_average_spookiness
  display title: 2) Average Spookiness
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
    version downloaded: 21
    created: September 28 2022, 0308 PM
    modified: October 18 2022, 0102 PM
  files:
    path: bakery_lab_monster_mash_code_average_spookiness
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files:
    - bakery_lab_monster_mash_code_average_spookiness\monster_mash.py
---
Define a function `average_spookiness` that consumes a `list[Monster]` and produces a float by calculating the average spookiness. The average spookiness is calculated by dividing the total spookiness of the given monsters by the number of monsters. If there are no monsters, then return `0.0` instead.