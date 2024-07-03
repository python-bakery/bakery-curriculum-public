---
waltz:
  title: bakery_project1_3cp_hand_to_string
  display title: 5.2) hand_to_string
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    start_view: text
    disable_tifa: true
  forked:
    id: 684
    version: 30
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 132
    created: October 06 2021, 1020 PM
    modified: September 28 2022, 1024 AM
  files:
    path: bakery_project1_3cp_hand_to_string
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function **hand_to_string** that accepts a list of three integers as described in the 3-card poker assignment, and returns a string suitable for showing the hand to the player.

The string should have the cards on the same line with one space between them and no spaces on either side. Values 2-9 may be displayed as usual. Values 10-14 should be displayed as X, J, Q, K, A, respectively.

Define at least three **assert_equal** tests for your function.

**Hint**: Define a helper function (e.g., `convert_hand`) that converts a single integer to the appropriate string. Then you can use that function three times!