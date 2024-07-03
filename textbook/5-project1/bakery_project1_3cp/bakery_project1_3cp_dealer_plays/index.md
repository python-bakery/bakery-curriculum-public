---
waltz:
  title: bakery_project1_3cp_dealer_plays
  display title: 5.8) dealer_plays
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    start_view: text
  forked:
    id: 687
    version: 72
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 51
    created: October 11 2021, 0256 PM
    modified: September 28 2022, 1031 AM
  files:
    path: bakery_project1_3cp_dealer_plays
    hidden but accessible files:
    - bakery_project1_3cp_dealer_plays\score_hand.py
    - bakery_project1_3cp_dealer_plays\score.py
    - bakery_project1_3cp_dealer_plays\hands.py
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function **dealer_plays** that accepts a list of three integers as described in the 3-card poker assignment, and returns `True` if and only if the hand has a queen high or better (i.e., the hand has a "feature" or highest card is at least a queen).

You may assume that the function **score_hand()** has already been defined. Use it!

Define at least three **assert_equal** tests for your function.