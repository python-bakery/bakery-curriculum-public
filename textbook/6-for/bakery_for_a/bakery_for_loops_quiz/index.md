---
waltz:
  title: bakery_for_loops_quiz
  display title: 6A1) For Loops
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
    modified: July 13 2022, 0320 PM
  files:
    path: bakery_for_loops_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_for_loops_read"
  },
  "questions": {
    "Loop Components": {
      "type": "matching_question",
      "points": 3,
      "body": "Identify each of the components of the `for` loop:  \n![18-1-quiz-loop-parts.png][7]\n\n   [7]: https://i.imgur.com/zQDwPr7.png",
      "answers": [
        "For keyword",
        "Iteration Variable",
        "In keyword",
        "Body",
        "List Variable"
      ],
      "statements": [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6"
      ]
    },
    "Colon Usage": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Type the character used at the end of the first line of a `for` loop."
    },
    "Iteration Variable Type": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the type of the Iteration Variable in this code?\n```python\ngroceries = [\"Apples\", \"Cookies\", \"Steaks\"]\nfor grocery in groceries:\n    print(grocery)\n```",
      "answers": [
        "List",
        "String",
        "Integer",
        "None"
      ]
    },
    "Loop Facts": {
      "type": "multiple_answers_question",
      "points": 5,
      "body": "Mark each of the following statements about `for` loops that are true:",
      "answers": [
        "The body of a <code>for</code> loop will have one statement for each element of the\niteration list.",
        "<code>for</code> Loops and Functions are basically the same thing",
        "The Iteration Variable will take on each value of the List Variable, one at a time.",
        "<code>for</code> Loops always execute the body four times, which is where they get their\nname.",
        "Like an <code>if</code> statement and a Function Call, the <code>for</code> Loop might cause the\nexecution to not follow the order of lines."
      ]
    },
    "Loop Tracing": {
      "type": "fill_in_multiple_blanks_question",
      "points": 11,
      "body": "Trace the values of this code. If a variable is not yet defined, put an \"X\" (without quotes). If you need more space,\nclick the \"Hamburger Button\" in the top left and right corners of Canvas.\n```python\ngrades = [[10, 20]]\ntotal = 0\nfor grade in grades:\n    adjusted = grade + 10\n    total = total + adjusted\n```\n\nstep | line | grades | grade | adjusted | total  \n---|---|---|---|---|---  \n1 | 1 | [[10,20]] | X | X | X  \n2 | 2 | [[10,20]] | [grade2] | X | [total2]  \n3 | 3 | [[10,20]] | [grade3] | X | [total3]  \n4 | 4 | [[10,20]] | [grade4] | 20 | [total4]  \n5 | [line5] | [[10,20]] | [grade5] | [adjusted5] | [total5]  \n6 | [line6] | [grades6] | [grade6] | [adjusted6] | [total6]  \n7 | [line7] | [[10,20]] | [grade7] | [adjusted7] | [total7]  \n8 | [line8] | [[10,20]] | [grade8] | [adjusted8] | 50"
    }
  }
}