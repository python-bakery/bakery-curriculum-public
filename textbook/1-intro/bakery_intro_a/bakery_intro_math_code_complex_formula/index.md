---
waltz:
  title: bakery_intro_math_code_complex_formula
  display title: 1A6.2) Complex Formula
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
    version downloaded: 383
    created: June 28 2022, 0300 PM
    modified: September 02 2022, 1102 AM
  files:
    path: bakery_intro_math_code_complex_formula
    hidden but accessible files: []
    instructor only files:
    - bakery_intro_math_code_complex_formula\correct.py
    extra starting files: []
    read-only files: []
---
For this problem, you will encode the logic of the Quadratic Formula as Python math expressions. If you don't recall, the quadratic formula helps you determine the x coordinates where a parabola crosses over the y-axis, as shown visually in [this image](https://i.imgur.com/kqOVSC8.png) (The red dots are the x coordinates where the red line crosses over the axis).

<img src="https://i.imgur.com/zQdtR5n.png" width="200px"/>

Because of the plus/minus operator in the formula, you will need to calculate the formula twice: once where you subtract and once where you add. In both cases, encode the formula as shown, substitute `a`, `b`, and `c` for the appropriate values, and `print` the final result.

The values to substitute for the variables are:
* `a = 2`
* `b = 4`
* `c = -6`

Hint: You can do square roots by using a fractional exponent (e.g., `4 ** .5` is the square root of `4`).