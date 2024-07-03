---
waltz:
  title: bakery_structures_primer_read
  display title: 4) Primer
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: true
  additional settings:
    small_layout: true
    disable_timeout: true
    header: Chapter 4 Primer) Dataclasses
    slides: bakery_structures_primer.pdf
    youtube:
      Bart: H1B_0Z_8eqM
      Amy: QwAicUfNqzk
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0120 AM
  files:
    path: bakery_structures_primer_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Introduction to Data Structures

* Lists: A new type that can hold multiple values of the same type.
* Dataclasses: A way of making new types that combine multiple bits of different kinds of data into one bundle.

Previously, we have learned about five primitive types: integers, floats, strings, booleans, and the special None value.
In this chapter, we get a new type and an entire system for making additional types that greatly extend our capabilities.
First we will learn about dataclasses, that essentially allow us to combine different types of data into a single new type.
Then we will learn about lists, which is a type that allow us to group together values of the same type into a single value.
Both types have mutability, which introduces an exciting new way for our programs to go badly!

## Dataclasses

```python dataclasses
from dataclasses import dataclass

@dataclass
class Food:
    name: str
    calories: int
    cost: float
  
milk = Food("Jug of Milk", 2400, 4.33)
apples = Food("Bag of Apples", 285, 1.31)

print(milk.calories//milk.cost)
print("Would you like", apples.name+"?")
```

Dataclasses are basically collections of variables that can be combined to represent a single thing.
To be clear, dataclasses are not a monolithic type themselves, but a way to make new types.
In the example program shown here, we create a new `Food` dataclass and then make *instances* of the new type, storing them in variables named `milk` and `apples`.
The syntax for creating dataclasses is a little tricky, requiring not only an `import` but also a new annotation called a decorator (the `@dataclass` bit above the `class` keyword).
Forgetting any part of the syntax will prevent the dataclass from being properly formed, and can cause quite a few errors.
In addition to learning the new syntax, you also have to learn quite a bit of terminology.
Defining the dataclass, or class, creates not only a new type but also gives you a *constructor* function with the same name, which is what is called to create *instances* of the dataclass.
Afterwards, you can access *fields* (also known as *attributes*) that were passed into the constructor, by using a period and the name of the field.

## Dataclasses in Action

```python dataclasses-in-action
from dataclasses import dataclass
from bakery import assert_equal

@dataclass
class Food:
    name: str
    calories: int
    cost: float

def calories_per_dollar(a_food: Food) -> float:
    return a_food.calories // a_food.cost
apples = Food("Bag of Apples", 285, 1.31)
assert_equal(calories_per_dollar(apples), 217.0)
```

A primary use case for dataclasses is that we can pass them into or return them from functions, reducing the number of parameters we need and letting our functions do more.
This requires us to use the dataclasses name as a type in our parameters and header return types, but is otherwise no different than any other type of value being used as a parameter.
Dataclasses really only support two kinds of operations, the equality operator and the attribute lookup with the period.
However, that attribute lookup is extremely powerful, allowing us to access and modify data in the dataclass.
In general, attribute lookup is just another kind of expression that results in a value, and can be used in math operations, function calls, and return statements like anything else.

## Designer Worlds

```python designer-worlds
from designer import *
from dataclasses import dataclass

@dataclass
class World:
    cookie: DesignerObject
    score: DesignerObject

def eat(world: World):
    world.cookie.scale *= .9
    world.score.text = 1+int(world.score.text)
when('clicking', eat)
start(World(emoji('🍪'), text('black', '0')))
```

A nifty thing about dataclasses is that they let us write more sophisticated Designer programs.
We are no longer limited a single object, now we can have an entire `World` of objects!
In fact, that is the recommended convention within Designer for naming the dataclasses that are used as the state of the game.
Previously we learned how to manipulate that state by binding functions to events and then calling the `start` function.
Now, using `World` dataclasses, we can do even more sophisticated state.
Plus, since Designer Objects are essentially dataclasses too, we can manipulate their state more directly when making our games.
In this example program, we have a simplified version of the classic Cookie Clicker game, where clicking on the screen shrinks a cookie and increases your score.

## Lists

```python list-examples
# list[int]
scores = [100, 95, 33, 85]

# list[str]
animals = ["dog", "cat", "gerbil"]

# list
empty = []
```

The other data structure in this chapter is the list, which is used to combine multiple values of the same type.
Lists are created using square brackets with the elements inside separate by commas.
The elements should all be of the same type, which becomes the element type of the list.
In the example code shown, we have the type that would be used for the list if it were used as a parameter or a return value.

## List Operations

```python list-operations
animals = ["dog", "cat", "gerbil"]
# Indexing
print(animals[0])
print(animals[-1])
# Subscripting
print(animals[:2])
# Membership test
print("cat" in animals)
print("rabbit" in animals)
# Appending
animals.append("snake")
print(animals)
```

Much more so than dataclasses, lists introduce many operations that you can use to manipulate and access their contents.
Most of the operators are similar to ones we have previously seen with strings.
However, there are also methods that need to be used in precise ways when it comes to adding new elements to the list.
The list operations we cover in this chapter are indexing, subscripting, membership tests, append, and pop.

## Mutability

```python mutability-example
def add_5(items: list[int], number: int):
    items.append(5)
    number = number + 5

values = [1, 2, 3]
age = 1
print(values, age)

# Only `values` changes!
add_5(values, age)
print(values, age)
```

In the final section, we confront one of the great challenges associated with our new data structures: mutability.
Unlike the primitive types we learned before, both dataclasses and lists are mutable.
That means you can manipulate the actual underlying value of the data as opposed to only creating new values in their place.
When you modify a string or an integer, you were never actually modifying those values - you were actually creating new values and changing the variable to hold those new values instead.
But with lists and dataclasses, the actual data changes.
This has serious implications when it comes to functions, which can suddenly manipulate data outside of our scope rules!