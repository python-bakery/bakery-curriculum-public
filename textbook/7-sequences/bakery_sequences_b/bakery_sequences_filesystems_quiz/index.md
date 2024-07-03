---
waltz:
  title: bakery_sequences_filesystems_quiz
  display title: 7B1) Filesystems
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
    modified: August 20 2022, 1209 PM
  files:
    path: bakery_sequences_filesystems_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_sequences_filesystems_read"
  },
  "questions": {
    "ExplanatoryTextForThonny": {
      "type": "text_only_question",
      "points": 0,
      "body": "In the lessons, you are shown how to run a number of commands. The exclamation marks (`!`) shown in the lesson are only\nthere because Thonny requires them; most command line systems would not require them. Please do not use `!` in any of\nthe following questions.\n\nAs a helpful reminder, here are the commands from the lesson:\n\nCommand | Description  \n---|---  \npwd | Print current working directory  \nls | List files in current working directory  \nls \"path\" | List files in the directory of the path  \ncd \"path\" | Change the current working directory"
    },
    "CdUp": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Write the command for moving up a directory."
    },
    "CdFolder": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Write the command for moving to a folder named `\"homework\"` that is in the current directory."
    },
    "Pwd": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Write the command for printing the current directory."
    },
    "Ls": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Write the command for listing files in the current directory."
    },
    "FindLocations": {
      "type": "multiple_dropdowns_question",
      "points": 2,
      "body": "Given the following map of a filesystem...\n```python\n/root/\n    python/\n        readme.rst\n        python.exe\n        qt.conf\n    classes/\n        cs1064/\n            adventure_game.py\n            assignment2.txt\n            ethics_submission.pdf\n        dog1223/\n            readings.pdf\n            project1.docx\n            DCIM-1221.jpg\n    data/\n        survey_results.csv\n        state_names.json\n        f15_student_logs.txt\n```\n\nAnswer the following:\n\n  * What is the full path to the folder \"data/\"? [data-full]\n  * What is the full path to the file \"DCIM-1221.jpg\"? [dcim-full]\n  * If you are currently in directory `data/`, which of the following is NOT a path to the `readings.pdf` file? [readings-relative]\n  * If you are currently in directory `cs1064/`, which of the following is NOT a path to the `survey_results.csv` file? [survey-relative]",
      "answers": {
        "dcim-full": [
          "DCIM-1221.jpg",
          "/root/classes/dog1223/DCIM-1221.jpg",
          "dog1223/DCIM-1221.jpg",
          "/root/python/classes/dog1223/DCIM-1221.jpg"
        ],
        "data-full": [
          "/root/data/",
          "data/",
          "survey_results.csv, state_names.json, f15_student_logs.txt"
        ],
        "readings-relative": [
          "../classes/dog1223/readings.pdf",
          "/root/classes/dog1223/readings.pdf",
          "dog1223/readings.pdf"
        ],
        "survey-relative": [
          "../data/survey_results.csv",
          "/root/data/survey_results.csv",
          "../../data/survey_results.csv"
        ]
      }
    },
    "WhyForward": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Why should you tend to use forward slashes in Python?",
      "answers": [
        "Back slashes in string literals represent escape characters, which can mess up the path.",
        "Back slashes are backwards, which means that only backwards people use them.",
        "Forward slashes look prettier to everyone.",
        "Forward slashes tend to work in both Mac and Windows."
      ]
    },
    "TerminalCommands": {
      "type": "true_false_question",
      "points": 1,
      "body": "The `pwd` command works in every Python environment, including ones like Thonny and BlockPy."
    }
  }
}