from logic import board
import logic
from random import choice


#strategy for normal set
def random():
    sets = logic.find_sets()
    if (len(sets) == 0):
        return -1

    return choice(sets)


#strategy for normal set
#picks sets that leave the most possible sets remaining on the board
def leave_most():
    sets = logic.find_sets()
    if (len(sets) == 0):
        return -1

    best_sets = []
    remaining = 0
    for set in sets:
        new_board = logic.board.copy()
        for i in set:
            new_board.pop(i)

        sets_left = len(logic.find_sets(new_board))
        if (sets_left > remaining):
            best_sets = [set]
            remaining = sets_left
        elif (sets_left == remaining):
            best_sets += [set]


    return choice(best_sets)


#strategy for normal set
#picks sets that leave the fewest possible sets remaining on the board
def leave_least():
    sets = logic.find_sets()
    if (len(sets) == 0):
        return -1

    best_sets = []
    remaining = -1
    for set in sets:
        new_board = logic.board.copy()
        for i in set:
            new_board.pop(i)

        sets_left = len(logic.find_sets(new_board))
        if (remaining < 0 or sets_left < remaining):
            best_sets = [set]
            remaining = sets_left
        elif (sets_left == remaining):
            best_sets += [set]


    return choice(best_sets)


#strategy for normal set
#picks sets that leave the most possible sets remaining on the board
def late_leave_most():
    if (len(logic.deck) <= 0): return leave_most()
    else: return random()


#strategy for ultra set
def random_ultra():
    sets = logic.find_ultra()
    if (len(sets) == 0):
        #ultra sets are guaranteed with 12 cards
        return -1
    else:
        return choice(sets)
