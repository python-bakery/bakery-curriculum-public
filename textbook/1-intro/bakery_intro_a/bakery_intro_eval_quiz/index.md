---
waltz:
  title: bakery_intro_eval_quiz
  display title: 1A8) Interactive Evaluation
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
    modified: August 10 2022, 0330 PM
  files:
    path: bakery_intro_eval_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_eval_read"
  },
  "questions": {
    "EvaluateExpressionLonger": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Evaluate the following expression:\n```python\n(1 + 2) * (3 + 4)\n```"
    },
    "RunningProgramUnusedExpression": {
      "type": "multiple_choice_question",
      "points": 2,
      "body": "What will happen when the following code is run as a program from the editor?\n```python\n400 / 2\n```",
      "answers": [
        "The program will crash because the syntax is not valid.",
        "The program will crash because the semantics are not valid.",
        "A value will be computed, but nothing will be printed in the console.",
        "A value will be computed, and printed on the console."
      ]
    },
    "EvaluatingExpressionConsole": {
      "type": "multiple_choice_question",
      "points": 2,
      "body": "What will happen when the following code is run on the interactive console?\n```python\n400 / 2\n```",
      "answers": [
        "The program will crash because the syntax is not valid.",
        "The program will crash because the semantics are not valid.",
        "A value will be computed, but nothing will be printed in the console.",
        "A value will be computed, and printed on the console."
      ]
    },
    "InteractiveConsoleFacts": {
      "type": "multiple_answers_question",
      "points": 4,
      "body": "Which of the following statements are true about the interactive console?",
      "answers": [
        "You must use `print` to make text appear on the console from a program.",
        "You do not need to use `print` to make text appear when you evaluate an expression from the interactive console.",
        "Every expression evaluated in a program will be printed on the console, by default.",
        "Every program must print, otherwise the program will not run."
      ]
    },
    "InteractiveConsoleTerminology": {
      "type": "matching_question",
      "points": 2,
      "body": "Match each term to its definition:",
      "answers": [
        "The interactive area of a programming environment where output is printed and input is taken from the user.",
        "To execute an expression and compute the result",
        "A synonym for the console",
        "To execute one or more lines of code, possibly with some kind of output (but that is not guaranteed)",
        "To put text onto the console"
      ],
      "statements": [
        "Console",
        "Evaluate",
        "Shell",
        "Run",
        "Print"
      ]
    }
  }
}