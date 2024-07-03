---
waltz:
  title: bakery_functions_calling_read
  display title: 2A1) Calling Functions Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Calling Functions
    slides: bakery_functions_calling.pdf
    youtube:
      Bart: 82IqXIziLfU
      Amy: RdaGz6sSktw
    summary: In this lesson, you will learn about how to use functions. Functions
      are a fundamental element of programming that allow you to reuse code. Functions
      are a complex tool, so we will learn more about them in the next lesson. When
      you complete this one, you should feel free to continue directly onto the next
      one!
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 7
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1252 AM
  files:
    path: bakery_functions_calling_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## What Are Functions?

* Functions: Reusable chunks of code

Functions are reusable chunks of code.
Once code is wrapped in a function, we can use it in other places.
First, we'll learn how to use functions.
Later, we'll learn how to make them for ourselves.

## Calling Functions

* "Use" a function
* "Call" a function
* "Invoke" a function
* "Execute" a function
* "Run" a function

When you want to "use" a Function, we say that you "call" it.
Another term is "invoking" a function.
You can also use the terms "execute" and "run", although those will usually be for full programs.

## Syntax

```python
# Function name followed by parentheses
round(3.75)
```

There are two essential parts to calling a function:
The name of the function, and then parentheses following the name.

## Calling or Not

![Two pictures, of a person talking about going to a store vs actually going to the store](functions_calling_parentheses.png)

To call a function, you MUST add parentheses.
Otherwise, you are simply referring to the name of the function rather than executing it.
Think of it as the difference between "thinking about going to the store" as opposed to "actually physically going to the store".
The parentheses are what actually make this a function call, and not just the function name being referenced for no reason.

## Functions vs. Programs

![A diagram shows a box labelled "input" with an arrow pointing towards a bigger box labelled "processing", and another arrow pointing out that box pointing to "output". The bigger box is annotated as a "program". Inside the bigger box is a series of three sets of three smaller boxes, each labelled "input -> processing -> output". These boxes are labelled as functions. All together, there is a small black arrow tracing through all the boxes in order.](functions_calling_input_processing_output.png)

A program and a function are similar, but not quite the same.
They both have the same "Input-Process-Output" pattern.
However, functions are typically much smaller, and are meant to accomplish a single specific task.

## Functions vs. Methods

```python method-example
message = "MAKE THIS LOWERCASE"
# Call the `lower` method
message = message.lower()
print(message)
```

Methods are a special kind of function.
They are attached strongly to a value.
The way we write a method call is slightly different too, since it needs to incorporate that value.
When you want to use a Method, you need the name, parentheses, AND two more pieces:
The calling value or variable and a period.
In later lessons, we'll learn more about this strange syntax.
For now, get comfortable with the difference between calling functions and methods.

## Metaphor

![On the left, a boss asks an employee to "create a report on sales". In the middle, the phrase "time passes" appears.  On the right, the employee has returned and says "Here is the report, sir"](functions_calling_magic_report.png)

You don't have to know *how* a function accomplishes its goal, in order to use it.
Think of it like a well-run office.
When you ask a co-worker to complete some work, you don't care how it happens, just the inputs and outputs to their process.
This separation of concerns allows you to focus on pieces of a program without worrying about the whole thing.


## Returning Values

```python returned-values
# call function, result is returned and assigned
new_value = round(3.9)

# Can use print it, update it, etc.
print(new_value)
new_value += 1
print(new_value)
```

Functions are useful because they can return values.
Functions can return any type of value: string, boolean, integer, whatever.
Mentally, when a function is called, you can imagine the result replacing the entire function call.
In a way, this is similar to what happens when you do addition or subtraction.

## Arguments

```python arguments-example
# 1 argument
round(4.3)

# 3 arguments
print("First", "Second", "Third")
```

One of the most useful features of functions are arguments.
Arguments are values that are given to functions that affect the behavior of the function.
Arguments for a function are placed inside the parentheses, and each one is separated by a comma.
We say that these arguments are being "passed" to the function.

## Metaphor

![A picture of a machine with two slots on top and one slot on the right side. Numbers are going into the slots on top and coming out of the slot on the right. The machine is labeled as "Magic Function Box", the slots coming in are labeled as "arguments", and the slot coming out is labeled as "returns".](functions_calling_magic_box.png)

Think of a function as a magic black box.
You cannot see inside the box to know how it works, but you do not need to.
Arguments are the knobs and dials on the outside of the box that let you control its workings.
Returned values are like a slot that dispenses the results of the function.