---
waltz:
  title: bakery_structures_lists_quiz
  display title: 4B1) Lists
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
    modified: August 24 2022, 0412 PM
  files:
    path: bakery_structures_lists_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_structures_lists_read"
  },
  "questions": {
    "EvaluatePrimitiveCompositeType": {
      "type": "matching_question",
      "points": 2,
      "body": "Identify each of the following as a Primitive Type, Composite Type, or Not a Type.",
      "answers": [
        "Primitive type",
        "Not a type",
        "Composite type"
      ],
      "statements": [
        "None",
        "True",
        "List",
        "Integer"
      ]
    },
    "EvaluateListType": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the type of the following literal value?\n```python\n[4.5, 3.2, 7.3]\n```",
      "answers": [
        "List",
        "Float",
        "Int",
        "String",
        "Boolean",
        "None"
      ]
    },
    "EvaluateListElementType": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the element type of the following literal value?\n```python\n[4.5, 3.2, 7.3]\n```",
      "answers": [
        "List",
        "Float",
        "Int",
        "String",
        "Boolean",
        "None"
      ]
    },
    "ListArrayVector": {
      "type": "true_false_question",
      "points": 1,
      "body": "Lists can also be correctly referred to as \"Arrays\" or \"Vectors\"."
    },
    "PossibleListElementType": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Which of the following are possible element types for a list?",
      "answers": [
        "Float",
        "String",
        "Boolean",
        "List"
      ]
    },
    "ListsAndStringsAreSequences": {
      "type": "true_false_question",
      "points": 1,
      "body": "Lists and strings are both sequences of data."
    },
    "ListLiteralOrStringIndexing": {
      "type": "matching_question",
      "points": 2,
      "body": "Identify each of the following as either \"List literal\" or \"String indexing\".",
      "answers": [
        "List literal",
        "String indexing"
      ],
      "statements": [
        "[]",
        "\"Hermione\"[1]",
        "[\"Hermione\"]",
        "[1]",
        "\"\"[1]"
      ]
    }
  }
}