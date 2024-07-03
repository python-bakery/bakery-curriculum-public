---
waltz:
  title: bakery_structures_mutability_quiz
  display title: 4B3) Mutability
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
    path: bakery_structures_mutability_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_structures_mutability_read"
  },
  "questions": {
    "Immutable or Mutable": {
      "type": "matching_question",
      "points": 1,
      "body": "Identify each of the following as mutable or immutable:",
      "answers": [
        "Immutable",
        "Mutable"
      ],
      "statements": [
        "String",
        "List",
        "Integer",
        "Boolean"
      ]
    },
    "Methods Always Mutate": {
      "type": "true_false_question",
      "points": 1,
      "body": "When you call a method, it will always change the value of the variable you called it on. For example, the following\ncode changes the value of the variable `name`:\n```python\nname = \"Klaus\"\nname.lower()\n```"
    },
    "Result of Mutable Method": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What value will the variable `longer_list` have after the following code runs?\n```python\nlonger_list = [1,2]\nlonger_list = longer_list.append(3)\n```",
      "answers": [
        "[1,2,3]",
        "[1,2]",
        "3",
        "None",
        "[3,1,2]"
      ]
    }
  }
}