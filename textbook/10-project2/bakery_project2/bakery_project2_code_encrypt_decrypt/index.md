---
waltz:
  title: bakery_project2_code_encrypt_decrypt
  display title: 4) encrypt_text/decrypt_text
  resource: problem
  type: blockpy
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 38
    created: October 12 2022, 0318 PM
    modified: November 01 2022, 1028 AM
  files:
    path: bakery_project2_code_encrypt_decrypt
    hidden but accessible files: []
    instructor only files:
    - bakery_project2_code_encrypt_decrypt\solutions.json
    - bakery_project2_code_encrypt_decrypt\correct.py
    extra starting files: []
    read-only files: []
---
The `encrypt_text` function should consume the plaintext `message` (a string) and `rotation_amount` (an integer) and produces a string where the text is encrypted as follows:

  1. Convert the string to a list of integers using `ord`.
  2. Rotate each integer of the string by `rotation_amount` amount. To rotate a value, use the following formula: `rotated = (original+rotation-32) % 94 + 32`. Hint: use a helper function.
  3. Insert the tilde ASCII value (`126`, which translates to `"~"`) after every integer less than `48`. Hint: Append more than once.
  4. Convert the list of integers back to a string using `chr`.

The `decrypt_text` function should consume the encrypted `message` (a string) and `rotation_amount` (an integer) and produces a string where the text is decrypted as follows:

  1. Convert the string to a list of integers using `ord`.
  2. Filter the list to remove any occurrence of the value `126` (the tilde `"~"`).
  3. The integers in the list are rotated `-rotation_amount` amount.
  4. Convert the list of integers back to a string using `chr`.