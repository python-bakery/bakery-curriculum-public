---
waltz:
  title: bakery_intro_values_quiz
  display title: 1A4) Values
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
    path: bakery_intro_values_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_values_read"
  },
  "questions": {
    "ExplainPurposeOfValues": {
      "type": "true_false_question",
      "points": 1,
      "body": "The purpose of a value is to represent data from the real world."
    },
    "OnlyPrintLiterals": {
      "type": "true_false_question",
      "points": 1,
      "body": "The \"print\" instruction can only print literal values."
    },
    "LiteralValueDefinition": {
      "type": "true_false_question",
      "points": 1,
      "body": "Literal values are specific values written in the source code."
    },
    "ValueRepresentation": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What does the following value specifically represent?\n\n`24`",
      "answers": [
        "The number of hours in a day",
        "We have no way of knowing without more information.",
        "The number of cookies I ate last night",
        "A popular TV show"
      ]
    },
    "WhatCanValuesRepresent": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "Which of the following could be represented with a value?",
      "answers": [
        "A person's height",
        "The text of Moby Dick",
        "The number of meals you've eaten this week",
        "A text description of someone's emotional response to a poem",
        "An audio recording of a song"
      ]
    }
  }
}