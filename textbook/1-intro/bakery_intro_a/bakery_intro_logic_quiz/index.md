---
waltz:
  title: bakery_intro_logic_quiz
  display title: 1A7) Logic
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
    path: bakery_intro_logic_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_logic_read"
  },
  "questions": {
    "EvaluateConditional": {
      "type": "matching_question",
      "points": 6,
      "body": "Identify whether each of these are True or False.",
      "answers": [
        "True",
        "False",
        "Causes an error"
      ],
      "statements": [
        "3 < 5",
        "False",
        "10 == 10.0",
        "10 == \"10\"",
        "5 == 5.5",
        "7 != 7",
        "3 < \"5\"",
        "not False",
        "1 < 2 and 5 < 7",
        "5 < 4 or 3 == 3",
        "True or (True and False)",
        "not True and False"
      ]
    },
    "ConditionalOperatorArity": {
      "type": "matching_question",
      "points": 2,
      "body": "How many values can each of these operators take?",
      "answers": [
        "2 values",
        "1 value"
      ],
      "statements": [
        "<",
        "not",
        "and",
        "!="
      ]
    },
    "ConditionalsAreNotDistributive": {
      "type": "true_false_question",
      "points": 1,
      "body": "Given the following code:\n```python\nage = 0\n```\n\nAre the following two expressions equivalent?\n```python\nage == 10 or 0\nage == 10 or age == 0\n```"
    }
  }
}