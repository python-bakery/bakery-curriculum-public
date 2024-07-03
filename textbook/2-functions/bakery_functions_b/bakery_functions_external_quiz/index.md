---
waltz:
  title: bakery_functions_external_quiz
  display title: 2B4) External Functions
  resource: problem
  type: quiz
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: true
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 1
    created: June 28 2022, 0300 PM
    modified: August 18 2022, 0358 PM
  files:
    path: bakery_functions_external_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_functions_external_read"
  },
  "questions": {
    "ExternalFunctionsFacts": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "Which of the following statements are true about importing?",
      "answers": [
        "Imported functions cannot be called in user-defined functions.",
        "Imported variables cannot be read in user-defined functions.",
        "You must always test imported functions using `assert_equals` to make sure they work correctly.",
        "Some libraries are not built into standard Python distributions and must be installed separately.",
        "Importing functions is pointless, because you can always just implement the function yourself instead."
      ]
    },
    "DesignerObjectFunctions": {
      "type": "multiple_answers_question",
      "points": 2,
      "body": "According to the [designer documentation](https://designer-edu.github.io/designer/students/functions.html), which of the following are functions that create Designer Objects?",
      "answers": [
        "circle",
        "triangle",
        "apple",
        "rectangle",
        "emoji",
        "text",
        "int"
      ]
    },
    "DesignerCircleFunction": {
      "type": "multiple_answers_question",
      "points": 2,
      "body": "Most Designer functions can take a variable number of arguments, depending on whether you need to override default values. According to the [designer documentation](https://designer-edu.github.io/designer/students/docs.html#circle), which of the following are valid ways to create a circle?",
      "answers": [
        "circle('blue')",
        "circle('red', 10)",
        "circle('green', 10, 0, 0)",
        "circle('yellow', 10, 'top of screen')",
        "rectangle('orange', 50, 30)"
      ]
    },
    "DesignerValidProgram": {
      "type": "true_false_question",
      "points": 1,
      "body": "Will the following code correctly draw an emoji of a fire in the center of the window? (Hint, you can try running it yourself and see!)\n\n```python\nfrom designer import *\n\ndraw(emoji('\ud83d\udd25'))\n```"
    },
    "DesignerDrawMissingArgument": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Why won't the following code make a gold circle appear on the screen?\n\n```python\nfrom designer import *\n\ncircle('gold', 50)\n\ndraw()\n```",
      "answers": [
        "The string `gold` is not a valid Designer color.",
        "The `circle` function needs to have at least four parameters.",
        "The `save` function was not called.",
        "The `draw` function needs to have the result of the `circle` function provided as an argument.",
        "The `import` statement is wrong",
        "Trick question, the code works perfectly."
      ]
    },
    "DesignerMinimumProgram": {
      "type": "multiple_answers_question",
      "points": 2,
      "body": "Which of the following are required at a minimum in order to have a functioning Designer program?",
      "answers": [
        "The `from designer import *` line",
        "One call to the `draw` function, at the end of the program",
        "At least one call to the `rectangle` function",
        "One call to the `save` function, at the end of the program",
        "One call to the `save` function, anywhere in the program"
      ]
    }
  }
}