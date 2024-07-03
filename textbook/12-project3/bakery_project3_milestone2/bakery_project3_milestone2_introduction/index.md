---
waltz:
  title: bakery_project3_milestone2_introduction
  display title: 2.1) Introduction Reading
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: true
    publicly indexed: false
  additional settings:
    small_layout: true
    disable_tifa: true
    preload_files: '{"course": {"37": {"canvas_data.json": true}}}'
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 18
    created: November 11 2022, 1112 AM
    modified: November 13 2022, 0912 PM
  files:
    path: bakery_project3_milestone2_introduction
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Welcome to Part 2 of the project! Here you will start working with the submissions for individual courses. The data model (and the data) gets more complex, and there are more functions for you to implement.

## Get Submissions

Previously, we showed you how to use `get_courses` to access the courses for a given `user_token`. Now we will use the `get_submissions` function, which consumes both a `user_token` and a `course_id` (an integer) in order to return a list of `Submission`.

```python try-get-submissions
from bakery_canvas import get_courses, get_submissions

# Access one of the courses' data
courses = get_courses('annie')
some_course = courses[0]
print(some_course)

# Actually access submission data
submissions = get_submissions('annie', some_course.id)
for submission in submissions:
    print(submission)
```

The code above first prints out one of the courses (we chose the first one, but you could look at other courses too). Then, it prints out each of the `Submission` objects for that course.

You can use the code above to explore the dataset more fully, and learn what submissions different user tokens have. For your convenience, here is a list of the user tokens we have prepared for you:

* `annie` - a strong student who has taken 6 classes and done well in all of them
* `jeff` - a weak student who has taken 6 classes but gotten barely passing grades
* `pierce` - a terrible student who has taken 0 classes
* `troy` - an okay student who has taken only 1 class but did okay in it
* `shirley` - another strong student who has done well in all 6 of their classes
* `abed` - another okay student who has taken 6 classes

## Submission Data Model

![Diagram modeling the Submission dataclass and its related classes](submission_diagram.png)

The `Submission` dataclass has quite a few fields, two of which involve other dataclasses: `comments` is a `list[Comment]` and `assignment` is a single `Assignment`. The singular `Assignment` dataclass in turn has a single `Group` dataclass (the Assignment Group). In other words, a `Submission` always has an `Assignment` and an `Assignment` always has a `Group`. Any given `Submission` may have any number of `Comment` instances associated with it.

Many of the fields of a `Submission` may be "blank" (representing an unsubmitted or ungraded assignment), but the fields of the `Assignment` for that `Submission` will still have data. The `status` field can be used to determine what state the assignment is in (`"submitted"`, `"graded"`, `"missing"`, `"late"`). Only two checks usually need to be made in a `Assignment`: whether the `grade` field is an empty string (indicating an ungraded assignment) and whether the `missing` field is `True` (indicating an unsubmitted assignment). Otherwise, the assignment should have a meaningful `score`. For some of our courses in the test data, you will find that all assignments have been submitted; but in others, you may find that students have not submitted assignments or the assignments have not yet been graded.

The `score` will be a float, usually less than the `points_possible` for the `Assignment` (although extra credit is possible on Canvas!). Since `score` is the raw points earned for the assignment, you will need to divide the `score` by the `points_possible` for the student's actual performance. The `grade` is usually a letter grade representation of a `score` (e.g., `A-`), although some courses have `grade` as a number. Scores always need to be multiplied by the `weight` of the `Group` to determine their contribution to the final grade. All the distinct groups in a course should have their weights add up to 100 (keep in mind that two different assignments may be in the same group). Put together, this gives us the following formula for determining a given assignment's actual weighted score in the overall course (assuming it has been graded):

```
(Score / Points Possible) * (Group Weight) = Weighted Assignment Percentage
```

<!-- A number of fields in the data are strings representing dates/times (e.g., `submitted_at`, `graded_at`). The documentation mentions that they are in "ISO format" (when not blank), which is an international standard format for writing dates. We will wait until Part 3 to work with that data more closely.-->

## Submission Test Data

We have attempted to generate authentic-seeming test data for you to work with. This is a surprisingly difficult problem (especially since we have limited access to example courses and students!). Do not be surprised if, after you pass our unit tests, you have to make further refinements to the code to work with your own courses' data. Who knows what strange twists and turns other instructors will do to their courses? Certainly not us. If you find that the functions we have you write pass our tests but fail on your own courses, it'd be interesting to report back what happens, so we could generalize our data a little!