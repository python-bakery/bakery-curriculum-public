---
waltz:
  title: bakery_if_patterns_make_pig_latin
  display title: 3B2.2) Better Pig Latin
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
    version downloaded: 18
    created: September 09 2022, 0922 AM
    modified: September 09 2022, 0941 AM
  files:
    path: bakery_if_patterns_make_pig_latin
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `make_pig_latin` that consumes a word (a string) and converts it to actual pig latin (also a string). If the first letter of the word is a vowel, just return that word with `"ay"` added to the end. Otherwise, take the first character of the word and move it to the end of the string, and *then* add `"ay"` to the end. Do not worry about capitalization. If the empty string is given, return `"ay"`.