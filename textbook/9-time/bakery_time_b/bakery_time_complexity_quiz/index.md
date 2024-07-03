---
waltz:
  title: bakery_time_complexity_quiz
  display title: 9B1) Time Complexity
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
    version downloaded: 4
    created: June 28 2022, 0300 PM
    modified: October 13 2022, 0249 PM
  files:
    path: bakery_time_complexity_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_time_complexity_read"
  },
  "questions": {
    "Recall Program Evaluation Criteria": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "What three criteria are commonly used to evaluate a program?",
      "answers": [
        "How readable the program is.",
        "Whether the program uses enough loops.",
        "How fast the program is.",
        "How clever the program is.",
        "Whether the program is correct.",
        "How many lines of code are in the program."
      ]
    },
    "Define Program Measurement Methods": {
      "type": "matching_question",
      "points": 1,
      "body": "Match each description to its most accurate label.",
      "answers": [
        "Wall Clock Time",
        "RAM Model",
        "Lines of Code",
        "Quadratic Growth",
        "Time Equation",
        "Random Guessing"
      ],
      "statements": [
        "Measuring the actual time taken by the program.",
        "Estimating the time each statement of a program will take via a simplified model of execution.",
        "The number of statements in the program."
      ]
    },
    "Order Time Complexity": {
      "type": "matching_question",
      "points": 1,
      "body": "Put these mathematical relationships in order from slowest to fastest growth relative to each other.",
      "answers": [
        "Constant",
        "Linear",
        "Quadratic"
      ],
      "statements": [
        "Fastest",
        "In-between",
        "Slowest"
      ]
    },
    "Identify Time Complexity of Problems": {
      "type": "matching_question",
      "points": 1,
      "body": "Mark each of the following as either constant, linear, or quadratic based on the size of the input. You can assume that we are talking about the worst possible input for each possible given size input.",
      "answers": [
        "constant",
        "linear",
        "quadratic"
      ],
      "statements": [
        "Adding together three numbers.",
        "Adding up a list of numbers.",
        "Doubling every element of a list.",
        "Checking to see if a list contains a negative number.",
        "Getting the first and last elements of a list and adding them together.",
        "Getting the first element of each row of a 2-dimensional list.",
        "Check to see if a certain number is in a 2-dimensional list." 
      ]
    }
  }
}