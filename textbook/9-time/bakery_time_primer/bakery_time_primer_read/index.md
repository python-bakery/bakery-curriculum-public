---
waltz:
  title: bakery_time_primer_read
  display title: 9) Primer
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: true
  additional settings:
    header: Time and While
    youtube:
      Bart: 9-wR7VDj-qg
      Amy: TgUEHWS1SYY
    summary: ''
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 3
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0622 PM
  files:
    path: bakery_time_primer_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## While Loops

```python while-loop-example
command = input("Type EXIT to stop.")
while command != "EXIT":
    command = input("Type EXIT to stop.")
print("You typed EXIT")
```

We previously learned how `for` loops can iterate through a list of elements, a string, or a file.
Since we always know how long those values are, we can iterate safely in these forms of *finite* iteration.
But what about times when we have to loop an arbitrary number of times?
For example, if we need to repeatedly ask the user to enter input, until the user successfully enters a number and not something invalid.
For this, programmers have the `while` loop, which is a more powerful and therefore more dangerous form of iteration.
It's sort of like an `if` statement, except instead of continuing on to the rest of the program, while the condition is `True` the body will keep repeatedly executing.
Anything that a `for` loop can do, a `while` loop can do too.
However, a `while` loop can do some things that a `for` loop cannot easily do.
Be careful, though, the programmer must be very careful to avoid causing an infinite loop and letting the program run forever!

## While Loop Patterns

* Numeric While
* List While
* Read-Evaluate-Print-Loop
* User Input Loop
* Random Looping
* Main Game/Server Loop

Like `for` loops, we introduce some patterns for `while` loops that can help guide your coding.
However, these patterns are much looser than the patterns we cover with `for` loops, and are less generalizable.
You can think of them as more like examples, or loose guidelines at best.
In general, you should try to first think if a given problem can be solved with a `for` loop before you try to jump to a `for` loop.
You would not immediately leap to a chainsaw when a pair of scissors would do.
But of course, sometimes you need a bit of extra chopping power and a chainsaw becomes needed.
In the same way, when you need a `while` loop, nothing else will suffice.
These patterns can help you see opportunities for using this interesting control structure.

## Time Complexity

* Correct
* Readable
* Fast
* (Pick two out of those three!)

How fast is your program? That is the question that we try to answer by using time complexity.
The second half of this chapter introduces a critical idea about measuring how long a program takes, beyond our previous criteria of being correct and easy to understand.
Three different ways of measuring the length of a program are covered, including the number of lines, the time the program takes according to a watch, and an estimation-approach called the RAM Model of Computation.
We only really scratch the surface of the idea of Time Complexity, but this lays the foundation for a lot of important concepts later on. 

## Sorting and Search

* Sorting: Moving elements of a list into order
* Searching: Finding a specific element of a list
* Binary Search: A massive improvement to iterative search that depends on sorting

A substantial section of this chapter is dedicated to two specific problems: sorting and searching.
These two problems have been seriously studied for many years in Computer Science, and are very well understood.
Furthermore, they have interesting properties that make them very educational for those just starting off.
Searching is a problem we have seen before, where we are trying to find an element in a list.
Previously, we used an iterative search algorithm to check each element.
However, in the worst case, that might require as many checks as there are elements in the list.
A massive improvement can be found by using Binary Search, which repeatedly divides the search space in half, achieving *logarithmic* time complexity.
In order to use Binary Search, however, the list must already be sorted.
Sorting a list means putting the elements in order.
There are many algorithms for sorting a list, although we will only look at a few of them.
You can expect to revisit searching and sorting many more times in the future.