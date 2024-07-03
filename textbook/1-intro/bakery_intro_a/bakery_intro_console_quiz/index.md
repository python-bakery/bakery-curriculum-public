---
waltz:
  title: bakery_intro_console_quiz
  display title: 1A3) Console I/O
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
    path: bakery_intro_console_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_console_read"
  },
  "questions": {
    "DefinePrintFunction": {
      "type": "true_false_question",
      "points": 1,
      "body": "Print is an instruction to the computer to retrieve input from the user."
    },
    "DefineConsole": {
      "type": "true_false_question",
      "points": 1,
      "body": "The console is like a chat box that you can type instructions into."
    },
    "ClassifyInputOrOutput": {
      "type": "matching_question",
      "points": 3,
      "body": "Classify each of these as either \"Input\" or \"Output\".",
      "answers": [
        "Input",
        "Output"
      ],
      "statements": [
        "Typing on the keyboard",
        "A monitor displaying information",
        "A printer making a report",
        "A robot moving its arm",
        "Moving the mouse",
        "Data being loaded from a file"
      ]
    },
    "PredictPrintOutput": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Write exactly what will be printed by running the following command:\n```python\nprint(\"Hello World!\")\n```"
    },
    "PredictInputOutput": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Write exactly what will be printed by running the following command:\n```python\ninput(\"Type a number:\")\n```\n\nThe user will type `5` in the box that appears."
    }
  }
}