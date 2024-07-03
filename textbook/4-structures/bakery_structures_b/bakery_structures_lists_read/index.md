---
waltz:
  title: bakery_structures_lists_read
  display title: 4B1) Lists Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Lists
    slides: bakery_structures_lists.pdf
    youtube:
      Bart: PNORle-Exs0
      Amy: I38uX075700
    summary: In this lesson, you learn about the List type. Unlike the primitive types,
      the List type is a complex type composed of other types. They are essential
      for creating programs that do more complex and interesting things at a bigger
      scale.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0125 AM
  files:
    path: bakery_structures_lists_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Lists

```python list-examples
# List of integers
print([45, 55, 32])

# List of strings
print(["Apples", "Oranges", "Bananas"])

# List of booleans
print([True, False, True])

# Empty List
print([])
```

The next data structure we will learn about is the `list` type.
A list is a sequence of values, all of the same type.
For instance, you could have a list of numbers, or a list of strings.
You can even have a generic empty list.

## Lists of X

```python integer-list-print
# list[int]
print([45, 55, 32])
```

A `list` is a type, much the same way that `int` (for "integer") is a type.
However, the `list` will also usually have an "element type", which is what the list is composed of.
So if you have a list of integers, its type is "List" and its element type is "integer".


## Defining a List

```python integer-list-assignment
my_numbers = [45, 55, 32]

print(my_numbers)
```

We create lists using square brackets on their own.
Each value that we want to put into the list is separated by commas.
The square brackets are critical to making this a list; without them it is not a list.

## Square Brackets

```python square-brackets
# Creating lists with square brackets
values = ["Hello", "World", "!"]

# Subscripting with square brackets
message = "Hello World!"
print(message[1])
```

We've seen square brackets used before, when we were subscripting and indexing a string.
Confusingly, Python ALSO uses square brackets for creating lists. 
You might struggle at first figuring out when you're looking at subscripting or list creation.
The key is whether the square brackets come AFTER an expression - that means subscripting.
If the square brackets are on their own, you have a list.

## Empty Lists

![Two rows of code, with a picture of a bag next to each one. The first line of code is an empty list symbolized by a pair of square brackets, next to an empty bag. The second line of code is a list with three integers inside of the square brackets, next to a bag with three integers inside.](bakery_structures_lists_empty_list.png)

A pair of square brackets with nothing between them creates an empty list.
An empty list is like an empty bag: you may not have anything in it, but you still have the bag itself.
Empty lists do not have an element type, until you put something in them.

## Truthiness of Lists

```python list-truthiness
my_money = []
if my_money:
    print("I have some money!")
else:
    print("I have no money.")

your_money = [10, 10, 20, 1, 1]
if your_money:
    print("You have some money!")
else:
    print("You have no money.")
```

When used as a conditional, a list evaluates to True unless it is empty according to the rules of Truthiness.
This can be very convenient when writing conditional expressions involving lists.
If you want to test if the list is not empty, you just write the name of the variable holding the list.

## Printing Lists

```python printing-lists
names = ["Alice", "Bob", "Carol"]
print(names)
# ['Alice', 'Bob', 'Carol']
```

When you print a list, you will notice that the square brackets are printed too.
In fact, Python print each value of the list as if it was a literal value.
So notice that the strings have quotes around them now!

## The Box Model

![A list of integers is shown in code, and then below it is the same numbers shown in a row of boxes. The boxes are numbered starting from 0 to 4.](bakery_structures_lists_box_model.png)

Lists are often shown in diagrams as a row of boxes, to help us visualize the data.
Each box will have a value in it.
The boxes may also have numbers below them, showing the indices of the values starting from zero.
This is similar to how indexing strings works.

## List Type

```python list-type
# Function that consumes a list of integers
def add_numbers(numbers: list[int]) -> int:
    pass

# Function that consumes a list of strings
def join_strings(texts: list[str]) -> str:
    pass

# Function that makes a generic list
def make_list() -> list:
    pass
```

When you define a function, you need to specify the types of the parameters and the return value.
If you don't know the element type of the list, you can just use the `list` type like we would a string or an integer.
The left function consumes a list and produces an integer.
But if we do know the element type, we add the element type, wrapped in square brackets, after the word `list`.
These example functions here demonstrate how this looks visually; we do not know how to implement them yet, but they can at least show us how to write the types.

## Terminology

![The term "List" is different from the terms "Array" or "Vector".](bakery_structures_lists_list_terminology.png)

Some people will use the words "Array" or "Vector" to describe lists.
These are actually slightly different concepts, which we will not cover in this course.
Don't be thrown off if someone refers to a list as an "Array", but don't use that word yourself!