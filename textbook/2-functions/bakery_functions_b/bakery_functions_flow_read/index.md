---
waltz:
  title: bakery_functions_flow_read
  display title: 2B3) Function Flow Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Function Data Flow
    slides: bakery_functions_flow.pdf
    youtube:
      Bart: kWECzKYb8rM
      Amy: _1m1wqR2ICQ
    summary: In this lesson, you will learn how data flows between functions in a
      program.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0103 AM
  files:
    path: bakery_functions_flow_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Scope and Values

1. Variables inside a function cannot be used outside
2. Variables outside a function should not be used inside
3. Function return values, not variables

Previously, we learned about scope: the idea that variables inside a function
cannot be used outside of the function, and variables outside a function
should not be used inside the function.
Further, we learned that functions do not consume or return variables;
instead they consume and return values.
These ideas are critical in understanding how data flows through a program.
The goal as a programmer is to isolate variables to regions of the program, so that those regions are easier to think about without having to keep the entire program in your mind all at once.

## Data Flow

![A picture of a winding river, with values (e.g., `64` and `"Klaus"`) inside. Some of the values are annotated with the names of variables.](bakery_functions_flow_river.png)

You can think of a program as a flowing, twisting river.
Regular execution makes the river flow south, but functions disrupt this flow.
Along the way, values are carried by the current.
At times, we give these values names by using variables, but it is 
the values that flow through the program, not the variables.

## Substitution

```python substitution-model
def add(left, right):
    return left + right

5 + add(3, 4)
# 5 + add(3, 4)
# 5 + 7
# 12
```

When you call a function, each parameter is assigned the value of a relevant argument. 
When you return from a function, the function call is substituted for the returned value.
These are the only tools we should use in Python to move data around a program.
This is just like what happens when you use an operator like plus or minus.
Even though we do not see the substitution visually, it still happens.


## Call Frames

![A block of code is shown on the left, demonstrating an `add_period` function. On the right, two rectangles are shown representing the call frames of the program. In the top Global Frame, the variable message is shown. In the bottom add_period frame, two local variables are shown.](bakery_functions_flow_add_period.png)

Each time we call a function, we say that its local variables are inside their
own scope.
We will also call this scope the **frame**, and it can be used to show
the current variables and their values.
Notice that the global frame is separate from the local frame.
The frames shown here are from if we stopped the program right before the `return` statement got executed.
After the `return` statement is executed, we would cross out the `add_period` stack frame, to indicate that the function's scope has ended.

## Data between Functions

```python data-between-functions
def calculate_grade(raw, weight):
    grade = 10 * (weight+raw) ** .5
    return grade
    
def make_grade_message(grade):
    return "Your grade was:" + str(grade)
    
raw = 45
weight = 5
grade = calculate_grade(raw, weight)
message = make_grade_message(grade)
print(message)
```

To move data from one function to another, you cannot just look at the two functions.
You must also look at where the functions were called.
The returned value of one function should be fed into the next function.
In the code shown, the variables defined inside `calculate_grade` are distinct from the variables outside of the function.
In fact, it is only the last 4 lines that actually move values between functions.
Without using return values and arguments, we cannot move data between functions.

## Functions Calling Functions

![Another stack frame diagram, with code on the left. The code has two functions, one of which calls the other. This results in three stack frames on the right, the bottom two being crosed out.](bakery_functions_flow_double_add3.png)

Things get even more complicated when functions call other functions, but
this happens all the time.
We are used to calling built-in functions, but we can call our own functions too.
When we call a function inside another function, we **stack** the new function
 call's frame below the current frame, with the bottom frame being the current scope.
When a function call ends, we remove that bottom stack and return to the one above it.
Each function call's frame is separate from all other frames, even if they
come from the same function or have variables with the same name.
In the stack frames shown here, you can see that the `number` variable has different values in the different scopes, at the end of the program.
You can also see how some scopes have expired, resulting in their call frames being crossed out.
Their data is no longer available.