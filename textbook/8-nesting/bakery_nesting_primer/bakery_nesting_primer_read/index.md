---
waltz:
  title: bakery_nesting_primer_read
  display title: 8) Primer
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: true
  additional settings:
    header: Nesting Data
    youtube:
      Bart: 3W0BTvy2zYU
      Amy: zEXsP36PEZE
    summary: ''
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 3
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0614 PM
  files:
    path: bakery_nesting_primer_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Lists of Dataclasses

```python list-of-dc
from dataclasses import dataclass

@dataclass
class Picture:
    width: int
    height: int
    filename: str

pictures = [
  Picture(256, 256, "cool_dog.png"),
  Picture(128, 512, "family_photo.png"),
  Picture(512, 128, "help_infographic.png")
]
print(pictures)
```

We've previously learned two main data structures for holding multiple pieces of data in one place.
Lists hold data of the same type, while dataclasses make new types that can hold different kinds of data.
Up until now, we've only put primitive data into our lists and dataclasses.
But now, we will start mixing these datatypes.
The chapter begins with one of the most useful and common combinations: lists of dataclasses.
In the example shown here, we have a list of `Picture` instances.
Each element of the list is a Picture, and each Picture has the same type of attributes.
Each Picture has distinct values, though, allowing us to represent many complicated things in one place.
A comparable idea is a table or spreadsheet.
Much of this chapter is dedicated to showing how we can process this kind of data using the loop patterns we have already seen.

## Nested Dataclasses

```python nested-dc
from dataclasses import dataclass

@dataclass
class Address:
    city: str
    state: str 

@dataclass
class Person:
    name: str
    home: Address
    work: Address

alice = Person("Alice",
  Address("Baltimore", "MD"),
  Address("Newark", "DE")
)
print(alice)
print(alice.home.state)
```

Dataclasses can be placed not only in lists, but also in other dataclasses.
We have actually already seen this with Designer's `World` dataclasses, which had `DesignerObject`s inside.
But now we will make own our dataclasses with other dataclasses inside.
Composing dataclasses allows us to isolate chunks of data into smaller pieces that are easier to think about.
We can also reuse those new dataclasses in more than one place.
Nesting dataclasses requires chaining together multiple attribute accesses, which can feel a little strange at first.

## Nested Lists

```python nested-lists
numbers_2d = [
  [100, 95, 97, 88],
  [55, 66, 75, 94],
  [99, 95, 97, 92]
]

print(numbers_2d[1][2])

for y, row in enumerate(numbers_2d):
    for x, number in enumerate(row):
        print(x, y, number)
```

In some ways, nesting lists inside of each other is simpler than nesting dataclasses, since lists are a built-in type.
However, dealing with nested `for` loops can be quite tricky.
The example code shown here also incorporates an `enumerate`, which is not necessary unless you want access to the indexes as well.
Critically, note how we first iterate through each `row`, and then each `number` inside of that `row`.
Also demonstrated here is indexing a specific element, which requires chaining together two indexes.

## Heavy Nesting

```python heavy-nesting-example
from dataclasses import dataclass

@dataclass
class Address:
    city: str
    state: str

@dataclass
class Person:
    name: str
    duty: str
    home: Address

@dataclass
class Company:
    boss: Person
    employees: list[Person]

my_company = Company(
  Person("Alice", "Manager", Address("Nome", "AK")), [
    Person("Bob", "Janitor", Address("Newark", "DE")),
    Person("Carol", "Coder", Address("Wilmington", "DE")),
    Person("Dave", "QA", Address("Baltimore", "MD")),
])
```

There's no end to how much we can nest dataclasses and lists together.
By doing so, we can represent truly complex data.
Of course, this also requires more nesting of control structures and attribute accesses.
Just like with the other combinations of data structures, all of the same rules apply.
It's all just a matter of keeping the data clear in your mind.