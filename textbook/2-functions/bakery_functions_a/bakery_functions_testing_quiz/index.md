---
waltz:
  title: bakery_functions_testing_quiz
  display title: 2A5) Testing Functions
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
    path: bakery_functions_testing_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_functions_testing_read"
  },
  "questions": {
    "UnitTestImportStatement": {
      "type": "true_false_question",
      "points": 1,
      "body": "The first line of the following code is unnecessary:\n```python\nfrom cisc108 import assert_equal\n\ndef days_to_hours(days:int)->int:\n    return 24 * days\n\nassert_equal(days_to_hours(2), 24)\n```"
    },
    "UnitTestDefinition": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "A unit test is:",
      "answers": [
        "A collection of known inputs and outputs for a function.",
        "A conditional that determines whether the units (e.g., inches, gallons) are correct.",
        "A function that returns a Boolean value.",
        "A function that consumes a function and returns whether the function is correct."
      ]
    },
    "UnitTestIdentification": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Given this function, which of the following unit tests will pass?\n```python\nfrom cisc108 import assert_equal  \n\ndef simple_formula(x: int) -> int:\n    return 3 * x + 4\n```",
      "answers": [
        "assert_equal(simple_formula(0), 4)",
        "assert_equal(simple_formula(3), 13)",
        "assert_equal(simple_formula(-.5), 2.5)",
        "assert_equal(simple_formula(0), 0)",
        "assert_equal(simple_formula(-1), 2)",
        "assert_equal(simple_formula(0:int)->int, 0: int)"
      ]
    },
    "UnitTestAdvantages": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Which of the following are advantages of unit tests?",
      "answers": [
        "They help you find problems early.",
        "They help you facilitate changes down the road.",
        "They make it easier to glue together pieces of code.",
        "They make your code easier to read.",
        "They make your code run faster."
      ]
    },
    "UnitTestBasics": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "When someone says, \"My program looks correct, but it says it fails the unit tests.\"",
      "answers": [
        "The program is probably not correct.",
        "The program is probably correct."
      ]
    },
    "UnitTestQuantity": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "How many unit tests should a program have?",
      "answers": [
        "As many as it takes",
        "1",
        "5",
        "100",
        "One for each line of code"
      ]
    },
    "UnitTestSuccessRate": {
      "type": "true_false_question",
      "points": 1,
      "body": "Unit tests are a 100% effective way of determining if your program is correct."
    }
  }
}