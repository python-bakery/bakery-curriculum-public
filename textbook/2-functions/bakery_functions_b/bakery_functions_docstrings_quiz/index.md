---
waltz:
  title: bakery_functions_docstrings_quiz
  display title: 2B2) Docstrings
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
    path: bakery_functions_docstrings_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_functions_docstrings_read"
  },
  "questions": {
    "DocumentationSingleLineSymbol": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Enter the symbol (not its name) used for single-line comments in Python."
    },
    "DocumentationMultiTripleQuotes": {
      "type": "true_false_question",
      "points": 1,
      "body": "Multi-line comments in Python are actually just triple-quoted strings."
    },
    "DocumentationSingleLineIgnored": {
      "type": "true_false_question",
      "points": 1,
      "body": "Single-line comments are ignored by Python, and so are only for human benefit."
    },
    "DocumentationAlwaysComment": {
      "type": "true_false_question",
      "points": 1,
      "body": "You should always document every line of a program."
    },
    "DocumentationIntepret": {
      "type": "fill_in_multiple_blanks_question",
      "points": 3,
      "body": "Interpret the documentation below to fill in the blanks:\n```python\ndef make_time(hour:int, minute:int, second:float)->str:\n    '''\n    Creates a string representation of the given hour, minute, and second.\n    Note that this takes into account Daylight Savings Time.\n\n    Args:\n        hour (int): The number of hours past midnight (military time).\n        minute (int): The number of minutes past the hour.\n        second (float): The number of seconds past the minute, which can be a\n                        decimal number (indicating milliseconds).\n    Returns:\n        str: A string representation of the time (\"hh:mm:ss.sss\") including\n             milliseconds.\n    '''\n```\n\n  1. This function takes [paramCount] parameters.\n  2. The second parameter is named [secondParameter].\n  3. The third parameter's type is [thirdType].\n  4. The function's return type is [returnType].\n  5. We want to change the type of `hour` to be text. You need to replace `int` with [strType].\n  6. We need to add a new parameter named `is_dst` to test if it is daylights saving time. This will be a boolean value. What is the name and type that will go in the Args of the documentation? Don't include indentation, the colon or a description, just the name and type with parentheses: [newArg]"
    },
    "DocumentationReasons": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Which of the following are reasons for commenting code?",
      "answers": [
        "To support code sharing",
        "To make it easier to understand our own code, later.",
        "To test if a function has the right inputs for some given outputs",
        "To keep a copy of code that you want to eliminate, in case you need it later."
      ]
    }
  }
}