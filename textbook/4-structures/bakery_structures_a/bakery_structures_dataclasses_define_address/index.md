---
waltz:
  title: bakery_structures_dataclasses_define_address
  display title: 4A1.4) Define Address
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
    version downloaded: 55
    created: August 15 2022, 0952 PM
    modified: September 19 2022, 1253 AM
  files:
    path: bakery_structures_dataclasses_define_address
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
An `Address` is a dataclass with the fields `number` (integer), `street` (string), `city` (string), and `state` (string). Define the dataclass, create an instance representing the address `18 Amstel Ave, Newark, DE`, store the `Address` in the variable `location`, and print the instance's state field.

If you can't tell, the `street` portion is `Amstel Ave`. Do not include the commas in the `street`, `city`, or `state`.

Hint: Print the instance's **state field**. Do not print the entire instance!