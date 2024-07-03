---
waltz:
  title: bakery_advanced_plotting_code_running_sum
  display title: 11A1.4) Plotting a Running Sum
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
    version downloaded: 61
    created: November 13 2022, 0656 PM
    modified: November 13 2022, 1003 PM
  files:
    path: bakery_advanced_plotting_code_running_sum
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files:
    - bakery_advanced_plotting_code_running_sum\scores.txt
---
The file `scores.txt` contains a series of scores from someone's attempt at an activity over time. Plot the scores as a *running sum* line plot.

In a running sum line plot, rather than plotting the values directly, you plot the *sum* of the points over time. You can achieve this by combining the Sum pattern with the Map pattern: each iteration, you calculate the current sum and append that value to the list.

Title the graph `"Score over Time"`, label the X-axis as `"Time"`, and the Y-axis as `"Score"`.

Note that you will also need to open the file, process it line-by-line, and convert each value to an integer using the `int` function.

You'll know if the plot is correct if it's a nice wavy line that slowly increases over time. If it is a jagged, spiky line, then you are probably plotting the values directly instead of the running sum!