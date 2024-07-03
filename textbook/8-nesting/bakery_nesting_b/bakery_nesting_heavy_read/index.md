---
waltz:
  title: bakery_nesting_heavy_read
  display title: 8B2) Heavily Nested Data Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Heavily Nested Data
    youtube:
      Bart: 51QBGqmH-Ts
      Amy: sId3gYdTzYw
    summary: ''
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 6
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0621 PM
  files:
    path: bakery_nesting_heavy_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## The Types

* Primitive Types: Integer, Float, Boolean, String, None
* Composite Types: List, Dataclasses

The 5 primitive types we've learned about are Integer, Float, Boolean, String, and None.
The 2 composite types we've seen so far are Lists and Dataclasses.
These 2 new composite types are special because they are composed of other types.
It's worth reminding you, dataclasses are not actually a type themselves, but a way of making new types.
There are actually many more composite types in Python.
But for now, we'll stick to these basic 7 types.
In the earlier parts of this chapter, we saw how we could mix and match those composite types to make lists of dataclasses,
dataclasses inside of dataclasses, and lists of lists.
There's actually no limit to how much we can combine these different types.

## Example Nested Data

```python heavy-nesting-example
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    pets: int

@dataclass
class House:
    address: str
    owner: Person

@dataclass
class Neighborhood:
    name: str
    houses: list[House]

green_acres = Neighborhood("Green Acres", [
  House("14 Sun Drive", Person("Mary", 1)),
  House("15 Sun Drive", Person("Jenny", 0)),
  House("16 Sun Drive", Person("Jim", 5)),
])
```

Let us look at a concrete example.
Shown here we have three dataclasses, where two of the dataclasses have fields referencing other dataclasses.
In fact, for the first level, the `Neighborhood` dataclasses `houses` field is actually a list of the `House` dataclass.
At the deepest point, there are four levels of nested data structure here.

## A Representative Element

![A diagram shows three boxes connected with two lines. Each box describes the name and fields of the classes described on the previous slide: Neighborhood, House, and Person](bakery_nesting_heavy_class_diagram.png)

To quickly understand the structure of complex nested data, we find it useful to model the data in a "Class Diagram".
In the diagram shown here, we draw each dataclass in its own box.
Then, we connect the related dataclasses together with lines.
If the relationship includes a list, we draw an empty diamond starting from the owning dataclass.
There is actually a lot more to class diagrams than what we have shown here, but this should be enough to get us started.

## Accessing Nested Data

* Iterating through lists
* Indexing and subscripting a list
* Accessing attributes in a dataclass instance

As you process this complex nested data's structure, you have to stay aware of where you are.
This is similar to needing to navigate a maze.
However, you also have to be aware of the tools at your disposal for accessing the data.
When working with a list layer, you can either iterate through the data with a `for` loop, or index specific elements if you only need one.
When working with a dataclass layer, you can only access attributes of the instance at that layer.
In the `green_acres` example from before, if we wanted to add up the number of pets across everyone in the neighborhood, we would need to do an attribute access, followed by iteration, followed by a pair of attribute accesses.

## Iterating in Code

```python count-pets
def count_pets(neighborhood: Neighborhood) -> int:
    pets = 0
    houses = neighborhood.houses
    for house in houses:
        pets += house.owner.pets
    return pets
```

Here is an example function that counts the number of pets across all the neighborhoods.
Notice that we have extracted the `neighborhood.houses` expression to a temporary variable first; we could have used the expression directly in the loop, if we had wanted to.
We could also have broken up the `house.owner.pets` expression with some temporary variables.
And we could have made a helper function to help count the number of pets in an individual neighborhood.
Whether that is effective is partially a matter of opinion, but also a matter of how complex the code is.
This function is not super complicated, so we did not bother breaking it up.
But what if we had a more complicated structure?

## Layers of Nesting

![A diagram has two large blocks of code on either side. On the left side, there are the definitions of four dataclasses. On the right side, a list of instances are created as an example of the dataclasses. In the middle, there is a class diagram describing the complicated model.](bakery_nesting_heavy_complex.png)

As previously mentioned, there are no limits to how much nesting can happen.
Here we see a `Planner` dataclass that has a list of `Day` dataclasses inside.
That `Day` class has not only a `Date` dataclass in one of its fields, but it also has a list of `Event` dataclass instances.
On the right hand side, we have a list of Planner instances making a very large example data structure.

## Another Example Function

```python planner-example
def total_average(planners: list[Planner]) -> float:
    total = 0
    for planner in planners:
        total += average_duration(planner)
    return total

def average_duration(planner: Planner) -> float:
    count = 0
    total = 0
    for event in planner.events:
        count += 1
        total += event.duration
    return total / count
```

In this example, we define two functions, `total_average` and `average_duration`, with the goal of calculating the total average duration across multiple planners.
Since this time, we had so many nested pieces of data, we found it quite helpful to break things up with helper functions.
A good rule of thumb is that you should avoid having `for` loops directly inside of each other, unless you are working explicitly with a 2-dimensional list like we saw in the previous chapter.
When we start dealing with truly nested data like this, we instead start relying even more heavily on functional decomposition to help us manage the complexity.