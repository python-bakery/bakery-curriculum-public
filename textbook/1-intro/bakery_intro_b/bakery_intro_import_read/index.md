---
waltz:
  title: bakery_intro_import_read
  display title: 1B5) Importing Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Importing
    slides: bakery_intro_import.pdf
    youtube:
      Bart: yTFORY1mOvo
      Amy: megr_Sj3jI8
    summary: In this lesson, you will learn how you can organize code into modules.
      Modules are a collection of code, and particularly functions. Rather than sharing
      functions directly, programmers actually share modules. You will learn how to
      use other modules to access more functions by importing them.
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 7
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 1246 AM
  files:
    path: bakery_intro_import_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Modules

* Modules are Python Programs

Whenever you create a new Python program, you are actually creating a Module.
In other words, a module is just a Python program.
A module is useful, however, because it can be imported into another module.
Any variables created in the module will then be available in the other module.

## Terminology

* Module
* Library
* Package

Modules are sometimes also known as packages or libraries.
Typically, a package is a collection of one or more modules.
However, the words are all more-or-less interchangeable.

## Import

```python example-import
import math

print("The value of pi is", math.pi)
```

To import data from another module, you use the Import statement.
There are three different ways to import a module.
The simplest is shown here, where we write the keyword import and the name of the module.
Once a module is imported, you can reference its definitions using the name of the module, a period (`.`), and then the name of the variable you want to use.

## Specific Import

```python example-from-import
from math import pi

print("The value of pi is", pi)
```

It can be bothersome to repeat the module name each time you want to use a function.
Therefore, Python has a convenient syntax for importing the functions directly.
This version uses the "from" keyword, followed by the module name, the "import" keyword, and then the name of the function or other definition you want to use.
Afterwards, you can use the variable as if it were defined in that file.

## Standard Library

```python example-string-library
from string import digits

print("The digits are", digits)
```

Python has a number of useful built-in modules called the Standard Library.
Further, Python programmers have created many other "third party libraries" that are easy to install.
Many of these modules come prepackaged in distributions that are easy to obtain.
We will not cover all these modules in this course, but you will often come across them when solving real-world problems.

## Installing New Libraries

```
> pip install pygame
> pip install requests
> pip install matplotlib
```

Although you may not have to do it very often, it is very easy to install new modules from a command line.
You can use the `pip` command to install a module.
You will need to know the exact module name.
Make sure that you have the right module name; when you install a new module, you are trusting the developer to not install anything malicious!
Most modern editors, including Thonny, also include a package manager that let's you install packages without writing code.
BlockPy does not allow you to install new libraries, but you can at least write new modules.


## New Modules in BlockPy

![A screenshot of BlockPy's file system interface, with an additional file available to the user named `my_second_module.py`.](bakery_intro_import_blockpy_file.png)

Most editors allow you to create additional Python files that can be imported into your main Python file.
BlockPy has this feature, but most problems disable that functionality so that you are not distracted.
Still, sometimes you will see an additional row of tabs that allow you to view and add new files.
In some cases, we'll have already created the file for you, but in others we may ask you to create the new file.
The second Python file will be available to be imported just like if it was in your local filesystem.
In this case, the external module would be `my_second_module.py`