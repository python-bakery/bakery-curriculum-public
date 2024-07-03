---
waltz:
  title: bakery_intro_types_read
  display title: 1A5) Types Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Types
    slides: bakery_intro_types.pdf
    youtube:
      Bart: HfmZ5vhA0Q4
      Amy: BqqYgax-7Aw
    summary: In this lesson, you will learn about how data is organized as types.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1228 AM
  files:
    path: bakery_intro_types_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## The Basic Types

* `143`: Integer  
* `44.07`: Float  
* `"A string"`: String  
* `True`: Boolean  
* `None`: None

All values in Python have a type.
The five basic types are: integer, float, string, booleans, and None.
There are many other types you will learn about.
Basically, types are a way to group values based on how related they are.
Text is very different from numbers, so there are different types for text and numbers.
There are also different types of numbers, though, and other types too.

## What are Types

```python valid-operations
# These will work fine
print(1 + 2)
print(1 - 2)
print(1 * 2)
print("Adding strings " + "is great")

# This will break!
print("Can't subtract" - "strings")
```

Types control what you can and cannot do with things.
We know that a number is a number because we can add it to another number, or subtract it, or multiply it.
We can add two strings together, but we cannot subtract them - this is one reason why a string and a number are different.
So another way of thinking about types is that they are a set of rules for what you can and cannot do with values.

## Integer Types (int)

```python example-ints
print(-1024)
print(-55)
print(0)
print(1)
print(13)
print(1737)
```

Integer types are whole numbers.
They include both negative and positive numbers, so there are a lot of them.
Integer is often shortened to `int` for convenience.

## Float Types (float)

```python example-floats
print(-56.4)
print(-1.0)
print(.0)
print(0.5)
print(1.02)
print(100.)
```

When numbers have decimals, we call them Float types.
The decimal is what distinguishes Floats and Integers.
Remember - if a number has a period in it, then it is a `float`!
Even if a number seems to be a whole number, Python will consider the number to be a float as long as it has a decimal somewhere in the number.

## String Types (str)

```python example-strings
print("My name is Anna")
print("")
print("Doggo")
print("5")
print("Four Score and Seven Years ago...")
```

Textual data is represented using String values.
The tricky thing about Strings is that *anything* can be stored as a String.
The only thing that makes it a string is the quotes.
A special case is the "empty string", which is a pair of quotes with nothing inside.
String is often shorted to `str` for convience.


## Boolean Types (bool)

```python example-booleans
print(True)
print(False)
```

Surprisingly often in programming, we are faced with "yes or no" values.
These two values are referred to as Boolean values.
Specifically, we have a `True` and a `False` value.
Note that the T and F are capitailized, and there are no quotes around the words.
Booleans are different from strings! 
Boolean is often shortened to `bool` for convenience.

## The None Type (None)

```python example-none
print(None)
```

Sometimes, you need to represent the absence of value, which we call `None`.
The None type is a special type that has only one value.
The None type can be hard to wrap your head around, so we'll save that one for later.
For now, just remember that it has a capital N, and no quotes.
