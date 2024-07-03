---
waltz:
  title: bakery_project3_milestone1_introduction
  display title: 1.1) Introduction Reading
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
    version downloaded: 24
    created: November 03 2022, 0111 AM
    modified: November 08 2022, 0604 PM
  files:
    path: bakery_project3_milestone1_introduction
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Welcome to the Final Project! Or rather, the *first milestone* of the final project. This project is so long, you will be completing it in parts. The overall project will have you access and analyze data from Canvas - the same Learning Management System we've been using all semester!

The Canvas Learning Management System has a very robust "API" ("Application Programming Interface" - a set of tools for letting programmers interact with a website or other software system). This allows both instructors AND students to access data programmatically using web requests. The actual code required to interact with the website is a little more complicated than accessing weather data or Reddit data, but not significantly so. However, one critical difference is the addition of authentication. We have prepared a library to help scaffold all this, but we have to dissect everything a little before we start using it.

## Bakery Canvas Library

You may be interested in doing the majority of your development outside of BlockPy, since writing longer programs in Canvas can be a little frustrating. Certainly, by the end of the project, you will want to run your code on your own computer to get the full effect of the software. For that reason, our first step will be to download the Bakery Canvas Library.

1. Create a new folder in your computer where you can store files related to this project.
2. Create a new file named `final_project.py` where you will write your code for this project.
3. Run the (empty) file in Thonny to change the current working directory to the folder you have created.
4. Next, still in that folder, you will need to download both of the following files. Make sure that both files retain their original filename! Confirm that they are in the right place and have the right names using the Files panel in Thonny.

    * <a href="https://blockpy.cis.udel.edu/blockpy/download_file?placement=course&directory=37&filename=bakery_canvas.py" download>Bakery Canvas Library (<code>bakery_canvas.py</code>)</a>
    * <a href="https://blockpy.cis.udel.edu/blockpy/download_file?placement=course&directory=37&filename=bakery_canvas_cache.sqlite" download>Bakery Cache File (<code>bakery_canvas_cache.sqlite</code>)</a>

5. Make sure everything worked by running the following code in `final_project.py`:

```python
from bakery_canvas import get_courses
```

If there are no errors, then you are clear to proceed onward!

## Test Data

The Bakery Canvas Library is similar to the Bakery Weather and Bakery Reddit libraries previously provided. They have a bunch of dataclasses and functions that will help you access data. However, we have also provided an additional file this time: the Bakery Cache File.

With the previous libraries, the cache file was generated automatically the first time you used the libraries. Recall that a cache allows you to store requests to reuse them later. With the other libraries, we used this to cut down on redundant requests. But now we'll see another use case: simplifying testing web-based data.

The cache file we are providing you comes seeded with a large amount of test data that we have created. By using the right set of arguments, you can retrieve this data instead of your own, allowing you to test on your computer locally without needing to constantly check BlockPy. Of course, you will need to submit each Milestone before its due date (the penalties are severe for not doing so!). However, you may find this simpler for most of your development.

Before we can talk about the shape and nature of the Test Data, however, we must understand the concept of *user tokens* and how we can use them to access Canvas' data.

## User Tokens

The Canvas API uses *user tokens* to *identify* and *authenticate* the account accessing the site's data. Canvas then determines what data, if any, that account is *authorized* to access. *Identification*, *authentication*, and *authorization* are the three pillars of computer security (really, all security):

* *Indentification* means claiming to be a particular individual,
* *Authentication* means proving it (e.g., by proving you have a file or password that only the identified individual would have), and 
* *Authorization* is the set of actions the identified individual may take (such as accessing a given piece of data).

In our test data, the user tokens will be human-readable names of our (fake) users with Canvas API data (like `annie` or `jeff`). However, in the real data, you might be surprised to find that the tokens look like long strings of seemingly random characters. That is because these tokens are essentially passwords - you would not want someone to be able to randomly guess your API user token just by writing your name, since they would then have full access to all of your Canvas data!

User tokens have a great deal of power, and with power comes risk. At some point in the project, you may wish to access your own Canvas data by generating your own user token. **Do not share your user token with anyone**, including the course staff. Treat the token as if it were a password to your bank account or social media. When you submit code to the autograder, never include your actual user token!

## Using Test Data

The Bakery Canvas library exposes two functions that you will need to use. For this milestone, you will only need the first function, `get_courses`, which returns a list of `Course` dataclass instances.

```python try-get-courses
from bakery_canvas import get_courses

courses = get_courses("annie")

for course in courses:
    print(course)
```

To fully understand what the `get_courses` function returns, you will need to consult the file and read over the docstrings of the `Course` dataclass. However, the function itself is quite simple: given a user token (a string), the function returns a list of `Course` objects. We can then process that data further for various kinds of analysis. You can get a preview of the Course dataclass from the diagram below - do not worry if it seems a little small, we'll be accessing a lot more data in the second milestone!

![A diagram of the Course dataclass](course_diagram.png)

Here are all of the users we have in the test data:

* `annie` - a strong student who has taken 6 classes and done well in all of them
* `jeff` - a weak student who has taken 6 classes but gotten barely passing grades
* `pierce` - a terrible student who has taken 0 classes
* `troy` - an okay student who has taken only 1 class but did okay in it
* `shirley` - another strong student who has done well in all 6 of their classes
* `abed` - another okay student who has taken 6 classes
