---
waltz:
  title: bakery_if_truthiness_read
  display title: 3A2) Truthiness Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Truthiness
    slides: bakery_if_truthiness.pdf
    youtube:
      Bart: fxVqHpsKY0o
      Amy: 2jUOideXVKc
    summary: In this lesson, you will learn about how any expression can be used in
      an If statement's conditional expression, in an idea called Truthiness.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0110 AM
  files:
    path: bakery_if_truthiness_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## What is Truthiness

* Truthiness: The ability to use any type of value as a conditional, not just booleans

Unlike some languages, Python does not require that `if` statements have boolean expressions in their conditional.
This may seem surprising, but it is actually an extremely convenient feature named Truthiness.
The idea is that any expression, whether it is an integer, string, boolean, or otherwise, can be evaluated in a conditional.

## Type Truthiness

![A table of the Truthiness values for each type.](bakery_if_truthiness_table.png)

Any expression can be evaluated as a conditional according to the rules of Truthiness.
How it is evaluated depends on its type.
For integers and floats, any non-zero value is considered True.
For strings, any non-empty string is considered True.
The None type has no true values.

## String Example

```python truthy-string
name = input("What is your name?")
# `name` is a string variable
if name:
    # This path if `name` is NOT the empty string
    print("Your name is", name)
else:
    # This path if `name` is empty string
    print("No name given.")
```

Let's look at a simple example, where we take some input from a user.
If the user entered an empty string, then we'll print out a different message.

## Unnecessary Comparisons

```python
if a_string != "":
    ...
# Simplifies to
if a_string:
    ...
#-----------------------
if a_number != 0:
    ...
# Simplifies to
if a_number:
    ...
```

When you need to check if a string is not empty, or a number is not 0, truthiness is the way to go.
Notice how each of the following can become much more concise and clear.

## Accidental Truthiness

```python accidental-truthiness
alpha = 5

if alpha == 3 or 4:
    print("This WILL be printed!")
```

One of the reasons why understanding Truthiness is so important is that it opens up an entire new set of mistakes.
The example program shown here demonstrates the mistake.
If you read over the code out loud, you would probably expect the condition to evaluate to False and the `print` statement to not be executed.
The variable `alpha` holds the value `5`, which is not equal to `3` or `4`.
However, you may recall that the `or` operator has a lower priority than the `==` operator.
Python will first evaluate the equality test between the variable `alpha` and the value `3`, which will result in `False`.
Since the operator is `or`, we next evaluate its right-hand operand, so Python will evaluate the value `4` on its own, and use that value as the result of the conditional expression.
Since `4` is a non-zero value, the entire expression evaluates to True, thanks to the rules of Truthiness.
When evaluating expressions, you must keep track of whether Truthiness was accidentally involved.