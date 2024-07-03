---
waltz:
  title: bakery_if_nesting_code_animal_rater
  display title: 3B1.3) Animal Rater
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
    version downloaded: 7
    created: June 28 2022, 0300 PM
    modified: September 09 2022, 0257 PM
  files:
    path: bakery_if_nesting_code_animal_rater
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Create a function named <code>rate_animal</code> that will rate the value of animals on a numeric scale (1-4, where 1 is best and 4 is worst). Your function should consume a variable (holding a string value) named <code>an_animal</code> and return an integer from 1-4 for each of four possible inputs: <code>"dog"</code>, <code>"cat"</code>, <code>"capybara"</code>, and <code>"danger noodle"</code>. Each animal should have its own value. If the string given is not a valid animal from the list, return <code>-1</code>.

Unit test the result, but also use your function to print out your favorite animal's rating. This should be the animal that produces the value 1.