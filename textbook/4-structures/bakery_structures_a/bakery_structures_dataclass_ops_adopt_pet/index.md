---
waltz:
  title: bakery_structures_dataclass_ops_adopt_pet
  display title: 4A2.9) Adopt Pet
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
    version downloaded: 77
    created: August 15 2022, 0834 PM
    modified: August 28 2022, 0235 PM
  files:
    path: bakery_structures_dataclass_ops_adopt_pet
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `adopt` that consumes a `Person`, a first name (string), and a kind of pet (string), and produces a new `Pet` that has the appropriate information.

A `Person` has the fields `first_name` (string), `last_name` (string). A `Pet` has the fields `first_name`, `last_name`, and `kind` (string).

The `Pet` returned by `adopt` should use the `last_name` of the given `Person`, but its `first_name` should come from the parameter instead of the `Person`'s first name.