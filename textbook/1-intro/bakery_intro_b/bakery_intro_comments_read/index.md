---
waltz:
  title: bakery_intro_comments_read
  display title: 1B4) Comments Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    small_layout: true
    header: Comments
    slides: bakery_intro_comments.pdf
    youtube:
      Bart: hkxAEemC3m4
      Amy: FD3nBWlN5zI
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 9
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1244 AM
  files:
    path: bakery_intro_comments_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Code is Confusing

![Picture of a human looking confused, while a computer looks happy.](intro_comments_confusing_code.png)

Code is confusing. There's no way around it.
Figuring out what a program does is often just as hard as writing the code in the first place, and sometimes even harder.
Bad code is so easy to write.
Comments are a way for programmers to understand what code does.
They are written explanations embedded directly in the code that explain the code to the reader.
The computer does not care about comments, and do not even look at them.
They are expressly for humans to make code less confusing.

## Comments in Python

```python example-comments
print("This line is executed!")

# All the following lines are valid, because they're comments
# This line is not executed
# 1 / 0
# 5 = a
```

In Python, the main way of writing comments is to use the Hash symbol (`#`), also known as the Octothorpe or pound sign.
When Python runs your program, it first scans for any hash symbols.
Those symbols and ALL text following it on the line are then removed.
The only exception to this rule is if a comment is inside of a literal string value.
Otherwise, comments are always removed from any Python program.

## Tracing Comments

```python skipped-lines
print("First line, first step.")
# Skipped line!
print("Third line, second step.")
```

Because commented code is removed from the program, Python will skip over those lines when running your code.
This is one reason why, when tracing your program, the current line and the currently executed step might not be the same.
In the program shown here, the second line is commented out, meaning the second step is actually the third line executed!

## Improving Names to Avoid Comments

```python better-names
# Store the current time (42 minutes)
x = 42
# Convert to hours, add the offset
y = x / 60 + .5
# Print result
print(y)
# ----------------------------------------
# Convert the time from minutes to hours, with an offset
minutes = 42
hours = minutes/60
offset = .5
time = hours + offset
print(time)
```

Comments aren't always necessary.
Sometimes, instead of trying to add additional explanations about code, you should just make the code less confusing.
For example, in the code shown here, the first version uses variable names that are vague and confusing.
But the second version has better variable names, which make it easier to understand the code's purpose.
This is especially as programs get bigger and more complex, where explaining every line has more of a penalty.

## How Many Comments Are Enough?

* Extreme opinion: Comment every line
* Opposite extreme opinion: Never comment
* Reasonable middle ground: Comment confusing code

How many comments should you write?
Opinions vary, and there's no perfect answer.
Some people believe you should explain every line.
Some people believe that comments should never be necessary, since you should just write the code to be more clear.
A middle stance, that we support, is to write comments for any code that is unexpected or surprising.

## Commenting Out

```python commented-out
minutes = 42
## Used to be integer //, now float / for correctness
# hours = minutes//60
hours = minutes / 60
offset = .5
time = hours + offset
print(time)
```

Comments can also be used to temporarily remove code. We call this "commenting out" code.
However, removing code using comments is generally bad practice.
In future courses, you can learn more advanced ways to keep track of code over time.
But for now, when you are thinking about how to share code with others, remove any comments that don't help explain the existing code.
If you are going to comment out code, be sure to leave an additional comment for yourself explaining what that old code was there for.
Remember, you are going to forget what a program does. The less time spent trying to remember, the better your future life will be.