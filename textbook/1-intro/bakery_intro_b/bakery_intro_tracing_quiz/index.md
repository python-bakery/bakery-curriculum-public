---
waltz:
  title: bakery_intro_tracing_quiz
  display title: 1B2) Tracing
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
    path: bakery_intro_tracing_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_tracing_read"
  },
  "questions": {
    "Variables Change Value over Program": {
      "type": "true_false_question",
      "points": 1,
      "body": "Variables change their value over time according to the instructions in a program."
    },
    "ReadWriteVariable": {
      "type": "matching_question",
      "points": 2.5,
      "body": "Label each of the following as either a \"Read\", a \"Write\", or a \"Read and Write\" for the variable \"x\".",
      "answers": [
        "Write",
        "Read",
        "Read and Write"
      ],
      "statements": [
        "x = 0",
        "print(x)",
        "y = x + z",
        "x = x + 1",
        "x == 1"
      ]
    },
    "VariableUsageSynonyms": {
      "type": "matching_question",
      "points": 1,
      "body": "For each word, choose the best synonym:",
      "answers": [
        "Write",
        "Initialize",
        "Update",
        "Read"
      ],
      "statements": [
        "Set",
        "Define",
        "Change",
        "Store",
        "Use",
        "Load",
        "Increment",
        "Create"
      ]
    }
  }
}