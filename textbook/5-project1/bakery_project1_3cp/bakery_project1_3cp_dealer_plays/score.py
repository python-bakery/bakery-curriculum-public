from hands import has_pair, has_triple, has_straight

def score_hand(hand):
    bonus=16**3
    score=hand[0]*16**2 + hand[1]*16 + hand[2]
    if has_triple(hand):
        score += bonus*16
    elif has_straight(hand):
        score += bonus*15
    elif has_pair(hand):
        score += bonus*has_pair(hand)
    return score
