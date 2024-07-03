---
waltz:
  title: bakery_intro_strings_quiz
  display title: 1B6) Strings
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
    path: bakery_intro_strings_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_strings_read"
  },
  "questions": {
    "LiteralStringValues": {
      "type": "multiple_answers_question",
      "points": 3.5,
      "body": "Select any of the following that are string literal values.",
      "answers": [
        "<code>\"5\"</code>",
        "<code>my_string</code>",
        "<code>\"my_variable\"</code>",
        "<code>_5</code>",
        "<code>5</code>",
        "<code>\"Hello</code>",
        "<code>'World\"</code>"
      ]
    },
    "StringsHaveNumbers": {
      "type": "true_false_question",
      "points": 1,
      "body": "True or False: Strings are composed of only letters and symbols."
    },
    "AddingStrings": {
      "type": "true_false_question",
      "points": 1,
      "body": "```python\n\"1\" + \"1\" = \"2\"\n```"
    },
    "WritingStringLiterals": {
      "type": "fill_in_multiple_blanks_question",
      "points": 2.5,
      "body": "How do you write each of the following as string literals?\n\nThe first letter of the alphabet, lower case: [lettera]  \nA tab character: [tab]  \nA new line: [newline]  \nA double quote: [doublequote]  \nA single quote: [singlequote]  \nThe empty string: [empty]"
    }
  }
}