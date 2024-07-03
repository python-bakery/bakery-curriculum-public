---
waltz:
  title: bakery_functions_scopes_quiz
  display title: 2B1) Scopes and Bodies
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
    path: bakery_functions_scopes_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_functions_scopes_read"
  },
  "questions": {
    "ScopeLifetime": {
      "type": "true_false_question",
      "points": 1,
      "body": "The scope of a variable is how long the variable is \"alive\"."
    },
    "ScopeQuantity": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "How many scopes are there in this program?\n```python\ndef make_message(value: int):\n    return \"The result is\" + str(value)\ndef modify_number(a_number: int) -> int:\n    return a_number * 5 + 3\nstart = 10\nprint(make_message(modify_number(start)))\n```",
      "answers": [
        "1 global scopes, 2 local scope",
        "1 local scope, 2 global scopes",
        "2 global scopes",
        "6 global scopes",
        "4 local scopes, 2 global scopes",
        "4 local scopes, 1 global scope"
      ]
    },
    "ScopeRulesOfThumb": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Mark each of the following that are good rules of thumb:",
      "answers": [
        "Variables inside a local scope should not be used outside that local scope.",
        "Variables outside a local scope should not be used inside that local scope.",
        "Variables inside a local scope should only be used outside that local scope.",
        "Variables outside a local scope should only be used inside that local scope."
      ]
    },
    "ScopeIdentify": {
      "type": "matching_question",
      "points": 3,
      "body": "Identify each variable as local to the function `calculate_price` or global:\n```python\ncoupon = 2.99\ndef calculate_price(cost: float) -> float:\n    tax = 1.1\n    price = cost * tax - coupon\n    return price\noriginal_cost = 7.99\nnew_price = calculate_price(original_cost)\n```",
      "answers": [
        "global",
        "local"
      ],
      "statements": [
        "coupon",
        "tax",
        "cost",
        "price",
        "original_cost",
        "new_price"
      ]
    },
    "ScopeReturnVariable": {
      "type": "true_false_question",
      "points": 1,
      "body": "Return can be used to return a variable so that variable is available outside a local scope."
    },
    "ScopeCountUsage": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Consider this program:\n```python\n1 | x = 5\n2 | def do_math(x: int) -> int:\n3 |     return (x ** x + x)\n4 | do_math(x)\n```\n\nHow many times is the variable `x` defined on line 1 used (i.e. either read or written) in this program (including on\nline 1)?"
    },
    "ScopeMutation": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Given the following code:\n```python\ny = 0\ndef increase(y: int) -> int:\n    y = y + 1\n    return y\nincrease(y)\nincrease(y)\nprint(y)\n```\n\nWhat will be printed?"
    },
    "ScopeBadGlobals": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Why are global variables bad?",
      "answers": [
        "They make it harder to think about the program.",
        "They \"leak\" memory so that data can escape the program.",
        "Global variables are not bad.",
        "They make the program slower."
      ]
    },
    "ParameterScopeGood": {
      "type": "short_answer_question",
      "points": 1,
      "body": "What is printed after the code below is executed?\n```python\ndef add_half(a_variable: int) -> float:\n    a_variable = a_variable+.5\n    return a_variable\n\na = 1\na = add_half(a)\nprint(a)\n```"
    },
    "ParameterScopeBad": {
      "type": "short_answer_question",
      "points": 1,
      "body": "What is printed after the code below is executed?\n```python\ndef change_value(a_variable: int) -> int:\n    a_variable = 5\n    return a_variable\n\na = 7\nchange_value(a)\nprint(a)\n```"
    }
  }
}