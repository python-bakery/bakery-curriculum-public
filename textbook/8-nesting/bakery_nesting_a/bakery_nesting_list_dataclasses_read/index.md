---
waltz:
  title: bakery_nesting_list_dataclasses_read
  display title: 8A1) Lists of Dataclasses Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Lists of Dataclasses
    youtube:
      Bart: TdKsQeO-gd8
      Amy: KrBevOVW6NE
    summary: ''
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 11
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0616 PM
  files:
    path: bakery_nesting_list_dataclasses_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Lists and Dataclasses

* Lists: A sequence of data, accessible in order, all of the same type
* Dataclasses: A bundle of data, accessible by field name, composed of many possible types

Recall our two composite data types that we have learned so far: lists and dataclasses.
Lists allow us to represent **many** of the **same kind** of thing.
Dataclasses allow us to represent **one** thing that has **many different** parts.
We can access elements of a list in order sequentially or a specific one by position.
We can access fields of a dataclass by the name of the field.
They are both data structures that are composed of simpler primitive types and, as we will soon see, they are even compatible with each other.

## Nesting Data

![On the left, a picture of a table of data representing four pets. On the right, a code representation of that data made by defining a Pet dataclass and then calling the pet constructor four times inside of a list literal.](bakery_nesting_list_dataclasses_tabular_code.png)

In order to represent more complicated reality, we have to start nesting data structures inside of other data structures.
A list of dataclasses is one of the most important ways to nest data structures, because it can represent a large number of things.
A comparable idea is a table of data, where each column is of the same type and each row represents a single instance.
An individual row corresponds to a dataclass, whereas all the rows together represent the overall list.
In the example shown here, we see a table on the left representing four pets, and code on the right also representing the same pets.

## Nested Creation

```python nested_creation
from dataclasses import dataclass

@dataclass
class Circle:
    color: str
    radius: int

circles = [Circle("red", 4),
           Circle("blue", 10),
           Circle("green", 6)]
print(circles)
```

Creating lists is done with the square brackets.
Creating dataclasses is done by calling the constructor function.
Creating a list of dataclasses works the same way, with the constructor calls being placed inside of the square brackets, separated by commas.
The amount of whitespace inside of the square brackets and between the commas does not matter.
Sometimes longer lists are placed on multiple lines to make it easier to read them, although that is not required.

## What's in the List?

```python nested_access
from dataclasses import dataclass

@dataclass
class Circle:
    color: str
    radius: int

circles = [Circle("red", 4), Circle("blue", 10)]

print(circles[0])
print(circles[1].radius)
```

Accessing nested data can be quite confusing, but the same consistent rules apply that we have learned throughout.
If you have a list of things, you can access specific elements using indexing.
When you index a list of dataclasses, that means you get one dataclass out, and you can then access attributes of that element.
In the code shown here, the first `print` indexes the first element of the list and looks at the entire instance.
The second `print` indexes for the second instance, and then accesses its `radius` field.

## The Type of the Iteration Variable

```python iteration_variable
from dataclasses import dataclass

@dataclass
class Animal:
    name: str
    weight: int
    big: bool

zoo = [Animal("Klaus", 17, True),
       Animal("Tigger", 12, True),
       Animal("Wrex", 2, False)]

for an_animal in zoo:
    print(an_animal)
```

Since we have a list of dataclasses, we can also iterate through the list.
While inside the body of the iteration, we gain access to each instance and therefore the specific fields of each dataclass instance.
A question to ask yourself is: what type of value is stored in the iteration variable?
Many folks will incorrectly answer a string or an integer, because they are comfortable with those primitive types.
However, the answer is the same as it was back when we were dealing with lists.
The iteration variable's type is the element type of the list.
If you have a list of dataclasses, then the iteration variable's type will be the type of the dataclass.
In the example shown here, the `zoo` variable holds a list of `Animal` dataclasses. When we iterate through the `zoo`
with a `for` loop, we create a new variable named `an_animal`. That iteration variable `an_animal` will be of type `Animal`.
Not a string representing the animals name, or its weight, but the entire Animal is stored in that variable.

## Using Fields

```python using_fields
from dataclasses import dataclass

@dataclass
class Book:
    name: str
    price: float

shelf = [Book("Harry Potter 1", 5.00),
         Book("Harry Potter 2", 6.00),
         Book("Harry Potter 3", 3.00)]

total_price = 0
for a_book in shelf:
    total_price = total_price + a_book.price
print(total_price)
```

The code shown here demonstrates how we can still apply the Loop Patterns we have seen so far.
The only major difference to the Sum pattern shown here is that we cannot use the `a_book` variable directly.
The `total_price` variable is an integer, while the `a_book` variable is a `Book` instance.
The addition operator is not compatible with those datatypes.
Instead, we must specifically access the `price` field of `a_book` and add that instead.
By correctly accessing the right field, we can unpack the complex data structure and use its juicey goodness.

## List of Dataclass Function

```python example-lod-function
from bakery import assert_equal
from dataclasses import dataclass

@dataclass
class Circle:
    color: str
    radius: int

def get_red_circles(circles: list[Circle]) -> list[Circle]:
    filtered = []
    for circle in circles:
        if circle.color == 'red':
            filtered.append(circle)
    return filtered

my_circles = [Circle("red", 4), Circle("blue", 10)]
assert_equal(get_red_circles(my_circles), [Circle("red", 4)])
```

Putting the `for` loop and attribute lookups inside of a function does not fundamentally change how everything works, either.
Here we have a `get_red_circles` function, which uses the Filter pattern to only get the red circles from a list of circles.
Note the parameter type and return type, which is a list of `Circle`s.
Although there is a lot going on in this code, you have seen each concept before in some form.
The only thing complicating matters is that we are putting them all together in one place.