---
waltz:
  title: bakery_functions_external_read
  display title: 2B4) External Functions Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    small_layout: true
    header: External Functions
    slides: bakery_functions_external.pdf
    youtube:
      Bart: Ae7jAthi3Ro
      Amy: dQySTh2LfmQ
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 9
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0103 AM
  files:
    path: bakery_functions_external_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Why External Functions

```python try-randint
from random import randint

# Each of these prints a random number!
print(randint(0, 100))
print(randint(0, 100))
print(randint(0, 100))
print(randint(0, 100))
```

We have previously used `import` statements to load variables defined in another module.
But even more common is to use `import` statements to load functions defined in another module.
In fact, Python has a large number of modules available through it's built-in "standard library".
For instance, the `random` module has many useful functions for producing random numbers, such as in the code shown here.
Using externally defined functions, we greatly increase the capabilities available to us.

## Using External Functions

```python try-math
from math import floor, pi

def calculate_area(radius: int) -> int:
    return floor(pi * radius ** 2)

print(calculate_area(5))
```

Imported functions are just like any functions built into Python, or defined in your own code.
Once they're imported, you can use them inside of existing functions.
We can also use variables from other modules in the same way.
In this example, we import a function and variable from the `math` module to calculate the area of a circle and floor the result.
Flooring means to remove any decimals, and is also known as trunctation.

## Third Party Libraries

![The official PyPi logo](bakery_functions_external_pypi.png)

Some modules are not built into the regular Python distribution, but are available through other services.
The most popular repository of Python modules is named PyPi, which stands for the Python Package Index.
Anyone is free to upload code to PyPi, which is both good and bad.
As long as you can trust a package to not act maliciously, you can get access to a huge set of powerful tools.
Unfortunately, there have been cases where people have uploaded bad packages with names similar to well-known packages.
The bad actors took advantage of the fact that people are not always careful when writing out names, and sometimes make typos, to have them accidentally install their evil library instead.
You must be very careful when installing software from the internet, thinking critically and paying close attention to what you agree to do.

## Designer Functions

![The logo for Designer](bakery_functions_external_designer.png)

BlockPy has some popular libraries already pre-installed.
One library that we can use is named `Designer`, meant for making graphics and games.

## Designer Example

```python designer-shapes
from designer import *

# rectangle(color, width, height)
box = rectangle('blue', 30, 50)

# circle(color, radius, x, y)
orb = circle('red', 25, 150, 30)

# emoji(name)
frog = emoji('frog')

draw(box, orb, frog)
```

The example code here shows one of the simpler ways to use Designer.
After importing the `designer` module, there are a bunch of new functions available for creating shapes, images, and text.
By calling those functions, we create special Designer Objects that can then be passed to Designer's `draw` function.


## Positioning and Sizing Objects

```python designer-movement
from designer import *

dog = emoji('dog')

turn_left(dog, 45)
move_to_xy(dog, 40, 40)
grow(dog, 2)

draw(dog)
```

Designer also exposes a bunch of helper functions for rotating, moving, and scaling objects.
The example code here demonstrates the `turn_left` function that takes an object and an angle,
the `set_xy` function that takes an object and a pair of x-y coordinates, and the `grow` function
that takes an object and a new scale multiplier.
By calling the right functions, you can create entire scenes and images.

## Your Own Designer Functions

```python designer-bullseye
from designer import *

def bullseye(radius: int, color: str) -> DesignerObject:
    core = circle('black', radius//4)
    ring1 = circle(color, 2*radius//4)
    ring2 = circle('black', 3*radius//4)
    ring3 = circle(color, radius)
    return group(ring3, ring2, ring1, core)

draw(bullseye(50, 'red'))
```

Just like with functions from the `math` module, we can use Designer functions in on our own functions.
This example demonstrates creating a bullseye image using concentric circles.
Notice how we call the Designer `group` function at the end to flatten the circles into a single image.
Afterwards, we could use the positioning, sizing, and other Designer functions to manipulate the bullseye
as a single object.

## More About Designer

* For more information, check out the Designer website!

The Designer library has a ton of functions and features that you can use to make both graphics and games.
We'll be revisiting the library a few more times this semester, as we learn new code constructs and abilities.
However, if you're excited about Designer, and wish to learn more, you can visit the link shown to start reading over the [Designer documentation and quick start guides](https://designer-edu.github.io/designer/quickstart/quickstart.html).