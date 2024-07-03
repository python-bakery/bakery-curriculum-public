---
waltz:
  title: bakery_for_composition_quiz
  display title: 6B2) Loop Composition
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
    path: bakery_for_composition_quiz
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
{
  "settings": {
    "readingId": "bakery_for_composition_read"
  },
  "questions": {
    "FlowBetweenLoopFunctions": {
      "type": "multiple_answers_question",
      "points": 3,
      "body": "Given the program below,\n```python\nmessages = [\"go\", \"fly\", \"a\", \"kite\"]\n\ndef join_strings(messages: [str]) -> str:\n    result = \"\"\n    for message in messages:\n        result = result + \", \" + message\n    return result\n\ndef map_title_case(messages: [str]) -> str:\n    result = []\n    for message in messages:\n        result.append(message.title())\n    return result\n\n# ____ <-- What goes here?\n\nprint(messages)\n```\n\nWhich of the following lines of code should be put in the blank to make the strings Title Cased and joined together with\ncommas?",
      "answers": [
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>map_title_case(messages)\njoin_strings(messages)\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>messages <span style=\"color: #666666;\">=</span> join_strings(map_title_case(messages))\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>map_title_case()\njoin_strings()\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>join_strings(map_title_case(messages))\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span><span style=\"color: #008000; font-weight: bold;\">print</span>(map_title_case(messages))\n<span style=\"color: #008000; font-weight: bold;\">print</span>(join_strings(messages))\n</pre></div>",
        "<div class=\"codehilite\" style=\"background: #f8f8f8;\"><pre style=\"line-height: 125%;\"><span></span>messages <span style=\"color: #666666;\">=</span> map_title_case(messages)\nmessages <span style=\"color: #666666;\">=</span> join_strings(messages)\n</pre></div>",
        "None are necessary, because the variables share the same name."
      ]
    },
    "LoopCompositionAdvantages": {
      "type": "multiple_answers_question",
      "points": 1,
      "body": "What are advantages and reasons to compose loops?",
      "answers": [
        "Breaking up complex loops into separate functions makes each function easier to debug.",
        "Smaller loop functions are easier to write because piece is simpler.",
        "Loop composition makes loops faster because they are broken up.",
        "Loop composition takes less time because variables can be shared between the functions.",
        "We don't need loops at all if we are composing functions."
      ]
    },
    "AvoidUnnecessaryLoopInLoopComposition": {
      "type": "multiple_choice_question",
      "points": 1,
      "body": "Given the following code to calculate the average of a list of numbers, identify the correct statement.\n```python\ndef average(numbers: [int]) -> float:\n    if not numbers:\n        return None\n    for number in numbers:\n        return sum(numbers) / count(numbers)\n```",
      "answers": [
        "This function does not need a for loop.",
        "This code is perfectly fine.",
        "The arguments to sum and count should be number, not numbers.",
        "You shouldn't need to sum or count in order to calculate the average of a list of numbers.",
        "You cannot check whether a list is empty with the condition in the if statement.",
        "The result of the count function needs to be passed as an argument to the sum function."
      ]
    },
    "ReorderLoopComposition": {
      "type": "multiple_answers_question",
      "points": 2,
      "body": "Consider the following functions' names, parameters, and return values.\n```python\ndef convert_grade(grade: int) -> str:\n    pass\n\ndef map_convert_grades(grades: [int]) -> [str]:\n    pass\n\ndef remove_failed_grades(text_grades: [str]) -> [str]:\n    pass\n\ndef get_passing_text_grades(grades: [int]) -> [str]:\n    pass\n```\n\nWhich of the following statements would be good compositions?",
      "answers": [
        "The <code>map_convert_grades</code> function will directly call <code>convert_grade</code>",
        "The <code>get_passing_text_grades</code> function will directly call <code>remove_failed_grades</code>",
        "The <code>get_passing_text_grades</code> function will directly call <code>map_convert_grades</code>",
        "The <code>get_passing_text_grades</code> function will directly call <code>convert_grade</code>",
        "The <code>remove_failed_grades</code> function will directly call <code>convert_grade</code>",
        "The <code>map_convert_grades</code> function will directly call <code>remove_failed_grades</code>",
        "The <code>map_convert_grades</code> function will directly call <code>get_passing_text_grades</code>",
        "The <code>convert_grade</code> function will directly call <code>get_passing_text_grades</code>"
      ]
    }
  }
}