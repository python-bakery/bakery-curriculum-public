---
waltz:
  title: bakery_structures_dataclasses_quiz
  display title: 4A1) Dataclasses
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
    modified: August 24 2022, 0410 PM
  files:
    path: bakery_structures_dataclasses_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_structures_dataclasses_read"
  },
  "questions": {
    "IdentifyPartsOfDataclass": {
      "type": "fill_in_multiple_blanks_question",
      "points": 3,
      "body": "Given the following dataclass:\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Assignment:\n    name: str\n    points: int\n    late: bool\n```\n\nHow many fields are in the dataclass? [fieldCount]\n\nWhat is the type of the first field? [firstFieldType]\n\nWhat is the name of the last field? [lastFieldName]\n\nWhat is the name of the constructor function? [constructorName]\n"
    },
    "DataclassDefinitionRequires": {
      "type": "multiple_answers_question",
      "points": 4,
      "body": "Which of the following parts of a dataclass definition are required?",
      "answers": [
        "The dataclass decorator",
        "The dataclass import",
        "The name of the dataclass",
        "The `class` keyword",
        "A field named `name` with the type `str`",
        "At least three fields",
        "Indentation under the header",
        "An `if` statement"
      ]
    },
    "DefineDataclassTerms": {
      "type": "matching_question",
      "points": 3,
      "body": "Match each term to the best definition possible.",
      "answers": [
        "Dataclass",
        "Attribute",
        "Field",
        "Decorator",
        "Instance",
        "Constructor",
        "Period",
        "Conditional"
      ],
      "statements": [
        "A data structure for combining multiple kinds of data together to represent something",
        "A synonym for field",
        "A named bit of data inside of a Dataclass",
        "The `@dataclass` above the header",
        "A specific, concrete version of a general dataclass with actual values",
        "A function automatically created when you define a Dataclass that allows you to make instances"
      ]
    },
    "AvoidAccessingClassField": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "In the following code, what value will be printed?\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass House:\n    color: str\n    address: str\n\nprint(House.color)\n```",
      "answers": [
        "Nothing, an error will occur because you are accessing the field of the dataclass instead of an instance",
        "The type, `str`",
        "The empty string, which is the default for strings",
        "The text `red`, because Python knows that our house is red.",
        "Nothing, an error will occur because you did not unit test the constructor function."
      ]
    },
    "PredictAccessInstanceField": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "In the following code, what value will be printed?\n\n```python\nfrom dataclasses import dataclass\n\n@dataclass\nclass Tree:\n    height: float\n    age: int\n    kind: str\n\nspruce = Tree(25.7, 12, 'Spruce')\n\nprint(spruce.height)\n```",
      "answers": [
        "The value `25.7`, because the `height` field will have that value",
        "The value `12`, because the fields will be alphabetically ordered in the constructor",
        "The value `Spruce`, because you can only print strings",
        "The text `Tree(height=25.7, age=12, kind='Spruce')`, because you can only print the entire dataclass, not its fields",
        "Nothing, an error will occur because you are accessing the field of an instance, instead of the dataclass"
      ]
    },
    "ListDataclassAdvantages": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "Which of the following are advantages of a Dataclass?",
      "answers": [
        "Dataclasses allow us to combine multiple types of values into a single new type",
        "Instances of a dataclass can be printed to see what they contain",
        "Dataclasses are faster than functions, and do the same thing only better",
        "Dataclasses are faster than `if` statements, and do the same thing only better",
        "Dataclasses do not require any imports, so they are very easy to write like `if` statements and function definitions",
        "You can make any number of instances based on a single dataclass definition."
      ]
    }
  }
}