---
waltz:
  title: bakery_structures_dataclass_ops_read
  display title: 4A2) Using Dataclasses Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    small_layout: true
    header: Using Dataclasses
    youtube:
      Bart: Sk_tKKSyDIg
      Amy: Fj-ViZdaOp8
    slides: bakery_structures_dataclass_ops.pdf
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 8
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0122 AM
  files:
    path: bakery_structures_dataclass_ops_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Using Dataclasses

```python dataclass-operations
from dataclasses import dataclass

@dataclass
class Circle:
    radius: int
    color: str

# True
print(Circle(5, "red") == Circle(5, "red"))
# False
print(Circle(5, "blue") == Circle(5, "red"))
# Error
print(Circle(5, "red") + Circle(5, "red"))
```

Most operators do not work with dataclasses.
Addition, subtraction, and the other math operations will not work, causing TypeErrors.
Similarly, the ordering operators (like the greater than and less than comparison operators) will not work.
The equality and inequality operators DO work, however.
When you check if two dataclasses are equal, each field is checked in order to make sure they are equal.
However, you will not often need to think about equality or any other operators with dataclasses directly.
Instead, you should be thinking about accessing the *fields* of a dataclass, in order to perform operations using the data stored inside of the dataclass.

## Using Attributes

```python dataclass-attributes
from dataclasses import dataclass
@dataclass
class Rectangle:
    length: int
    width: int

box = Rectangle(5, 3)

print("The box area is", box.length * box.width)
```

We have previously discussed how we can access the fields of instances, in order to use their values.
The syntax is quite simple.
We have the name of the variable holding the instance, a period, and then the name field.
This is similar to the syntax for a method, and that is no coincidence.
Technically speaking, a method is just an attribute that holds a function.
We will not bother learning to define methods in our dataclasses, yet.
Instead, the important thing to focus on is that we can access fields from instances.
This is especially useful when we start passing dataclasses into functions.

## Functions Consuming Dataclasses

```python using-dataclasses
from bakery import assert_equal
from dataclasses import dataclass

@dataclass
class Rectangle:
    length: int
    width: int

def area(rect: Rectangle) -> int:
    return rect.length * rect.width

box = Rectangle(5, 3)
assert_equal(area(box), 15)
```

In the program shown here, we have moved the multiplication inside of a function, to create a reusable `area` function that consumes a `Rectangle` instance and produces an integer.
Notice the `rect` parameter, which has the type `Rectangle`, matching our previously defined dataclass.
In the `assert_equal`, that parameter is matched to the corresponding argument, which in this case is the variable `box`.
That `box` is containing an instance of the `Rectangle` dataclass created using its constructor.
Just to recap, we have a dataclass named `Rectangle`, which is also the name of the constructor AND the new type `Rectangle` created.
We can assign a constructed instance to a variable of our own choosing, which in this case was `box`.
That variable can then be used as an argument to a function consuming a `Rectangle`, like the `area` function.
Inside of that function, we use the dataclasses type name on the right-hand side of the colon to indicate the type of the parameter.
But on the left-hand side, we are free to give whatever name we want to the local variable holding the instance.
We chose the name `rect` as a convenience, but could have chosen other names like lowercase `rectangle` or `a_rectangle`.
As long as we are consistent within the function definition, the name does not matter to Python.
From there, the function is able to use the fields of the instance to calculate and return the area.
Notice how we only had to pass in one parameter to this function!

## Functions Returning Dataclasses

```python returning-dataclasses
from dataclasses import dataclass
from bakery import assert_equal

@dataclass
class Card:
    suit: str
    rank: int

def parse_card(card: str) -> Card:
    return Card(card[0], int(card[1:]))

assert_equal(parse_card("H2"), Card("H", 2))
assert_equal(parse_card("D5"), Card("D", 5))
```

Functions not only can consume dataclasses, they can also create them.
In this example, we have a `parse_card` function that consumes a string value and produces a `Card` instance.
To do so, the function must call the `Card` constructor and pass in the appropriate fields.
In this case, that means the first character of the string as the first argument, and then the rest of the string converted to an integer for the second field.
In the `assert_equal`, we call the function and then assert that the result is the same as calling the constructor with the literal values.
In this way, we have a function that can return a dataclass.
The utility of a Dataclass is that we can bundle related fields together in order to represent a more complex object, and pass them conveniently around the program without having to have a huge number of variables.

## Fields As Arguments

```python fields-as-arguments
from dataclasses import dataclass

@dataclass
class Rectangle:
    length: int
    width: int

def as_string(rect: Rectangle) -> str:
    return str(rect.length) + "x" + str(rect.width)

box = Rectangle(4, 5)
print(as_string(box))   # 4x5
```

There is nothing special about the values stored in fields of instances.
The attribute access expression using the period is no different than other expression such as a variable lookup, math operation, or function call.
That means we can pass the result of such expressions to other function calls, math operations, or even return them.
In this example, we use the `str` function by passing in the values associated with the fields of the given `rect` instance, in order to create a nice string representation of the instance.

## Mutable Updates

```python mutate-dataclass
from bakery import assert_equal
from dataclasses import dataclass
@dataclass
class Rectangle:
    length: int
    width: int

def stretch(rect: Rectangle) -> Rectangle:
    rect.length = rect.length * 2
    return rect

box = Rectangle(5, 3)
assert_equal(stretch(box), Rectangle(10, 3))
```

One of the most useful but confusing aspects of a dataclass is that fields' values can also be changed later.
In the example shown here, the `stretch` function consumes and produces the same Rectangle.
However, before returning the `Rectangle`, its `length` field is doubled from its previous value.
The syntax for updating the fields of a dataclass are almost exactly the same as updating the value of a variable.
As we will discuss later in the section about Mutability, there are many dangers to mutably updating fields like this.
Therefore, we will look at an alternative.

## Immutable Copies

```python copy-dataclass
from bakery import assert_equal
from dataclasses import dataclass

@dataclass
class Rectangle:
    length: int
    width: int

def stretch(rect: Rectangle) -> Rectangle:
    return Rectangle(rect.length*2, rect.width)

box = Rectangle(5, 3)
assert_equal(stretch(box), Rectangle(10, 3))
```

A common way to avoid mutation is to create a brand new instance with new values instead of updating the old instance.
This may sound wasteful, but fortunately Python is quite fast about creating new instances.
And in turn, we can use the new instance without worrying about the original being affected.
If you want to see the tangible difference with this approach, try printing out the `box` variable at the end of the program shown here and the program shown before.
In the mutable version, the original `box` variable is changed, while in this version, the original `box` is left untouched.
Under what circumstances would you want to modify the original compared to making a copy?
The tradeoff might not be clear just yet, but for now remember that there are two ways to change a dataclasses: by making a new one based on an old one, or by editing the fields of an existing one.