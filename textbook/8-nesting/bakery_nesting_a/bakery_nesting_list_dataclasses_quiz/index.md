---
waltz:
  title: bakery_nesting_list_dataclasses_quiz
  display title: 8A1) Lists of Dataclasses
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
    modified: October 17 2022, 1002 AM
  files:
    path: bakery_nesting_list_dataclasses_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_nesting_list_dataclasses_read"
  },
  "questions": {
    "Count Instances": {
      "type": "fill_in_multiple_blanks_question",
      "points": 3,
      "body": "Given the following code...\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Shape:\n    color: str\n    type: str\n    size: int\n    \nshapes = [Shape(\"red\", \"circle\", 25),\n          Shape(\"blue\", \"triangle\", 30),\n          Shape(\"green\", \"square\", 27),\n          Shape(\"red\", \"triangle\", 27)]\n```\n\n1. How many lists are there? [countList]\n2. How many dataclass instances are there? [countInstance]\n3. How many string literal values are there? [countStrings]"
    },
    "Evaluate Nested Access": {
      "type": "multiple_dropdowns_question",
      "points": 3,
      "body": "Given the following code...\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Shape:\n    color: str\n    type: str\n    size: int\n    \nshapes = [Shape(\"red\", \"circle\", 25),\n          Shape(\"blue\", \"triangle\", 30),\n          Shape(\"green\", \"square\", 27),\n          Shape(\"red\", \"triangle\", 27)] \n```\n\nWhat will each of the following expressions produce?\n\n1. `shapes[0].color`: [firstColor]\n2. `shapes[-1].type`: [lastType]\n3. `shapes.size[0]`: [shapesSize]\n4. `Shape.color`: [shapeColor]\n5. `size[shapes]`: [sizeShapes]",
      "answers": {
        "firstColor": [
          "\"red\"",
          "\"blue\"",
          "\"green\"",
          "\"circle\"",
          "\"triangle\"",
          "\"square\"",
          "25",
          "27",
          "30",
          "int",
          "str",
          "An error occurs"
        ],
        "lastType": [
          "\"red\"",
          "\"blue\"",
          "\"green\"",
          "\"circle\"",
          "\"triangle\"",
          "\"square\"",
          "25",
          "27",
          "30",
          "int",
          "str",
          "An error occurs"
        ],
        "shapesSize": [
          "\"red\"",
          "\"blue\"",
          "\"green\"",
          "\"circle\"",
          "\"triangle\"",
          "\"square\"",
          "25",
          "27",
          "30",
          "int",
          "str",
          "An error occurs"
        ],
        "shapeColor": [
          "\"red\"",
          "\"blue\"",
          "\"green\"",
          "\"circle\"",
          "\"triangle\"",
          "\"square\"",
          "25",
          "27",
          "30",
          "int",
          "str",
          "An error occurs"
        ],
        "sizeShapes": [
          "\"red\"",
          "\"blue\"",
          "\"green\"",
          "\"circle\"",
          "\"triangle\"",
          "\"square\"",
          "25",
          "27",
          "30",
          "int",
          "str",
          "An error occurs"
        ]
      },
      "retainOrder": true
    },
    "Evaluate Iteration Type": {
      "type": "fill_in_multiple_blanks_question",
      "points": 3,
      "body": "Given the following code...\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Animal:\n    name: str\n    type: str\n    weight: float\n\nzoo = [ Animal(\"Terry\", \"Giraffe\", 80.0),\n        Animal(\"Jerry\", \"Elephant\", 100.0),\n        Animal(\"Kerry\", \"Penguin\", 20.0)\n]\nresult = \"\"\nfor an_animal in zoo:\n    result += an_animal.name\nprint(result)\n```\n\nWhat will be the most accurate *type* of the following variables?\n\n1. `an_animal`: [iterVarType]\n2. `an_animal.weight`: [weightType]\n3. `zoo`: [listType]\n4. `result`: [resultType]"
    },
    "Evaluate Loop Pattern": {
      "type": "short_answer_question",
      "points": 1,
      "body": "When this code is executed, what will be printed?\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Animal:\n    name: str\n    type: str\n    weight: int\n\nzoo = [ Animal(\"Terry\", \"Owl\", 5),\n        Animal(\"Perry\", \"Giraffe\", 80),\n        Animal(\"Kerry\", \"Penguin\", 20),\n        Animal(\"Harry\", \"Lion\", 50),\n        Animal(\"Larry\", \"Monkey\", 30),\n        Animal(\"Jerry\", \"Elephant\", 100)\n]\n\nresult = []\ntaking = True\nfor animal in zoo:\n    if animal.name[1] == 'a':\n        taking = False\n    elif taking:\n        result.append(animal)\nbiggest = result[0]\nfor animal in result:\n    if animal.weight > biggest.weight:\n        biggest = animal\nprint(biggest.type)\n```"
    }
  }
}