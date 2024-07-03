---
waltz:
  title: bakery_for_primer_read
  display title: 6) Primer
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: true
  additional settings:
    small_layout: true
    youtube:
      Bart: CxOl_iwL1Wg
      Amy: vQHeZcG7OVc
    header: For Loops
    summary: Note that there is a second page in this Primer, containing a reference
      sheet for the Loop Patterns! Make sure you download a copy of that reference
      sheet!
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: September 24 2022, 0208 PM
  files:
    path: bakery_for_primer_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Introduction to For Loops

```python simple-loop
names = ["Ada", "Babbage", "Captain"]

for name in names:
    print(name)
```

Writing the same code over and over again, in order to do something multiple times, is tedious and likely to lead to mistakes.
That's why we have loops to let us do an action repeatedly.
In Python, the most common looping construct is the `for` loop, which works directly with lists.
Using a `for` loop, each element of the list is processed one at a time.
A `for` loop has three major components: the iteration variable, the iteration list, and the body of the loop.
The iteration list is the variable following the `in`, and represents the data we are going to iterate over.
The variable before the `in` is the iteration target, and it will be a newly created variable that did not exist prior to the loop.
The iteration variable is key to understanding the `for` loop, since it represents each element of the list, but only one at a time.
That iteration variable is available inside the body of the `for` loop, which will be executed one time for each element of the list.
Each time the loop executes, the iteration variable gets set to a new value from the list, until the list is empty.

## Loop Patterns

![Two blocks of code side by side. The left side shows the Sum Loop Pattern, and the right side shows the actual code that would be based off that pattern.](bakery_loops_primer_use_template.png)

Because there are so many ways to use `for` loops, we focus on covering loop *patterns*, which are reusable code templates to
solve commonly occuring problems involving loops.
To use the loop pattern, you copy and paste the pattern into your program and fill in the blanks.
You are always going to have certain blanks to fill in, like the fact that there's an original list you are iterating over, an iteration variable, and some kind of resulting value from the loop.
However, past that, the actual patterns vary quite a bit between each other.
Sometimes, you have to make alterations to the template, or use more than one line to capture the original idea.
At the end of the day, the patterns are only guidelines, not concrete rules.
We use the patterns as a teaching guide to help you get started with loops, although they do reflect the kinds of loops that professional programmers write all the time.

## All the Patterns

* Count: Count how many elements are in a list
* Sum: Add up all the numbers in a list
* Accumulation: Combine elements into a single value
* Map: Modify all the elements of a list
* Filter: Remove elements from a list
* Find (First and Last): Get an element based on its value
* Take: Remove elements past a certain point in the list
* Minimum/Maximum: Get the highest or lowest value in a list

The complete list of Loop Patterns covered in this chapter is shown here.
As you can see, there are quite a few patterns.
Let's quickly run through each one.
The Count pattern is used to determine how many elements are in a list, and works on any kind of list.
The Sum pattern only works on lists of numbers, in order to add them all together.
However, the Sum pattern is related to the Accumulation pattern, which generalizes summing to other types like strings and booleans.
The Map pattern is more distinctive, letting you create a new list based on an old list, modifying each value along the way.
The Map pattern might be used to convert elements from one type to another, but it might also be used to just change a value without changing its type.
The Filter pattern is used to create a new list by only keeping certain elements, through the use of an `if` statement embedded inside of the loop.
The Find pattern also uses an `if` statement, but only determines a specific element rather than producing an entire list.
The third related pattern is Take, which also produces a list based off the original list, but this time removes all the elements until a certain condition is encountered.
Note that Find and Take are different from indexing and subscripting, since they are based on the actual values of the list rather than their positions.
Finally, there is the Minimum and Maximum patterns, which find the lowest and highest values in the list, respectively.

## Loop Composition

```python loop-composition
def remove_dollars(amounts: list[str]) -> list[str]:
    new_amounts = []
    for amount in amounts:
        new_amounts.append(amount[1:])
    return new_amounts

def sum_amounts(amounts: list[str]) -> int:
    total = 0
    for amount in amounts:
        total = total + int(amount)
    return total

dollars = ["$1", "$5", "$10", "$1"]
print(sum_amounts(remove_dollars(dollars)))
```

Working with loops can be quite tricky, even with the patterns helping you.
When you need to do multiple loop patterns all at once, you can sometimes get overwhelmed with the logic of the loops.
The final part of this chapter describes how you can compose loops using functions, where each function only implements
one loop pattern.
Although this increases the number of functions you have to write and test, there can be some huge advantages when you start working with more complex programs.
First, each function can be tested in isolation, to make sure that it works.
Second, the pieces of the functions are reusable, so you might save yourself some work later.
Third, the final problem becomes easier to think about, as demonstrated by the final line of code here, where we can simply compose a few function calls to achieve our purpose rather than having to look at a single big ugly `for` loop.
Each individual function only does one thing, and does it well, so we can determine any mistakes in that function more easily.