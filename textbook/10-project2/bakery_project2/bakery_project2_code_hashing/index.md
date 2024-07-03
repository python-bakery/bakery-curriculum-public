---
waltz:
  title: bakery_project2_code_hashing
  display title: 6) hash_text
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
    version downloaded: 16
    created: October 12 2022, 0334 PM
    modified: October 13 2022, 1227 PM
  files:
    path: bakery_project2_code_hashing
    hidden but accessible files: []
    instructor only files:
    - bakery_project2_code_hashing\solutions.json
    - bakery_project2_code_hashing\correct.py
    extra starting files: []
    read-only files: []
---
The `hash_text` function will consume a string (any kind of `message`) and two integers (`base` and `hash_size`), and produces an integer that attempts to uniquely represent the text.

  1. Convert the string to a list of integers using `ord`.
  2. Transform each integer of the list using the following formula: `new value = (index + base) ** (old value)`. Hint: to get the index, you can use the Count pattern or the built-in `enumerate` function.
  3. Sum the list of integers.
  4. Use the modulo operator (`%`) to limit the total value to `hash_size`.