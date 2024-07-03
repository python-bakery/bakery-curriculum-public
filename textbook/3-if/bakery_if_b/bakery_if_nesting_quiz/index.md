---
waltz:
  title: bakery_if_nesting_quiz
  display title: 3B1) Nested If Statements
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
    path: bakery_if_nesting_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_if_nesting_read"
  },
  "questions": {
    "EquivalentIfs": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Select the two snippets of code that are equivalent.",
      "answers": [
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span><span style=\"color: #008000; font-weight: bold;\">if</span> is_on_fire():\n    <span style=\"color: #008000; font-weight: bold;\">pass</span>\n<span style=\"color: #008000; font-weight: bold;\">if</span> door_is_open():\n    <span style=\"color: #008000; font-weight: bold;\">pass</span>\n<span style=\"color: #008000; font-weight: bold;\">else</span>:\n    <span style=\"color: #008000; font-weight: bold;\">pass</span>\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span><span style=\"color: #008000; font-weight: bold;\">if</span> is_on_fire():\n    <span style=\"color: #008000; font-weight: bold;\">pass</span>\n<span style=\"color: #008000; font-weight: bold;\">elif</span> door_is_open():\n    <span style=\"color: #008000; font-weight: bold;\">pass</span>\n<span style=\"color: #008000; font-weight: bold;\">else</span>:\n    <span style=\"color: #008000; font-weight: bold;\">pass</span>\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span><span style=\"color: #008000; font-weight: bold;\">if</span> is_on_fire():\n    <span style=\"color: #008000; font-weight: bold;\">pass</span>\n<span style=\"color: #008000; font-weight: bold;\">else</span>:\n    <span style=\"color: #008000; font-weight: bold;\">if</span> door_is_open():\n        <span style=\"color: #008000; font-weight: bold;\">pass</span>\n    <span style=\"color: #008000; font-weight: bold;\">else</span>:\n        <span style=\"color: #008000; font-weight: bold;\">pass</span>\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span><span style=\"color: #008000; font-weight: bold;\">if</span> is_on_fire():\n    <span style=\"color: #008000; font-weight: bold;\">pass</span>\n<span style=\"color: #008000; font-weight: bold;\">else</span> <span style=\"color: #008000; font-weight: bold;\">if</span> door_is_open():\n    <span style=\"color: #008000; font-weight: bold;\">pass</span>\n<span style=\"color: #008000; font-weight: bold;\">else</span>:\n    <span style=\"color: #008000; font-weight: bold;\">pass</span>\n</pre></div>"
      ]
    },
    "NestedWhitespace": {
      "type": "short_answer_question",
      "points": 1,
      "body": "If an `if` statement is nested inside another `if` statement, how many spaces will the body of the inner `if` statement\nhave?"
    },
    "IfInFunctions": {
      "type": "true_false_question",
      "points": 1,
      "body": "You can nest `if` statements inside of other `if` statements, but not functions."
    },
    "OptionalElseElif": {
      "type": "true_false_question",
      "points": 1,
      "body": "Every `if` statement must be followed by either an `else` or an `elif`."
    },
    "EqualElif": {
      "type": "true_false_question",
      "points": 1,
      "body": "The `elif` is equivalent to an `else` with an `if` statement nested inside it."
    }
  }
}