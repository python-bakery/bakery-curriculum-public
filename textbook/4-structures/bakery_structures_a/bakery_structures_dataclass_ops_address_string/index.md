---
waltz:
  title: bakery_structures_dataclass_ops_address_string
  display title: 4A2.2) Address as String
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    start_view: text
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 71
    created: August 15 2022, 0832 PM
    modified: August 28 2022, 0235 PM
  files:
    path: bakery_structures_dataclass_ops_address_string
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The function `address_to_string` consumes an `Address` and produces a string representation of its fields.

An `Address` has a `number` (integer), `street` (string), `city` (string), and `state` (string).

The string representation should combine the `number` and `street` with a space, the `city` and `state` with a comma and a space, and then a newline between those two parts.

So the `Address(18, "Amstel Ave", "Newark", "DE")` would become `"18 Amstel Ave\nNewark, DE"`