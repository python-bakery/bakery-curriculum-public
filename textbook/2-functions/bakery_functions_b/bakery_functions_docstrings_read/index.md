---
waltz:
  title: bakery_functions_docstrings_read
  display title: 2B2) Docstrings Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Docstrings
    slides: bakery_functions_docstrings.pdf
    youtube:
      Bart: jiJjoRE3aUQ
      Amy: ofYpDXmKqiA
    summary: In this lesson, you will learn how to document a function.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0102 AM
  files:
    path: bakery_functions_docstrings_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Why Document Code?

1. For sharing code
2. To organize our current code
3. To make re-reading old code easier

Programmers write documentation in order to explain what a function does.
This is useful not only for sharing code with other programmers, but when we 
come back to code we wrote later.
To document code, you create **comments** that are ignored when the code is executed.
These comments are for the benefit of humans, not the computer.
Python has two ways of writing comments.

## Single-line Comment

```python single-line-comment
# This line is ignored
a = 0 # The rest of this line is ignored
b = 0
```

To make a single-line comment in Python, you should use the hash symbol (also known as "pound" or "octothorpe", written as #).
Everything after the hash symbol on the same line is completely ignored by your program.
These are often used to document a single line of code.
However, you must not use single line comments to create docstrings.

## Multi-line Comment

```python example-docstring
def my_function(x:int, y:int)->int:
    """
    The start of this string needed to be
    indented, otherwise you would have a syntax
    error!
    """
```

To write multi-line comments in Python, you actually create a triple-quoted string. 
When Python evaluates this string, the value is unused, so it is safely ignored by the computer.
However, unlike the single-line comment, that means that the start of a 
multi-line comment must respect indentation rules as shown here.
However, on the plus side, this triple-quote string counts as the body of the function, so you no longer need the `pass` statement.

## How Much to Comment?

* High: Every line of code
* Medium: Only confusing or large chunks of code
* Low: Only Functions

There are many opinions on when to write comments, and no "correct answer".
Some people believe you need to document every single line.
Some people believe you should only document functions and programs as a whole.
Eventually, you will need to find your own balance - for example, rather than 
documenting every line, you might only document lines that are particularly 
confusing, or document a chunk of code.

## Documenting functions

```python full-docstring
def fix_capitalization(title: str)->str:
    '''
    This function capitalizes the first letter of each
    word in the title, correctly ignoring prepositions.
    
    Args:
        title (str): A book or movie title
            that we want to fix.
    Returns:
        str: The corrected title
    '''
```

Many people agree that, at a minimum, you should document all your functions.
Use a triple-quoted string as the first line in the definition of the function.
Then, give a quick description of what the function does.
To give complete documentation, you should also explain what the parameters
and returned value mean.
Leave a blank line, and then type "Args:".
Indent the next line, and then type the name of the first parameter followed by its type in parentheses. On the same line, write a colon and then describe the parameter. If you need to continue onto the next line, make sure it is indented past the previous line.
You should repeat this for all the parameters of your function.
Finally, write "Returns:" and then on the next line write the name of the 
return type, followed by a colon and a description of the returned value.

