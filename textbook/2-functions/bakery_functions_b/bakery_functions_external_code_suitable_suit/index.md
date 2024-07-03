---
waltz:
  title: bakery_functions_external_code_suitable_suit
  display title: 2B4.2) Suitable Suit
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
    version downloaded: 180
    created: August 18 2022, 0301 PM
    modified: September 11 2022, 0814 PM
  files:
    path: bakery_functions_external_code_suitable_suit
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The `random` module has useful functions for generating random data. One of its functions is named `choice`, which consumes a string and produces a single randomly-chosen character from the string.

Define a function named `choose_suit` that consumes an integer (indicating the rank, or number, of a card) and produces a string representing a card by putting a randomly chosen suit symbol (`'♦♠♣♥'`) after the number. So for example, the argument `5` might produce the string `"5♣"` or the string `"5♥"`.

Unit testing functions that use random data is difficult, so instead just print the result of calling `choose_suit` four times and inspect the output visually.

**Hint**: In case it is not clear, `'♦♠♣♥'` is a valid string literal that you can pass to the `choice` function!
**Hint 2**: You can convert integers to strings using `str`