---
waltz:
  title: bakery_functions_defining_quiz
  display title: 2A3) Defining Functions
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
    path: bakery_functions_defining_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_functions_defining_read"
  },
  "questions": {
    "FunctionLabeling": {
      "type": "matching_question",
      "points": 3,
      "body": "Identify each part of the function and its call:\n\n![Code annotated with numbers][3]\n\n   [3]: https://i.imgur.com/rNCjHXG.png",
      "answers": [
        "Definition keyword",
        "Function name",
        "Parameter name",
        "Parameter type",
        "Parentheses",
        "Dash and greater than arrow",
        "Return type",
        "Colon",
        "Body",
        "Return value",
        "Argument"
      ],
      "statements": [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11"
      ]
    },
    "FunctionHeaderColon": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Type the symbol that goes at the end of the function definition's header."
    },
    "PassStatement": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What does the `pass` statement do?",
      "answers": [
        "Passes a value to a function",
        "Absolutely nothing",
        "Passes the result of the function back to where it was called."
      ]
    },
    "AdvantagesOfFunctions": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Mark all of the following that ARE advantages of functions.",
      "answers": [
        "Make it easy to reuse code",
        "Code in a function executes faster",
        "Easier to debug code in a function because it is isolated",
        "Functions allow us to store values in variables."
      ]
    },
    "IdentifyFunctionName": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Given the function definition below, what is the name of the function?\n```python\ndef get_area(width:int, height:int) -> int:\n    return width*height\n```"
    },
    "IdentifyFunctionReturnType": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What type of thing is returned from the function below?\n```python\ndef is_on_fire() -> bool:\n    return True\n```",
      "answers": [
        "Boolean",
        "String",
        "Function",
        "None",
        "True",
        "False"
      ]
    },
    "FunctionPossibleReturnTypes": {
      "type": "true_false_question",
      "points": 1,
      "body": "Every function must return an integer or string."
    },
    "FunctionRequiresNames": {
      "type": "true_false_question",
      "points": 1,
      "body": "Every function defined with the \"def\" keyword MUST have a name."
    },
    "MeaningOfDefKeyword": {
      "type": "true_false_question",
      "points": 1,
      "body": "The keyword \"def\" is short for \"define\"."
    },
    "TracingFunctions": {
      "type": "fill_in_multiple_blanks_question",
      "points": 3,
      "body": "Read the following code, and then fill in the blanks below.\n```python\n1| def f(x:int) -> int:\n2|     x = x + 1\n3|     return x\n4| val = 0  \n5| y = f(val)\n6| print(y)\n```\n\n  * What line is executed first? [first]\n  * What line is executed second? [second]\n  * After line 3 is executed, what will be the next line executed? [last]\n\nYou can run the code on [PythonTutor](http://www.pythontutor.com/visualize.html#code=def%20f%28x%3Aint%29%20-%3E%20int%3A%0A%20%20%20%20x%20%3D%20x%20%2B%201%0A%20%20%20%20return%20x%0Aval%20%3D%200%0Ay%20%3D%20f%28val%29%0Aprint%28y%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) to step through and see what\nhappens."
    },
    "GoodValidPythonNames": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "You have been tasked with creating a function that opens a garage door. Which of the following are good, valid names?",
      "answers": [
        "ogd, a short abbreviation that saves many letters when typing.",
        "open_garage_door, a concise name that captures the idea",
        "open garage door, a concise name that captures the idea",
        "door, a short name that saves many letters while typing",
        "openThePodBayDoorsHal, a fun reference to a classic sci-fi movie"
      ]
    }
  }
}