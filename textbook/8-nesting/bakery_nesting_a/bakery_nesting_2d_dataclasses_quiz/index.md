---
waltz:
  title: bakery_nesting_2d_dataclasses_quiz
  display title: 8A2) Nested Dataclasses
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
    modified: December 07 2022, 1024 PM
  files:
    path: bakery_nesting_2d_dataclasses_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_nesting_2d_dataclasses_read"
  },
  "questions": {
    "Interpret Nested Access": {
      "type": "multiple_dropdowns_question",
      "points": 4,
      "body": "Given the following code...\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Location:\n    city: str\n    state: str\n\n@dataclass\nclass Trip:\n    origin: Location\n    destination: Location\n    duration: int\n    \nmy_trip = Trip(Location(\"Newark\", \"DE\"),\n               Location(\"Baltimore\", \"MD\"),\n               90)\n```\n\nWhat will each of the following expressions produce?\n\n1. `my_trip[0].state`: [errorAccess]\n2. `my_trip.origin.state`: [originState]\n3. `my_trip.duration`: [tripDuration]\n4. `my_trip.destination.city`: [destinationCity]\n5. `Trip.Location.state`: [typeAccess]\n6. `my_trip.origin.city[0]`: [firstLetterOriginCity]",
      "answers": {
        "errorAccess": [
          "\"Newark\"",
          "\"DE\"",
          "\"Baltimore\"",
          "\"MD\"",
          "\"N\"",
          "\"D\"",
          "\"B\"",
          "\"M\"",
          "90",
          "0",
          "int",
          "str",
          "Location",
          "Trip",
          "An error occurs"
        ],
        "originState": [
          "\"Newark\"",
          "\"DE\"",
          "\"Baltimore\"",
          "\"MD\"",
          "\"N\"",
          "\"D\"",
          "\"B\"",
          "\"M\"",
          "90",
          "0",
          "int",
          "str",
          "Location",
          "Trip",
          "An error occurs"
        ],
        "tripDuration": [
          "\"Newark\"",
          "\"DE\"",
          "\"Baltimore\"",
          "\"MD\"",
          "\"N\"",
          "\"D\"",
          "\"B\"",
          "\"M\"",
          "90",
          "0",
          "int",
          "str",
          "Location",
          "Trip",
          "An error occurs"
        ],
        "destinationCity": [
          "\"Newark\"",
          "\"DE\"",
          "\"Baltimore\"",
          "\"MD\"",
          "\"N\"",
          "\"D\"",
          "\"B\"",
          "\"M\"",
          "90",
          "0",
          "int",
          "str",
          "Location",
          "Trip",
          "An error occurs"
        ],
        "typeAccess": [
          "\"Newark\"",
          "\"DE\"",
          "\"Baltimore\"",
          "\"MD\"",
          "\"N\"",
          "\"D\"",
          "\"B\"",
          "\"M\"",
          "90",
          "0",
          "int",
          "str",
          "Location",
          "Trip",
          "An error occurs"
        ],
        "firstLetterOriginCity": [
          "\"Newark\"",
          "\"DE\"",
          "\"Baltimore\"",
          "\"MD\"",
          "\"N\"",
          "\"D\"",
          "\"B\"",
          "\"M\"",
          "90",
          "0",
          "int",
          "str",
          "Location",
          "Trip",
          "An error occurs"
        ]
      },
      "retainOrder": true
    },
    "Recall Order of Definitions": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Which of the following statements about the order of definitions is NOT correct?",
      "answers": [
        "Given dataclasses A and B, if dataclass A has an attribute of type B, then you must define dataclass B before dataclass A",
        "Given dataclass A and function X, if function X returns an instance of dataclass A, then you must define dataclass A before function X",
        "Given functions X and Y, if function X calls function Y, then you must define function X before function Y",
        "In general, you must define the dataclass A before you can make an instance of A",
        "In general, you must define the function X before you can call the function X",
        "In general, you must define a variable before you can use the variable"
      ]
    },
    "Recall Allows Iteration": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Which of the following can be iterated over directly with a `for` loop?",
      "answers": [
        "Strings",
        "Integers",
        "Instances of dataclasses",
        "Lists"
      ]
    },
    "Write Multiple Nested Access": {
      "type": "short_answer_question",
      "points": 2,
      "body": "Given the following code:\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Position:\n    x: int\n    y: int\n    \n@dataclass\nclass Rectangle:\n    start: Position\n    end: Position\n    color: str\n    \n@dataclass\nclass Button:\n    box: Rectangle\n    text: str\n\n@dataclass\nclass World:\n    save: Button\n    load: Button\n```\n\nAssuming we had an instance of a `World` stored in a variable named `world`, what expression would correctly access the World's Save button's starting X coordinate?"
    },
    "Determine Temporary Unpacking Equivalence": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "Given the following code:\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Location:\n    city: str\n    state: str\n\n@dataclass\nclass Trip:\n    origin: Location\n    destination: Location\n    duration: int\n    \nmy_trip = Trip(Location(\"Newark\", \"DE\"),\n               Location(\"Baltimore\", \"MD\"),\n               90)\n```\nWhich of the following code blocks will print the text `DE`?",
      "answers": [
        "<pre>my_origin = my_trip.origin\nprint(my_origin.state)</pre>",
        "<pre>my_origin = my_trip.origin\nprint(state)</pre>",
        "<pre>my_state = my_trip.origin.state\nprint(my_state)</pre>",
        "<pre>my_trip.origin.state\nprint()</pre>",
        "<pre>print(my_trip.origin.state)</pre>",
        "<pre>print(my_trip.state.origin)</pre>",
        "<pre>print(Trip.origin.state)</pre>"
      ]
    }
  }
}