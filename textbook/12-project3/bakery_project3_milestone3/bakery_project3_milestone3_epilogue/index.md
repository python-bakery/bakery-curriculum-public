---
waltz:
  title: bakery_project3_milestone3_epilogue
  display title: 3.7) The End
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 2
    created: November 26 2022, 1213 PM
    modified: November 26 2022, 1231 PM
  files:
    path: bakery_project3_milestone3_epilogue
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
Welcome to the end of the final project! If you did everything correctly, you should now have a complete system for interacting with your own Canvas data.

## Your Own Data

In part 1, we described how you can obtain a user token to access your own data. We are repeating the instructions here, but also repeating the warnings. Take them seriously! Never let ANYONE have access to your user token, for any reason!

Follow these instructions to get <a href="https://community.canvaslms.com/t5/Admin-Guide/How-do-I-manage-API-access-tokens-as-an-admin/ta-p/89" target=_blank>a user access token from Canvas</a>. Name the token whatever you want. Be sure to have the token expire after about a day: that will limit the possible damage in case someone gets your token. It's easy to just get a new one when the old one expires.

Once you have the token, copy it somewhere secure that you will be able to find later (e.g., a local text file or password manager). Do *not* store the user token in your source code file. Remember, anyone with the token can impersonate you on Canvas, and who knows what damage they could do! Treat it like a password. If you think your token may have been leaked accidentally, immediately delete the token and generate a new one. There is no cost to generating new tokens! Do so as you need to, to protect yourself. 

We recommend you follow this process:

1. First, in Thonny, click the "View" menu at the top of the window (top of the screen in Mac). Then click "Program Arguments" to make the `Program arguments` box appear near the top of the interface. Copy and paste your user token into the `Program arguments` box. This is a new way to get values into your program, as "arguments"!
2. Inside of your main `final_project.py` file, you can use the following code to retrieve the contents of the `Program arguments` box and pass it to the `main` function at the end:

    ```python
    import sys

    # ... All the rest of the project code

    if __name__ == '__main__':
        my_user_token = sys.argv[1]
        main(my_user_token)
    ```


## Ideas for Extension

This project is just a starting point. We have some ideas below for more complex ways to extend the tool you have created. We hope you will consider trying them - even just attempting them will teach you a lot!

* More analyses:
    * Plot the quantity of assignments and comments across multiple courses, and see which of your classes are most complex or most interactive
    * Calculate the average duration of each assignment (based on when it opens and when it locks), or make a graph relating the weighted points possible for the assignment and its duration
    * Make a [box plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html) for comparing the distributions of each assignment group in a course
    * Make scatter plots comparing the dates for when assignments were *created* or *graded*, instead of just when they were *submitted*
    * Make a third line for `predict_grades` that uses *regression* to calculate a true *predicted* grade based on the other grades seen (e.g., using [Ordinary Least Squares linear regression](https://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.OLS.html))
* Prettier graphs: 
    * Add `label`s and a `legend` to your `predict_grades` graph. Consider making some be dotted lines, or change the colors of the lines.
    * Use the `xlim` and `ylim` functions to maintain a consistent domain and range for your axes
    * Try out the `seaborn` library (which is built on `matplotlib`) to make much prettier and more effective graphs
* Crack open the `bakery_canvas` library and look at how it gets and transforms its data (using the [Canvas API](https://canvas.instructure.com/doc/api/), or look at [Python libraries for accessing Canvas](https://pypi.org/search/?q=canvas+instructure):
    * Create a system for downloading your assignment submissions and making backups of everything you've submitted
    * Create a script that detects when new assignments have been created and pops up a notification, then set it to run regularly on your computer
    * ...?