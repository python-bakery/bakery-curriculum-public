---
waltz:
  title: bakery_functions_defining_read
  display title: 2A3) Defining Functions Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Defining Functions
    slides: bakery_functions_defining.pdf
    youtube:
      Bart: 9p8PW5u3Ee0
      Amy: 7jOAQvKra-A
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1253 AM
  files:
    path: bakery_functions_defining_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Defining Your Own Functions

![A picture of a box labelled "Homemade Functions"](functions_defining_homemade_box.png)

You can create your own functions in Python.
In fact, this is one of the most powerful features of programming, the ability
to create your own functions.

## Why Functions?

1. Code Reuse
2. Easier to debug
3. Clean decomposition

Lets' talk about three major advantages of functions:
First, they allow us to reuse code.
Second, they allow us to debug a chunk of code in isolation from the rest of the program.
Third, they let us break a program down into smaller pieces, and we don't have to worry about how the functions work internally.

## Definition Syntax

![Annotations mark each part of the function definition.  `def` is the define keyword.  `name` is the name of the function.  `(` and `)` are the parentheses.  `p1` and `p2` are parameters' names. `int` and `str` are the parameters' types. `,` is a comma, separating the parameters. `->` is dash and a greater than, forming an arrow. `bool` is the return type. `:` is a colon, ending the header. ](functions_defining_syntax.png)

To create a new function, you use the `def` keyword, which stands for "define".
You write `def`, the name of the function, an open parentheses
each of the **parameters** separated by commas,
a closed parentheses,
a dash and a greater than,
the **return** type of the function, and a colon
The parameters need: variable names, a colon, and their parameter type.
This entire line is called the **Header**.
  
## Function Body

```python add-function
def add(left: int, right: int) -> int:
    return left + right
```

When you call a function, you are executing the code stored in the "Body" of
the function. Everything "inside" the body should be indented 4 spaces.
In the block version, this is shown visually with a bar on the left.
The body must be there - in other words, it cannot be empty.


## Naming a function

1. Try to use verbs
2. Function names can only have letters, numbers, and underscores
3. Function names cannot start with numbers

Usually, you should use a verb as the name of the function.
The name helps other programmers understand what the function does.
Naming a function is just like naming a variable: you may only use letters, 
numbers, and underscores, and it cannot start with a number.
    
## Calling Your Functions

```python add5-function
def add5(a_number: int) -> int:
    return a_number + 5

add5(10)
add5(3)

# To see the result, you will need to use print:
print(add5(10))
```

After you've defined a function, you can use it by calling the function.
As we did before, we combine the name of the function with **calling parentheses**.
Note how we still pass in **arguments**.
Here we call the function `add5` twice, first passing in the argument 10
and then the calling it again with the argument 3.


## Parameters

```python subtract-function
def subtract(first: int, second: int) -> int:
    return first - second

print(subtract(3, 8))
print(subtract(-2, 5))

result = subtract(10, 10)
print(result)
```

When you define a function, you can choose to add in **parameters** to the header.
These parameters will take on the value of the arguments when the function is called.
This can be very tricky to understand.
Each argument exactly matches one parameter.
In the code below, the parameter `first` will match to 3, -2, and -10.
The parameter `second` will match to 8, 5, and 10.
Remember, each function call happens one after the other.

## Parameters and Types

```python get_speed-function
def get_speed(distance: int, time: int) -> float:
    return distance / time

get_speed(6, 2)
get_speed(3, 8)
```

In modern Python, we specify the type of each parameter.
So far, we know of five types: int, str, float, bool, and None.
Any time you call that function, the arguments must match the type of the parameter.

## Return

```python area-function
# Even though this says it returns a string,
#   it will actually return an integer!
def area(length:int, width:int) -> str:
    return length * width

# Try running it yourself!
print(type(area(5, 3)))
```

When defining a function, you can make it return a value.
Most functions return some kind of value. 
We make Python return values using the "return" statement.
We describe what type of value the function returns
using the arrow and a type in the header.
But note that it is the **return statement** that actually makes a value
get returned; the header just describes what should be returned.

## Calling and Printing

```python calling-and-printing
def area(length:int, width:int) -> int:
    return length * width

print(area(3, 4))
area(1, 8)
print(area(5, 2))
```

When you call a function, a value is always returned.
Even if you forget the return statement, the special value `None` will be
returned.
If you are writing code in the console, then you will see any non-`None` values
appear.
But if you are writing code in a regular editor, the value will not appear in
the console unless you use `print`.
We will sometimes print the result of calling a function, but remember
that printing is not necessary to call a function.

## Pass

```python do-nothing-function
def func(abc: bool) -> str:
    pass

func(True)
print(func(True))
```


Sometimes, we want to define a function without writing its body just yet.
We use a special statement named "pass" to fill in the body until we're ready to write it.
Pass is a very special statement: it does absolutely nothing but take up space, telling the computer to "pass over" this line.
Since we always have to have a body, if we didn't put the word pass there, Python would crash with a syntax error.
