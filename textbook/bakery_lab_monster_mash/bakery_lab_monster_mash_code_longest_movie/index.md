---
waltz:
  title: bakery_lab_monster_mash_code_longest_movie
  display title: 4) Longest Movie
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
    version downloaded: 20
    created: September 28 2022, 0308 PM
    modified: October 19 2022, 1031 PM
  files:
    path: bakery_lab_monster_mash_code_longest_movie
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files:
    - bakery_lab_monster_mash_code_longest_movie\monster_mash.py
---
Define a function `longest_movie` that consumes a list of `Media` and produces a string representing the `name` of the `Media` of `kind` "movie" with the highest `duration`. If no movies are found, return the string `"no movies"`.