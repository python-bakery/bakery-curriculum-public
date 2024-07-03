---
waltz:
  title: bakery_structures_list_ops_quiz
  display title: 4B2) List Operations
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
    path: bakery_structures_list_ops_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_structures_list_ops_read"
  },
  "questions": {
    "ListIndexing": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the value stored in \"my_var\" after the following strange code is executed?\n```python\nmy_var = [1,2,3][1]\n```",
      "answers": [
        "[1, 2, 3]",
        "[1]",
        "[2]",
        "1",
        "2",
        "An error occurs"
      ]
    },
    "InvalidListComparison": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the value stored in \"my_var\" after the following code is executed?\n```python\nmy_var = [1,2,3] < 5\n```",
      "answers": [
        "True",
        "False",
        "An error occurs"
      ]
    },
    "ListMembership": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the value stored in \"my_var\" after the following code is executed?\n```python\nmy_var = 5 in [1,3,5]\n```",
      "answers": [
        "True",
        "False",
        "An error occurs."
      ]
    },
    "InvalidListAddition": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the value stored in \"my_var\" after the following code is executed?\n```python\nmy_var = [1,2,3] + 4\n```",
      "answers": [
        "[1, 2, 3, 4]",
        "[1, 2, 3]",
        "10",
        "An error occurs"
      ]
    },
    "ListAppend": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Which of the following demonstrates how to add something to the following list variable?\n```python\ntemperatures = [44, 36, 72]\n```",
      "answers": [
        "append(temperatures, 42)",
        "append(42) to temperatures",
        "temperatures.append(42)",
        "temperatures = temperatures + 42",
        "temperatures = 42"
      ]
    }
  }
}