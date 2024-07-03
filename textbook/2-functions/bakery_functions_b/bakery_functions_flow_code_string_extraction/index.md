---
waltz:
  title: bakery_functions_flow_code_string_extraction
  display title: 2B3.3) String Extraction
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
    version downloaded: 10
    created: June 28 2022, 0300 PM
    modified: September 09 2022, 0254 PM
  files:
    path: bakery_functions_flow_code_string_extraction
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
<p>
The function below (<code>find_halfway</code>) calculates the middle index of
a string by using the <code>len</code> built-in function to calculate the length of 
the string, halving that length, and then converting the result to an integer
(recall that division results in a float).
</p>
<p>
Define a new function named <code>chop_half</code> (which consumes a string 
and produces the first half of the string) that uses <code>find_halfway</code>
to pass the unit tests.
</p>