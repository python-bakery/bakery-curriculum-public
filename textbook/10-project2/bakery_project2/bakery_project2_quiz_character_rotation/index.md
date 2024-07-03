---
waltz:
  title: bakery_project2_quiz_character_rotation
  display title: 3) Character Rotation
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
    created: October 12 2022, 0318 PM
    modified: October 30 2022, 0622 PM
  files:
    path: bakery_project2_quiz_character_rotation
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_project2_read_character_rotation"
  },
  "questions": {
    "Rotate Characters": {
      "type": "fill_in_multiple_blanks_question",
      "points": 5,
      "body": "<p>Rotate all of the following characters by the given amount, to determine a new character. Do not put quotes around the resulting character.</p>\n<p><code>A</code> by 1: [capitalAby1]</p>\n<p><code>A</code> by 2: [capitalAby2]</p>\n<p><code>A</code> by 10: [capitalAby10]</p>\n<p><code>A</code> by -1: [capitalAbyNeg1]</p>\n<p><code>B</code> by 2: [capitalBby2]</p>\n<p><code>B</code> by 25: [capitalBby25]</p>\n<p><code>=</code> by -1: [equalSignBy1]</p>\n<p><code>a</code> by 1: [lowerABy1]</p>\n<p><code>z</code> by 5: [lowerZBy5]</p>\n<p><code>z</code> by 8: [lowerZBy8]</p>\n<p><code>2</code> by -30: [twoByNeg30]</p>"
    },
    "Rotate String": {
      "type": "multiple_choice_question",
      "points": 2,
      "body": "<p>Which of the following is the result of rotating the string <code>Hello</code> by 29?</p>",
      "answers": [
        "<code>/,,%f</code>",
        "<code>ROOH+</code>",
        "<code>.++$e</code>",
        "<code>d#**-</code>",
        "<code>e$++.</code>",
        "<code>pmmfI</code>",
        "<code>f%,,/</code>"
      ]
    },
    "Rotate String Blank": {
      "type": "short_answer_question",
      "points": 5,
      "body": "What is the result of rotating the string <code>Dragons!</code> by 10? Do not put quotation marks around your answer, just enter the characters."
    }
  }
}