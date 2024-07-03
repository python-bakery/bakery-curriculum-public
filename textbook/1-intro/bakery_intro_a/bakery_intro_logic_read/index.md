---
waltz:
  title: bakery_intro_logic_read
  display title: 1A7) Logic Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Logic
    slides: bakery_intro_logic.pdf
    youtube:
      Bart: UmEY8LKMRcQ
      Amy: 3gtfkhuH40w
    summary: In this lesson, you will learn about how to create logical expressions.
      In other words, how you use logic when programming.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1231 AM
  files:
    path: bakery_intro_logic_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Purpose

* Comparison Operators: Asks a question about two numbers' relationship
* Boolean Operators: Asks a question about other comparisons

One of the major reasons that programs are useful is because they can do different things depending on their inputs.
To be able to make these decisions, we need to be able to write "logical expressions".
Think of these as a question that the computer can ask about the data.
We will learn about two groups of operators: comparison operators and boolean operators.
Comparison operators ask questions about two numbers' relationship to each other.
Then boolean operators can ask questions that combine those comparisons and other questions.

## Comparison Operators

* Equaliy `==`
* Inequality `!=`
* Less than `<`
* Greater than `>`
* Less than or equal to `<=`
* Greater than or equal to `>=`

Often, we want to know about the relationship between two numbers.
For this, we use the comparison operators.
Each of these operators takes two numbers and returns either True or False.

## == (Equal Operator)

```python example-equality
print(5 == 5)
print(10 == 7)

print(5.0 == 5)
```

The most basic test is whether two numbers are equal.
This may sound weird, but in Python we use two equal signs to test for equality.
Do not use one equal sign, that means something COMPLETELY different.

## != (Not equal operator)

```python example-inequality
print(5 != 5)
print(10 != 7)

print(5.0 != 5)
```

The second most basic test is whether two numbers are NOT equal.
The operator for this is even weirder.
In Python, to test if two things are NOT equal, we use an exclamation mark and an equal sign.

## <, <=, >, >= (Greater than and Less than)

```python example-order
print(5 < 10)
print(5 <= 5)
print(10 > 5)
print(10 >= 10)
```

There are four other operators:
The less than operator, the greater than operator, the less than or equal to operator, and the greater than or equal to operator.
These four operators ask about the order of two numbers.

## Returning True or False

```python true-false
# prints True
print(10 == 10)
# prints False
print(10 != 10)
```

I said before that the operators return either True or False.
Mentally imagine the result of these operations being replaced by True or False.
If you print the value, it will literally be the text True or False.

## Boolean Operators

* Boolean `and`
* Boolean `or`
* Boolean `not`

In the same way we can add and subtract numeric expressions together, we can also combine boolean expressions together.
There are three operators for this: `and`, `or`, and `not`.

## And

```python example-and
# Literal boolean values
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Or with math
print(4 < 5 and 5 < 6)
print(5 < 4 and 5 < 6)
print(5 < 4 and 6 < 5)
```

The `and` operator returns True if both the left and right operands are True.
If either operand is false, then the result is False too.
Notice in the second chunk of code, we are combining the `and` operator with mathematical comparisons.

## Or

```python example-or
# Literal boolean values
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

# Or with math
print(4 < 5 or 5 < 6)
print(5 < 4 or 5 < 6)
print(5 < 4 or 6 < 5)
```

The `or` operator returns True if either the left or right expressions are True.
If either operand is True, then the result is True too.
This is not the opposite of `and`, but it is different.

## Not

```python example-not
# Literal boolean values
print(not True)    # False
print(not False)   # True

# Or with math
print(not 4 < 5)
print(not 5 < 4)
```

The `not` operator returns `True` if the expression is `False`, and `False` if the expression is `True`.
This is sometimes called the "negation" or "logical opposite".
Unlike the `and` and `or` operators, the `not` operator only takes in a single value.

## Nesting Logic

```python example-nesting
print((5 < 4 and 3 > 7) or (not False and 3 < 2))
print(not (not (not (not True))))
```

You can nest logical expressions, just like you could with math.
Following the logic can be tricky, just remember that the boolean operators have the lowest priority.
They will always be the last operation applied, unless parentheses upset the order.
The comparison operators have the second lowest priority.
They will be applied after any math operations, but before the boolean operators.

## Logic Expressions Are Not Distributive

```python example-not-distributive
# Correct!
print(5 < 1 or 5 < 2)

# WRONG
print(5 < 1 or 2)
```

A common beginner mistake is to think that you can distribute logical expressions.
You might think that the code shown second asks if the number 5 is less than 1 or less than 2.
But the `or` operator makes the 2 evaluated separately from the rest of the comparison.
To properly ask this question, you need to write the first statement, with the less than operator repeated a second time.
If you run the code shown, then the second printed value will be `2` instead of `False`, which you may find surprising.
In a future lesson, we will learn why this happens.
For now, just remember that you must be explicit when trying to use `or` and `and` with comparison operators.
