---
waltz:
  title: bakery_for_patterns2_read
  display title: 6B1) For Loop Patterns 2 Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: More Loop Patterns
    slides: bakery_for_patterns2.pdf
    youtube:
      Bart: r6JWfmmdMb8
      Amy: rNZP9cZ3ih8
    sumary: This lesson covers more loop patterns. These additional patterns involve
      more complex conditionals and state.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 7
    created: June 28 2022, 0300 PM
    modified: October 05 2022, 0220 PM
  files:
    path: bakery_for_patterns2_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Even More Loop Patterns

* Find
* Take
* Min/Max

We've already seen the Accumulate, Map, and Filter patterns.
Now we're going to cover a few more patterns that have more complex conditionals.
These are the Find, Take, Min, and Max patterns.

## The Find Pattern

```python
found = None
for item in my_list:
    if ___:
        found = item
```

We have a list of items and want to find a specific value based on a condition.
This requires us to walk through the entire list and check whether that value satisfies our condition.
When we are done, the desired value will be in the `found` variable, or found will have the value `None`.
You will need to replace the blank with an appropriate condition, and you will often want to replace the value `None` with a suitable default value.

## Find Last Variant

```python find-last-variant
from bakery import assert_equal

def find_last_question(words: list[str]) -> str:
    result = "Missing"
    for word in words:
        if word[-1] == "?":
            result = word
    return result

some_words = ["Hi?", "Oh.", "Uh?"]
assert_equal(find_last_question(some_words), "Uh?")
```

The Find pattern actually comes in two variants.
The first version will find the last element in the list that matches the given condition.
The key idea is that the accumulation variable is manipulated repeatedly by the loop and only returned when the entire loop is finished.
Contrast that with the next variant of the Find pattern, though.

## Find First Variant

```python find-last-variant
from bakery import assert_equal

def find_first_question(words: list[str]) -> str:
    for word in words:
        if word[-1] == "?":
            return word
    return "Missing"

some_words = ["Hi?", "Oh.", "Uh?"]
assert_equal(find_first_question(some_words), "Hi?")
```

In this variant of the Find pattern, the program actually behaves differently.
Instead of returning the last element that matches the given condition, the first element that is encountered is returned instead.
This variant relies on the control flow breaking behavior of the `return` statement to exit out of the `for` loop as soon as an element matches the condition.
The `return` statement, when encountered, immediately ends the `for` loop and the entire function, regardless of anything else.
This is why it is absolutely critical to make sure that your `return` statements are always guarded by `if` statements.
You will pretty much never ever see a `return` statement directly inside of a `for` loop UNLESS there is an `if` statement wrapped around it.

## The Take Pattern

```python
taking = True
new_list = []
for item in my_list:
    if ___:
        taking = False
    elif taking:
        new_list.append(item)
```

The Take pattern is a cousin of the Find and Filter patterns, but has significant more complexity.
We have a list of items, and we want a copy of the items up until a certain point.
We again have to walk through the list, but this time we will stop taking elements
after we satisfy our condition.
Notice that the body of this loop is more complicated, using an `elif` statement
to prevent us from taking elements after we have met the condition.
We should look at an example with more context.

## The Take Pattern in Action

```python take-pattern-example
words = ["Oh", "Hi", "There!", "Okay", "Bye!"]
taking = True
first_words = []
for word in words:
    if word[-1] == "!":
        taking = False
    elif taking:
        first_words.append(word)

print(first_words)
# ['Oh', 'Hi']
```

In this example program, we use the Take pattern to grab the first three elements of the list.
However, it was not that we intentionally only chose the first three elements specifically.
Instead, the logic of the pattern had us go through every element of the list until we encountered the first element that matched our condition.
After that element, we stopped accumulating elements in our new list.
At the end, the fact that we only took the first three elements is a consequence of their data, not some arbitrary constant length.

## The Min/Max Pattern

```python max-pattern
maximum = a_list[0]
for item in a_list:
    if item > maximum:
        maximum = item

print(maximum)
```

The last pattern is used to find the highest or lowest element in a list.
This pattern is similar to the Find pattern.
However, you can see that the conditional compares each value to the accumulated value.
Using this pattern, the accumulated value (in this case a maximum) will end up as the highest value in the list.
The corresponding minimum pattern works similarly, except the less than operator is used instead of the greater than operator.

## Maximum of Non-Empty Lists

```python non-empty-max
def highest(numbers: list[int]) -> int:
    # Critical guard!
    if not numbers:
        return 0
    # Pattern continues from here
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
```

A small but important detail often overlooked with the minimum and maximum patterns is that they require the list to be non-empty before you initialize the accumulation variable.
Remember, you cannot index the first element of an empty list, since there is no first element in an empty list.
Therefore, most practical implementations of the pattern will begin by incorporating the Guard pattern that we previously learned about in Logical Patterns.