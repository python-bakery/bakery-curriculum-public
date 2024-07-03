---
waltz:
  title: bakery_if_events_quiz
  display title: 3B3) Events
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
    version downloaded: 2
    created: June 28 2022, 0300 PM
    modified: September 11 2022, 0922 AM
  files:
    path: bakery_if_events_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_if_events_read"
  },
  "questions": {
    "RecallEventBindingRules": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "When binding events in designer, you:",
      "answers": [
        "MUST NOT include parentheses after the name of the function inside of the `when`",
        "MUST put the `when` function calls AFTER the function definitions but BEFORE the `start` call",
        "MAY have some parameters and not others for certain events (e.g., the `typing` event MAY have a `key` parameter).",
        "MUST NOT call the `when` function more than once.",
        "MAY put the function definition inside of the `when` call, instead of the function name on its own."
      ]
    },
    "DescribeEventStrings": {
      "type": "matching_question",
      "points": 2,
      "body": "Match each event string to the relevant description of when it occurs:",
      "answers": [
        "updating",
        "typing",
        "clicking",
        "starting",
        "deleting",
        "integer",
        "listening"
      ],
      "statements": [
        "The function will be run many times every second.",
        "The function will be run whenever the user presses a key on the keyboard.",
        "The function will be run whenever the user presses a mouse button.",
        "The function will be run once at the beginning of the game."
      ]
    },
    "IdentifyBindingSyntax": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "After defining a function named `move_dog`, which of the following correctly binds the function to the `'typing'` event?",
      "answers": [
        "when('typing', move_dog())",
        "when(typing, move_dog)",
        "typing = move_dog()",
        "when('typing', move_dog)",
        "if 'typing':\n  move_dog()"
      ]
    },
    "DifferentiateIfWhen": {
      "type": "multiple_answers_question",
      "points": 2,
      "body": "Which of the following statements are true?",
      "answers": [
        "`if` is a statement, while `when` is a function",
        "Both `if` and `when` have a body directly below their header.",
        "Anything that you can do with an `if`, you can also do with a `when`; they are meant to be used interchangeably.",
        "You will use `when` in most Python programs, since it's a useful built-in part of the language just like `if`"
      ]
    },
    "DescribeWorldParameter": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "The first parameter of an event's bound function...",
      "answers": [
        "is the same type as the argument that was passed into `start`",
        "Is the same exact value every time the bound function gets called.",
        "Can be of type `DesignerObject`",
        "Represents the current state of the game",
        "Can be manipulated inside the body of the bound function"
      ]
    },
    "ExplainDesignerUpdating": {
      "type": "multiple_choice_question",
      "points": 3,
      "body": "When the following program runs, what is the best explanation of what will occur?\n\n```python\nfrom designer import *\n\ndef mystery(dragon: DesignerObject):\n    set_visible(dragon, not get_visible(dragon))\n\nwhen('updating', mystery)\nstart(emoji(\"Dragon\"))\n```",
      "answers": [
        "Every time the user clicks the mouse, the dragon will flash invisible",
        "Every time the user presses the enter key, the dragon will flash invisible",
        "Many times a second, the dragon will flash invisible",
        "Nothing, because the code has a runtime error",
        "Nothing, because the `mystery` function is not bound correctly"
      ]
    },
    "IdentifyDesignerMistakes": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "The following program is meant to make a red box move across the screen. What problems are in the following program?\n\n```python\nbox = rectangle(\"red\", 50, 100)\n\ndef make_smaller():\n    change_x(box, 10)\n\nwhen('updating', make_smaller)\nstart()\n```",
      "answers": [
        "The `designer` library is not being imported",
        "There are no unit tests",
        "Scope rules are being violated",
        "The `box` variable should have been passed into `start`",
        "There are no print statements"
      ]
    }
  }
}