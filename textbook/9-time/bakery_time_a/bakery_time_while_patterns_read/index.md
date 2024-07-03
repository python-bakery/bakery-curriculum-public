---
waltz:
  title: bakery_time_while_patterns_read
  display title: 9A2) While Loop Patterns Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: While Loop Patterns
    youtube:
      Bart: rzJgYfnj3l0
      Amy: q9kHljJQHrs
    summary: ''
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 11
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0625 PM
  files:
    path: bakery_time_while_patterns_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## While Patterns

* Numeric While
* List While
* Read-Evaluate-Print-Loop
* User Input Loop
* Random Looping
* Main Game/Server Loop

We have previously seen a number of loop patterns related to `for` loops.
This time, we will see general patterns that are useful for `while` loops.
The `while` loop patterns vary much more widely than the `for` loop patterns, since the power of a `while` loop is more unbounded.

## Numeric While

```python numeric-while-example
counter = 100
while counter > 1:
    counter = counter // 2
    print(counter)
```

We have already talked about how `for` loops are better for iterating over a range of numbers.
However, one immediate advantage for `while` loops is when we need to iterate through numbers non-sequentially.
In the code shown below, instead of decreasing by one each time, we are instead halving the value in `counter`.
This demonstrates exponential decay, and will decrease much more rapidly down to a number less than one.
Any kind of numeric conditions can be used with `while` loops, making them more flexible than `for` loops with numbers.

## List While

```python list-while-example
targets = [2, 3, 5, 4, -1, 1]
index = 0

while targets[index] != -1:
    index = targets[index]
    print(index)
```

Just as we saw that a `while` loop can replace a `for` loop for processing numbers, we can also use the `while` loop to process a list.
This allows us to process the list in interesting ways that previously were not possible with simple `for` loop, which just iterates through the sequence from start to finish.
Now, we can jump to different places in the list.
As before, however, you must be careful to avoid accidentally looping forever or indexing out of bounds.
Remembering to update the current index is very important.
Before you run this program, try to predict what will be printed.

## Read-Evaluate-Print-Loop

```python repl-loop
command = ""
while command != "EXIT":
    command = input("Input a word, or write EXIT:")
    print("You wrote", command)

print("No more words!")
```

Another use case where a `while` loop is more useful than a `for` loop is dealing with repeated user input.
For instance, the Read-Evaluate-Print-Loop (or REPL) that powers the Console uses a `while` loop.
The pattern shown here is one way to handle repeated user input.
This repeatedly asks for words until the string `"EXIT"` is given, at which point it will exit the loop.

## Check User Input Loop

```python check-user-input
user_input = input("What is your age?")
while not user_input.isdigit():
    user_input = input("Age must be a number!")
age = int(user_input)
print("Your numeric age is", age)
```

Users are notoriously untrustworthy, and they often make mistakes.
A `while` loop can be used to safeguard user input and make sure that they are correctly entering data.
The pattern is similar to before, where we repeatedly get user input until a condition is satisfied.
In this example, we are repeatedly looping until we are given digits for the `age` variable.

## Random Looping

```python random-looping
from random import randint

first_number = randint(0, 10)
second_number = randint(0, 10)
while first_number == second_number:
    second_number = randint(0, 10)

print(first_number, second_number)
```

Another interesting use case for a `while` loop is to repeatedly pick random numbers.
This is less of a specific pattern, and more of a general use case, but the principle is the same each time.
Basically, we use random (also known as stochastic) processes to repeatedly try solutions until one satisfies our constraint.
In this example code, we want to pick two different numbers, so we call the `randint` function twice.
If the second number is the same as the first number, we repeatedly reroll the second number until the two numbers are different.
There are often ways to achieve the same effect using complicated math, but a `while` loop can be straightforward solution.
Of course, in the worst case scenario, we might end up rolling badly each time, and waste a lot of time waiting to find a good number.

## Main Game/Server Loop

```python
while True:
    pass
```

One more kind of loop you will occasionally see, but rarely write, is the main game loop, also sometimes used for servers and other long-running programs.
Essentially, this is a loop that is never supposed to end.
Some programs, such as games or websites, are not really supposed to end.
The user is expected to just keep interacting with the game, until the computer is intended to be shut down.
Therefore, the loop uses the unconditional value `True` for its condition, meaning its body will repeatedly execute.
Do not try running this program, unless you know what you are doing.
Almost always, other software, like Designer, will handle this kind of loop for you.