---
waltz:
  title: bakery_lecture_debugging_loops_instructions
  display title: 1) Instructions
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 11
    created: August 17 2022, 1227 PM
    modified: September 24 2022, 0240 PM
  files:
    path: bakery_lecture_debugging_loops_instructions
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
# Biggest Bed in the Flower Garden

There are two coding problems in this assignment, both of which are trying to solve the same problem: to define a function `biggest_bed` that consumes a string (representing a garden) and producing a string representing the biggest bed of flowers in that string. You can see an example garden below. Notice how garden is a single string with commas separating flowers of the same kind. Each group of flowers is a *bed*, and the goal of our function is to find the biggest (longest) bed. You can assume that all flowers in the bed are of the same type.

```python
# Example garden
"🌹🌹,🌷🌷,🌼🌼🌼,🌱🌱🌱🌱🌱,🌳,🌸,🌺🌺🌺🌺,🌻🌻🌻"
```

There are two extra difficulties to this function:

1) We need to ignore any beds that have seedlings (`"🌱"`), since those are not yet fully grown.
2) We need to stop looking at any beds once we encounter a tree (`"🌳"`), since that marks the edge of our property.

In the example above, the answer *would* be `"🌺🌺🌺🌺"`, were it not for these rules. Instead, the answer would become `"🌼🌼🌼"` since we ignore the row of seedlings and ignore everything past the tree.

## The Two Versions

The two coding problems already have a substantial amount of code and test cases provided for you.
Unfortunately, each one has four small bugs.
The bugs are all minor typos, and isolated to their own line. We might have changed a value, or deleted part of an expression, or moved variables around in a statement.
The bugs are not the same between the two programs, because the programs solve the problem in two very different ways:

* The first version is *decomposed*, so there are a bunch of helper functions that try to tackle each part of the overall problem.
* The second version is *monolithic*, so there is only one function with a single big loop inside.

The test cases are all correct. Do not modify the test cases. The instructor test cases will be the same as the test cases we give you, so modifying them won't help you!

## Working Together

In this assignment, you will be making an individual submission.
However, you should choose a partner to discuss ideas with.
Both of you will submit your own version, but you are expected to solve the problems together.

## Bouncing Around

You are free to work on either the first or the second coding problem, in whatever order you want.
You might take a look at both, and tackle the one that you think is easier.
We might also suggest that one version is easier than the other...

You may choose to work in Thonny instead, although be careful copying and pasting the flowers!

## Final Submission

Once one partner has finished, make sure that both partners submit in their own version of the assignment to get the points.

## If You Missed This Activity...

If you missed this activity, then fill out the [**Class Absence Form**](https://udel.instructure.com/courses/1664471/pages/syllabus#class-absence-form) and attend office hours to makeup the points.