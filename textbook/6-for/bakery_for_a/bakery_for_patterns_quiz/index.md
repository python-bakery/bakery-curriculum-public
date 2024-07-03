---
waltz:
  title: bakery_for_patterns_quiz
  display title: 6A2) For Loop Patterns 1
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
    modified: July 13 2022, 0320 PM
  files:
    path: bakery_for_patterns_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_for_patterns_read"
  },
  "questions": {
    "SumVariablePrediction": {
      "type": "short_answer_question",
      "points": 1,
      "body": "After the third iteration of the loop, what is the value of `sum`?\n```python\nsum = 0\nvalues = [4, 2, 6]\nfor value in values:\n    sum = sum + value\n```"
    },
    "UnderstandCountUpdate": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What does line 4 do?\n```python\ncount = 0\nvalues = [4,5,6]\nfor value in values:\n    count = count + 1\n```",
      "answers": [
        "Takes the current value of count, adds 1 to it, and then updates count with the new value.",
        "Causes an error, because it is algebraically impossible for a number to be one more than itself.",
        "Increases count by the value.",
        "Adds 1 to the list of values."
      ]
    },
    "StatementInsideBody": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Is the `print` call before, inside, or after the `for` loop?\n```python\nfor name in names:\n    print(name)\n```",
      "answers": [
        "Inside",
        "Before",
        "After"
      ]
    },
    "PredictingBooleanAccumulation": {
      "type": "short_answer_question",
      "points": 1,
      "body": "What is the value of `any` after the following Boolean Accumulation is executed?\n```python\nconditions = [False, False, True, False]\nany = False\nfor condition in conditions:\n    any = any or condition\nprint(any)\n```"
    },
    "PredictingStringAccumulation": {
      "type": "true_false_question",
      "points": 1,
      "body": "True or false: the following code prints `True`. You can see this code execute [here][8].\n```python\nnames = [\"Alice\", \"Bob\", \"Carol\"]\njoined_names = \"Alice, Bob, Carol\"\nadded_names = \"\"\nfor name in names:\n    added_names = added_names + name + \", \"\nprint(added_names == joined_names)\n```\n\n   [8]: https://goo.gl/axAGX7"
    }
  }
}