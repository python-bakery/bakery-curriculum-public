---
waltz:
  title: bakery_lab_monster_mash_instructions
  display title: 0) Instructions
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    hide_files: false
    small_layout: true
    disable_tifa: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 26
    created: August 17 2022, 1234 PM
    modified: October 15 2022, 1011 PM
  files:
    path: bakery_lab_monster_mash_instructions
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files:
    - bakery_lab_monster_mash_instructions\monster_mash.py
---
You are going to be working in groups of 3 today, although in a strange way. Your goal is to end up with solutions for all the coding questions in this module.

You might choose to break up the work by having folks work together on specific questions. Or you might have some folks work more individually and then share answers. You could even alternate between working together and working independently. How you break things up should be decided by your group.

To share code with each other, you might use a Google Doc or [pastebin](https://pastebin.com/). There is also value in seeing the solution and retyping it yourself. In future courses, you will learn more sophisticated ways to share code between developers working together.

Begin by reading the instructions and examples below. Then, decide how you will split up the work. Finally, carry out your plan!

## Monster Mash

Every Halloween, monsters get together to celebrate the season by hosting parties called "Monster Mashes". They're a real graveyard smash, we assure you. Your team has been hired to help do party planning in the future, and all good party planning starts with data analysis. You have collected some example data from past Monster Mashes, and will need to write some functions to process that data. 

You do **not** define the dataclasses and test data for this assignment, you only define the functions to process the data.

The diagram below helps explain the format of the `MonsterMash` dataclass and its associated classes `Party`, `Monster`, `Media`, `Potion`, and `Ingredient`.

![A class diagram of the MonsterMash dataclass and its associated classes](monster_mash_diagram-v3.png)

*The field spookyiness should be spelled spookiness*

The descriptions of each of the classes is as follows:

* `MonsterMash`: All of the data related to a single instance of a monster party, including the party metadata, some of the key monsters attending, what media they enjoyed, and the drinks they had (brews).
* `Party`: Metadata about the party including its name, venue, and size.
* `Monster`: A representation of a specific monster attending the party.
* `Media`: Either a song, movie, or game that is played at the party.
* `Potion`: A (possibly delicious) magical potion that can be consumed to produce a certain magical effect. Requires ingredients and time to brew.
* `Ingredient`: A specific ingredient for a potion. May or may not be rare.

Notice that some of these dataclasses are *lists* in the `MonsterMash` dataclass, not just single instances! In fact, only the `party` field is actually a single dataclass - all the other fields are lists!

## The Data

You have four existing `MonsterMash` instances to use as test data. And good news, that should be all you need for this assignment. Although you are free to write more test cases if it helps you think, you are not required to write any additional ones. All of the test data has been written for you.

Although we have already provided you with the test cases, you may find it helpful to review the actual data of the Monster Mashes, so you understand how the values were calculated. Run any of the examples below to get access to the `monster_mash.py` file (you will also find the file in each programming problem of this assignment).

## Examples

**Example 1:** Define a function `get_party_size` that consumes a `Party` and determines if the party is `"large"` (40 or more monsters), `"small"` (less than 20 monsters), or `"medium"`.

```python get_party_size
from bakery import assert_equal
from monster_mash import *

def get_party_size(party: Party) -> str:
    """
    Determines if a party is "large", "medium", or "small" based
    on the headcount.
    """
    if party.head_count >= 40:
        return "large"
    elif party.head_count < 20:
        return "small"
    else:
        return "medium"

assert_equal(get_party_size(party1.party), "small")
assert_equal(get_party_size(party2.party), "small")
assert_equal(get_party_size(party3.party), "medium")
assert_equal(get_party_size(party4.party), "large")
```

**Example 2:** Define a function `count_werewolves` that consumes a list of `Monster`s and produces the number that are of kind `"werewolf"`.

```python count_werewolves
from bakery import assert_equal
from monster_mash import *

def count_werewolves(monsters: list[Monster]) -> int:
    werewolves = 0
    for monster in monsters:
        if monster.kind == 'werewolf':
            werewolves = werewolves + 1
    return werewolves

assert_equal(count_werewolves(party1.monsters), 0)
assert_equal(count_werewolves(party2.monsters), 3)
assert_equal(count_werewolves(party3.monsters), 0)
assert_equal(count_werewolves(party4.monsters), 1)
```

## If You Missed This Activity...

If you missed this activity, then fill out the Class Absence Form and attend office hours to makeup the points.