---
waltz:
  title: bakery_sequences_indexes_quiz
  display title: 6A1) Index Iteration
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
    modified: September 09 2022, 1052 AM
  files:
    path: bakery_sequences_indexes_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_sequences_indexes_read"
  },
  "questions": {
    "Best Way to Iterate": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Which of the following is the easiest way to print each element of a list in Python?",
      "answers": [
        "<pre>for i in range(len(a_list)):\n  print(a_list[i])</pre>",
        "<pre>for element in a_list:\n  print(element)</pre>",
        "<pre>i = 0\nfor element in a_list:\n  print(a_list[i])\n  i += 1</pre>"
      ]
    },
    "Reasons for Avoiding Indexes": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Which of the following are reasons to avoid using indexes to process a list?",
      "answers": [
        "Index iteration requires extra operations and function calls",
        "Index iteration is a more complex form of iteration to reason about",
        "Index iteration can sometimes skip values in a list.",
        "Index iteration requires a second loop."
      ]
    },
    "Always Avoid Indexing": {
      "type": "true_false_question",
      "points": 1,
      "body": "You should ALWAYS avoid using index iteration to process a list. There are no advantages to it."
    },
    "Enumerate Indexes": {
      "type": "short_answer_question",
      "points": 1,
      "body": "The `enumerate` function consumes a list and returns each element paired with its index. When the following code is run, what is printed on the first line?\n```python\nvalues=[1,2,3]\nfor i, value in enumerate(values):\n    print(i, value)\n```\n\nIf you are not sure, consider trying the code out - you don't have to guess!"
    },
    "Predict Range Function": {
      "type": "short_answer_question",
      "points": 1,
      "body": "The `range` function consumes an integer and can be used to produce a list of numbers from 0 to that integer. When the following code is run, what is printed on the LAST line?\n```python\nfor value in range(10):\n    print(value)\n```\n\nIf you are not sure, consider trying the code out - you don't have to guess!"
    },
    "Predict Range Len Function": {
      "type": "short_answer_question",
      "points": 1,
      "body": "The `range` and `len` functions can be combined to iterate through indices. When the following code is run, what is printed FIRST? Pay close attention to the code inside the `for` loop!\n```python\nvalues=[6, 7, 8]\nfor index in range(len(values)):\n    print(values[index-1])\n```\n\nIf you are not sure, consider trying the code out - you don't have to guess!"
    },
    "Predict Multiple Updates": {
      "type": "fill_in_multiple_blanks_question",
      "points": 3,
      "body": "The following code is executed:\n\n```python\ndata = [[4, 6, 8]]\n\nfor index, value in enumerate(data):\n    data[[index]] = data[[index]] + 1\n    value = value * 2\n\ndata[[1]] = 8\n```\n\nRun the code and evaluate each expression:\n\n1. `data[[0]]`: [index1]\n2. `data[[1]]`: [index2]\n3. `value`: [value]"
    },
    "Swap Variables": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "When this code is executed, what will be printed?\n```python\ndata = [4, 6, 8]\ndata[2], data[0] = [data[0], data[2]]\nprint(data)\n```",
      "answers": [
        "Nothing, because there is an error.",
        "[4, 6, 8]",
        "[4, 8, 6]",
        "[6, 4, 8]",
        "[6, 8, 4]",
        "[8, 4, 6]",
        "[8, 6, 4]"
      ]
    }
  }
}