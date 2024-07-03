---
waltz:
  title: bakery_sequences_strings_code_hot_cold
  display title: 7A2.3) Hot Cold
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
    version downloaded: 9
    created: June 28 2022, 0300 PM
    modified: September 09 2022, 1022 AM
  files:
    path: bakery_sequences_strings_code_hot_cold
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
<p>A scientist has been recording observations of the temperature for the past while. On hot days, they write <code>"H"</code>, and for cold days, they write <code>"C"</code>. Instead of using a list, they kept all of these observations in a single long string (e.g., <code>"HCH"</code> would be a hot day, followed by a cold day, and then another hot day).</p><p>Write a function <code>add_hot_cold</code> that consumes a string of observations and returns the number of hot days minus the number of cold days. To accomplish this, you should process each letter in turn and add <code>1</code> if it is hot, and <code>-1</code> if it is cold. For example, the string <code>"HCH"</code> would result in <code>1</code>, while the string <code>"CHCC"</code> would result in <code>-2</code>. </p><p>You cannot use the built-in <code>count</code> method or the <code>len</code> function. Unit test your function.</p>