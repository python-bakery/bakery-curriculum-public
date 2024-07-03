---
waltz:
  title: bakery_nesting_2d_lists_quiz
  display title: 8B1) Nested Lists
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
    modified: September 22 2022, 0553 PM
  files:
    path: bakery_nesting_2d_lists_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_nesting_2d_lists_read"
  },
  "questions": {
    "Write Nested Index Expressions": {
      "type": "fill_in_multiple_blanks_question",
      "points": 3,
      "body": "Captain the Cat has created a treasure map using the following code:\n\n```python\nsea = [\n    [[\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\"]],\n    [[\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\"]],\n    [[\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf34\",\"\ud83d\udc8e\",\"\ud83c\udf0a\"]],\n    [[\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\"]],\n    [[\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\"]],\n    [[\"\ud83c\udff4\u200d\u2620\ufe0f\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\"]],\n    [[\"\ud83d\udea2\",\"\ud83d\udc08\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83c\udf0a\",\"\ud83d\udc20\"]],\n]\n```\n\nWrite the nested indexing expressions that will produce the following values:\n\n* `\"\ud83c\udf34\"`: [palmTree]\n* `\"\ud83d\udc8e\"`: [treasure]\n* `\"\ud83d\udea2\"`: [ship]\n* `\"\ud83c\udff4\u200d\u2620\ufe0f\"`: [pirateFlag]\n* `\"\ud83d\udc20\"`: [fish]"
    },
    "Predict Indexing Type": {
      "type": "matching_question",
      "points": 2,
      "body": "Given the following code...\n\n```python\nscores = [ [5, 3, 4, 3],\n           [7, 3, 4, 3],\n           [5, 2, 3, 2]]\n\ntotal = 0\nfor row in scores:\n    for score in row:\n        total = total + score\n```\n\nWhat is the most accurate type for each of the following expressions?",
      "answers": [
        "int",
        "list[int]",
        "list[list[int]]",
        "int[list]",
        "str"
      ],
      "statements": [
        "scores",
        "scores[0]",
        "scores[0][0]",
        "row",
        "score",
        "total"
      ],
      "retainOrder": true
    },
    "Count Nested List Elements": {
      "type": "fill_in_multiple_blanks_question",
      "points": 2,
      "body": "Given the following code...\n\n```python\nscores = [[ [5, 3, 4, 3]],\n           [[7, 3, 4, 3]],\n           [[5, 2, 3, 2]] ]\n```\n\n* How many lists are there? [countList]\n* How many integers are there? [countIntegers]\n* How many elements are in the `scores` list? [lengthList]\n* How many integers are in the first inner list? [lengthFirstList]"
    },
    "Predict Nested Loop Pattern MinMax": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Given the following code...\n\n```python\ndef beta(values: list[int]) -> int:\n    result = values[0]\n    for value in values:\n        if value > result:\n            result = value\n    return result\n\ndef alpha(values: list[list[int]]) -> int:\n    result = beta(values[0])\n    for row in values:\n        beta_row = beta(row)\n        if beta_row < result:\n            result = beta_row\n    return result\n    \ngrades = [\n    [90, 99, 95],\n    [75, 50, 60],\n    [80, 90, 100]\n]\n```\n\nWhat value will be produced when the expression `alpha(grades)` is evaluated?"
    },
    "Predict Nested Loop Pattern Find": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Given the following code:\n\n```python\ndef foo(values: list[list[str]]) -> list[str]:\n    result = []\n    for row in values:\n        result.append(bar(row))\n    return result\n    \ndef bar(row: list[str]) -> str:\n    result = \"\"\n    for word in row:\n        if word and word[-1] == \"?\":\n            result = word\n    return result\n    \nwords = [\n    [\"Yes\", \"What?\", \"No\"],\n    [\"Huh?\", \"Why?\", \"How?\"],\n    [\"Oops\", \"All\", \"Gone\"]\n]\n```\n\nWhat value will be produced when the expression `foo(words)` is evaluated?",
      "answers": [
        "[\"Yes\", \"Huh?\", \"Oops\"]",
        "[\"Yes\", \"What?\", \"No\"]",
        "[\"Huh?\", \"Why?\", \"How?\"]",
        "[\"What?\", \"Huh?\", \"\"]",
        "[\"What?\", \"How?\", \"\"]",
        "[]",
        "[\"\", \"\", \"\"]"
      ]
    }
  }
}