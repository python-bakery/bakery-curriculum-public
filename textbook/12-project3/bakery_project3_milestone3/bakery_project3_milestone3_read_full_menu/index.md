---
waltz:
  title: bakery_project3_milestone3_read_full_menu
  display title: 3.5) Full Menu Commands
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    small_layout: true
    disable_tifa: true
    preload_files: '{"course": {"37": {"canvas_data.json": true}}}'
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 9
    created: November 25 2022, 0458 PM
    modified: November 26 2022, 1200 PM
  files:
    path: bakery_project3_milestone3_read_full_menu
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
We are nearing the end of the project, so it is time to bring all the pieces back together. You are going to need to extend your `execute` function from before with all of the new commands described below. You will also need to make a minor change to your `main` function. But first, you need to combine all of your code into a single file.

### Merging Code

You need to create a single file with all of the code that you have previously defined. If you have been working in Thonny and keeping all the functions in one file, you may find this part relatively easy; otherwise, you will have to go back through all of the previous parts of the project and collect all of the code into one place (you may find the Grades or BlockPy Dashboard pages easier to navigate).

When combining your code for this final phase, make sure that you do not have redundant `import` statements. Remember, you only need to import `bakery_canvas`, `bakery`, `datetime`, and `matplotlib.pyplot` once each.

You do not have to remove unit tests or any code that tests your plotting functions - the autograder should ignore these when grading you.

### The execute function

To complete the program, you must implement the following commands in your `execute` function (you have already completed the first two commands). Note that except for the first two commands, all the other commands return the same value (the current course ID that was provided as a parameter, unchanged).

* `exit`: (*part 1*) Quits the program by returning `0` unconditionally.
* `course`: (*part 1*) Changes the current course ID by:
    1. Printing the available courses,
    2. Prompting the user for a new course ID,
    3. Converting the result to an integer
    4. Printing that course's full name, and then
    5. Returning the new course ID.
* `points`: (*part 2*) Prints the result of calling `total_points` on the current course ID, to print out the total points available on all assignments.
* `comments`: (*part 2*) Prints the result of calling `count_comments` on the current course ID, to print the number of comments made in this course.
* `graded`: (*part 2*) Prints the result of calling `ratio_graded` on the current course ID, to print out the ratio of ungraded and graded assignments.
* `score_unweighted`: (*part 2*) Prints the result of calling `average_score` on the current course ID, to print out the average unweighted assignment score.
* `score`: (*part 2*) Prints the result of calling `average_weighted` on the current course ID, to print out the average weighted assignment score.
* `group`: (*part 2*) Prints out the average of a group by:
    1. Prompting the user for a group name
    2. Calling the `average_group` function
    3. Printing the result
* `assignment`: (*part 2*) Prints out the details for an assignment by:
    1. Prompting the user for an assignment ID
    2. Converting the result to an integer
    3. Calling the `render_assignment` function
    4. Printing the result
* `list`: (*part 2*) Prints out the result of calling `render_all` on the current course ID, to list all the current assignments.
* `scores`: (*part 3*) Call the `plot_scores` function to create a graph of the distribution of fractional scores of graded assignments.
* `earliness`: (*part 3*) Call the `plot_earliness` function to create a graph of the distribution of the earliness of submissions relative to their due date.
* `compare`: (*part 3*) Call the `plot_points` function to create a graph of the relationship between assignments' points possible and their weighted points possible, to analyze how different the values are.
* `predict`: (*part 3*) Call the `predict_grades` function to create a graph with three running sums showing the possible grades that could be earned in the course (maximum ever possible, maximum still possible, minimum still possible).
* `help`: (*new*) Print out all the commands with a brief description of each one. You can use the following text as a base, but can change the text however you see fit (as long as you mention the name of each command at least once):

    ```python
    """
    exit > Exit the application
    help > List all the commands
    course > Change current course
    points > Print total points in course
    comments > Print how many comments in course
    graded > Print ratio of ungraded/graded assignments
    score_unweighted > Print average unweighted score
    score > Print average weighted score
    group > Print average of assignment group, by name
    assignment > Print the details of a specific assignment, by ID
    list > List all the assignments in the course
    scores > Plot the distribution of grades in the course
    earliness > Plot the distribution of the days assignments were submitted early
    compare > Plot the relationship between assignments' points possible and their weighted points possible
    predict > Plot the trends in grades over assignments, showing max ever possible, max still possible, and minimum still possible
    """
    ```

### The main function

The only change you need to make to your `main` function is to change the printed text for the prompt (i.e., the argument to `input`) to include the `help` command, so that users know what commands are available. You are free to make the text of this command say whatever you want, as long as it mentions that the `help` command exists.