---
waltz:
  title: bakery_project3_milestone2_quiz
  display title: 2.1) Introduction
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
    version downloaded: 0
    created: November 11 2022, 1112 AM
    modified: November 11 2022, 0336 PM
  files:
    path: bakery_project3_milestone2_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_project3_milestone2_introduction"
  },
  "questions": {
    "RecallGetSubmissions": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What does the `get_submissions` function consume for its second argument?",
      "answers": [
        "A user token",
        "A Submission",
        "A submission ID",
        "A Course",
        "The name of a Course",
        "The code of a Course",
        "A course ID"
      ]
    },
    "RecallDataclassRelationships": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Which of the following statements are accurate?",
      "answers": [
        "Each Submission has exactly one Assignment",
        "Each Submission has exactly one Comment",
        "Each Assignment has exactly one Group",
        "Each Assignment has exactly one Comment"
      ]
    },
    "InterpretScoreFormula": {
      "type": "multiple_answers_question",
      "points": 2,
      "body": "Which of the following statements are accurate?",
      "answers": [
        "The <code>grade</code> field is a string, containing either nothing (empty), a number, or a letter grade.",
        "The <code>score</code> is a float representing the ratio of points earned vs the points possible.",
        "The <code>weight</code> of a group is used to adjust the score for the overall course.",
        "The <code>score</code> will be an empty string if the assignment has not yet been graded.",
        "The <code>attempts</code> needs to be subtracted from the <code>score</code> in order to calculate students' actual performance.",
        "If the <code>grade</code> is an empty string, then the weighted assignment score cannot be meaningfully calculated."
      ]
    },
    "DetermineAnniesCourses": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Which of the following is NOT one of the course IDs that `annie` is taking?",
      "answers": [
        "679554",
        "386814",
        "4182",
        "394382",
        "212432",
        "100167",
        "134088"
      ]
    },
    "DetermineAnnieAssignments": {
      "type": "short_answer_question",
      "points": 1,
      "body": "How many assignments does `annie` have for her second course (\"Intro to English\")? Remember, you can use the runnable code area above to look at various user's courses' submissions/assignments!"
    },
    "DetermineTroyGrade": {
      "type": "short_answer_question",
      "points": 1,
      "body": "What `score` did `troy` earn on the only assignment in his one course?"
    },
    "DetermineJeffPoints": {
      "type": "short_answer_question",
      "points": 1,
      "body": "How many `points_possible` is the last assignment in `jeff`'s last course (\"Physical Education Education\")?"
    }
  }
}