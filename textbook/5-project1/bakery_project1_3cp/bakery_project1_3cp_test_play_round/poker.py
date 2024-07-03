def get_choice():
    choices='pf'
    answer=input()
    while len(answer)!=1 and answer not in choices:
        print("Please choose one of",choices)
        answer=input()
    return answer

def sort_hand(hand):
    if hand[0]<hand[1]:
        hand[0],hand[1] = hand[1],hand[0]
    if hand[1]<hand[2]:
        hand[1],hand[2] = hand[2],hand[1]
    if hand[0]<hand[1]:
        hand[0],hand[1] = hand[1],hand[0]
    return hand

def hand_to_string(hand):
    rep="0A23456789XJQKA"
    return rep[hand[0]]+rep[hand[1]]+rep[hand[2]]

def has_pair(hand):
    if hand[0]==hand[1] or hand[1]==hand[2]:
        return True
    return False

def has_straight(hand):
    return hand[0]==hand[1]+1==hand[2]+2

def has_triple(hand):
    return hand[0]==hand[1]==hand[2]

def score_hand(hand):
    bonus=16**3
    score=hand[0]*16**2 + hand[1]*16 + hand[2]
    if has_triple(hand):
        score += bonus*16
    elif has_straight(hand):
        score += bonus*15
    elif has_pair(hand):
        score += bonus*hand[1]
    return score

def dealer_plays(hand):
    return score_hand(hand) >= score_hand([12,3,2])

__deck__ = []
def deal():
    if not __deck__:
        raise RuntimeError("Deal at most two hands per round!")
    return __deck__.pop(0)

def fix_deal(cards):
    global __deck__
    __deck__ = cards
    return play_round()

def play_round():
    pass