---
waltz:
  title: bakery_sequences_strings_code_make_cards
  display title: 7A1.4) Make Cards
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
    version downloaded: 63
    created: September 09 2022, 1223 PM
    modified: September 09 2022, 0345 PM
  files:
    path: bakery_sequences_strings_code_make_cards
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `make_cards` that consumes a string `suit` (one of `"♦️"`, `"♥"`, `"️♣"`, or `"️♠️"`), and an integer `rank` and produces a list of strings representing cards. For each number starting from `2` and going to `rank` (but not including that number), add a string to the list with the given suit. The format of the strings should be `♦4`. So an example would be:

```python
assert_equal(make_cards("♦", 5), ["♦2", "♦3", "♦4"])
```

**Hint:** The `range` function actually has a two argument version that let's you specify the starting value too: `range(2, 10)` will give you the values from 2 to 10 but not including 10.