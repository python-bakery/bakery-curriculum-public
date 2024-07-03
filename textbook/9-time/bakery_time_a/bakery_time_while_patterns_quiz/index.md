---
waltz:
  title: bakery_time_while_patterns_quiz
  display title: 9A2) While Loop Patterns
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
    modified: October 17 2022, 1013 AM
  files:
    path: bakery_time_while_patterns_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_time_while_patterns_read"
  },
  "questions": {
    "InputLimit": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "How many times does the loop body below execute?\n```python\ncommand = \"\"\nwords = []\nwhile command != \"quit\":\n    command = input(\"Type a word:\")\n    words.append(command)\nprint(words)\n```",
      "answers": [
        "None",
        "At least once",
        "At least twice",
        "No more than 10 times"
      ]
    },
    "Linear Decay": {
      "type": "short_answer_question",
      "points": 1,
      "body": "How many times will the code below print? If the loop executes infinitely, then enter -1 instead.\n\n```python\ncounter = 500\nwhile counter > 1:\n    counter = counter - 2\n    print(counter)\n```"
    },
    "Logarithmic Decay": {
      "type": "short_answer_question",
      "points": 1,
      "body": "How many times will the code below print? If the loop executes infinitely, then enter -1 instead.\n\n```python\ncounter = 500\nwhile counter > 1:\n    counter = counter // 2\n    print(counter)\n```"
    },
    "Define Patterns": {
      "type": "matching_question",
      "points": 1,
      "body": "Match each description to the appropriate pattern.",
      "answers": [
        "Numeric While",
        "Random Looping",
        "Read-Evaluate-Print-Loop",
        "User Input Loop",
        "Main Game/Server Loop",
        "While Map Loop",
        "Reverse Dataclass Loop"
      ],
      "statements": [
        "An infinite loop used to make a program continue indefinitely.",
        "Satisfying some complicated constraint by trying many different numbers over and over again.",
        "Iterating over numbers, usually in a non-linear fashion.",
        "Repeatedly getting text from the user in order until the input is correct.",
        "Repeatedly getting text from the user in order to execute commands based on what they enter."
      ]
    }
  }
}