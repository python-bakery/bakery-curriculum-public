---
waltz:
  title: bakery_nesting_2d_lists_code_render_lights
  display title: 8B1.2) Render Lights
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
    version downloaded: 77
    created: September 19 2022, 0338 PM
    modified: September 19 2022, 0404 PM
  files:
    path: bakery_nesting_2d_lists_code_render_lights
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Define a function `render_lights` that consumes a list of list of booleans and produces a single string. The 2D list of booleans represents a grid of lights that are either on (`True`) or off (`False`). You resulting string is going to be a sequence of two possible emoji (`"⬛"` or `"💡"`), with each new row of the characters being separated by a newline. So for example:

```python
[ [ False, False, True, False],
  [ False, True, True, False],
  [ False, True, True, True] ]
```

Would become `"⬛⬛💡⬛\n⬛💡💡⬛\n⬛💡💡💡\n"`.

**Hint:** This is actually a fairly straightforward application of the Nested Accumulate pattern that was demonstrated in this chapter, only instead of adding numbers we are adding strings based on boolean values.