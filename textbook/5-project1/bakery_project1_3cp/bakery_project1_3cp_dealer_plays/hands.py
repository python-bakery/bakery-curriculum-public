def has_pair(hand):
    if hand[0]==hand[1]:
        return hand[0]
    if hand[1]==hand[2]:
        return hand[1]
    return False

def has_triple(hand):
    return hand[0]==hand[1]==hand[2]

def has_straight(hand):
    return hand[0]==hand[1]+1==hand[2]+2
