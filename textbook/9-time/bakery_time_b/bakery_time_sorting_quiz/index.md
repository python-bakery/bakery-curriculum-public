---
waltz:
  title: bakery_time_sorting_quiz
  display title: 9B2) Sorting
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
    modified: October 17 2022, 1030 AM
  files:
    path: bakery_time_sorting_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_time_sorting_read",
    "attemptLimit": -1,
    "coolDown": -1,
    "feedbackType": "IMMEDIATE",
    "questionsPerPage": -1,
    "poolRandomness": "ATTEMPT"
  },
  "questions": {
    "Differentiate Sorting and Searching Speed": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Which is faster, sorting a list of elements or searching the same list of elements?",
      "answers": [
        "Sorting is always faster.",
        "Searching is always faster.",
        "Sorting is usually faster, unless the list is already sorted and the item we search for is not in the list.",
        "Searching is usually faster, unless the list is already sorted and the item we search for is not in the list."
      ]
    },
    "Actual Values Affect Runtime": {
      "type": "true_false_question",
      "points": 1,
      "body": "True or False: time that an algorithm takes is always dependent on the size of the input, not on the actual values of the input."
    },
    "Binary Search on Unsorted List": {
      "type": "true_false_question",
      "points": 1,
      "body": "True or False: binary search would not work on an unsorted list of numbers."
    },
    "Binary Search on Strings": {
      "type": "true_false_question",
      "points": 1,
      "body": "True or False: binary search only works on numbers, because you cannot order strings."
    },
    "Binary Search vs Iterative Search Speed": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Why is binary search faster than iterative search?",
      "answers": [
        "Binary search uses binary numbers, which are faster than regular numbers.",
        "Binary search repeatedly divides the search space in half each time.",
        "Binary search uses ancient forbidden magic taught to us by the elder gods.",
        "Binary search uses the RAM Model to estimate where the item is before seeking it.",
        "Binary search alternates between checking the first and last elements, moving inwards, finding the value in half the time.",
        "Nobody knows. The secret is lost to time."
      ]
    },
    "Counting Search Checks": {
      "type": "matching_question",
      "points": 2,
      "body": "Each time a search algorithm considers a possible item in a list, that is considered a \"check\".",
      "answers": [
        "0 checks",
        "1 check",
        "2 checks",
        "6 checks",
        "10 checks",
        "100 checks"
      ],
      "statements": [
        "In the best case, how many checks would iterative search need to find an item in a list of 100 numbers?",
        "In the worst case, how many checks would iterative search need to find an item in a list of 100 numbers?",
        "In the best case, how many checks would binary search need to find an item in a list of 100 numbers?",
        "In the worst case, how many checks would binary search need to find an item in a list of 100 numbers?"
      ]
    },
    "Describe Insertion Sort": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Which of the following is an accurate summary of Insertion Sort?\n\nWe recommend you check out this page: <https://visualgo.net/en/sorting>",
      "answers": [
        "Repeatedly find the smallest element in the rest of the list and move it to the front of the list.",
        "Walk through each position of the list, and move the current element into the earlier position in the list where it belongs.",
        "Swap each pair of elements repeatedly until all the elements are in the proper order.",
        "Repeatedly divide the list into two halves, sort each half, and then merge them back together.",
        "Repeatedly shuffle the list until the list is in sorted order."
      ]
    },
    "The Importance of Sorting and Searching": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Which of the following are valid reasons that Computer Scientists study sorting and searching so much?",
      "answers": [
        "Searching and sorting are common problems for lists.",
        "Both searching and sorting have been studied closely, so they are well-understood.",
        "Programmers often need to make their own sorting and search algorithms, since most languages do not have their own implementation built-in to the language.",
        "Sorting and searching are very complicated problems, so studying them makes us feel smarter and superior to other disciplines."
      ]
    }
  },
  "pools": []
}