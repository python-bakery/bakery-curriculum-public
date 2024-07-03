---
waltz:
  title: bakery_project1_3cp_instructions
  display title: '1: Instructions'
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
    version downloaded: 31
    created: August 16 2022, 1116 AM
    modified: September 29 2022, 0151 PM
  files:
    path: bakery_project1_3cp_instructions
    hidden but accessible files: []
    instructor only files: []
    extra starting files: []
    read-only files: []
---
In this project, you will develop a simple "Three-card Poker" game. Don't be concerned if you're unfamiliar with Poker, "standard" playing cards, or games in general: all requirements will be detailed in the assignment.

The game is played over multiple "rounds". Each round, a human player and a computer player will each be given a "hand" of three playing cards as described below. The human player will then decide if they have a good enough hand to risk a bet. Three-card Poker is, like Blackjack, a perfect game for a human to play against a computer opponent because only the human gets to make judgement calls: the computer player will follow a fixed set of rules.

Remember you can use the "Pop-out" button in the top-right corner to pop out these instructions to a separate tab!

## Cards

Poker uses [standard playing cards](https://en.wikipedia.org/wiki/Standard_52-card_deck), the basic form of which has been around for a couple hundred years. Each card has one of 13 ranks (traditionally ordered from lowest to highest as 2, 3, ..., 10, Jack, Queen, King, Ace), and one of four suits (Clubs, Diamonds, Hearts, Spades), collectively forming a "deck" of 52 cards.

We're going to simplify the cards for this project by ignoring the suits, and considering only the ranks. The rank will be recorded as an integer in the range 2-14 (inclusive), but when displaying the cards to the player the rank will be shown as one of the characters "23456789XJQKA", so a card with Rank 10 will be shown as an 'X', a card with Rank 12 will be a 'Q', etc.

![Picture of the playing cards in our game.](cards.png)

## Hands

In a 3-card Poker game, a hand is a collection of three cards. Both players, the human and the computer, will each have one hand at a time that will be used to determine a winner. Since each card only has a rank, we'll represent a hand as a list of three integers.

A hand of three cards has a "feature" if one of the following hold:

* "Three of a Kind" (a "triple") is when all three cards have the same rank (e.g., JJJ or 333)
* A "straight" is when the three cards form a sequence (e.g., 987 or JX9). For simplicity, the A can only be at the top of a straight (AKQ).
* A "pair" is when exactly two of the three cards have the same rank (e.g., AAX or 422)

![The three kinds of features](features.png)

When comparing two hands, any "Three of a Kind" beats any "Straight", which beats any "Pair", which beats any hand without a feature. If the two hands both have a "Pair", the winner is determined by the higher valued "Pair". Otherwise, if both hands have the same "feature" (or no feature at all), the winner is determined by first comparing the highest card in each hand, then (if there is a tie), the second highest, then (if there is a tie), the lowest card. In the extremely rare case that both hands are identical, the player will win.

![Example of three different games](example.png)

## Determining the outcome of a round

Your job will be to construct a function called `play_round` that will determine how many points a player wins or loses based on their cards and their choices. The round will progress as follows.

1. The player is shown their hand of cards. Remember, a "hand" is a list of three integers: you'll get this list by calling the pre-defined `deal()` function, and you'll show the hand by calling the `hand_to_string()` function and `print`ing the result.
2. The player must choose to either `'p'`lay the hand or `'f'`old. You'll obtain the player's choice by calling the pre-defined `get_choice()` function.
3. If the player chooses to fold, they lose 10 points, and the round is over (go to step 5).
4. Otherwise, the dealer is dealt a hand of three cards (`deal()`, again), which is immediately shown to the player (with `hand_to_string()`, again).
    1. If the dealer's hand has no feature and no card equal or higher than a Queen, the dealer folds, the player wins 10 points, and the round is over (go to step 5).
    2. Otherwise (the dealer has at least a Queen high card), the player's hand and the dealer's hand must be compared as describe above. If the player's hand is higher, they win 20 points. Otherwise, they lose 20 points.
5. Return the number of points the player has won (or lost, as a negative value).

## Program design

Each hand of cards will be a list of thee integers sorted from highest to lowest. The following functions will be used to construct the program:

* `hand_to_string(hand: list[int])->str` : consumes a hand and returns a string that can be read and understood by the human player (e.g., `hand_to_string([14,9,4])` will produce `"A 9 4"`).
* `sort_hand(hand: list[int]) -> list[int]`: consumes a hand and returns the same hand, but in descending order (from greatest to smallest).
* `has_pair(hand: list[int])->bool` : consumes a hand and returns `True` if and only if the hand has a pair.
* `has_straight(hand: list[int])->bool` : consumes a hand and returns `True` if and only if the hand is a straight.
* `has_triple(hand: list[int])->bool` : consumes a hand and return `True` if and only if the hand is three of a kind.
* `score_hand(hand: list[int])->int` : consumes a hand and returns an integer representing the "value" of a hand so that it can be compared to other hands. Scores the value of a hand as described below (will use the above three functions as helpers).
* `dealer_plays(hand: list[int])->bool` : consumes a hand and returns `True` if the dealer should play the hand, `False` if the dealer should fold.
* `play_round()->int` : play one hand of cards and determine the outcome. Returns how many points are won (negative for losses). This will be the last function you actually define!

There are also two special functions that will be defined for you and provided when you need them:

* `get_choice()->str` : Returns either `"p"` or `"f"` according to the player's choice. (*This function will be defined for you.*)
* `deal()->list[int]` : Returns one hand (a list of three integers). (*This function will be defined for you.*)


## Scoring hands

The easiest way to compare two hands of cards is by assigning each hand a numerical score and comparing those numbers. If the cards could only have values from 0-9, and we knew the largest digit was on the left and the smallest on the right, then we could directly score each hand as a three-digit number: a list of three cards is just the same as a number between `000` and `999`. Additionally, we could signal the "features" (kind of hand) in a fourth (left-most) digit such that 3-of-a-kind beats straight, and a "better" 2-of-a-kind wins, etc. Ties at every level will be taken care of automatically.

When we count and write numbers, we normally use base-10 (`0-9` digits, and then the next number is `10`, with the `1` carrying over into the next column). To represent the numbers `[5, 4, 7, 1]` in base-10, you multiply the `5` by `10³`, multiply the `4` by `10²`, multiply the `7` by `10`, and then add all four numbers together. This would be `5000+400+70+1`, or `5471`.

However, since card values are from `2`-`14`, we need a different approach. The solution is an idea common in programming called use *base-16* (also called hexadecimal or hex), where we can represent values greater than `9` in each digit place. The trick is that instead of multiplying by a power of `10` for each place, we instead multiply by a power of `16`. Let's say we wanted to represent the numbers `[5, 12, 14]` (which is not `5123`, but `5QA` in our game). We multiply `5*16² = 160`, `12*16 = 192`, and then add them all together: `160+192+14 = 366`, which is the final score of our hand when translating from base-16 to base-10.

Besides the three numbers from the list, we must also consider the value from the feature as the most significant "digit" (or left-most value in the hand):

* Three-of-a-kind: The feature's value is `16`
* Straight: The feature's value is `15`
* Two-of-a-kind: The feature's value is the number that's repeated in the hand
* No feature: The feature's value is `0`

Our coding/numbering scheme for a 3-card-hand using base-sixteen can be seen visually as:

![project_1_explanation.png](project_1_explanation.png)

It is okay if you do not quite understand WHY the math for this works out. The important thing is that you can apply the scoring formula to a given hand:

* Determine the appropriate value of the Feature using the boolean functions
* Multiply the Feature's value by `16³`
* Multiply the first number in the hand list by `16²`
* Multiply the second number in the hand list by `16`
* Add all four numbers together 

### Examples

The table below gives some more examples of the math at work:

<table class="table table-striped table-condensed"><thead><tr><th>Hand</th><th>4-coded cells</th><th>calculation</th><th>Integer Hand Value</th></tr></thead><tbody><tr><td>7 4 4</td><td>4  7  4  4</td><td>(4x16³) + (7x16²) + (4x16¹) + (4)</td><td>18244</td></tr><tr><td>11 10 9 (as J 10 9)</td><td>15 11 10 9</td><td>(15x16³) + (11x16²) + (10x16¹) + (9)</td><td>64425</td></tr><tr><td>3 3 3</td><td>16 3  3  3</td><td>(16x16³) + (3x16²) + (3x16¹) + (3)</td><td>66355</td></tr></tbody></table>