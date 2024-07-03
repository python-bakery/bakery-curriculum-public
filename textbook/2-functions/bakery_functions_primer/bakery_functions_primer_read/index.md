---
waltz:
  title: bakery_functions_primer_read
  display title: 2) Primer
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: true
  additional settings:
    small_layout: true
    header: Chapter 2 Primer) Functions
    youtube:
      Bart: 7604sPdRx2U
      Amy: lUyDpxA1BrY
    slides: bakery_functions_primer.pdf
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 6
    created: June 28 2022, 0300 PM
    modified: September 04 2022, 1003 PM
  files:
    path: bakery_functions_primer_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
# Functions

## Introduction to Functions

* Functions: Reusable chunks of code that can be used to build up more complicated programs.

Functions are one of the most important concepts in this entire book, so we start off with them here in the second chapter.
Some people refer to functions as the "atomic unit of a program", since programs are built out of functions.
In fact, functions have many of the same properties and affordances as programs.
Fundamentally, you can think of a function as a miniature program with its own input, processing, output workflow.
In other words, they are reusable chunks of code.
Functions are critically important not only to this chapter, but to this course, and even to the rest of your career as a computer scientist.

## Calling Functions

```python example-calling
# The `input` function
height = input("How tall are you, in inches?")
# The `int` function
height = int(height)
# The `round` function
feet = round(height / 12)
# The `print` function
print("You are", feet, "feet tall, rounded to the nearest foot.")
```

The first two sections of this chapter are dedicated to *calling* functions, which is how functions are used.
When you call a function, you put parentheses after the name of the function.
Sometimes you also provide *arguments*, which are values that go inside the parentheses.
You might think of a function as a mysterious box that you cannot see inside of.
The arguments are slots on top of the box that you can put data into.
Then, more data will come out of the bottom of the box, which we call the *returned* values.
These values are substituted back into the program, just like how other operations evaluate to other values.
Python has many built-in functions, some of which you are already familiar with: `input`, `int`, `round`, and `print` are four examples shown here.

## Defining Functions

```python example-defining
def average(num1: int, num2: int) -> int:
    """
    Calculate the average of two integers, returning an integer.
    """
    return (num1 + num2) // 2

result = average(5, 10)
print(result)
```

The subsequent two sections are about how to define your own functions.
Critically, the programmer must use the `def` keyword and provide a lot of information about the function.
One of the most important pieces of information is the name of the function, which in the example shown is `average`.
The programmer must also provide formal names for the expected arguments to the function, and the expected types of those names.
These names are called *parameters*, and they become variables for the function to use.
The programmer must also include the expected return type for when the function is called, which in this case is the `-> int` part.
The line with the `def` keyword is known as the *header* of the function, and the following indented lines below it are the *body*.
The first line of the body is string literal value, known as a docstring, that explains the function's purpose.
Subsequent lines of the body are the instructions that will be executed when the function is called, with the final line being the `return` statement.
Once defined, functions can be called just like the built-in functions.

## Testing Functions

```python example-testing
from bakery import assert_equal

def average(num1: int, num2: int) -> int:
    """
    Calculate the average of two integers, returning an integer.
    """
    return (num1 + num2) // 2

assert_equal(average(5, 10), 7)
assert_equal(average(0, 0), 0)
assert_equal(average(1, 3), 2)
```

Just because you wrote a function, does not mean the function works correctly.
An entire section is dedicated to talking about how functions must be unit tested to try to prove their correctness.
A unit test is a special line provided in the program that shows an example input and the expected output when the function is working correctly.
Unit testing requires strong critical thinking skills.
In this course, we use a library named `bakery` that has a special function named `assert_equal` that can be used to test your programs.
Going forward, we will expect you to test all of your functions!

## Debugging

* Unit Testing
* Tracing
* Wolf-fence Debugging
* Rubber-duck Debugging
* Scientific Method

At the end of Part A, there is a quick chapter about different debugging strategies.
Since programs get significantly more complicated around now, it is useful to learn how professional programmers go about figuring out how to make their programs work correctly.
Strategies covered include learning how to talk to rubber ducks, fencing in wolves, and making random guesses.

## Scopes and Bodies

```python example-scope
# num1 and num2 are local variables for average

def average(num1: int, num2: int) -> int:
    return (num1 + num2) // 2

# my_height, your_height, and averaged_height are global variables
my_height = 40
your_height = 62
averaged_height = average(my_height, your_height)
```

The indented region under the header of a function is known as the *body* of the function.
The body of the function is the same concept as the body of a module.
In other words, every program has at least one body, and then every function also has its own body.
A separate-but-related concept is the idea of Scope, which is a body that controls the lifetime of variables.
Any variable inside of a scope will only be available inside of that scope, so when that scope ends, the variable is no longer available.
There is also a special global scope for the entire program, but you must be especially careful to avoid global variables inside of your functions.

## Docstrings

```python example-docstring
def average(num1: int, num2: int) -> int:
    """
    Calculate the average of two integers, returning an integer.
    """
```

We previously mentioned that the first line of the function's body should always be a string literal.
Specifically, it should always be a triple-quoted string with specially formatted contents.
This is a special kind of comment that Python recognizes as the function's docstring.
A docstring is a very important kind of documentation that helps explain the purpose of a function for other programmers.
Each line of the string should be indented to match the body of the function.
A common mistake is to try to put the docstring before or after the function.
However, docstrings only count if they are the first line of the body of the function!

## Data Flow

```python example-flow
def add5(number: int) -> int:
    result = number + 5
    return result

def double_and_add5(value: int) -> int:
    answer = 2 * add5(value)
    return answer

final = double_and_add5(7)
print(final)
```

The third section of Part B is one of the most critical and confusing ideas, which is Data Flow.
Metaphorically, data flows through a program from its inputs to its outputs, being transformed and modified along the way.
Up until now, that flow went from the top of the module to the bottom.
But now, program execution will actually jump around according to the rules of function calls and returns.
It is critical to track what data is available at each step of the program.
This is especially true when we start calling functions from within functions.

## External Functions

```python example-externals
from designer import *

set_window_size(100, 200)

def smiley_face(x: int, y: int) -> DesignerObject:
    face = circle('yellow', 25)
    left_eye = change_xy(circle('black', 5), -10, -10)
    right_eye = change_xy(circle('black', 5), 10, -10)
    smile = change_y(arc('black', 180, 360, 30, 10), 10)
    return move_to_xy(group(face, left_eye, right_eye, smile), x, y)

draw(smiley_face(50, 40),
     smiley_face(50, 100),
     smiley_face(50, 160))
```

The final section of this chapter acknowledges that although Python has a lot of useful built-in functions, we will often need even more functions.
Just like how variables can be defined in other modules, functions can also be defined externally in modules and then imported.
Once imported, they can be used to build truly magical programs.
Some of the examples in this section involve creating graphics using a library named `designer`.