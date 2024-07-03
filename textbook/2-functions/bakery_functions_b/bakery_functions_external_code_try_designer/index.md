---
waltz:
  title: bakery_functions_external_code_try_designer
  display title: 2B4.3) Try Designer
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    start_view: text
    save_turtle_output: true
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 116
    created: August 18 2022, 0237 PM
    modified: August 20 2022, 1217 AM
  files:
    path: bakery_functions_external_code_try_designer
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Use the `emoji`, `rectangle`, and `circle` function to make a little scene using `designer`.
Also call the `set_window_color` function to change the background color to something else.
You need at least one emoji, one rectangle, and one circle (you can use more).
For [example](https://i.imgur.com/Ks301v2.png), you could draw a dragon (emoji) sitting on green grass (rectangle) under a yellow sun (circle), or perhaps make your own flag.
Don't forget to call `draw` at the end and pass in the objects you created!

* `emoji(name: str)`: Create a picture based off the emoji. Note that the `emoji` function can take either the name of an emoji (`"dragon"`) or the emoji itself (`"🐉"`). [More information](https://designer-edu.github.io/designer/students/docs.html#id1)
* `rectangle(color: str, width: int, height)`: Draw a rectangle of the given width and height in the given color. [More information](https://designer-edu.github.io/designer/students/docs.html#id3)
* `circle(color: str, radius: int)`: Draw a circle of the given radius in the given color. [More Information](https://designer-edu.github.io/designer/students/docs.html#id4)
* `set_window_color(color: str)`: Change the background color of the drawing area. [More Information](https://designer-edu.github.io/designer/students/docs.html#designer.animation.set_window_color)

You may find it helpful to refer to the [Designer function cheat sheet](https://designer-edu.github.io/designer/students/functions.html) if you need a quick reference on the available functions.
In particular, the functions for [moving objects](https://designer-edu.github.io/designer/students/functions.html#moving-and-positioning-objects) (like `move_to_xy(target: DesignerObject, x: int, y: int)`) is very useful for this problem!