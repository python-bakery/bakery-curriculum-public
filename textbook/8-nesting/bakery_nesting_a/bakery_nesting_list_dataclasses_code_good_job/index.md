---
waltz:
  title: bakery_nesting_list_dataclasses_code_good_job
  display title: 8A1.4) Good Job
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
    version downloaded: 154
    created: September 17 2022, 0427 PM
    modified: October 16 2022, 0445 PM
  files:
    path: bakery_nesting_list_dataclasses_code_good_job
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
The dataclass `Job` is defined below with the fields `title` (str), `salary` (int), `available` (boolean), and `company` (str).

Define a function `best_job` that consumes a list of jobs and returns the `Job` with the highest `salary` that is `available`. If no jobs are available, then return the default `UNEMPLOYED` job instead.

You will need to unit test your code a sufficient number of times.

**HINT**: Define a helper function to filter out the unavailable jobs BEFORE you determine the highest salary `Job`. An `if` statement used as a Defensive Guard will be very effective for returning the appropriate value in the case where there are no available guards. Having two helper functions (one to filter available jobs, and one to determine the highest salary) in addition to the main `best_job` function makes this a lot easier to keep track of everything.