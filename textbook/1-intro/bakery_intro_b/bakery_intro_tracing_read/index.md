---
waltz:
  title: bakery_intro_tracing_read
  display title: 1B2) Tracing Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Tracing
    slides: bakery_intro_tracing.pdf
    youtube:
      Bart: iZ1Y0iRmYnI
      Amy: 92PerPC2fG4
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1241 AM
  files:
    path: bakery_intro_tracing_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Reading and Writing Variables

```python variable-reading-writing
# Writing variables
my_int_variable = 5
my_str_variable = "hello"
my_bool_variable = True

# Reading variables (and printing them)
print(my_int_variable)
print(my_str_variable)
print(my_bool_variable)

# Read AND write variable
my_int_variable = my_int_variable + 3

# Reading variables again (and printing again)
print(my_int_variable)
```

To write to a variable, you put its name on the left side of an "assignment statement".
To read from a variable, you simply use its name.

## = vs. ==

```python equality-assignment
# Assigning to a variable
current_hour = 7
print("The current hour is", current_hour)

# Equality operation
print(current_hour == 12)

# Assigning the result of an equality operation
is_midnight = current_hour == 12
print("Is it midnight?", is_midnight)
```

Notice that assignment statements use a single equal sign.
We mentioned before that the equality operator uses two equal signs.
They may appear to be visually similar, but they are distinct.
Assignment statements update the value in a variable, while equality operators ask a question about values.

## Lifetime

```python variable-lifetime
football_score = 0
print(football_score)

football_score = 10
print(football_score)

football_score = 27
print(football_score)
```

Variables have a lifetime.
At some point in the program, they are initialized, and then later on they are used.
At any given time, you can ask what the value of a variable is, and change it.
In the program shown here, the variable has a different variable each time it is printed, because of the assignment statements.

## Read after Write

```python read-after-write
# This will work
alpha = 5
print(alpha)

# This will NOT work!
print(beta)
beta = 5
```


A variable cannot be read until it has been written.
If you attempt to read an unwritten variable, an error will occur.
Make sure that any time you are reading a variable, make sure you have an assignment statement preceding it.

## Update

```python example-update
count = 0
count = count + 1
count = count + 1

print(count)
```

We often want to increase or decrease a variable by a variable.
For instance, when we're counting the number of things in a list, we need to add one to a existing variable.
In the code shown here, we have a variable on the left and right hand side of the assignment statement.
This really highlights the difference between math and computing.
In algebra, it would have been impossible to write that statement, because you were solving for the variable.
But in computing, you are ASSIGNING to the variable.
You are overwriting whatever was there before.
That's why you should read this statement starting from the right side first.
The expression literally means, "Evaluate the expression on the right and update the variable on the left with the result".

## Tracing

```python example-tracing
# Variable does not exist yet
count = 0
# count is 0
count = count + 5
# count is now 5
count = count + 2
# count is now 7
```

It is often useful to track the value of variables over time.
We call this "tracing" a variable.
Although the computer only keeps track of the latest state of the variables, we humans want to think about the entire lifetime of the variables.
Often, to debug a program, we will write down the name of each variable on a piece of paper.
Then, we check each line of the program, one at a time, writing down the variable's value next to its name whenever the variable is assigned.
If the variable already has a value, you cross out the value and replace it with the new value.

## Initializing and Updating

```python initialize-update
# Initialization
count = 0

# Update
count = count + 5

# Read
print(count)
```

The first time a variable is written to, we say that that variable has been "initialized" or "created".
Any time after that, writing to the variable is referred to as being "updated" or "changed".

## Terminology

* Write: Set, Store
* Initialize: Define, Create
* Update: Change, Increment
* Read: Use, Load

Besides "reading" and "writing", there are many other words. You should get a sense of the different ways we refer to variables.

