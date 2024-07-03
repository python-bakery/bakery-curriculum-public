---
waltz:
  title: bakery_if_syntax_read
  display title: 3A1) If Statements Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: If Statements
    slides: bakery_if_syntax.pdf
    youtube:
      Bart: wwIRRH78qbA
      Amy: FePlwjuZ_3Y
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
    modified: August 26 2022, 0108 AM
  files:
    path: bakery_if_syntax_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## The Idea of If Statements

![A box labelled "IF ___" has two arrows coming out. One arrow points to a box labelled "THEN do A" and another arrow points to another box labelled "THEN do B". Both of those boxes have arrows that converge on a fourth box labelled "Continue...".](bakery_if_syntax_overview.png)

If an expression is true, then take some action.
Otherwise, don't do take that action.
Either way, execution continues afterwards.
That's the core idea of an IF statement.

## Purpose

![Three lines of text with pictures. The first line reads "IF" followed by a raining cloud. The second line reads "THEN bring" followed by an umbrella. The third line reads "OTHERWISE do not."](bakery_if_syntax_weather.png)

If statements make code smarter.
They let you do different things in different situations.
In this example, we decide to bring an umbrella or not based on whether it is raining.
That's a simple but logical decision that we can make.

## Syntax

![An `if` statement is shown, with the components labelled as "if keyword", "conditional", "colon", "indentation", and "body".](bakery_if_syntax_diagrammed.png)

There are four parts to an IF statement.
First, you have the keyword "if".
Then, you have the conditional.
The conditional is followed by a colon.
Finally, you have the body of the IF statement.

## Conditionals

```python
if age > 21:
    pass

if "cat" in animal_name:
    pass

if rent > 2000 and rooms < 2:
    pass

if not on_fire():
    pass
```

You already learned about writing conditionals.
Conditional expressions can be variables, comparisons, function calls, or combinations using `and`, `or`, and `not`.
In the code shown here, you can see quite a few different kinds of valid conditional expressions.

## Body

```python example-body
if income > 2000:
    # Body starts here, indented
    tax = .8
    adjusted = income * tax
    print("Income:", adjusted)
    # Body ends here
```

The body of an IF statement is a sequence of one or more statements.
This body must be indented with 4 spaces.
Anything indented below the IF keyword is said to be "inside" the IF statement.
These indented statements will be executed if the conditional was evaluates to true.
Otherwise, Python will skip right over them.

## The "Else" block

```python else-example
if precipitation > 0:
    print("It is raining")
else:
    print("It is NOT raining")
```

IF statements can optionally have an `else` body.
If the conditional evaluates to false, then the `else` will be executed instead of the `if` body.
The IF body will literally be skipped over as if it didn't exist .
Only one of the two bodies will be executed!
Note the colon after the word `else`, and that it has its own body.

## Branching

![A program with an `if` statement is shown. Two lines extend from the top of the program down to the bottom. One of the lines goes straight down, while the other curves inward to follow the indentation. These demonstrate how the program might skip over or go through the body.](bakery_if_syntax_flow.png)

Think about your program as a flowing stream.
Normally it will go from top to bottom.
An IF statement changes that flow, to optionally go around.
We call that behavior branching.
Every time you have another IF statement, you have another two branches.

## Trace Tables

![A program is shown on the left, with a trace table on the right showing off its values.](bakery_if_syntax_trace_tables.png)

We have previously shown how you can make a trace table that follows the execution of an IF statement.
We now have to add an extra column to this table, to differentiate between steps and lines.
With IF statements, it is possible that a step may skip a line of code.
Even though the program shown below has 6 lines of code, it only has 4 steps!
Notice that on lines with IF statements, we still have a step, but we simply repeat the values unchanged.
