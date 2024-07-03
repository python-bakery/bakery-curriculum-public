---
waltz:
  title: bakery_intro_variables_quiz
  display title: 1B1) Variables
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
    path: bakery_intro_variables_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_variables_read"
  },
  "questions": {
    "ValidPythonNames": {
      "type": "multiple_answers_question",
      "points": 5,
      "body": "Choose which of the following are valid Python variable names. Note that they do not have to be _good_ variable names,\njust valid.",
      "answers": [
        "current-temperature",
        "_54__",
        "pag_counnt",
        "asdffdf",
        "page count",
        "\"books\"",
        "_bad_news",
        "_5_99_555_999",
        "4th_property",
        "EarthQuake"
      ]
    },
    "GoodPythonNames": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "You have a variable that represents your allowance, measured in dollars. Which of the following are _good_ variable\nnames? In this case, \"good\" means that they are not too long, not too short, and the intent of the variable is\nunambiguous.",
      "answers": [
        "allowance",
        "d",
        "allowance_in_dollars",
        "data",
        "integer",
        "a_variable_that_will_hold_my_allowance_money"
      ]
    },
    "VariableSolvingUnknown": {
      "type": "true_false_question",
      "points": 1,
      "body": "A variable is useful because it allows to solve for an unknown value."
    },
    "ComputersUnderstandVariableNames": {
      "type": "true_false_question",
      "points": 1,
      "body": "Variable names are important because computers understand the meaning of names and change their value accordingly."
    }
  }
}