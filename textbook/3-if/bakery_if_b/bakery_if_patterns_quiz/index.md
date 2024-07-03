---
waltz:
  title: bakery_if_patterns_quiz
  display title: 3B2) Logical Patterns
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
    modified: August 10 2022, 0417 PM
  files:
    path: bakery_if_patterns_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_if_patterns_read"
  },
  "questions": {
    "DefinePatterns": {
      "type": "matching_question",
      "points": 3,
      "body": "Match each explanation to the most relevant pattern",
      "answers": [
        "And vs Nested If",
        "Defensive Guard",
        "Early Return",
        "Multiple Return Spots",
        "Build-Up-Return",
        "Define-and-Refine"
      ],
      "statements": [
        "An `if` statement with an `and` can be replaced with two `if` statements, one inside the other.",
        "Wrap some code with an `if` statement so that errors are not caused in certain conditions.",
        "Return a value from a function if a condition is not met, in order to avoid errors.",
        "Return a value from a function with many `if`/`elif`/`else` branches by putting `return` statements in each branch.",
        "Return a value from a function with many `if`/`elif`/`else` branches by updating a variable and then only having one `return` statement at the end.",
        "Avoid having multiple `else` branches to specify default behavior by assinging an initial value to a variable prior to the `if` statements."
      ]
    },
    "DescribeMultipleReturnBehavior": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "What happens when there are multiple `return` statements in a function?",
      "answers": [
        "The program ends when the first `return` statement is reached.",
        "The function ends when the first `return` statement is reached.",
        "An error will occur, because you cannot have more than one `return` statement.",
        "The last `return` statement will be used to determine the returned value.",
        "All the values from all the `return` statements will be combined using the type rules.",
        "The `return` statements must be placed under other control structures like `if` statements, or the other `return` statements will not be reachable."
      ]
    },
    "JustifyBuildUpPattern": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "Why might you use the Build-Up-Return pattern instead of the Multiple-Returns pattern?",
      "answers": [
        "The Build-Up-Return pattern only has one `return` statement, so the control flow is a little less complicated.",
        "The Build-Up-Return pattern often leads to shorter code",
        "The Build-Up-Return pattern often leads to faster code",
        "The Build-Up-Return pattern guarantees that a value will be returned no matter what, unlike the Multiple-Returns where you might forget to return a value from a branch.",
        "The Multiple-Returns pattern is not functionally equivalent to the Build-Up-Return pattern, so that pattern is more powerful."
      ]
    },
    "UseDefensiveGuard": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "In which of these cases might you need a Defensive Guard to avoid an error?",
      "answers": [
        "Make sure that a value is not zero before division",
        "Make sure a string contains only digits, before you convert it to an integer",
        "Make sure an integer is positive, before you convert it to a string",
        "Make sure a boolean value is True, before you invert it with `not`",
        "Make sure that a string has at least one character, before you index the first character",
        "Make sure that a string has at least 5 characters, before you subscript the first ten characters"
      ]
    },
    "RelateLogicalPatterns": {
      "type": "multiple_answers_question",
      "points": 2,
      "body": "Which of these comparions between the patterns are accurate?",
      "answers": [
        "The Early Return and Defensive Guard patterns are similar, since they both avoid problematic code with an `if` statement.",
        "The \"And vs Nested If\" pattern is similar to the \"Defensive Guard\", since one incorporates the `and` operator and the other incorporates the `or` operator",
        "The Build-Up-Return pattern and the Multiple Return Spots patterns are similar, since they both achieve the same result.",
        "The Define-and-Refine pattern is useful for specifying default behavior to avoid having too many branches, just like the Multiple Returns pattern."
      ]
    },
    "PredictNestedIf": {
      "type": "short_answer_question",
      "points": 1,
      "body": "In the following code, what will be printed?\n\n```python\nalpha = 20\nbeta = 3\n\nif alpha > 10:\n    if beta > 10:\n        alpha = 10\n\nprint(alpha)\n```"
    },
    "DeterminePatternEquivalency": {
      "type": "multiple_answers_question",
      "points": 2,
      "body": "Given the following code:\n\n```python\ngamma = \"Hello!\"\nif gamma and gamma[-1] == \"!\":\n    print(\"Exclaim\")\n```\n\nWhich of the following programs are functionally equivalent to the conditional part?\n```python\n#A\nif len(gamma) > 0 and gamma[-1] == \"!\":\n    print(\"Exclaim\")\n``` \n```python\n#B\nif gamma or gamma[-1] == \"!\":\n    print(\"Exclaim\")\n``` \n```python\n#C\nif gamma:\n  if gamma[-1] == \"!\":\n    print(\"Exclaim\")\n``` \n```python\n#D\nif gamma:\n  print(\"Exclaim\")\nif gamma[-1] == \"!\":\n  print(\"Exclaim\")\n``` \n```python\n#E\nif gamma:\n  print(\"Exclaim\")\nelif gamma[-1] == \"!\":\n  print(\"Exclaim\")\n```",
      "answers": [
        "A",
        "B",
        "C",
        "D",
        "E"
      ]
    }
  }
}