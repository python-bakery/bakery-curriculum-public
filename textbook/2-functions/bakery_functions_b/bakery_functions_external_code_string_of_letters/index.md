---
waltz:
  title: bakery_functions_external_code_string_of_letters
  display title: 2B4.1) String Of Letters
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    start_view: text
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 10
    created: June 28 2022, 0300 PM
    modified: September 09 2022, 0254 PM
  files:
    path: bakery_functions_external_code_string_of_letters
    hidden but accessible files: []
    instructor only files:
    - bakery_functions_external_code_string_of_letters\correct.py
    extra starting files: []
    read-only files: []
---
<p>The <code>string</code> module has a variable named <code>ascii_letters</code>. Import this variable, and use it to write the function <code>starts_with_letter</code> that consumes a non-empty string and returns whether the first character is a letter (as opposed to a number or symbol). Remember to unit test your function.</p><p>Technically, this function violates our scope rules - however, it is okay because we are not changing the value inside letters (it's a global <span style="font-style: italic;">constant</span>).</p>