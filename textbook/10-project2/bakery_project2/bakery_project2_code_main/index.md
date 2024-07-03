---
waltz:
  title: bakery_project2_code_main
  display title: 7) Main Function
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
    version downloaded: 33
    created: October 13 2022, 1228 PM
    modified: October 13 2022, 1236 PM
  files:
    path: bakery_project2_code_main
    hidden but accessible files: []
    instructor only files:
    - bakery_project2_code_main\solutions.json
    - bakery_project2_code_main\correct.py
    extra starting files: []
    read-only files: []
---
### 4) The Main Function

The `main` function works as follows:

  1. The user is prompted to `input` their desired action.
  2. If the user enters `encrypt`: 
    1. The user is prompted to `input` their plaintext message.
    2. The message is encrypted (choose your own  `rotation_amount`)
    3. The plaintext message is hashed to produce a secure value (`31` is a good base, and `1000000000` is a good hash size).
    4. Both the encrypted message and hash are printed to the user.
  3. Otherwise, if the user enters `decrypt`: 
    1. The user is prompted to `input` their encrypted message.
    2. The message is decrypted (reuse the same `rotation_amount` from before).
    3. The user is prompted to `input` the expected hash.
    4. The hash of the decrypted message is compared to the expected hash.
    5. If the hashes are the same, print the decrypted message.
    6. If the hashes are different, your output _must_ include the text "error".
  4. Otherwise, print an error message and exit the app.

Unlike the previous project, we have not provided any imports; you should copy over your existing code from the previous parts.

We are not checking the exact text of what you print to the user, so you are free to make up your own prompts and instructions.
However, you must call the `input` function an appropriate number of times (once to get the user's chosen action, once more if they encrypt, and twice more if they decrypt).