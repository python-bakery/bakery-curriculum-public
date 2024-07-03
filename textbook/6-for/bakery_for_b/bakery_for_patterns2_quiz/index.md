---
waltz:
  title: bakery_for_patterns2_quiz
  display title: 6B1) For Loop Patterns 2
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
    version downloaded: 2
    created: June 28 2022, 0300 PM
    modified: July 13 2022, 0320 PM
  files:
    path: bakery_for_patterns2_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_for_patterns2_read"
  },
  "questions": {
    "TakePatternPrediction": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "After this code is executed, what is printed?\n```python\nnames = ['Tasha', 'Bruce', 'Tony?', 'Steve?', 'Bucky']\nknown_names = []\ntaking = True\nfor name in names:\n    if \"?\" in name:\n        taking = False\n    elif taking:\n        known_names.append(name)\n\nprint(known_names)\n```",
      "answers": [
        "['Tasha', 'Bruce']",
        "['Tasha', 'Bruce', 'Tony?']",
        "['Tasha', 'Bruce', 'Bucky']",
        "Tony?",
        "Bruce",
        "['Tony?', 'Steve?', 'Bucky']"
      ]
    },
    "FindMissingPrediction": {
      "type": "short_answer_question",
      "points": 1,
      "body": "After this code is executed, what value is stored in `my_value`?\n```python\nmy_value = None\nvalues = [\"Hi\", \"there\", \"my\", \"friend\"]\nfor value in values:\n    if value.upper() == \"MY\":\n        my_value = value\n```"
    },
    "FilterVsMaxPattern": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Which pattern does this code most resemble?\n```python\nlowest = 100\ngrades = [90, 64, 72, 50]\nfor grade in grades:\n    if lowest > grade:\n        lowest = grade\nprint(lowest)\n```",
      "answers": [
        "Min/Max Pattern",
        "Filter",
        "Take Pattern",
        "Sum",
        "Accumulator"
      ]
    },
    "IdentifyLoopPatternInFunction": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Which pattern does this function implement?\n```python\ndef get_dog(animals: [str]) -> str:\n    last_dog = None\n    for animal in animals:\n        if \"dog\" in animal.lower():\n            last_dog = animal\n    return last_dog\n```",
      "answers": [
        "Find Pattern",
        "Filter",
        "Take Pattern",
        "Max Pattern",
        "Accumulator"
      ]
    },
    "MatchLoopPatternDescriptions": {
      "type": "matching_question",
      "points": 3,
      "body": "Based on the description, determine the most appropriate loop pattern OR list operation.",
      "answers": [
        "List indexing",
        "List subscripting",
        "Find pattern",
        "Filter pattern",
        "Map pattern",
        "Count pattern",
        "Sum pattern",
        "Take pattern",
        "Min pattern",
        "Max pattern"
      ],
      "statements": [
        "I need to find the last value in a list of numbers.",
        "I need to get the first five elements in a list of numbers.",
        "I need to get the last even number in a list.",
        "I need to find all the even numbers in a list.",
        "I need to triple the value of all the numbers in a list.",
        "I need to determine how many numbers are in a list.",
        "I need to add up all the numbers in a list.",
        "I need to get all the numbers in a list until we encounter zero.",
        "I need the lowest number in a list.",
        "I need the highest number in a list."
      ]
    }
  }
}