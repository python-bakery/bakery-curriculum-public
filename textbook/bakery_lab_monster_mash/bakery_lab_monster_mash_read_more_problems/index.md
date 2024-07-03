---
waltz:
  title: bakery_lab_monster_mash_read_more_problems
  display title: 7) Additional Problems
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 3
    created: October 12 2022, 0301 PM
    modified: October 13 2022, 0144 PM
  files:
    path: bakery_lab_monster_mash_read_more_problems
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The following problems are strictly *optional*. Doing them will not affect your grade.

* Define a function `spookiest_undead` that consumes a List of `Monster` and produces the name of the `Monster` that `is_undead` and has the highest `spookiness`.
* Define a function `turn_undead` that consumes a List of `Monster` and produces a new list of `Monster` where all the `is_undead` fields are set to `False` and the `spookiness` is set to `1`.
* Define a function `total_songs` that consumes a list of `Media` and produces the sum of the `duration` of the `"song"` `kind`.
* Define a function `average_duration` that consumes a list of `Media` and produces the average `duration` of all `Media`.
* Define a function `list_options` that consumes a list of `Potion` and produces a single string that joins together the `label` of each of the potions with commas.
* Define a function `total_rare_brew_time` that consumes a list of `Potion` and produces the sum of all the `time_required` to brew each `Potion`, but only if the `Potion` has an ingredient that `is_rare`.
* Define a function `get_potion_counts` that consumes a list of `Potion` and produces a list of integers representing the number of ingredients in each `Potion`.
* Define a function `get_ingredient_matrix` that consumes a list of `Potion` and produces a 2D-list of all the potions' ingredients' names.
* Define a function `vip_ratio` that consumes a `MonsterMash` (!!) and produces a float by dividing the number of `Monster` in the `monsters` list (the VIP monsters) by the number of monsters attending (the `head_count` in the `party` field).
* Define a function `plan_potions` that consumes a `MonsterMash` and produces a list of integers representing the total amount of time that each `Potion` will take to brew, multiplied by the number of monsters attending in the `head_count`. If there are no `"movie"` `kind` of `Media` at the party, though, then you should double that number since they will have less to do.