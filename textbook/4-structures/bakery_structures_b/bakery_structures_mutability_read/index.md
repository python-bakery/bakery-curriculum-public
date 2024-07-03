---
waltz:
  title: bakery_structures_mutability_read
  display title: 4B3) Mutability Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Mutability
    slides: bakery_structures_mutability.pdf
    youtube:
      Bart: Rvm-G-N5jaI
      Amy: Ty89jCYtGlw
    summry: This lesson shows how lists are different from other types because they
      are mutable (the variable's value can be changed, as opposed to taking on a
      new value).
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 5
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0127 AM
  files:
    path: bakery_structures_mutability_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## What is Mutability?

* Mutability: Whether or not a value can change, or whether instead only new values can be produced based on that value.

Mutability is an important concept now that we have more advanced data structures.
Fundamentally, the idea is whether values of the given type can actually change their inherent value, or if the value cannot change what it is.
When we store values into variables, we often need to consider whether that variable is holding a mutable value.
Many kinds of bugs can occur when we try to use an immutable value mutably or a mutable value immutably.


## Mutability of Types

* Immutable: Strings, floats, integers, booleans
* Mutable: Lists, Dataclasses

Strings and lists are similar because they are both sequences of elements.
However, a big difference between them is their Mutability.
Strings are immutable while lists are mutable.
Integers and other primitive types are all immutable, in fact, while lists and dataclasses are both mutable.

## Immutable Primitives

```python example-primitives
name = "Ada Bart"
print(name)

# The following line doesn't change `name`
name.lower() 
print(name)

# The following line doesn't change `name`
lowered_name = name.lower() 
print(lowered_name)
print(name)

# Now `name` has been changed!
name = name.lower() 
print(name)
```

Say you have a string variable.
When you add another string to that variable, you need to assign the result - otherwise it is lost.
Similarly, when you call a string method, you need to assign the result - otherwise it is lost.
This is the idea of immutability - you are never changing the string, you are simply creating new ones.
Integers and floats follow the same principle: you cannot fundamentally turn the value `5` into a different integer; you are always creating new integers based on the old one, but you cannot change the fact that `5` is `5`.

## Mutable Lists

```python example-list
grades = [90, 65, 78]
print(grades)

# This adds 98 to the list
grades.append(98)
print(grades)

# Bad! We add 44, but then overwrite the variable
#   `grades` with None, which is returned by `.append()`
grades = grades.append(44)
print(grades)
```

Now say you have a list variable.
Appending a value to the list fundamentally changes the list value itself, so that the list has a different sequence of values inside.
This is the idea of mutability, the fact that the list itself can change.
A tricky thing to remember with lists is that if you append a value to the list variable, you must not assign the result back to that variable, unlike with strings.
The append method modifies the list variable, and then returns None, so if you assign the method's result you overwrite the list variable.
As long as you don't assign back, the append call will mutate the list - changing the data inside the list without affecting the list variable.

## Mutable Dataclasses

```python example-dataclass
from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    age: int

babbage = Dog("Babbage Bart", 5)
print(babbage.name)
# Mutably update the instance
babbage.name = "Sir Babbage Bart"
# Value will have changed!
print(babbage.name)
```

Dataclasses can also be mutated. Any time you assign to an instance's field, you are modifying the instance.
In the example shown, we create an instance of a `Dog` dataclass, and then later update its `name` field.
Afterwards, the `name` field has a different value.
In this way, you can also see how fields are similar to variables.


## Mutability and Parameters

```python mutability-parameters
def add_x(a_list, a_str):
    a_list.append("X")
    a_str = a_str + " X"

courses = ["Biology", "Music", "Math"]
name = "Ada"
add_x(courses, name)
print(courses)
# ["Biology", "Music", "Math", "X"]
print(name)
# "Ada"
```

We have seen mutability before when we learned about parameters of functions.
Let's take a look at this function `add_x` that consumes a list and a string,
and adds the string value `"X"` to the end. When the function call is over,
only the list has actually been changed. Even though we were using local
versions of each variable, the mutability of the list type meant that the
original list was changed. If we wanted to change the `name` variable, we would
have had to return the modified value and assign it back to the `name` variable.