---
waltz:
  title: bakery_if_truthiness_quiz
  display title: 3A2) Truthiness
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
    modified: September 11 2022, 0448 PM
  files:
    path: bakery_if_truthiness_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "poolRandomness": "ATTEMPT",
    "readingId": "bakery_if_truthiness_read"
  },
  "questions": {
    "EvaluateTruthinessExplanation": {
      "type": "text_only_question",
      "points": 0,
      "body": "Select each of the following if the expression evaluates to True, according to the rules of Truthiness in Python. The\nquestions might change each time you take the quiz."
    },
    "ET-ZeroString": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"0\"`"
    },
    "ET-Or1": {
      "type": "true_false_question",
      "points": 1,
      "body": "`1 > 5 or 3`"
    },
    "ET-SpaceString": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\" \"`"
    },
    "ET-ZeroFloat": {
      "type": "true_false_question",
      "points": 1,
      "body": "`0.0`"
    },
    "ET-FilledString": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"Corgis are cute\"`"
    },
    "ET-EmptyString": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"\"`"
    },
    "ET-NegativeFloat": {
      "type": "true_false_question",
      "points": 1,
      "body": "`-5.0`"
    },
    "ET-NegativeZero": {
      "type": "true_false_question",
      "points": 1,
      "body": "`-0`"
    },
    "ET-SmallFloat": {
      "type": "true_false_question",
      "points": 1,
      "body": "`0.01`"
    },
    "ET-NegativeInt": {
      "type": "true_false_question",
      "points": 1,
      "body": "`-12332`"
    },
    "ET-LargeInt": {
      "type": "true_false_question",
      "points": 1,
      "body": "`134342`"
    },
    "ET-MediumInt": {
      "type": "true_false_question",
      "points": 1,
      "body": "`144`"
    },
    "ET-SmallInt": {
      "type": "true_false_question",
      "points": 1,
      "body": "`1`"
    },
    "ET-ZeroInt": {
      "type": "true_false_question",
      "points": 1,
      "body": "`0`"
    },
    "ET-EmptyStringSingle": {
      "type": "true_false_question",
      "points": 1,
      "body": "`''`"
    },
    "ET-FalseString": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"False\"`"
    },
    "ET-QuoteString": {
      "type": "true_false_question",
      "points": 1,
      "body": "`'\"'`"
    },
    "ET-TrueString": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"True\"`"
    },
    "ET-CompareString": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"1 > 5\"`"
    },
    "ET-MathInt": {
      "type": "true_false_question",
      "points": 1,
      "body": "`8-4*2`"
    },
    "ET-MathPlus": {
      "type": "true_false_question",
      "points": 1,
      "body": "`1+0`"
    },
    "ET-MathDivision": {
      "type": "true_false_question",
      "points": 1,
      "body": "`1/2`"
    },
    "ET-False": {
      "type": "true_false_question",
      "points": 1,
      "body": "`False`"
    },
    "ET-None": {
      "type": "true_false_question",
      "points": 1,
      "body": "`None`"
    },
    "ET-SubscriptEmpty": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"Hermione\"[4:4]`"
    },
    "ET-SubscriptFull": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"Harry\"[1:-1]`"
    },
    "ET-IndexCharacter": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"Harry\"[0]`"
    },
    "ET-EmptyMethod": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"\".upper()`"
    },
    "ET-MethodItself": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"\".upper`"
    },
    "ET-FullMethod": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"HI\".lower()`"
    },
    "ET-1Or0": {
      "type": "true_false_question",
      "points": 1,
      "body": "`1 or 0`"
    },
    "ET-1And0": {
      "type": "true_false_question",
      "points": 1,
      "body": "`1 and 0`"
    },
    "ET-AndIsNotAddition": {
      "type": "true_false_question",
      "points": 1,
      "body": "`-5 and 5`"
    },
    "ET-AndTrue": {
      "type": "true_false_question",
      "points": 1,
      "body": "`-1 < 4 and 0`"
    },
    "ET-AndFalse": {
      "type": "true_false_question",
      "points": 1,
      "body": "`5 < 4 and 3`"
    },
    "ET-AndStrings": {
      "type": "true_false_question",
      "points": 1,
      "body": "`\"Hi\" and \"Low\" and \"\"`"
    }
  },
  "pools": [
    {
      "amount": 12,
      "questions": [
        "ET-ZeroString",
        "ET-Or1",
        "ET-SpaceString",
        "ET-ZeroFloat",
        "ET-FilledString",
        "ET-EmptyString",
        "ET-NegativeFloat",
        "ET-NegativeZero",
        "ET-SmallFloat",
        "ET-NegativeInt",
        "ET-LargeInt",
        "ET-MediumInt",
        "ET-SmallInt",
        "ET-ZeroInt",
        "ET-EmptyStringSingle",
        "ET-FalseString",
        "ET-QuoteString",
        "ET-TrueString",
        "ET-CompareString",
        "ET-MathInt",
        "ET-MathPlus",
        "ET-MathDivision",
        "ET-False",
        "ET-None",
        "ET-SubscriptEmpty",
        "ET-SubscriptFull",
        "ET-IndexCharacter",
        "ET-EmptyMethod",
        "ET-MethodItself",
        "ET-FullMethod",
        "ET-1Or0",
        "ET-1And0",
        "ET-AndIsNotAddition",
        "ET-AndTrue",
        "ET-AndFalse",
        "ET-AndStrings"
      ]
    }
  ]
}