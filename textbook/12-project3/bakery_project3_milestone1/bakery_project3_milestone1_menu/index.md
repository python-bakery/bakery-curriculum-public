---
waltz:
  title: bakery_project3_milestone1_menu
  display title: 1.6) Menu
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    disable_tifa: true
    preload_files: '{"course": {"37": {"canvas_data.json": true}}}'
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 257
    created: November 03 2022, 0115 AM
    modified: November 26 2022, 1053 AM
  files:
    path: bakery_project3_milestone1_menu
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
You are now going to create the menuing system for your application. This will have a few steps, and will depend on all the functions you've written previously. You will also be extending this function further in future milestones.

**Part 1**: Copy over the functions you defined previously in for the project: `count_courses`, `find_cs1`, `find_course`, and `render_courses`. You will not need their unit tests, nor do you need to unit test any functions here.

**Part 2**: You need to define a function `execute` that consumes a `command` (a string), a `user_token` (a string), and a `course_id` (an integer); the function returns an integer representing a new course ID (or the course ID that was passed in). The `execute` function should essentially be a large `if`/`elif`/`else` chain that determines what to do based on the given `command`:

* If the command is `"course"` then...
    1. Print out all the courses using `render_courses`
    2. Use the `input` function to get the ID of a new course from the user (remember to convert with `int`!)
    3. Print out the full name of the new course using `find_course`
    4. Return the new ID
* If the command is `"exit"`, then just return `0` (this will eventually make the program exit)
* If the command is anything else, then return the `course_id` that was passed in.

**Part 3**: You need to define a function `main` that consumes a `user_token` (a string) and then does a read-evaluate-print-loop using the `execute` function. A critical part of this REPL is the "current course ID", which will have an initial value prior to the start of the loop, and then be changeable inside the loop by using an appropriate command. Here is the logic for the `main` function:

* Use `count_courses` to determine if the current `user_token` has no courses, in which case print the message `"No courses available"` and return from the function.
* Use the `find_cs1` function to get a default value for the current course ID
* If the result returned by `find_cs1` was `0`, then instead set the current course ID to be the first course available
* Then, after the above is done, you can start the main loop. The loop will continue while the current course ID is greater than 0.
    * Inside the loop, use the `input` function to ask the user what they want to do. You will need to print some text for the menu options to remind the user what they can do: so far the options are `course` and `exit`.
    * Then, call the `execute` function using the command inputted by the user, the user token, and the current course ID.
    * Assign the result of calling `execute` to the current course ID, so that the loop is escapable.