---
waltz:
  title: bakery_intro_math_quiz
  display title: 1A6) Math
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
    path: bakery_intro_math_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_math_read"
  },
  "questions": {
    "ArithmeticOperatorPrecedence": {
      "type": "matching_question",
      "points": 2,
      "body": "Put these operators in order of their precedence (what order they are evaluated):",
      "answers": [
        "Parentheses",
        "Exponents",
        "Multiplication, Modulo, and Division",
        "Addition, Subtraction"
      ],
      "statements": [
        "First:",
        "Second",
        "Third",
        "Fourth"
      ]
    },
    "Question": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Predict the result of this expression:\n```python\n4 + 5 * 2\n```"
    },
    "FloatDivisionConversion": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Predict the result of this expression:\n```python\n10 / 5 - 1\n```"
    },
    "IntegerDivisionConversion": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Predict the result of this expression:\n```python\n10 // 5 - 1\n```"
    },
    "ModuloOperator": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Predict the result of this expression:\n```python\n(10+8) % 12\n```"
    },
    "AdditionOperatorArity": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "How many things can be added at once with the \"+\" operator?",
      "answers": [
        "None, computers can't add.",
        "Two things.",
        "Any number of things."
      ]
    },
    "StringPlusInt": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the result if you ask Python to perform the following computation?\n```python\n\"2\"+2\n```",
      "answers": [
        "\"22\"",
        "4",
        "\"4\"",
        "You cannot add these together."
      ]
    }
  }
}