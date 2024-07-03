---
waltz:
  title: bakery_if_patterns_read
  display title: 3B2) Logical Patterns Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    small_layout: true
    header: Logical Patterns
    youtube:
      Bart: 3R6qVpSpxEE
      Amy: 1PHKlrb6Swo
    slides: bakery_if_patterns.pdf
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 6
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0113 AM
  files:
    path: bakery_if_patterns_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Logical Patterns

* And vs Nested If
* Defensive Guard
* Early Return
* Multiple Return Spots
* Build-Up-Return
* Define-and-Refine

Since `if` statements are so useful, they can actually be a little overwhelming when you get started.
This section gives some examples of patterns that can help guide your thinking about using `if` statements in different ways.
They are not exhaustive, since there are many ways to leverage and twist conditionals.
But if you treat them as ideas, you may find that they inspire you in different directions.

## And vs Nested If

```python
if __A__ and __B__:
    # ...

# Is the same as...

if __A__:
    if __B__:
        # ...
```

An `if` statement nested inside of an `if` statement is equivalent to having both conditions combined with an `and` statement.
The advantage of an `and` expression is usually brevity, since the code will only take up a single line without an extra indentation.
The advantage of the nested `if` statement, however, is a little more nuanced.
Statements can be added before or after the inner `if` statement, allowing more statements for the first case but not necessarily for the second.
You can specify also additional cases' behavior by adding in `else` statements to the inner `if` statements, if you need to narrow the behavior further in the case where the first condition is true and the second condition is false. 

## Defensive Guard

```python defensive-guard
# Guard against division by zero
if time > 0:
    speed = distance / time

# Guard against bad conversion
if user_input.isdigits():
    age = int(user_input)
```

There are operations and functions which are valid syntactically but will cause an error in practice.
A classic example is division by zero, which causes a `ZeroDivisionError`.
Using an `if` statement, you can make sure that a variable such as time is greater than zero, and therefore safe to use for the denominator.
As another example, you can use the `isdigits` method of strings, to make sure that the string is all numbers before you try to convert it to a `float` or an `integer.
Other common checks include checking the length of the string, before you index.

## Early Return

```python
# Early Return
def ___(___):
    if ___:
        return ___
    # do something ...
    return ___
```

The Early Return pattern is similar to the Defensive Guard pattern, with an `if` statement aborting a path before an error can be caused or other undesirable operation.

## Example of Early Return

```python early-return
def get_punctuation(message: str) -> str:
    if not message:
        return "empty string"
    last_character = message[-1]
    if last_character == "?":
        return "question"
    elif last_character == ".":
        return "statement"
    return "other"
```

In the example shown here, we check if the `message` parameter does not have a truthy value. For a string, any non-empty string will be considered Truthy.
In this case, then, indexing is only attempted if the `message` is not empty.
This is very important, since indexing the last character of the string will cause an `IndexError` if the empty string was indexed.
The early return prevents that mistake from occurring, allowing us to safely use the logic in the rest of the function to determine what kind of punctuation symbol the last character of the string holds.

## Multiple Return Spots

```python
def ___(___):
    if ___:
        return ___
    elif ___:
        return ___
    # ...
    else:
        return ___
```

Parsing code with multiple returns can be a little tricky. What actually gets returned?
The key insight to remember is that a function can only return exactly once.
That will happen regardless of whether you have a `return` statement.
But if a `return` statement is encountered, the function is over and whatever value is specified in the `return` statement is what is brought back to the original call site.
That's why having more than one `return` statement only makes sense when you have `if` statements.
The `if` statements can disrupt the control flow of the function, branching off different paths for each `return` statement.
For each call to the function, only one path needs to be taken, with only one `return` statement being activated.

## Example of Multiple Return Spots

```python multiple-return-spots
def convert_ordinal(number: int) -> str:
    if number == 1:
        return "first"
    elif number == 2:
        return "second"
    elif number == 3:
        return "third"
    else:
        return "other"
```

In this example, the `convert_ordinal` function consumes an integer and produces a string representation of the ordinal number, such as "first", "second", or "third".
The value stored in `number` is matched against each of the possibilities in turn, but only one can be true since we are using a mutually exclusive chain of `if`/`elif`/`else` statements.
Ultimately, if none of the expressions evaluate to True, then the `else` block is entered and the value `"other"` is returned.

## Build-Up-Return Pattern

```python
def ___(___):
    if ___:
        result = ___
    elif ___:
        result = ___
    # ...
    else:
        result = ___
    return result
```

A related pattern is the Build-Up-Return pattern.
How is this different from the Multiple Return Spots pattern? Functionally, they are equivalent. The value being returned is meant to be the same in either pattern.
The difference comes in the number of `return` statements, and the exact path that the control flow takes through the program.

Some folks try to avoid having multiple return spots in their program, since it is a common source of mistakes in beginner programs.
For those struggling with control flow, it can make a lot of sense to avoid trying to mix the confusing branching of `if` statements with the abrupt finality of `return` statements. The Build-Up-Return Pattern can help you isolate the `return` to a single spot, making it easier to reason about.

## Example of Build-Up-Return Pattern

```python build-up-return
def convert_ordinal(number: int) -> str:
    if number == 1:
        result = "first"
    elif number == 2:
        result = "second"
    elif number == 3:
        result = "third"
    else:
        result = "other"
    return result
```

In the previous `convert_ordinal` pattern, we had `return` statements inside of the `if` statements.
But now, there is only one `return` after all of the conditionals.
Instead, assignment statements are used.
The end result is still the same though.

## Define-and-Refine Pattern

```python
value = ___
if ___:
    if ___:
        value = ___
```

The `else` statement is a powerful way to specify default behavior after `if` and `elif` statements.
But when nesting these statements, the `else` branch is not always conveniently available.
The nested statements represent specific, narrow cases involving multiple conditions.
In order to provide a default situation with `else` statements, every single level of nested `if` would need to have an `else` statement, sometimes leading to redundant code.
However, the Define-and-Refine pattern allows you to specify an initial value for a variable, and then only specify the specific branches to change that value.

## Example of Define-and-Refine Pattern

```python

```