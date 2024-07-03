---
waltz:
  title: bakery_intro_string_ops_quiz
  display title: 1B7) String Operations
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
    path: bakery_intro_string_ops_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_intro_string_ops_read"
  },
  "questions": {
    "EvaluateStringConditionals": {
      "type": "multiple_answers_question",
      "points": 5,
      "body": "Mark each of the following expressions if they evaluate to True. Assume that the following code is executed first:\n```python\ntitle = \"Harry Potter\"\n```",
      "answers": [
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>\"word\" in \"The last word\"\n</pre></div>",
        "<pre>\"c\" in \"Do Capital Letters Matter?\"</pre>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>\"it\" in title\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>\" \" in title\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>\"\" in title\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>\"Alabama\" &lt; \"Virginia\"\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>\"Coward\" &lt;= \"Coward\"\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>\"Dog\" == \"Dog\"\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>title not in \"Harry Potter Book 1\"\n</pre></div>"
      ]
    },
    "StringIndexingZero": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Predict the output of the following code:\n```python\nname = \"Hermione\"  \nprint(name[0])\n```"
    },
    "StringIndexingPositive": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Predict the output of the following code:\n```python\nname = \"Hermione\"  \nprint(name[4])\n```"
    },
    "StringIndexingNegative": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Predict the output of the following code:\n```python\nname = \"Hermione\"  \nprint(name[-2])\n```"
    },
    "StringSubscriptRight": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Predict the output of the following code:\n```python\nname = \"Hermione\"  \nprint(name[:2])\n```"
    },
    "StringSubscriptPositives": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Predict the output of the following code:\n```python\nname = \"Hermione\"  \nprint(name[4:7])\n```"
    },
    "StringSubscriptLeftNegative": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Predict the output of the following code:\n```python\nname = \"Hermione\"  \nprint(name[-3:])\n```"
    }
  }
}