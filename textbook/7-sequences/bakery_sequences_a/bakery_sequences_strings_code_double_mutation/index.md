---
waltz:
  title: bakery_sequences_strings_code_double_mutation
  display title: 7A1.2) Double Mutation
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
    version downloaded: 40
    created: September 09 2022, 1222 PM
    modified: September 09 2022, 0146 PM
  files:
    path: bakery_sequences_strings_code_double_mutation
    hidden but accessible files: []
    instructor only files:
    - bakery_sequences_strings_code_double_mutation\correct.py
    extra starting files: []
    read-only files: []
---
The following function doubles every element of the list, but does so using mutation. Notice how this causes the second test of each pair to fail, because the original variable is changed. Modify the function so that `double_elements` no longer mutates the list, but still produces a doubled list.