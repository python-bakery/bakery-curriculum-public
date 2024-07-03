---
waltz:
  title: bakery_structures_list_ops_read
  display title: 4B2) List Operations Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: List Operations
    slides: bakery_structures_list_ops.pdf
    youtube:
      Bart: AeE_KDbkuXs
      Amy: 46l1uGrBAok
    summary: In this lesson, you learn about how to manipulate lists. Lists have many
      similarities to strings, except that they are mutable - they can be changed
      in place.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0126 AM
  files:
    path: bakery_structures_list_ops_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Doing Stuff with Lists

* Indexing
* Subscripting
* Membership Test
* Appending
* Popping

Once we have data inside of a list, we can do stuff with it.
There are actually many, many operations you can do on a list, so we'll learn about a few of them here.
The list includes indexing, subscripting, membership testing, appending, and popping.

## Indexing a List

```python index-a-list
names = ["Alice", "Bob", "Carol"]
# Second element
print(names[1])   # Bob

numbers = [10, 20, 30, 40]
# First element
print(numbers[0])    # 10

# Last element
print(numbers[-1])   # 40

# List creation AND indexing
print([2][0])
```

Much like strings, you can use square brackets to access a specific element of the list.
Notice that the syntax is the same, including the fact that we start counting from zero and can use negative numbers to access elements from the back.
Do not be confused by the square brackets here - when they are first, they are list creation.
When they are second, they are list indexing.

#### Subscripting a List

```python subscript-a-list
names = ["Alice", "Bob", "Carol"]
# Second until end
print(names[1:])
# ["Bob", "Carol"]

numbers = [10, 20, 30, 40]
# Second until fourth
print(numbers[1:3])
# [20, 30]

# Second to last until end
print(numbers[-1:])
# [40]
```

Much like strings, you can use a colon and square brackets to access a range of elements from a list.
The rules are the same as for strings: the first number is the starting index, and the second element is the ending index.
If you skip the first number, it will assume you want to start from the beginning.
If you skip the second number, it will assume you want to stop at the end.
And again, negative numbers work just as well.
Remember, if you are struggling to the calculate an index or subscript, write down the elements in boxes with numbers below for indexing or between for subscripting.

## List Membership

```python list-membership
names = ["Alice", "Bob", "Carol"]

print("Carol" in names)
# True

print("Ellie" in names)
# False

print("Car" in names)
# False

print("David" not in names)
# True
```

Much like strings, you can ask if a list has a specific value in it.
The `in` operator has a list on the right, and then any kind of value or variable on the left.
There is also a `not in` operator to determine the inverse.
Note that the operator matches exactly.
In the example code shown here, the string `"Car"` does not match `"Carol"` because it's not an exact match.

## Appending to a List

```python append-list
colors = ["red", "blue", "green"]

colors.append("cyan")

print(colors)
# ['red', 'blue', 'green', 'cyan']

# This will cause an error!
print(colors + 'yellow')
```

You cannot add elements to a list using the + operator.
Instead, you must call a method of the list, called `append`.
The word "Append" means "add to the end".
Append lets you add one thing to the end of the list.
The `append` method returns `None`, so be careful not to assign it back to the variable.

## Pop from a List

```python pop-list
colors = ["red", "blue", "green"]

last_color = colors.pop()

print(colors)
# ['red', 'blue']
print(last_color)
# green

# This will cause an error!
print(colors - 'blue')
```

You can also remove one thing from the end of the list using the "pop" method.
You will not need to do this too often in this course, because removing things
from a list can actually be a little tricky.
Just remember, you cannot remove items from a list with subtraction.
