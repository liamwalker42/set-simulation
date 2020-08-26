import logic
from random import choice


#strategy for normal set
def random():
    sets = logic.find_sets()
    if (len(sets) == 0):
        if (logic.deal_cards(3)):
            return -1
        else:
            return random()
    else:
        return choice(sets)
