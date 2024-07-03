---
waltz:
  title: bakery_time_while_read
  display title: 9A1) While Loops Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: While Loops
    youtube:
      Bart: VA64IYVPPUU
      Amy: -Voqgfi7UxE
    small_layout: true
    summary: In this lesson, you will learn about a new kind of loop called WHILE
      loops. These loops are somewhat different from FOR loops, and in fact act more
      like IF statements. Although more powerful than FOR loops, they have some disadvantages
      - we will use them sparingly.
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 5
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0623 PM
  files:
    path: bakery_time_while_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Another Kind of Iteration

```python
while condition:
    pass
```

`for` loops allow us to iterate through each element of a list.
They are the most common form of iteration in Python.
However, there is another kind of iteration that is useful, called `while` loops.


## Syntax

![A while loop is annotated with the terms "While keyword", "Conditional", "Colon", and "Body":](bakery_time_while_loop_syntax.png)

Notice how the syntax for a `while` loop is similar to that of an `if` statement.
We have the word `while`, followed by a condition, ending with a colon.
Then we can have any number of statements inside the body.
Remember that this body, like a FOR loop or an IF statement, is indented with 4 spaces.

## A Simple Example

```python runnable-while
count_down = 4

while count_down > 0:
    count_down -= 1
    print(count_down)
    
print("Reached the end")
```

In this runnable example, you can see intialization before the loop, the condition of the loop, the body of the loop, and then output after the loop is complete.
Most `while` loops need some kind of variable that is defined before the loop, used in the conditional, and updated inside the loop.
Otherwise, the loop will continue forever.
In this example, we are repeatedly decreasing the `count_down` variable, printing its value each time, until the variable's value is 0 or less.

## Like IF Statements

![An arrow traces the flow in the code below, with a branch at the end of the loop's body: one branch moves back up to the start of the loop, and the other moves further downward.](bakery_time_while_loop_flow.png)

`while` loops are actually very similar to `if` statements.
However, instead of executing once or none, they will execute repeatedly until the condition is false.
Note that a loop won't end until the condition evaluates to false - even if the condition would be false during the loop body, the loop can't end until the end of the body.

## Tracing the Flow

![The code from before is shown with arrows indicating how many time each chunk of code executes, with the `while` loop arrow indicating it loops four times.](bakery_time_while_tracing_the_flow.png)

When a `while` loop is executed, the program follows a similar looping behavior as a `for` loop.
Here we can see that behavior in a `while` loop to count down from 10.
The program tests the condition, and if it is true, then it moves through each statement in the body.
Then, it returns to the top and tests the condition again.
If it is still, true, it repeats the previous loop.
Otherwise, if the condition is ever false, before the body is executed the first time, then the program skips to the end of the `while` body.

## Looping Forever

![An annotation points out that the first line of the loop only increases the variable, so it never reaches 0.](bakery_time_while_loop_bad.png)

A tricky thing about WHILE loops is that it is easy to loop forever by accident.
Consider the incorrect code below.
Because the variable `count_down` is only ever increasing, it will never reach zero and the loop never ends.

## Unnecessary While Loops

```python while-vs-for
# While loop version
index = 0
while index < 10:
    index += 1
    print(index)

# For loop version
for index in range(10):
    print(index)
```

A major advantage of `for` Loops instead of `while` Loops is that they terminate based on a list, so they are very unlikely to loop forever.
When possible, you should probably use a `for` loop instead of a `while` loop.
As an example, consider the counting code shown here.
Instead, that same code can be efficiently replaced with a `for` loop that calls the `range` function, to achieve the same effect.

## Power of While

* For loops: Safe form of finite iteration over a list or range
* While loops: Powerful form of unbounded iteration based on a condition 

So why would you want to have `while` loops, if `for` loops are so convenient and safe?
The tradeoff is that `while` loops are able to handle more forms of loops.
Because a `while` loop can work with an arbitrary condition, it is not limited to the length of a list or a known range of numbers.
While a `for` loop is a kind of *finite* iteration, a `while` loop can potentially last infinitely and iterate in other ways.
Although there *are* advanced techniques to make `for` loops more powerful, the reality is that many kinds of problems are more naturally solved with a `while` than a `for` loop.
That said, the real power lies in knowing when to use one or the other.
If all you need to do is go through a list or a range of numbers, stick with `for` loops.
In the next section, we will learn other uses for `while` loops.
