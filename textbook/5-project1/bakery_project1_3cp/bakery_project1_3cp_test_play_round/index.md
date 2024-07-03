---
waltz:
  title: bakery_project1_3cp_test_play_round
  display title: 5.9) Testing play_round()
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    disable_student_run: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 79
    created: August 26 2022, 0239 AM
    modified: September 30 2022, 1024 PM
  files:
    path: bakery_project1_3cp_test_play_round
    hidden but accessible files: []
    instructor only files:
    - bakery_project1_3cp_test_play_round\poker.py
    - bakery_project1_3cp_test_play_round\answer_suffix.py
    - bakery_project1_3cp_test_play_round\answer_prefix.py
    extra starting files: []
    read-only files: []
---
Write a **play_round()** function as described in the 3-card poker assignment. Tests will be applied.

All the required functions except for **play_round()** have been implemented in the "poker" library that has been imported in the first line of the starter code. Do not change that line. You must call those functions: do not attempt to "re-implement" any of them in this submission.

**play_round()** is "in charge" of actually playing the game. It just needs to report how many points were won (or lost, if negative).

We recommend you write this function in Thonny. We will not run the code you write here in BlockPy, except to test that it works correctly.