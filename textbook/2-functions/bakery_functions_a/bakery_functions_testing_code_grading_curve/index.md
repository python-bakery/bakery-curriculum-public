---
waltz:
  title: bakery_functions_testing_code_grading_curve
  display title: 2A5.4) Grading Curve
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
    version downloaded: 8
    created: June 28 2022, 0300 PM
    modified: September 09 2022, 0251 PM
  files:
    path: bakery_functions_testing_code_grading_curve
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
<p>The formula below calculates a curved grade by applying a square root:</p><pre>curved_grade = original_grade<sup>.5</sup> * 10</pre><p>Define a function named <code>curve_grade</code> that consumes a grade (int) and uses the formula to return the curved grade (float). Write at least three unit tests for the function to confirm that it works.</p>