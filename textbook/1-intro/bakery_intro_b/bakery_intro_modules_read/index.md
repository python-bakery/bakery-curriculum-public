---
waltz:
  title: bakery_intro_modules_read
  display title: 1B3) Modules Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Modules
    slides: bakery_intro_modules.pdf
    youtube:
      Bart: n_-r45H6P08
      Amy: _t1RIhD_bSU
    summary: In this lesson, you will learn how programs are composed of statements
      and expressions into modules.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 5
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1242 AM
  files:
    path: bakery_intro_modules_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Sequential Execution

```python step-by-step
count = 0                # Step 1
print(count)             # Step 2
count = count + 5        # Step 3
count = count + 2        # Step 4
print(count)             # Step 5
```

Programs execute line by line, one step at a time.
Many times, the programs run super fast, and you won't see this behavior. 
We have some tools that let us slow down and see the execution.
But either way, programs run one line at a time.

## Metaphor

![A picture of a person reading a book, with an arrow pointing down the page.](intro_modules_reading.png)

Think about reading a book or acting out a script, how we move down a page.
This is just like how the instructions of a program are read.

## Time

![A clockwatch is next to some lines of code. Below the lines of code, annotations indicate how long the code took to run for each line.](intro_modules_time.png)

The result of this step-by-step instruction is that programs are executed *over time*.
Although execution happens very, very fast, it does not happen all at once.
Time is a crucial component in running programs.

## Statements

```python example-statements
# Assignment statement
count = 5

# Print statement
print(count)
```

A single line of code is known as a "Statement".
A program is really a collection of statements.
We call this collection the "body" of a program.
There are many kinds of statements, but we only know about a few so far.

## Expressions

* Literal values: `5`, `10.0`, `True`, `"Hello"`, `None`  
* Math operations: `1 + 2`, `4 - 5`, `8 / 4`  
* Logic operations: `5 > 4`, `False or not True`  
* Variables: `age`, `score`, `my_string_variable`
* Nested expressions: `(1 + 5) > age and not True`

An expression is any kind of combination of literal values, arithematic operators, boolean operators, and variables.
Any value is an expression.
Any variable is an expression.
Expressions can be made up of expressions.

## Connecting Statements and Expressions

![On the left, a picture of BlockPy statement blocks highlighting that they have vertical notches (an assignment block and a print block).  On the right, a picture of BlockPy expression blocks highlighting that they have only a rounded connecting edge on the left (an addition block, a string value block, and a number value block).](intro_modules_statements_expressions_blocks.png)

In BlockPy, you can see that expression blocks have a rounded left edge.
Statement blocks have a pointy bit on the bottom and a notch on the top.
This visually shows you the difference between statements and expressions.

## Order is Important

![A picture of a confused person looking at a series of book chapters out of order: "Chapter 15", "Chapter 1", "Prologue", "Chapter 5".](intro_modules_order_matters.png)

Since programs run from top to bottom, the order of statements is important.
If you rearranged the sentences of a book at random, they wouldn't make much sense - the same is true for programs.
