---
waltz:
  title: bakery_intro_comments_quiz
  display title: 1B4) Comments
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
    modified: August 10 2022, 0348 PM
  files:
    path: bakery_intro_comments_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_comments_read"
  },
  "questions": {
    "CommentSymbolSynonyms": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Which of the following are synonyms for the comment symbol in Python?",
      "answers": [
        "Octothorpe",
        "Exclamation",
        "Sigil",
        "Hash",
        "Decorator",
        "Variable",
        "Print",
        "Pound Sign"
      ]
    },
    "DetermineCommentedOutEnd": {
      "type": "short_answer_question",
      "points": 1,
      "body": "What part of this line's code will be commented out?\n```python\na = 7#+3#+2\n```"
    },
    "DetermineCommentedOutEntire": {
      "type": "short_answer_question",
      "points": 1,
      "body": "What part of this line's code will be commented out?\n```python\n# 1/0\n```"
    },
    "DetermineCommentedOutString": {
      "type": "short_answer_question",
      "points": 1,
      "body": "What part of this line's code will be commented out?\n```python\nm = \"#3\" #4\n```"
    },
    "RecallCommentingAdvice": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "According to our advice, which of these scenarios justifies leaving a comment in your program?",
      "answers": [
        "A syntax error is breaking your program, so you comment that code out",
        "One line of code works, but it is somewhat confusing despite all your attempts to make it more clear; you want to explain how it works.",
        "Every line of code should be commented, so that anyone can read the code.",
        "Never leave a comment, it's a useless feature",
        "You have some old code that you no longer need, and want to remove it from your program with a comment."
      ]
    },
    "InterpretCommentedLineCounts": {
      "type": "fill_in_multiple_blanks_question",
      "points": 2,
      "body": "Given the program below:\n\n  ```python\n  # Here is my program.\n\n  x = 12\n  # Do some math\n  y = x / 60 + .5\n  print(y)\n  ```\n\n1. How many lines are there? [lineCount]\n2. How many steps will be executed? [stepCount]"
    }
  }
}