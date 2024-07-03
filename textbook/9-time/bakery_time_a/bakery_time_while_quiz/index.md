---
waltz:
  title: bakery_time_while_quiz
  display title: 9A1) While Loops
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
    modified: September 19 2022, 1029 PM
  files:
    path: bakery_time_while_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_time_while_read"
  },
  "questions": {
    "LabelWhile": {
      "type": "matching_question",
      "points": 2.5,
      "body": "Identify each part of the while loop shown:\n\n![https://i.imgur.com/CwzqVmS.png quizGraphics.png](https://i.imgur.com/CwzqVmS.png)",
      "answers": [
        "While keyword",
        "Conditional",
        "Colon",
        "Indentation",
        "Body"
      ],
      "statements": [
        "1",
        "2",
        "3",
        "4",
        "5"
      ]
    },
    "WhileVsFor": {
      "type": "true_false_question",
      "points": 1,
      "body": "Syntactically, `while` loops look just like `for` loops. They both have a keyword, a colon, and a list to iterate over."
    },
    "WhileExecutesOnce": {
      "type": "true_false_question",
      "points": 1,
      "body": "A While loop will always execute at least once."
    },
    "LoopEndDecrement": {
      "type": "true_false_question",
      "points": 1,
      "body": "The program below will NOT loop forever.\n```python\ncount = 10\nwhile count >= 0:\n    count = count - 1\nprint(count)\n```"
    },
    "LoopEndIncrement": {
      "type": "true_false_question",
      "points": 1,
      "body": "The program below will NOT loop forever.\n```python\ncount = 0\nwhile count > 0:\n    count = count + 1\nprint(count)\n```"
    },
    "LoopEndMidway": {
      "type": "true_false_question",
      "points": 1,
      "body": "The program below will NOT loop forever.\n```python\nalpha = 'dog'\nwhile alpha == 'dog':\n    alpha = 'cat'\n    print(alpha)\n    alpha = 'dog'\nprint(alpha)\n```"
    },
    "LoopForever": {
      "type": "true_false_question",
      "points": 1,
      "body": "The program below will NOT loop forever.\n```python\nwhile True:\n    print(\"Loop again\")\n```"
    },
    "LoopConvenience": {
      "type": "true_false_question",
      "points": 1,
      "body": "`while` loops are more common in Python than `for` loops because they are safer."
    },
    "LoopLength": {
      "type": "true_false_question",
      "points": 1,
      "body": "A `while` loop will execute once for each expression in the conditional."
    },
    "ControlStructureBodies": {
      "type": "multiple_answers_question",
      "points": 3.5,
      "body": "Which of the following have a body?",
      "answers": [
        "<code>while</code> loop",
        "<code>for</code> loop",
        "Function definition",
        "Function call",
        "<code>if</code> statement.",
        "Dictionary access"
      ]
    }
  }
}