---
waltz:
  title: bakery_lab_monster_mash_code_get_rarest_potion
  display title: 6) Get Rarest Potion
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
    version downloaded: 19
    created: September 28 2022, 0308 PM
    modified: October 18 2022, 0103 PM
  files:
    path: bakery_lab_monster_mash_code_get_rarest_potion
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files:
    - bakery_lab_monster_mash_code_get_rarest_potion\monster_mash.py
---
Define the function `get_rarest_potion` that consumes a list of `Potion` and returns the `label` of the `Potion` that requires the most `is_rare` ingredients. If there are no rare ingredients in any of the potions, then return `"N/A"` instead.