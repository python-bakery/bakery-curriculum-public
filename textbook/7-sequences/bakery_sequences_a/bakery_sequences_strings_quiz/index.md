---
waltz:
  title: bakery_sequences_strings_quiz
  display title: 7A2) String Iteration
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
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: September 09 2022, 1022 AM
  files:
    path: bakery_sequences_strings_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_sequences_strings_read"
  },
  "questions": {
    "Lists vs. Strings": {
      "type": "true_false_question",
      "points": 1,
      "body": "Strings are sequences of characters, and lists are sequences of any type."
    },
    "Split Type": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the type of the result of the following expression?\n```python\n\"1,2,3,4\".split(\",\")\n```",
      "answers": [
        "List",
        "String",
        "Integer",
        "Causes an error"
      ]
    },
    "Split Element Type": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the element type of the result of the following expression?\n```python\n\"1,2,3,4\".split(\",\")\n```",
      "answers": [
        "List",
        "String",
        "Integer",
        "Causes an error"
      ]
    }
  }
}