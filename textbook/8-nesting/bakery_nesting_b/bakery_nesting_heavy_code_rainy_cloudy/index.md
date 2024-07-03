---
waltz:
  title: bakery_nesting_heavy_code_rainy_cloudy
  display title: 8B2.2) Rainy, Cloudy Days
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
    version downloaded: 31
    created: September 19 2022, 0500 PM
    modified: September 19 2022, 0541 PM
  files:
    path: bakery_nesting_heavy_code_rainy_cloudy
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Copy over the dataclasses you defined in the previous problem. Then, define the function `rainiest_cloudy` that consumes a list of `Forecast` and produces a boolean representing whether or not the day with the *most* rainfall was `cloudy`.

If there were no days in any reports, then just return `False`.

**Hint:** Write a helper function that consumes a list of `Forecast`s and returns a list of `Report`s by using the Map pattern appropriately.