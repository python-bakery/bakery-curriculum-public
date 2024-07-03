---
waltz:
  title: bakery_project1_3cp_finale
  display title: 10) Play the Game
  resource: problem
  type: reading
  visibility:
    hide status: false
    subordinate: false
    publicly indexed: false
  additional settings: {}
  identity:
    owner id: 1
    owner email: acbart@udel.edu
    course id: 37
    version downloaded: 8
    created: September 24 2022, 0655 PM
    modified: September 28 2022, 0747 PM
  files:
    path: bakery_project1_3cp_finale
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
You should now be able to take all the pieces of your game, put them in a single file in Thonny, and then run the game with the following code at the end:


```python

def get_choice() -> str:
    """
    Get user input and return either 'p' or 'f' depending on the player's choice.
    """
    answer= ' '
    while answer not in 'pf':
        answer=input("Please enter either 'p' or 'f':")
    return answer

from random import randint

def deal() -> list[int]:
    """
    Simple random card dealing function that returns three randomly chosen cards,
    represented as integers between 2 and 14.
    """
    return [randint(2, 14), randint(2, 14), randint(2, 14)]

score = 0
while True:
    score += play_round()
    print("Your score is", score, "- Starting a new round!")
```