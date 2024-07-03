---
waltz:
  title: bakery_functions_flow_quiz
  display title: 2B3) Function Flow
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
    path: bakery_functions_flow_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_functions_flow_read"
  },
  "questions": {
    "FlowReturn": {
      "type": "true_false_question",
      "points": 1,
      "body": "You can use the `return` statement to return a variable from a function."
    },
    "FlowParameters": {
      "type": "true_false_question",
      "points": 1,
      "body": "Values enter functions as arguments when the function is called, and then the arguments' values are assigned to\nparameters when the function's body begins executing."
    },
    "FlowPrint": {
      "type": "true_false_question",
      "points": 1,
      "body": "The `print` function is necessary to call a function."
    },
    "FlowShare": {
      "type": "true_false_question",
      "points": 1,
      "body": "The two functions below share a variable named `score`:\n```python\ndef increase(score: int) -> int:\n    return score+1\ndef decrease(score: int) -> int:\n    return score-1\n```"
    },
    "FlowBetween": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "Given the program below,\n```python\nname = input(\"What is your name?\")\ndef fix_capitalization(name: str) -> str:\n    return name.title().strip()\ndef make_message(name: str):\n    return \"Hello\" + name + \"how are you?\"\n```\n\nWhich of the following lines of code will have the data flow correctly through both functions in order to produce the\nmessage with the fixed capitalization?",
      "answers": [
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\">\n<pre style=\"line-height: 125%;\">fix_capitalization(name)\nmake_message(name)\n</pre>\n</div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\">\n<pre style=\"line-height: 125%;\">make_message(fix_capitalization(name))\n</pre>\n</div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\">\n<pre style=\"line-height: 125%;\">fix_capitalization()\nmake_message()\n</pre>\n</div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\">\n<pre style=\"line-height: 125%;\"><span style=\"color: #008000; font-weight: bold;\">print</span>(fix_capitalization(name))\n<span style=\"color: #008000; font-weight: bold;\">print</span>(make_message(name))\n</pre>\n</div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\">\n<pre style=\"line-height: 125%;\">name <span style=\"color: #666666;\">=</span> fix_capitalization(name)\nmake_message(name)\n</pre>\n</div>",
        "None are necessary, because the variables share the same name."
      ]
    },
    "FlowSubstitution": {
      "type": "matching_question",
      "points": 2,
      "body": "Given the program below:\n```python\ndef x(a:int) ->int:\n    return 6+a\ndef y(a:int) -> int:\n    return a*2\ndef z(a:int) -> int:\n    return a-1\nprint(x(y(z(3))))\n```\n\nMatch each blank to the value that will be substituted as the last line is executed:",
      "answers": [
        "3",
        "2",
        "4",
        "10",
        "None",
        "1",
        "0",
        "5"
      ],
      "statements": [
        "print(x(y(z(___))))",
        "print(x(y(___)))",
        "print(x(___))",
        "print(___)",
        "___"
      ]
    }
  }
}