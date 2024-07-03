def has_pair(hand):
    return hand[0]==hand[1] or hand[1]==hand[2]

def has_triple(hand):
    return hand[0]==hand[1]==hand[2]

def has_straight(hand):
    return hand[0]==hand[1]+1==hand[2]+2
