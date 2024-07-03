---
waltz:
  title: bakery_sequences_files_code_plus_or_minus
  display title: 7B2.4) Plus Or Minus
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings:
    hide_files: false
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 11
    created: June 28 2022, 0300 PM
    modified: October 09 2022, 0747 PM
  files:
    path: bakery_sequences_files_code_plus_or_minus
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files:
    - bakery_sequences_files_code_plus_or_minus\plus and minus.txt
---
<p>The file attached has a series of <code>"+"</code> and <code>"-"</code> characters, representing additions and subtractions. Create a function named <code>convert_operator</code>, which consumes a string (a single character, either a <code>"+"</code> or a <code>"-"</code>) and returns either <code>1</code> or <code>-1</code>, respectively. Then apply this function to the contents of each of the following files to calculate the sum of all these pluses and minuses (so an integer number). Notice that the <code>"plus and minus.txt"</code> file is entirely on one line. Therefore, you should use the <code>read</code> method to access its contents. But you should only pass one character at a time to the function you write!</p>