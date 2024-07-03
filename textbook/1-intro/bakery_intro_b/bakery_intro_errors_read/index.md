---
waltz:
  title: bakery_intro_errors_read
  display title: 1B8) Errors Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Errors
    slides: bakery_intro_errors.pdf
    youtube:
      Bart: 2ElcRMGPzI0
      Amy: nF52lYUxmPI
    summary: In this lesson, you will learn how Python reports problems with your
      program, and how to respond to those errors.
    small_layout: true
    disable_tifa: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 6
    created: June 28 2022, 0300 PM
    modified: September 05 2022, 0940 PM
  files:
    path: bakery_intro_errors_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Purpose

![A picture of a computer with the word "ERROR!" displayed on its monitor.](intro_errors_confused.png)

When something goes wrong with your program, Python will give you an error message.
These messages are meant to help you find where your error is and what kind of error it is.

## Types of Error Messages

* NameError
* ImportError
* ValueError
* TypeError
* UnboundLocalError
* ...

Python has many, many error messages.
It can take a long time to learn them all.
When you encounter an error message you are unfamiliar with, you should first read and think about the message.
If you are not sure what it means, you should look up the error's meaning in the documentation.
Then, you can debug your program.
The list shown here is just a small subset of all the different kinds of errors.

## Terminology

* Error
* Exception

Just a minor point of terminology.
Errors are sometimes referred to as "Exceptions".
They're not quite identical, but for our purposes they might as well be.

## Identify the error type

![An example of a runtime error in BlockPy is shown](intro_errors_type_error.png)

Let's imagine that we ran some code, and encountered an error message.
In the bottom left of the error message, you can see the type of error.
In the example here, you can see that we have a "TypeError".
After the error type, there is usually some further description of the error.

## Find the Line

![The same error messages are shown from the previous slide, but this time the line number is circled instead.](intro_errors_line.png)

It can be tricky to read, but the error message should also identify WHERE the error occured.
Of course, sometimes the error is actually caused by code on a previous line.
You will have to think very critically about whether the error message is correct.

## Common Errors: NameError

```python example-name-error
student_grade = 10
# Note the typo below!
print(studten_grade)
```

Let's look at a few common errors.
First, here is a NameError.
A NameError comes up when you try to reference a variable that does not exist yet.
Sometimes, you mispelled the name of the variable.
Sometimes, you have not initialized the variable.
Sometimes, you initialized the variable, but you did so AFTER its first usage.
In this case, there is a typo in the name "student grade".
Try running the code to see the error.

## Common Errors: TypeError

```python example-type-error
print("7"+3)
```

Another common error is the TypeError, which occurs when you use an operator incorrectly.
For example, adding together a string and a number is not allowed.
When you read the error message that is produced, it will describe what went wrong.
Here, it says that we attempted to concatenate (which means combine) a string and an integer.

## Common Errors: SyntaxError

```python example-syntax-error
name = "Klaus von Wagglyschwantz"
age = 17
is_good_dog = True
print("Klaus is a good dog?)
print(is_good_dog)
```

A syntax error means that you broke Python's rules of spelling, grammar, and punctuation.
There are many ways to break a programs' syntax.
Usually, Python is very good at suggesting where the error is.
Still, sometimes it can be very tricky to track down a SyntaxError.

## Debugging Errors

![The previously confused looking student wearing a Sherlock Holmes outfit, now confidently staring in confusion at the Error Computer.](intro_errors_sherlock_holmes.png)

We'll learn some more techniques to help you fix your broken problems in the coming weeks.
For now, think critically about the errors you receive.
When you see one you don't understand, you should ask "What does this error message mean?" instead of "What is wrong with my program?"
