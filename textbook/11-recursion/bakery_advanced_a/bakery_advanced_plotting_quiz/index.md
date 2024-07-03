---
waltz:
  title: bakery_advanced_plotting_quiz
  display title: 11A1) Plotting
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
    created: November 13 2022, 0654 PM
    modified: November 13 2022, 0714 PM
  files:
    path: bakery_advanced_plotting_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_advanced_plotting_read"
  },
  "questions": {
    "GraphQuestions": {
      "type": "matching_question",
      "points": 1,
      "body": "Match the type of graph with the kind of information that that type of graph conveys.",
      "answers": [
        "Scatter Plot",
        "Histogram",
        "Line plot",
        "Bar Plot",
        "Bart Plot"
      ],
      "statements": [
        "The relationship between two lists of numbers",
        "The distribution of a list of numbers",
        "The trend in a list of numbers"
      ]
    },
    "ShowingGraphs": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Write the final function call that should be used after the following code, in order to actually make the plot appear:\n```python\nimport matplotlib.pyplot as plt\n\nplt.hist([1, 7, 5, 4, 3, 5, 6, 7])\n```"
    },
    "MergingGraphs": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "How many plots will the following code create?\n\n```python\nimport matplotlib.pyplot as plt\nplt.plot([1,2,3])\nplt.plot([1,2,3])\nplt.show()\n```",
      "answers": [
        "0",
        "1",
        "2",
        "3"
      ]
    },
    "ImportingMatPlotLib": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "How many times do you need to import MatPlotLib?",
      "answers": [
        "None, because it is built-in to Python.",
        "Once, at the start of the program.",
        "Once, at the end of the program.",
        "Once for each time that you are plotting, before you plot."
      ]
    },
    "HistogramsBarGraphs": {
      "type": "true_false_question",
      "points": 1,
      "body": "Bar graphs and Histograms are basically the same thing."
    },
    "InterpretingHistograms": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Assume that a library exists that can get lists of integers representing students' grades.\n\n```python\nfrom bakery_grades import get_grades\nimport matplotlib.pyplot as plt\n\ngrades = get_grades()\n\nplt.hist(grades)\nplt.show()\n```\n\nExecuting the code above generate this image:\n\n<a href=\"https://i.imgur.com/VHFSs2Q.png\" target=_blank><img src=\"https://i.imgur.com/VHFSs2Q.png\"></a>\n\nWhich of the following statements is the best interpretation of the graph?",
      "answers": [
        "Many students got a 100.",
        "Many students got a 0.",
        "Many students got between 50 and 60.",
        "Grades were very evenly distributed."
      ]
    }
  }
}