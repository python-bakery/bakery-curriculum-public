---
waltz:
  title: bakery_functions_calling_quiz
  display title: 2A1) Calling Functions
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
    path: bakery_functions_calling_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_functions_calling_read"
  },
  "questions": {
    "ValidCall": {
      "type": "multiple_answers_question",
      "points": 4,
      "body": "Mark all of the following that are valid function or method calls. Do not worry if a variable exists, only determine\nwhether 1) this is a function or method call, and 2) the syntax is valid.",
      "answers": [
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>list.pop()\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span><span style=\"color: #7D9029;\">.open</span>()\n</pre></div>",
        "fire",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>build(<span style=\"color: #666666;\">1</span>, <span style=\"color: #666666;\">2</span>, <span style=\"color: #666666;\">3</span>)\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>a <span style=\"color: #666666;\">=</span> <span style=\"color: #666666;\">0</span>\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span><span style=\"color: #008000; font-weight: bold;\">print</span>()\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span><span style=\"color: #BA2121;\">\"help\"</span>()\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span><span style=\"color: #BA2121;\">\"harry potter\"</span><span style=\"color: #666666;\">.</span>title()\n</pre></div>"
      ]
    },
    "MethodOrFunction": {
      "type": "matching_question",
      "points": 2,
      "body": "Identify whether the following is a method call or a function call.",
      "answers": [
        "Method call",
        "Function call"
      ],
      "statements": [
        "list.append()",
        "print()",
        "function.call()",
        "method()",
        "\"function\".method()"
      ]
    },
    "CallingFunction": {
      "type": "short_answer_question",
      "points": 1,
      "body": "How would you call a function named `openDoor`? Assume it takes no arguments."
    },
    "StringCallWithOperator": {
      "type": "short_answer_question",
      "points": 1,
      "body": "The function `makeCat` below returns the string \"Cat\". What value will the variable `x` hold after the line is executed?\n```python\nx = makeCat() + makeCat() + makeCat()\n```"
    },
    "IntegerCallWithOperators": {
      "type": "short_answer_question",
      "points": 1,
      "body": "The function `add5` below returns the number 5 added to the argument. What value will the variable \"x\" hold after the\nline is executed?\n```python\nx = add5(10) * add5(2)\n```"
    },
    "FunctionDefintion": {
      "type": "true_false_question",
      "points": 1,
      "body": "Functions are reusable chunks of code that have inputs and outputs."
    }
  }
}