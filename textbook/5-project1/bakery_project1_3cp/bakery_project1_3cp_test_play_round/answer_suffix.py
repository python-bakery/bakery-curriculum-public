
__deck__ = []
def deal():
    if not __deck__:
        raise RuntimeError("Deal at most two hands per round!")
    return __deck__.pop(0)

def fix_deal(cards):
    global __deck__
    __deck__ = cards
    return play_round()
