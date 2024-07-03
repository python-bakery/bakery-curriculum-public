---
waltz:
  title: bakery_intro_modules_quiz
  display title: 1B3) Modules
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
    path: bakery_intro_modules_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_modules_read"
  },
  "questions": {
    "SequentialStatements": {
      "type": "true_false_question",
      "points": 1,
      "body": "Normally, statements are executed from top to bottom."
    },
    "LeftToRightExpressions": {
      "type": "true_false_question",
      "points": 1,
      "body": "Expressions are evaluated from left to right"
    },
    "StepByStepExecution": {
      "type": "true_false_question",
      "points": 1,
      "body": "Programs may execute very quickly in computers, but they always happen one step at a time."
    },
    "ExpressionComponents": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "Which of the following can be involved in an expression?",
      "answers": [
        "Literal values",
        "Arithmetic operators",
        "Other expressions",
        "Conditional operators",
        "Statements",
        "Variables"
      ]
    },
    "ExpressionType": {
      "type": "matching_question",
      "points": 1,
      "body": "Evaluate each of the following expressions and identify the type of the result.",
      "answers": [
        "Float",
        "Integer",
        "Boolean",
        "String"
      ],
      "statements": [
        "(1 + 2) * 4 / 3",
        "1 + 2 + 3 + 4 + 5",
        "(1 + 2) > 4",
        "\"Hello \" + \"World\"",
        "4 > 5 or 5 == 6"
      ]
    }
  }
}