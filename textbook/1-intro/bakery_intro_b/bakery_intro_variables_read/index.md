---
waltz:
  title: bakery_intro_variables_read
  display title: 1B1) Variables Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Variables
    slides: bakery_intro_variables.pdf
    youtube:
      Bart: jrY2lmX2FLw
      Amy: eyxDCNwdNyk
    summary: In this lesson, you will learn about how to create variables by using
      assignment statements, and then read and use those variables in your programs.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 6
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1239 AM
  files:
    path: bakery_intro_variables_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Purpose

```python example-variables
cakes_needed = 4
cups_sugar = cakes_needed * 2
eggs = cakes_needed * 4
cups_flour = cakes_needed * 3
ingredients = cups_sugar + eggs + cups_flour
print("You need", ingredients, "ingredients.")
```

Variables let us store and load information.
In other words, we can "read" from and "write to" a variable with data.
This lets us use data later.
In the example code shown, the variables are `cups_sugar`, `eggs`, and `cups_flour`.

## Metaphor

![The number `87` is inside of a box labeled `total_age`, with an arrow coming into and out of the box.](intro_variables_box_model.png)

You can think of a variable as a box that holds data.
That data could be a number, a string, or any type of data.
After the data is put in, we can take it out later.

## Variables vs. Data

```python printing-literals
# Printing literal
print(14 * 7)

# Write-and-read variable
age = 14 * 7
print(age)
```

Anywhere that you use literal data, you can replace it with a variable.
In this example, we have extracted the math expression to a variable.
That variable can then be used in subsequent lines.

## Different from Math

```python update-variable
football_score = 0
print(football_score)
football_score = 10
print(football_score)
football_score = 27
print(football_score)
```

Variables in computing are very different from variables in math.
In math, a variable is an unknown that we are solving for.
In computing, we always know the value of a variable, but we are manipulating it.
A variable varies over time, but according to instructions that the programmer has written.
That means that you can change the value in the variable, even though that wouldn't have
been possible in math class.

#### Names

```python mystery-temperature
# Is this temperature in celsius? Or fahrenheit? Who knows!
temperature = 20

print("The temperature is", temperature)
```

Variables are defined by their name.
Names are absolutely crucial in programming, and choosing them is an art.
Names are best when they are accurate, meaningful, and concise.
We use good variable names to communicate clearly; not just with other programmers, but with ourselves as we try to figure out code that we have written.
Of course, computers do not understand variable names; their meaning only matters to humans.

#### Naming Rules

* Names can only have letters, numbers, and underscores
* Names must begin with a letter or underscore

There are two rules for naming variables.
First, names can only have letters, numbers, and underscores (_).
Second, names must begin with a letter or underscore.
You can use underscores to serve as spaces between words, since spaces are not allowed in variable names.

## Naming Suggestions

* Clear: understandable without explanation
* Concise: not too short, not too long
* Correct: name accurately reflects the value
* Consistent: same style throughout program
* Conventional: matches style of other programmers

Although there are only two hard rules, we have five suggestions for good variable names.
You might find it helpful to remember them as the Five Cs.
First, variable names should be clear.
Someone looking at the variable name should understand its meaning without needing additional explanations.
Second, the name should be concise, meaning neither too short nor too long.
Third, the name should be correct.
Although this may sound obvious, far too often programmers will let a variable not accurately describe the data the variable holds, and refuse to fix it.
The last two suggestions are for variables to be consistent and conventional.
Being consistent means having the same style throughout the program, while conventional means the same style as other programmers.
When we say style, we say things like using certain abbreviations, or using underscores consistently in place of spaces.
There are many other kinds of stylistic choices, but we'll learn them as we go.

## Lazy Naming

```python lazy-naming
x = 147
k = x * 2 + 4 - x
print(k)
```

Many novice programmers don't understand the value of good variable names.
They are eager and excited to write programs, willing to cut corners in their haste.
Sometimes, this means they will choose variable names like `x` or `k`.
What do those variable names mean? Who knows, certainly not anyone coming to read the code later on.
Don't be lazy when picking variable names.
Yes, having to actually think while coding is unpleasant, but sometimes we have to do hard things.