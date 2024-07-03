---
waltz:
  title: bakery_time_complexity_read
  display title: 9B1) Time Complexity Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Time Complexity
    youtube:
      Bart: ZTYq5nlvJaw
      Amy: Ct0eiVchytw
    summary: ''
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 11
    created: June 28 2022, 0300 PM
    modified: November 13 2022, 0717 PM
  files:
    path: bakery_time_complexity_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Questioning a Program

* Correct?
* Readable?
* Fast?

The first question a Computer Scientist asks about a program is whether the program is correct.
An incorrect program will not solve the problem it sets out to solve, and therefore is probably not useful.
The second question a Computer Scientist asks is whether the program is readable.
Although this may not seem important, you must remember that programs often end up living for a long time, and need to be read and debugged.
If a program is not understandable, then the program is not able to updated or improved.
But the last question that a Computer Scientist asks, is how long the program takes to run.

## The Length of a Program

![A diagram showing how wall clock time is calculated.](bakery_time_complexity_wall_clock.png)

There are several obvious ways to measure the length of a program.
An incorrect way would be to measure the number of lines of code.
With `while` and `for` loops, we have seen how even just a few lines of code can do an awful lot of work.
Relying on the number of lines of code as a measure of the length of a program is too limited.
An alternative approach that is much more helpful is to measure the amount of time the program takes to execute.
Imagine starting a watch when the program begins, and then stopping the watch when the program ends.
You take the difference between the two times, and that's the length of the program.
This is sometimes called the wall clock time.
This is much more accurate, but has the major downside that now we have to sit and measure our running programs to understand how long they take.

## Bigger and Bigger Data

* Empty list (zero elements, tiny)
* A list with one number (small)
* Ten number list (still small)
* One hundred elements (a little bigger)
* A million elements (big)
* A trillion elements (very big!)
* ...

Programs are useful because they can be given different inputs each time the program is run, and they will deliver the appropriate outputs.
With functions, for example, we can change the arguments as long as they still match the general type of the parameters we specified.
Integers can be higher numbers, strings can have more characters, and lists can have more elements.
These different sizes of values reflect the *size* of the input.
Sometimes, the size of the input can have an impact on how long the program takes to execute.
If we are adding up the elements of a list, then having more elements to add will take more time.
In other words, the time of the program often has a relationship with the size of the input to the program.

## Time as an Equation

![A table with two columns, number of elements and running time, showing off the relationship between these two values.](bakery_time_complexity_table.png)

A mathematical function establishes a relationship between one value and another value, unlike a programming function.
This mathematical function, or equation, can be determined by analyzing the trend over a bunch of example inputs and outputs.
In the table shown here, we match the number of elements with the running time of the program that we measured.
Careful analysis reveals that in this case, the relationship is that every new element takes 2 additional microseconds of work.
This is a time function, and can help you make predictions about how your program would run for different sizes of input.
Of course, in the real world, the trends are rarely so nice and neat.
How many datapoints do you need in order to accurately predict the future?
That is a very difficult question to answer.
Any time you think you see a trend, the next data point might sink your hypothesis.
Ideally, you would gather as much data as possible.
Unfortunately, that is still very time consuming.

## An Estimate

* Random-Access Machine (RAM) Model: Estimate execution time based on common operations

Measuring the number of lines in a program is easy, but very inaccurate.
Measuring the time taken with a watch is accurate, but could take a long time.
If Computer Scientists had to sit and wait to check the runtime of every program they wrote, they would never get anything done.
One approach that acts as a middle path is to make an estimate of the time by tracing the program, but with a simplified model of execution.
Computer Scientists have developed an approach called the Random-Access Machine, or RAM, Model that does exactly this.

## The RAM Model

* Assignment: One step
* Printing: One step
* Math/Logic Expression: One step
* `if` statement: One step
* `for` loop: N steps
* `while` loop: Varies
* Function call: Varies

In the RAM Model, most simple actions such as assignment or printing takes a single step.
In fact, all math and logic expressions take a single step too, even if there are many operations inside of the expression.
However, `for` and `while` loops are more complicated, as are function calls.
The `for` loop is not usually so bad, since it usually means that we just have to do one additional step for each element
of the input.
But with `while` loops and function calls, we cannot easily predict the time of the program.
This gets even more complicated when we start nesting functions inside of functions, or loops inside of loops.
By counting the number of steps using this model, though, we can get an estimate of the program time without waiting around, and can figure out a relatively accurate possible mathematical relationship.

## Common Math Relationships

* Constant: Input size does not affect run time (simple math, accessing attribute in class)
* Linear: Every additional input leads to a constant amount of extra time for every element (summing a list, filtering a list)
* Quadratic: Every additional input leads to a linear amount of extra time for every element (nested list iteration)

In general, we we will start off with three basic relationships.
There are many other kinds of relationships, one for each possible line you could see on a graph.
But for now, we want you to master these three.
The first is a constant relationship, which is when there is no relationship at all between the size of the input and how long the program takes to run.
This is common for simple mathematics, accessing attributes in classes, and the actual step of starting a function call.
The next relationship is linear, where every additional input requires another single unit of time.
This happens easily with list operations, such as summing or filtering a list.
The last relationship we'll talk about here is quadratic, where the input size increasing means linearly increasing the time required for every element.
We see this when we are iterating through a two-dimensional list. Each time we add another row, we are really adding a bunch of elements.
Quadratic growth can get out of hand quite quickly, and is not a good situation to be in.
Ideally, our programs would be constant time, but that is rarely the case for most interesting programs.

## An Iterative Example

```python runtime-example
values = input("Enter comma-separated numbers:")
numbers = values.split(",")
total = 0
for number in numbers:
    total = total + int(number)
print(total)
```

Let's take a look at a program with a linear relationship.
In the example shown here, we ask the user to enter a comma-separated list of numbers.
We have no idea how many numbers the user will enter, so it might be a lot of elements.
That `for` loop is going to have to do another addition for each element that we have in the list.
So in the end, we'll do a linear amount of work, based on the input given by the user.

## Key Points about Time Complexity

* Input size relates to program time
* Basic relationships are constant, linear, and quadratic
* The RAM Model can be used to estimate relationships
* Wall clock can be used to determine relationships

We are merely scratching the surface of the concept of Time Complexity, and you will see this concept many more times on your journey to be a Computer Scientist.
For now, focus on understanding how different input sizes can lead to different runtimes.
Try to get a handle on the relative sizes of the different relationships.
You can use the RAM model to estimate those relationships based on what the code does.
And when in doubt, try running the program with different sizes and measure the speed, to try to determine the relationship yourself.