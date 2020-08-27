import logic
from random import choice


#strategy for normal set
def random():
    sets = logic.find_sets()
    if (len(sets) == 0):
        if (logic.deal_cards(logic.types)):
            return -1
        else:
            return random()
    else:
        return choice(sets)


#strategy for ultra set
def random_ultra():
    sets = logic.find_ultra()
    if (len(sets) == 0):
        #ultra sets are guaranteed with 12 cards
        return -1
    else:
        return choice(sets)
