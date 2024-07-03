---
waltz:
  title: bakery_sequences_files_code_madlibs
  display title: 7B2.7) Madlibs
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
    version downloaded: 23
    created: June 28 2022, 0300 PM
    modified: October 16 2022, 0502 PM
  files:
    path: bakery_sequences_files_code_madlibs
    hidden but accessible files: []
    instructor only files:
    - bakery_sequences_files_code_madlibs\correct.py
    extra starting files: []
    read-only files:
    - bakery_sequences_files_code_madlibs\words.txt
    - bakery_sequences_files_code_madlibs\story.txt
---
<p>You are going to create some <a href="https://en.wikipedia.org/wiki/Mad_Libs#Format" target="_blank">Mad Libs</a>. There are two files available: a word list full of common words (<code>"words.txt"</code>), and a short story (<code>"story.txt"</code>). Process both files line-by-line in order to replace the words from the first file in the short story with the string <code>"____"</code> (four underscores). Then, print the resulting story, each line of the story on its own line.</p><p>One issue you may encounter: You cannot loop through a file again after you have read its contents once. Solve this issue by storing the words file in a list before processing the story.</p><p>You may find it helpful to keep in mind the mutability of certain types. You may also use the built-in <code>replace</code> method for strings. Refer to the string documentation for more information on using this method.</p>