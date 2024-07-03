---
waltz:
  title: bakery_nesting_heavy_quiz
  display title: 8B2) Heavily Nested Data
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
    version downloaded: 1
    created: June 28 2022, 0300 PM
    modified: October 17 2022, 0848 PM
  files:
    path: bakery_nesting_heavy_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_nesting_heavy_read"
  },
  "questions": {
    "PythonTypes": {
      "type": "matching_question",
      "points": 6,
      "body": "Label each of the following as a \"Primitive type\", \"Composite type\", or \"Not a type\":",
      "answers": [
        "Primitive type",
        "Composite type",
        "Not a type"
      ],
      "retainOrder": true,
      "statements": [
        "Boolean",
        "String",
        "List",
        "Attribute",
        "Types created as dataclasses",
        "Value",
        "Integer",
        "Float",
        "None",
        "Return",
        "For",
        "Literal"
      ]
    },
    "ListsOfDictionaries": {
      "type": "true_false_question",
      "points": 1,
      "body": "Lists can be composed of instances of dataclasses."
    },
    "DictionariesOfLists": {
      "type": "true_false_question",
      "points": 1,
      "body": "Dataclass instances can have lists."
    },
    "StringsOfLists": {
      "type": "true_false_question",
      "points": 1,
      "body": "Strings can be composed of Lists."
    },
    "ListOfList": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "What is the type of the following expression?\n\n[[0]]",
      "answers": [
        "List of List of Integers",
        "List of Integers",
        "Integer",
        "Not a valid expression"
      ]
    },
    "LengthOfLOD": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "How many elements are in the following list?\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Activity:\n    name: str\n    high_energy: bool\n\n@dataclass\nclass Animal:\n    name: str\n    age: int\n    hobby: Activity\n    type: str\n\nanimals = [\n    Animal(\"Ada\", 4, Activity(\"Fetch\", True), \"dog\"),\n    Animal(\"Babbage\", 5, Activity(\"Napping\", True), \"dog\"),\n    Animal(\"Captain\", 1, Activity(\"Destruction\", True), \"cat\")\n]\n```",
      "answers": [
        "0",
        "3",
        "4",
        "12",
        "15"
      ]
    },
    "ComplexExpressions": {
      "type": "matching_question",
      "points": 5,
      "body": "Given the following code:\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Movie:\n    name: str\n    length: int\n    cast: list[str]\n\nmovies = [\n    Movie(\"Jurassic Park\", 127, [\"Goldblum\", \"Neill\", \"Dern\"]),\n    Movie(\"Castle in the Sky\", 140, [\"Paquin\", \"Beek\", \"Leachman\"]),\n    Movie(\"It\", 135, [\"Curry\", \"Green\", \"Brandis\"])\n]\n```\n\nWhat is the value of the following expressions?",
      "retainOrder": true,
      "answers": [
        "Raises an error",
        "\"Jurassic Park\"",
        "\"Castle in the Sky\"",
        "\"It\"",
        "\"Curry\"",
        "\"Goldblum\"",
        "\"Leachman\"",
        "135",
        "0"
      ],
      "statements": [
        "movies[0].name",
        "movies[2].name",
        "movies[0][127]",
        "movies[1][1]",
        "movies[127].name",
        "movies[2].cast[0]",
        "movies[2].cast.Curry",
        "movies[1].cast[2]",
        "movies[2].Curry",
        "movies[-1].length"
      ]
    },
    "BigMovieExample": {
      "type": "text_only_question",
      "points": 0,
      "body": "The next few questions will all use the same code:\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Profit:\n    # In millions\n    costs: int\n    revenue: int\n\n@dataclass\nclass Movie:\n    name: str\n    length: int\n    profit: Profit\n    cast: list[str]\n    \n@dataclass\nclass Theater:\n    name: str\n    is_open: bool\n    showing: list[Movie]\n\ntheaters = [\n    Theater(\"Main Street Theater\", True, [\n        Movie(\"Jurassic Park\", 127, Profit(63, 1046),\n            [\"Goldblum\", \"Neill\", \"Dern\"]),\n        Movie(\"Castle in the Sky\", 140, Profit(3, 16),\n            [\"Paquin\", \"Beek\", \"Leachman\"]),\n        Movie(\"The Notebook\", 121, Profit(29, 118),\n            [\"McAdams\", \"Gosling\", \"Rowlands\"])\n    ]),\n    Theater(\"BlockBuster Cinema\", False, [\n        Movie(\"Cats\", 110, Profit(100, 75),\n            [\"Dench\", \"Corden\", \"Derulo\"]),\n        Movie(\"Morbius\", 104, Profit(86, 45),\n            [\"Leto\", \"Smith\", \"Arjona\"])\n    ]),\n    Theater(\"All Star Movies\", True, [\n        Movie(\"Gone with the Wind\", 221, Profit(4, 390),\n            [\"Leigh\", \"Gable\", \"Havilland\"])\n    ])\n]\n```\n\nA diagram is also provided to help you understand the data and its relationships.\n\n![A class diagram for the Theater, Movie, and Profit relationships](https://i.imgur.com/0MARcfM.png)"
    },
    "Evaluate Heavily Nested Types": {
      "type": "matching_question",
      "points": 4,
      "body": "Given the code above and the code below:\n\n```python\nalpha = 0\nfor theater in theaters:\n    for movie in theater.showing:\n        alpha += movie.profit.costs\n```\n\nInside of the loop body, what are the most accurate types of the following expressions:",
      "retainOrder": true,
      "answers": [
        "Theater",
        "list[Theater]",
        "Movie",
        "list[Movie]",
        "Profit",
        "list[Profit]",
        "int",
        "str",
        "bool",
        "An error occurs"
      ],
      "statements": [
        "theater",
        "theater.name",
        "theater.length",
        "theater.showing",
        "movie",
        "movie.name",
        "movie.length",
        "movie.profit",
        "movie.profit.costs",
        "alpha"
      ]
    },
    "Evaluate Nested Find Example": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Given the following function:\n\n```python\ndef alpha(theaters: list[Theater]) -> str:\n    for theater in theaters:\n        for movie in theater.showing:\n            potential = beta(movie)\n            if potential < 0:\n                return movie.name\n    return None\n    \ndef beta(movie: Movie) -> int:\n    profit = movie.profit\n    return profit.revenue - profit.costs\n```\n\nWhat will the expression `print(alpha(theaters))` output?"
    },
    "Evaluate Nested Filter Max": {
      "type": "short_answer_question",
      "points": 1,
      "body": "Given the following function:\n\n```python\ndef unknown(theaters: list[Theater]) -> str:\n    theaters = step1(theaters)\n    if not theaters:\n        return \"No results\"\n    result = step2(theaters)\n    return result.name\n\ndef step1(theaters: list[Theater]) -> list[Theater]:\n    result = []\n    for theater in theaters:\n        if theater.is_open:\n            result.append(theater)\n    return result\n    \ndef step2(theaters: list[Theater]) -> Theater:\n    result = theaters[0]\n    result_length = theaters[0].showing[0].length\n    for theater in theaters:\n        for movie in theater.showing:\n            if result_length > movie.length:\n                result = theater\n                result_length = movie.length\n    return result\n```\n\nWhat will the expression `print(unknown(theaters))` output?"
    }
  }
}