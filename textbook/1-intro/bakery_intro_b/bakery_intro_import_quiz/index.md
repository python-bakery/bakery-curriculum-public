---
waltz:
  title: bakery_intro_import_quiz
  display title: 1B5) Importing
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
    path: bakery_intro_import_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_import_read"
  },
  "questions": {
    "ImportFunction": {
      "type": "true_false_question",
      "points": 1,
      "body": "`import` is a function that takes in the name of a module and loads the functions, variables, and other definitions."
    },
    "MathModuleContents": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Review the [documentation][9] for the built-in `math` module. Which of the following are functions available from it?\n\n   [9]: https://docs.python.org/3/library/math.html",
      "answers": [
        "sqrt",
        "log",
        "log4",
        "log10",
        "exponent",
        "add"
      ]
    },
    "ExplainImport": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Which of the following is the best description of this line of code?\n```python\nfrom math import sqrt as square_root\n```",
      "answers": [
        "Loads the sqrt function in the math module but renames it square_root",
        "Loads the math function from the sqrt module but renames it sqrt",
        "Loads the square_root function from the math module but renames it sqrt",
        "Loads the sqrt and square_root functions from the math module"
      ]
    },
    "ModulePackageVariablesDefinitions": {
      "type": "matching_question",
      "points": 1,
      "body": "A _1 ___ contains _2_, which in turn can provide functions, _3_, and more after being imported",
      "answers": [
        "package",
        "module",
        "variables",
        "for loops",
        "if statements"
      ],
      "statements": [
        "1",
        "2",
        "3"
      ]
    }
  }
}