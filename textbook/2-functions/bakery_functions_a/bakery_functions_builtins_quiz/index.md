---
waltz:
  title: bakery_functions_builtins_quiz
  display title: 2A2) Built-in Functions
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
    path: bakery_functions_builtins_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_functions_builtins_read"
  },
  "questions": {
    "InputReturn": {
      "type": "true_false_question",
      "points": 1,
      "body": "The `input` function returns a string."
    },
    "PrintReturn": {
      "type": "true_false_question",
      "points": 1,
      "body": "The `print` function returns a string."
    },
    "StringCountReturn": {
      "type": "short_answer_question",
      "points": 1,
      "body": "According to the linked documentation, what _type_ of value does the [string.count()][1] function return?\n\n   [1]: https://python-sneks.github.io/pages/v3_0/references/strings.html#count"
    },
    "StringSplitParameters": {
      "type": "short_answer_question",
      "points": 1,
      "body": "According to the linked documentation, how many parameters does the [string.split()][2] function take?\n\n   [2]: https://python-sneks.github.io/pages/v3_0/references/strings.html#split"
    },
    "MethodCallResults": {
      "type": "fill_in_multiple_blanks_question",
      "points": 1,
      "body": "According to the [linked documentation](https://python-sneks.github.io/pages/v3_0/references/strings.html), what is the result of each of the following expression involving a method call?\n\n```python\n> \"To be Or not to be, that is the question.\".count(\"o\")\n```\n\n [count]\n\n```python\n> \"You should remember how to use subscripts\"[[5:10]].count(\"o\")\n```\n\n[countsubscripts]\n\n```python\n> \"Where's waldo?\".find(\"w\")\n```\n\n[findw]\n\n```python\n> \"To be or not to be, that is the question.\".upper().count(\"TO\")\n```\n\n[countupper]\n\n```python\n> \"eeeeee\".replace(\"ee\", \"e\").count(\"e\")\n```\n\n[doublee]"
    },
    "MethodComponents": {
      "type": "matching_question",
      "points": 1,
      "body": "Given the method call below, identify each component.\n```python\n\"Open the pod bay doors, Hal!\".replace(\"Open\", \"Close\")\n```",
      "answers": [
        "The calling value",
        "Method name",
        "Argument",
        "Parentheses"
      ],
      "statements": [
        "\"Open the pod bay doors, Hal!\"",
        "replace",
        "\"Open\"",
        "\"Close\"",
        "("
      ]
    },
    "DefineFunctionTerms": {
      "type": "matching_question",
      "points": 3,
      "body": "Match each word to the best definition.",
      "answers": [
        "Method",
        "Replace",
        "Print",
        "Parameter",
        "Parentheses",
        "Function",
        "Argument",
        "Documentation",
        "Call"
      ],
      "statements": [
        "The names given to the values that will be passed into a function.",
        "The curved symbols that go after a function name to ensure that it is called.",
        "A reusable chunk of code that can be called using its name and parentheses.",
        "The values passed into a function.",
        "The extra information about a function supplied to help other programmers understand how to use the function.",
        "The act of using a function via its name and parentheses."
      ]
    }
  }
}