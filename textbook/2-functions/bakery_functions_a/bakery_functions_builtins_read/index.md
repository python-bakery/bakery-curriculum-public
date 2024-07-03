---
waltz:
  title: bakery_functions_builtins_read
  display title: 2A2) Built-in Functions Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Builtin Functions
    slides: bakery_functions_builtins.pdf
    youtube:
      Bart: SOt_NuIjxz0
      Amy: Ri7eXDy9ZFo
    summary: In this lesson, you'll learn more about calling functions and methods.
      In particular, you will learn how to read documentation about built-in functions
      that you can use. You will also learn how to nest, chain, and combine functions
      and methods.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1253 AM
  files:
    path: bakery_functions_builtins_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## The Many Functions

* abs
* bool
* int
* pow
* len
* ...

Python has many, many built-in functions.
You could never learn them all in this course.
You will learn a few, but it's far more important that you learn how to learn more about functions.


## Learning about a Function

![Documentation of the built-in `len` function.](functions_builtin_docs.png)

Good programmers create documentation for their functions.
Documentation is extra information about a function that makes it clear how it works.
There are many ways to write documentation, but they usually have a few things in common.


## Function Documentation

![The same text from the previous slide with the following words circled: Name, Parameters, Return value, Description, Examples.](functions_builtin_docs_highlighted.png)

You should look for six major parts.
The function's name, its parameters, its return value, its description, and examples how to use the function.

## Parameters and Arguments

![A line of code is shown, with its documentation below. Annotations indicate that the `3` and `10` are arguments, while `length` and `width` are parameters.](functions_builtin_args_params.png)

The Arguments that are passed into a function are also known as Parameters.
Parameters are the formal names that allow us to refer to a the function.
In the example below, the arguments are 3, 10, and "Hello".
The documentation tells us that the corresponding parameters are X, Y, and Z.

#### Nesting Function Calls

![Arrows point from the value `"Hello World"` to the function name `len`, and then arrows point from `len` to the function name `print`.](functions_builtin_nested_function_calls.png)

A common task is to nest function calls inside of other function calls.
When nesting function calls, you read from the inside outward.
This can be a little unintuitive, but it may help to treat the parentheses the same as they are in math operations.
However, it's critical to remember that the parentheses are there because they are what actually call the function, not because they are doing math.

#### Chaining Methods

![Arrows point from the value "hello world" to the method name `title`, and then arrows point from `title` to the method name `count`.](functions_builtin_chained_methods.png)

When you need to call methods on the same string variable or value, it's a little different.
As shown below, you will repeat the period, name, and parenthese each time.
By placing them side-by-side, you will keep using the same variable, modifying it in turn from left to right.

#### Functions, Methods, and Operators

![Some code is shown with annotations. The `string_length =` is labelled as an assignment statement. The `len(` part is labelled as a function call. The `+` part is labelled as a string addition. The `.strip()` is labelled as a method call.](functions_builtin_labeled_parts.png)

Since calls are just another expression, you can freely combine them with each other.
Observe the code show, where we combine string addition, a string method call, and a function.
Notice the order of execution, this can be tricky to follow!

#### Input/Output

* print: Consumes any number of arguments, outputs them on the console, and returns None.
* input: Consumes a single string, takes user input, and returns the user's inputted string.

You already know two functions:
Print is a function that takes in arguments and writes to the console.
Input is a function reads from the console and returns it as a string value.
These two functions are strange, because they have side effects.
The Input function puts a textbox on the console, and the print function writes text to the console.
Going forward, we will use these two functions a lot less than we did up until now, although they will have their purpose.