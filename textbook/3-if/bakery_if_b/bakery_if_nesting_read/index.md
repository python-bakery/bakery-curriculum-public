---
waltz:
  title: bakery_if_nesting_read
  display title: 3B1) Nested If Statements Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Nested If Statements
    slides: bakery_if_nesting.pdf
    youtube:
      Bart: xE5tpGx9jkg
      Amy: 2fpzaBueVDU
    summary: In this lesson, you will learn about IF statements. These affect the
      flow of your program so that you can do different things at different times.
      In other words, IF statements make your program smart and adaptable to different
      situations.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0112 AM
  files:
    path: bakery_if_nesting_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Nesting

```python age-price-example
age = 22
cost = 45

if age > 21:
    if cost < 10:
        print("Buy")
    else:
        print("Too expensive")
else:
    print("Too young")
```

A program is made up of a sequence of statements, known as a body.
We sometimes refer to bodies as a block or chunk of code.
With `if` statements and function definitions, we have ways of putting a smaller body inside of the main global body.
But now, we will see that we can also put `if` statements inside of `if` statements and functions.
We call this "nesting" the bodies inside of each other.
As you develop more complex programs, you will do a lot of nesting.

## Number of Spaces

![Code is shown on the right, with nested if statements. On the left, annotations point out that there are: 0 spaces on the first and sixth lines; 4 spaces on the second, fourth, and last lines; and 8 spaces on the third and fifth lines.](bakery_if_nesting_number_spaces.png)

Every time you nest a block of statements inside another block, the body of the block gets indented another 4 spaces.
Observe the Python code on the right, and the numbers on the left.
Each level of nesting increases the number of space characters by 4.
These are called the whitespace rules, and they can be confusing, but they are consistent.
The amount of whitespace controls what code is in what body.

## IF and Functions

```python nested-if-function
from bakery import assert_equal

def adjust_price(price: float, age: int) -> float:
    if age > 60:
        return price * .8
    else:
        return price

assert_equal(adjust_price(5.75, 63), 4.60)
assert_equal(adjust_price(5.75, 45), 5.75)
```

You can put `if` statements inside of functions.
In fact, this is both common and useful.
Remember the whitespace rules when this occurs.
Each nested block is another 4 spaces in.
In this function `adjust_price`, the first line of the body is indented four spaces, but the second line of the body is indented 8 spaces.
The first line after the body of the function is not indented; in fact, that's what makes it the first line AFTER the body, is that it's not indented.

## What Goes Inside?

```python inside-outside
cost = int(input("What is the cost?"))

# One line in body
if cost > 5:
    discount = 1
price = 2

# Two lines in body
if cost > 5:
    discount = 2
    price = 3
```

It can be difficult to know if a line of code belongs inside or outside of a block.
You must think critically what you are trying to do with the `if` block.
Remember: statements inside the `if` block are executed only if its conditional evaluates to `True`.
In the code shown here, the first assignment of the `price` variable is AFTER the `if` statement's body, while the second assignment is INSIDE of the `if` statement.
That means the first assignment will always be executed, but the second assignment may or may not be executed depending on the value of `cost`.

## ELIF block

![Two equivalent blocks of code are shown, one with an elif statement and one with a combination of else and if statements.](bakery_if_nesting_if_elif.png)

In addition to the `if` and `else` blocks, there is a third type: `elif`.
The `elif` is exactly equivalent to an `else` block with an `if` statement inside.
Although they do not offer any new power, they are sometimes more convenient to write.

## Two IFs vs ELSE IF

![Two NOT equivalent blocks of code are shown, one with a pair of `if` statements and one with an `if` and `elif` statement](bakery_if_nesting_if_if_elif.png)

The following two pieces of code may look similar, but they are quite different.
The code on the left has two IF statements, and both will always be evaluated and potentially executed.
The code on the right has an ELIF statement, and the second will only be evaluated if the first one evaluates to false.

## Unnecessary IF

```python unnecessary-if
def check_senior(age: int) -> bool:
    # This `if` statement is unnecessary!
    if age > 60:
        return True
    else:
        return False

# Exactly equivalent to
def check_senior(age: int) -> bool:
    return age > 60
```


Two kinds of mistakes are very common with IF statements.
The first common mistake is using an IF statement when a conditional expression is fine on its own.
For example, consider this function definition that returns True if the parameter is greater than 5, or otherwise returns False.
The conditional expression already evaluates to either True or False, so it was unnecessary to use an If statement.
Instead, you can directly return the result of the conditional expression, as shown on the right.
**You do not need to use `if` statements if you are just returning `True` and `False`!**

## Unnecessary Test

```python unnecessary-test
def check_toddler(age: int):
    # The `== True` part is redundant!
    return (age >= 5) == True

def check_toddler(age: int):
    # Much better!
    return age >= 5
```

A second common mistake is to test if a Boolean expression is equal to True.
Although the expression here, `age >= 5 == True`, reads like it makes sense in English, it is redundant in Python.
`age > 5` already evaluates to either `True` or `False`.
If you compare a Boolean value to `True`, then the result is the same Boolean value.
Nothing is accomplished, you have simply made your code more complex.
It's just like adding zero or multiplying by one, or adding the empty string to a string.
Literally nothing happens.
True would become True, and False would become False.
