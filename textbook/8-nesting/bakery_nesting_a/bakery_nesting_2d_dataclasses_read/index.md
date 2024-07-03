---
waltz:
  title: bakery_nesting_2d_dataclasses_read
  display title: 8A2) Nested Dataclasses Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    header: Nesting Dataclasses
    youtube:
      Bart: OhuCWSfoBJY
      Amy: _fB8KSLY0PQ
    summary: ''
    small_layout: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 10
    created: June 28 2022, 0300 PM
    modified: September 22 2022, 0632 PM
  files:
    path: bakery_nesting_2d_dataclasses_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Nesting Dataclasses

```python nesting-example
from dataclasses import dataclass

@dataclass
class Address:
    city: str
    state: str

@dataclass
class Person:
    name: str
    work: Address
    home: Address

ada = Person("Ada", Address("Newark", "DE"), Address("Elkton", "MD"))
print(ada)
```

Just like how dataclasses can be nested inside of lists, Dataclasses can be nested inside of other Dataclasses.
This introduces some extra complexity, but can be quite helpful for organizing large complex objects and increasing reusability.
The `Person` class shown here depends on an `Address` class for two of its fields.
This allows us to cleanly separate the parts of an address from the parts of a Person, both in our minds and in our code.
When you print out the entire object, you can see that `ada` has two different addresses inside.

## Order of Definitions

```python order-matters
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    work: Address
    home: Address

@dataclass
class Address:
    city: str
    state: str

ada = Person("Ada", Address("Newark", "DE"), Address("Elkton", "MD"))
print(ada)
```

The order in which you define dataclasses matter.
If you try running the code shown here, you will get an error on the second line of the definition of the `Person` class.
That definition is expecting the `Address` class to already exist, so we a `NameError` occurs instead.
The dataclasses must be defined before they can be referenced, at least in Python.

## Nested Access

```python nested-access
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    work: Address

@dataclass
class Address:
    city: str
    state: str

ada = Person("Ada", Address("Newark", "DE"))
print(ada.work.state)
```

When you have multiple levels of nested data classes, you still use attribute access to get data inside of the classes.
However, you will have to chain the accesses together in order to get to the desired level.

## Visualization

![A visualization of the `ada.work.state` expression, where a box labeled `Person` has an arrow labeled `work` pointing to a box labeled `Address`, with an arrow pointing in turn to a string value `"DE"`, suggesting that the data is stored inside of other data.](bakery_nesting_2d_dataclasses_unpacking_visualization.png)

Imagine opening a box and finding another box inside, and then opening that box to find the value you are looking for.
Each level of nested dataclass means another box.

## Temporary Variables to Unpack Nested Data

```python temporary-variables
from dataclasses import dataclass

@dataclass
class Address:
    city: str
    state: str

@dataclass
class Person:
    name: str
    work: Address

ada = Person("Ada", Address("Newark", "DE"))
job = ada.work  # Introduced a temporary!
print(job.state)
```

A temporary variable can help alleviate some of the ugliness of heavily nested classes.
Assigning one part of the chained attribute access to a new variable allows you to name that expression
and reuse it later.
This is especially helpful if you are going to need to use the value stored inside multiple times.

## Lists in Dataclasses

```python lists-in-dataclasses
from dataclasses import dataclass

@dataclass
class Emails:
    user: str
    messages: list[str]

inbox = Emails("acbart", ["HELP!", "Department News",
  "Sign Up Today!", "Discord Notifications Digest"])

print(inbox.messages[2])
```

As you might have guessed by now, lists can also be nested inside of dataclasses.
Lists are just another type, after all, so using them inside of a dataclass is not a big deal.
The only part that might feel strange is how you access individual elements of the list.
Notice how we have to combine the attribute access syntax with the list indexing syntax.
All the same rules and operations apply that we have learned so far, they might just look a little funny at first.

## How Much Nesting?

```python unnecessary-nesting
from dataclasses import dataclass

# Not good nesting - the extra level adds nothing of value!
@dataclass
class Person:
    name: Name

@dataclass
class Name:
    full_name: str
```

When you are designing your dataclasses, you have to stop and reflect on how much nesting you want.
Breaking up complex dataclasses into smaller pieces can help make your code more reusable and more flexible, 
and can reduce your cognitive load.
However, you also will have to do more levels of access, and it can be difficult to remember where things are.
You need to learn to work with the brain that you have, and find an appropriate level of depth for the classes.
In the example shown here, we see a `Person` class that has a `name` field with a corresponding `Name` class, rather than being directly a `str`.
This makes no sense, since the `Name` class only ends up with one field.
But it might make sense if we were going to add some other fields, like `first_name` and `last_name` and `nickname` to the `Name` field.
Then we could reuse that structure across other classes that need complex names.