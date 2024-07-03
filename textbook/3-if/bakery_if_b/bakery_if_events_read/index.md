---
waltz:
  title: bakery_if_events_read
  display title: 3B3) Events Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: true
  additional settings:
    small_layout: true
    disable_timeout: true
    header: Events
    slides: bakery_if_events.pdf
    youtube:
      Bart: D8JWQniv7q4
      Amy: UV28G4kiXPI
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 8
    created: June 28 2022, 0300 PM
    modified: August 26 2022, 0116 AM
  files:
    path: bakery_if_events_read
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
## Events

* Normal: Start, Execute, End
* Interactive: Start, Events -> Output, Never End!

So far, most of our programs have been straightforward: the program is started, execution occurs, and then the program ends naturally.
But most programs that you use every day are not like that.
You start the program, a window appears, and then the program waits for you to do something.
Each time you click a button, or type some text, or scroll with your mouse, the program reacts in an appropriate way.
These input events trigger output, and the program allows you to do these interactions as many as you'd like.
The web browser you are using right now is a great example of a program like this.
You can keep scrolling and clicking and typing, until you eventually close the program.
Mastering this new model will greatly enhance the kinds of programs that we can build.
We will build these programs using Designer.

## Designer Events

```python designer-events
from designer import *

def spin(pie: DesignerObject):
    turn_left(pie, 10)

when('updating', spin)
start(emoji("pie"))
```

Designer uses an event-driven model to handle interactivity.
Designer provides a function named `when` that can take in the name of an event and a function name to execute when that event occurs.
Notice we said a function *name*.
This is a serious departure from all functions we have seen so far, which have not taken in a function.
Some functions can take in the result of *calling* a function, but that is very different from a function name.
Specifically, a function call is a function's name followed by parentheses.
That executes the function and returns a new value, depending on the return type of the function.
But now, without the parentheses, we are actually using the function as a value directly.
The reason for this is that Designer will call that function on our behalf.
In this example, we are binding the `spin` function to the `updating` event.

## When vs If

* `when`: A function that consumes the name of an event and a function to call later
* `if`: A statement that has a conditional expression and a body to execute now

When a function is bound with the `when` function, Designer will essentially wrap that function call in an `if` statement.
When the named event is active, the function is called.
Each type of event has different logic for when that event is active, corresponding to the conditional of an `if` statement.
The body of the `if` statement is basically the body of the bound function.

## Bound Functions

```python move-pie-right
from designer import *

initial_pie = emoji("pie", 0)

def move_right(pie: DesignerObject):
    change_x(pie, 4)

when('updating', move_right)
start(initial_pie)
```

So what is happening in these bound functions?
Previously, we learned how to use the Designer library to draw pictures, and how we could even make functions that drew pictures in a reusable way by returning `DesignerObject`s.
These bound functions, however, are completely different.
Now, the function consumes a `DesignerObject` in order to manipulate the object.
But where does that DesignerObject come from?
The answer is the new `start` function, which is exactly like `draw` but allows the program to keep running so it can accept interactive events.
That `start` function accepts an initial state for the game, in this case an `emoji` of a Pie.
That emoji becomes the state parameter for the bound function, passed in as argument every time the game updates, so that the bound function can mess with the current version.
But what do we mean by "every time the game updates"?

## Updates

* Picture of a game undergoing a state transition

Watching a movie, you can see the 

State parameter

void return? Probably. They just modify the state parameter via function calls.

Step event. Frames per second.

Collision handling event.


## Key Presses

Timer type of event.

Keypress event.

Mouse event.