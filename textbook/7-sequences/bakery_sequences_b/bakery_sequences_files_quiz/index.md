---
waltz:
  title: bakery_sequences_files_quiz
  display title: 7B2) Files
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
    version downloaded: 3
    created: June 28 2022, 0300 PM
    modified: August 20 2022, 1209 PM
  files:
    path: bakery_sequences_files_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_sequences_files_read"
  },
  "questions": {
    "OpenClose": {
      "type": "true_false_question",
      "points": 1,
      "body": "After opening a file, you should always close a file."
    },
    "ForFile": {
      "type": "true_false_question",
      "points": 1,
      "body": "A `for` loop will process a file sentence-by-sentence."
    },
    "OpenFile": {
      "type": "true_false_question",
      "points": 1,
      "body": "The `open` function consumes a string representing a path and returns a string of the file's data."
    },
    "TypeReading": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Given the file named `grades.txt` with the following contents:\n```python\n90, 85, 100\n```\n\nAnd the following python code:\n```python\ngrade_file = open(\"grades.txt\")\ngrade_data = grade_file.read()\n```\n\nWhat will be the type of `grade_data`?",
      "answers": [
        "List of String",
        "List of Integer",
        "Integer",
        "String",
        "Dictionary of Integers and Strings",
        "File object"
      ]
    },
    "FileNotFoundError": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Which of the following are causes of a `FileNotFoundError`?",
      "answers": [
        "A file was downloaded to the wrong folder.",
        "The coder mispelled the name of the file when calling <code>open</code>.",
        "The coder wrote <code>opne</code> instead of <code>open</code>.",
        "The coder did not give any arguments to the <code>open</code> function."
      ]
    }
  }
}