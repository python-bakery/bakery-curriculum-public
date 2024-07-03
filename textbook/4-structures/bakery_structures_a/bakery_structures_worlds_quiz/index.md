---
waltz:
  title: bakery_structures_worlds_quiz
  display title: 4A3) Worlds
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
    modified: August 19 2022, 0558 PM
  files:
    path: bakery_structures_worlds_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_structures_worlds_read"
  },
  "questions": {
    "RecallDesignerWorldFacts": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "Which of the following statements are true about Designer Worlds?",
      "answers": [
        "All functions bound to an event with `when` MUST return a `World`.",
        "The first parameter of a function bound with `when` should be of type `World`.",
        "`World`s can contain `DesignerObject`s in their fields.",
        "`DesignerObject`s are just like dataclasses, since they have fields that can be accessed and updated.",
        "The `starting` event is not necessary, since you can also pass values directly to the `start` function.",
        "The first field of a `World` should be of type `DesignerObject`."
      ]
    },
    "VerifyDesignerWorldTimerCode": {
      "type": "true_false_question",
      "points": 1,
      "body": "Does the code below correctly cause the chick to hatch after a period of time?\n\n```python\nfrom dataclasses import dataclass\nfrom designer import *\n\n@dataclass\nclass World:\n    timer: int\n    picture: DesignerObject\n    \ndef hatch(world: World):\n    if world.timer < 0:\n        world.picture.name = 'hatching chick'\n    else:\n        world.timer -= 1\n        \nwhen('updating', hatch)\nstart(World(60, emoji(\"egg\")))\n```"
    }
  }
}