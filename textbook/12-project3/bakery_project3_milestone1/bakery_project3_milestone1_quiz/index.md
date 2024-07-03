---
waltz:
  title: bakery_project3_milestone1_quiz
  display title: 1.1) Introduction
  resource: problem
  type: quiz
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 2
    created: November 03 2022, 0112 AM
    modified: November 08 2022, 0604 PM
  files:
    path: bakery_project3_milestone1_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_project3_milestone1_introduction"
  },
  "questions": {
    "DefineCache": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Which of the following is the best definition for a \"cache\" as it is used in this course?",
      "answers": [
        "A collection of items of the same type stored in a hidden or inaccessible place.",
        "A way of storing data for future reuse.",
        "A way of measuring how long a program takes.",
        "A system of breaking down complex tasks into simpler ones.",
        "Currency or money used for coding purposes."
      ]
    },
    "RecallUserTokens": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Which of the following statements are true about user tokens?",
      "answers": [
        "It's safe to share your user token with anyone.",
        "You should share your user token only with friends you trust.",
        "You can share your user token with the instructor of the course.",
        "You should not share your user token with anyone.",
        "You should sell your user token to the highest bidder."
      ]
    },
    "ListFakeUsers": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Which of the following are users in the test data?",
      "answers": [
        "luz",
        "jeff",
        "abed",
        "annie",
        "babbage",
        "ada",
        "captain"
      ]
    },
    "ReadDocumentationGetCourses": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What type of value does the `get_courses` function return?",
      "answers": [
        "Courses",
        "Course",
        "list[Course]",
        "Submission",
        "list[Submission]",
        "int",
        "str",
        "float",
        "bool"
      ]
    },
    "ReadDocumentationCourseFields": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "According to the docstring, what is the best explanation of what the `url` field of `Course` contains?",
      "answers": [
        "A link to the course on Canvas",
        "A link to the course's image on Canvas",
        "A link to the next course in the list",
        "A link to BlockPy",
        "A link to the official Canvas website"
      ]
    },
    "CheckTestData": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Which of the following are courses for `annie`? You should be able to check by running the example code above!",
      "answers": [
        "Intro to Math",
        "History of Ice Cream",
        "Intro to Spanish",
        "Introduction to Computer Science",
        "History of Rock",
        "Advanced Nerf Warfare"
      ]
    }
  }
}