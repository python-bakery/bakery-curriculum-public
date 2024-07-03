---
waltz:
  title: bakery_if_syntax_quiz
  display title: 3A1) If Statements
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
    path: bakery_if_syntax_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_if_syntax_read"
  },
  "questions": {
    "InsideBlock": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "In the following code, the print statement is ____ the IF statement.\n```python\nif conditional:\n    print(\"The conditional was true\")\n```",
      "answers": [
        "Before",
        "Inside",
        "After"
      ]
    },
    "CountingBranchesNoElse": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "How many branches does this code have?\n```python\nif conditional:\n    print(5)\nprint(2)\n```",
      "answers": [
        "0",
        "1",
        "2",
        "3"
      ]
    },
    "CountingBranchesNestedIf": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "How many branches does this code have?\n```python\nif conditional:\n    if second_conditional:  \n        print(5)  \n    print(1)\nprint(2)\n```",
      "answers": [
        "0",
        "1",
        "2",
        "3"
      ]
    },
    "CountingBranchesElse": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "How many branches does this code have?\n```python\nif conditional:\n    print(5)  \nelse:\n    print(2)\n```",
      "answers": [
        "0",
        "1",
        "2",
        "3"
      ]
    },
    "TracingBranching": {
      "type": "fill_in_multiple_blanks_question",
      "points": 1,
      "body": "Fill out the trace table below by following the execution. If the value is not yet defined, place an \"X\".\n```python\n1 | salary = 1000\n2 | if salary > 100:\n3 |    taxes = .5\n4 | else:\n5 |    taxes = .1\n6 | salary = taxes * salary\n7 | if salary > 100:\n8 |    if salary < 500:\n9 |        taxes = 0\n10|    salary = taxes * salary  \n```\n\nstep | line | salary | taxes  \n---|---|---|---  \n1 | 1 | 1000 | X  \n2 | 2 | 1000 | [taxes2]  \n3 | [line3] | 1000 | [taxes3]  \n4 | 6 | [salary4] | [taxes4]  \n5 | [line5] | [salary5] | [taxes5]  \n6 | [line6] | [salary6] | [taxes6]  \n7 | [line7] | [salary7] | [taxes7]"
    },
    "PossiblyUndefined": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the value of `number_of_users` after this program executes?\n```python\nif False:\n    number_of_users = 5\nprint(number_of_users)\n```",
      "answers": [
        "No value, because an error occurs since the value has not been defined",
        "0, because that is the default value for integer variables",
        "None, because that is the default value for all variables",
        "5, because of the assignment on line 2."
      ]
    }
  }
}