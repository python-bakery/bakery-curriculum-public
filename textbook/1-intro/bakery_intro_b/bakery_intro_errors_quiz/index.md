---
waltz:
  title: bakery_intro_errors_quiz
  display title: 1B8) Errors
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
    modified: July 12 2022, 1055 AM
  files:
    path: bakery_intro_errors_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_errors_read"
  },
  "questions": {
    "TracebackLine": {
      "type": "short_answer_question",
      "points": 1,
      "body": "According to the following error message, what line of code did the error occur on?\n```python\nTraceback (most recent call last):\n  File \"my_code.py\", line 32, in <module>  \n    45 + \"NameError\"\nTypeError: unsupported operand type(s) for +: 'int' and 'str'\n```"
    },
    "TracebackType": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "According to the following error message, what type of error occurred?\n```python\nTraceback (most recent call last):\n  File \"my_code.py\", line 32, in <module>  \n    45 + \"NameError\"\nTypeError: unsupported operand type(s) for +: 'int' and 'str'\n```",
      "answers": [
        "TypeError",
        "NameError",
        "SyntaxError",
        "No error occurred",
        "We cannot tell the type of error from the information provided"
      ]
    },
    "ErrorHandling": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "When your program has an error, the first thing you should do is:",
      "answers": [
        "Ask for help.",
        "Curl up into a ball and cry.",
        "Check the error message and consider its meaning.",
        "Start debugging your program."
      ]
    },
    "ErrorDescriptions": {
      "type": "matching_question",
      "points": 1,
      "body": "Match each of the following common errors with its description.",
      "answers": [
        "You have referenced a variable that does not exist.",
        "You have used an operator with incorrect types",
        "You have a mistake with your code's grammar or punctuation.",
        "This is not a common type of error."
      ],
      "statements": [
        "NameError",
        "TypeError",
        "SyntaxError",
        "TimeError"
      ]
    }
  }
}