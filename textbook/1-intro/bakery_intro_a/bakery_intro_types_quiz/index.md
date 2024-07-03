---
waltz:
  title: bakery_intro_types_quiz
  display title: 1A5) Types
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
    modified: August 30 2022, 0714 PM
  files:
    path: bakery_intro_types_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_types_read"
  },
  "questions": {
    "LiteralType": {
      "type": "matching_question",
      "points": 4,
      "body": "Identify the type of each literal value.",
      "answers": [
        "Integer",
        "Boolean",
        "Float",
        "String",
        "None"
      ],
      "statements": [
        "5",
        "False",
        "4.3",
        "\"Hello World\"",
        "\"4\"",
        "\"\"",
        "None",
        "0",
        "\"True\""
      ]
    },
    "PrimitiveTypeDescriptions": {
      "type": "matching_question",
      "points": 3,
      "body": "Match each type to its description.",
      "answers": [
        "Whole numbers",
        "Text",
        "Decimal numbers",
        "A special value that means nothing",
        "True or False",
        "This is not a type"
      ],
      "statements": [
        "Integer",
        "String",
        "Float",
        "None",
        "Boolean",
        "Python"
      ]
    },
    "IntegerLiterals": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "Which of the following are Integers, in Python?",
      "answers": [
        "0",
        "\"Five\"",
        "\"7\"",
        "5.5",
        "2.0",
        "-100000257"
      ]
    },
    "PrintStringOutput": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Write the output of the print statement:\n```python\nprint(\"5\")\n```"
    },
    "NumberOfValuesPerTypes": {
      "type": "matching_question",
      "points": 2,
      "body": "How many possible values are there for each type?",
      "answers": [
        "More than 100",
        "2",
        "1"
      ],
      "statements": [
        "Integer",
        "Boolean",
        "String",
        "Float",
        "None"
      ]
    },
    "TypeAbbreviations": {
      "type": "matching_question",
      "points": 2,
      "body": "Match each type to its abbreviation in Python:",
      "answers": [
        "int",
        "None",
        "bool",
        "str"
      ],
      "statements": [
        "Integer",
        "None",
        "Boolean",
        "String"
      ]
    }
  }
}