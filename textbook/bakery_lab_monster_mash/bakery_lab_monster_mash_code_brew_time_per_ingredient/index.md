---
waltz:
  title: bakery_lab_monster_mash_code_brew_time_per_ingredient
  display title: 5) Brew Time per Ingredient
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
    modified: October 18 2022, 0103 PM
  files:
    path: bakery_lab_monster_mash_code_brew_time_per_ingredient
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files:
    - bakery_lab_monster_mash_code_brew_time_per_ingredient\monster_mash.py
---
Define a function `brew_time_per_ingredient` that consumes a list of `Potion` and produces a float representing the average amount of time spent brewing overall. To do so, add up the time spent brewing for all the potions and then divide it by the total number of ingredients. If there are no ingredients, return the value `0.0`.