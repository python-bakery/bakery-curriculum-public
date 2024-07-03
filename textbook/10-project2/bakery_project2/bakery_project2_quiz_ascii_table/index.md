---
waltz:
  title: bakery_project2_quiz_ascii_table
  display title: 2) Ascii Table
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
    created: October 12 2022, 0317 PM
    modified: October 13 2022, 1005 AM
  files:
    path: bakery_project2_quiz_ascii_table
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_project2_read_ascii_table"
  },
  "questions": {
    "Ord Conversion": {
      "type": "fill_in_multiple_blanks_question",
      "points": 5,
      "body": "<p>Convert all of the following numbers into their ASCII character code (as if you passed them into the <code>chr</code> function).</p>\n<p>Do not include quotes.</p>\n<p>48: [zero]</p>\n<p>40: [leftparen]</p>\n<p>74: [capitalJ]</p>\n<p>109: [lowerM]</p>\n<p>126: [tilde]</p>"
    },
    "Ord Chr Length": {
      "type": "numerical_question",
      "points": 2,
      "body": "<p>The <code>ord</code> function consumes a string, and the <code>chr</code> function returns a string. In both functions, this string is the same length. How many characters are in the string?</p>"
    },
    "Chr Conversion": {
      "type": "fill_in_multiple_blanks_question",
      "points": 5,
      "body": "<p>Convert all of the following ASCII character codes into their integer representation (as if you passed them into the <code>ord</code> function).</p>\n<p><code>!</code>: [exclamation]</p>\n<p><code>.</code>: [period]</p>\n<p><code>9</code>: [nine]</p>\n<p><code>H</code>: [capitalH]</p>\n<p><code>z</code>: [lowerZ]</p>"
    }
  }
}