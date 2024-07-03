---
waltz:
  title: bakery_structures_worlds_read
  display title: 4A3) Worlds Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    small_layout: true
    disable_timeout: true
    header: Worlds
    slides: bakery_structures_worlds.pdf
    youtube:
      Bart: 2UxW8mkRjGs
      Amy: 3w2jWfBdcdA
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 7
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0123 AM
  files:
    path: bakery_structures_worlds_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Basic Designer Games

```python designer-object-fields
from designer import *

def the_pie_flies_right(pie: DesignerObject):
    pie.x += 4

when('updating', the_pie_flies_right)
start(emoji("pie", 0))
```

We have previously used Designer to make simple interactive games that respond to our mouse clicks and keyboard presses.
A central premise in those games the current game state, which at that point could only be a single Designer Object.
You may recall that we had a pie floating across the screen, or spinning, by calling the appropriate Designer functions like `change_x` and `turn_left`.
Well, it turns out that Designer Objects are objects just like those created by dataclasses, and they actually have their own fields that we can manipulate.
In fact, updating those fields allows us to update the objects on the screen.
We can use this, for example, to make the `pie` fly across the screen just as before, but this time we update the object's fields directly.

## Designer Worlds

```python designer-worlds
from designer import *
from dataclasses import dataclass

@dataclass
class World:
    pie: DesignerObject
    label: DesignerObject

def fly_the_pie(world: World):
    world.pie.x += 4

when('updating', fly_the_pie)
start(World(emoji('pie', 0), text('black', 'Pie')))
```

Until now, our games could only have one object on the screen, which sharply limited the possibilities for our games.
To make more complicated games, we must use Dataclasses to bundle our game's state into a single object.
Conventionally, Designer refers to these dataclasses as Worlds, although technically speaking there is nothing special about the name.
As long as you are consistent with using whatever name you choose, the first parameter will be whatever object you pass into the `start` function.
In the example shown here, our `World` dataclass has two fields, the `pie` and the `label`. The former is the emoji from before, but the latter is a `text` object that will appear in the center of the screen.
The syntax for updating the `world.pie.x` field is a little strange; we have to chain together two attribute accesses.
Alternatively, we could have passed the `world.pie` attribute into the `change_x` function like before.
Either way, the `x` coordinate of the Pie will be updated every step.

## Starting Event

```python starting-event
from designer import *
from dataclasses import dataclass

@dataclass
class World:
    pie: DesignerObject
    label: DesignerObject

def make_world() -> World:
    pie = emoji('pie')
    label = text('black', 'Pie')
    change_y(label, 30)
    return World(pie, label)

when('starting', make_world)
start()
```

A new event becomes a bit more useful, at this point.
The `starting` event occurs once at the very beginning of the game, and allows us to specify how the initial game state should start.
This way, we do not have to pass any special data into the `start` function.
Later on, if we ever want to create a new original copy of the `World`, we have a function which does so.

## Timers

```python designer-timer
from dataclasses import dataclass
from designer import *

@dataclass
class World:
    timer: int
    picture: DesignerObject
    
def hatch(world: World):
    if world.timer > 60: # 2 seconds * 30 fps
        world.picture.name = 'hatching chick'
    else:
        world.timer += 1
        
when('updating', hatch)
start(World(0, emoji("egg")))
```

Because our worlds can have more than one field, we can achieve some cool tricks.
A common pattern is to have some code execute after a certain amount of time.
By keeping track of the steps that have passed in a `timer` field, we can choose when to trigger an event like changing the current `name` field of an `emoji`, which in turn changes what picture is drawn.
This code will therefore have the egg emoji turn into a hatching chick after 60 seconds.