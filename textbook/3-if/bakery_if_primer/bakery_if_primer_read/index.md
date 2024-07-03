---
waltz:
  title: bakery_if_primer_read
  display title: 3) Primer
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: true
  additional settings:
    small_layout: true
    header: Chapter 3 Primer) If Statements
    slides: bakery_if_primer.pdf
    youtube:
      Bart: e3QvIptVyiE
      Amy: Kl0_2cXcZLc
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 6
    created: June 28 2022, 0300 PM
    modified: September 04 2022, 1003 PM
  files:
    path: bakery_if_primer_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Introduction to `if` statements

* `if` statement: a body of code that is executed based on a condition

Almost as fundamental to programming as the function, `if` statements let us make our programs smarter. They let code do different things based a conditional expression.
In this chapter, we go into the many ways that `if` statements can be used to control the flow of the program.
We see not only `if` statements, but also the similar `elif` and `else` statements, which can only be used in conjunction with `if` statements.
Since these statements all have bodies, and are compatible with functions, we spend a lot of time talking about how they can be combined together in different ways.
The chapter also introduces a sophisticated nuance of conditionals called Truthiness, which let's us use any type (not just booleans) as if they were boolean values.
Finally, the chapter also touches briefly on the related, advanced concept of "Event Handling", specifically in Designer, and how it relates to the idea of `if` statements.

## `if` Statements

```python example-if
speed_limit = 50
weather = 'sunny'

if weather == 'rainy':
    print("It is raining!")
    speed_limit = speed_limit - 20
else:
    print("Nice day outside!")

print("Speed limit is:", speed_limit)
```

The first section of the chapter is all about the syntax and usage of `if` statements. The two essential parts are the conditional (which is the expression after the `if` keyword) and the body.
The conditional expression is meant to be a question that determines whether the body will be executed, or skipped.
The body of an `if` statement is very similar to the body of a function, except they do not have their own scope; they use the same scope as the enclosing body.
An `if` statement can also have an `else` statement afterwards, which has its own body.
Should the conditional of an `if` statement evaluate to `False`, then the `else` body will be executed instead.
A key insight of the `if` statement is that it let's us skip over some lines, depending on the values of the variables at that step; we call this behavior "branching" execution, and it makes tracing the program much more complex.

## Truthiness

```python example-truthiness
message = "Hello!"

# Test if `message` is not the empty string
if message:
    punctuation = message[-1]
else:
    punctuation = "No punctuation symbol"

print(punctuation)
```

The second section of the chapter is about a curious idea called Truthiness.
Conceptually, the conditional of an `if` statement is supposed to be a boolean value, like the result of using the equality operator or greater than operators.
However, in Python (and many other modern languages), you can use any type of value in a conditional.
When you do, Python applies the rules of Truthiness to determine if the value should be treated as `True` or `False`.
Most values are considered true, with the exception of the empty string, the integer 0, the float 0.0, and the special value `None`.
All other values will be considered `True`, allowing us to write convenient shorthand when we want to test if a variable or expression is not one of those values.
Note that the value does not actually change to become `True` or `False`, this is merely about what Python considers in its mind.

## Nested `if` Statements

```python example-nested-if
from bakery import assert_equal

def count_sides(shape: str) -> int:
    if shape == 'triangle':
        return 3
    elif shape == 'rectangle':
        return 4
    elif shape == 'circle':
        return 1
    else:
        return 0

assert_equal(count_sides('triangle'), 3)
assert_equal(count_sides('circle'), 1)
assert_equal(count_sides('octogon'), 0)
```

This section covers how `if` statements can be combined together with functions and even other `if` statements to make much more complex programs.
The indentation rules for the bodies of these statements are consistent, but can still be tricky to follow.
The control flow is also a little bit tricky, since suddenly you can have more than one `return` statement inside of a function, because lines are able to be skipped based on different conditions.
This section also introduces the `elif` statement, which can appear any number of times after an `if` statement (but must always be before the `else` statement, if there is one).
The `elif` statement allows you to specify bodies that should be executed when the `if` statement (and any previous `elif` statements) are skipped.
Only one `if`/`elif`/`else` body will be executed in a chain.
The section also covers some ways that `if` statements are misused, such as in functions that return boolean values, or when programmers unnecessarily test for the equality of a boolean value.

## Logical Patterns

* And vs Nested If
* Defensive Guard
* Early Return
* Multiple Return Spots
* Build-Up-Return
* Define-and-Refine

To help see the different ways that `if` statements can be used, the penultimate section covers a list of "Logical Patterns" that provide templates of code to you, the programmer. The idea for each pattern is to fill in the blanks of the template, modifying the structure as needed.
There are six patterns covered in this section.
They can be somewhat narrow in their use, and are more like guidelines than strict suggestions, but should help give more examples of how code can be structured.

## Event Handling

```python example-events
from designer import *

set_window_size(200, 200)

# Function to spin the given dragon
def spin(dragon: emoji):
    turn_right(dragon, 22)

# Click the mouse to spin the dragon
when('clicking', spin)

# Begin the game
start(emoji("dragon"))
```

The final section goes into a somewhat specialized topic of event handling in Designer.
We have previously used Designer to generate simple graphics by calling functions.
However, event handling allows us to make more sophisticated programs that have user input, by binding functions to events using the `when` function of Designer.
When these events occur, like clicking the mouse or typing on the keyboard, the bound function will be executed.
In this way, the `when` function ends up being a little similar to the `if` statement.
However, the `when` function is a lot less flexible and meant strictly for event binding in Designer, and has no existence or purpose outside of that.