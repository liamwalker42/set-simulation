from random import shuffle

deck = []
board = []
features = 4
values = 3


def play_game(strategy, f = 4, t = 3):
    global features, values
    features = f
    values = t
    init_deck()

    sets_taken = 0
    sets = []
    while True:
        set = strategy()
        '''
        print(len(deck))
        print("board:", board)
        print("set:", set)
        '''

        if (set == -1):
            if(deal_cards(values) == -1):
                break
            continue


        sets_taken += 1
        sets += [[ board[set[0]], board[set[1]], board[set[2]] ]]
        if (len(board) - len(set) < features * values):
            replace_set(set)
        else:
            take_set(set)

    #add info as necesary
    #[number of sets taken]
    return [sets_taken, sets, board]
    #return [int(values**(features - 1) - len(board)/values)]



#TODO: make cleaner using modular arithmetic with range(values**features)
def init_deck():
    global deck, board
    deck = [[i] for i in range(values)]
    board = []

    for i in range(features - 1):
        temp = []
        for c in deck:
            for j in range(values):
                temp += [(c + [j])]
        deck = temp

    shuffle(deck)
    for i in range(features*values): deal_card()


def deal_cards(n, pos = len(board)):
    i = 0
    for i in range(n):
        if (deal_card(pos) == -1): break
    if (i == 0): return -1
    else: return i+1

def deal_card(pos = len(board)):
    if (len(deck) <= 0): return -1
    board.insert(pos, deck.pop())
    return 0


#set is a tuple of card indices
def take_set(set):
    for i in set:
        board.pop(i)


#set is a tuple of card indices
def replace_set(set):
    for i in set:
        board.pop(i)
        deal_card(i)


#Currently works for 3 values per feature
def find_sets(b = []):
    if (len(b) == 0): b = board
    sets = []

    for i in range(len(b)):
        for j in range(i):
            for k in range(j):
                c1 = b[i]
                c2 = b[j]
                c3 = b[k]
                s = [(c1[f] + c2[f] + c3[f]) % values
                     for f in range(features)]
                if (sum(s) == 0): sets += [[i, j, k]]

    return sets

#Currently works for 3 values per feature
def find_ultra():
    sets = []

    for i in range(len(board)):
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    c1 = board[i]
                    c2 = board[j]
                    c3 = board[k]
                    c4 = board[l]

                    #Python % makes the resulting sign nonnegative
                    s12 = [(c1[f] + c2[f] - c3[f] - c4[f]) % values
                           for f in range(features)]
                    if (sum(s12) == 0): sets += [[i, j, k, l]]
                    s13 = [(c1[f] + c3[f] - c2[f] - c4[f]) % values
                           for f in range(features)]
                    if (sum(s13) == 0): sets += [[i, j, k, l]]
                    s14 = [(c1[f] + c4[f] - c2[f] - c3[f]) % values
                           for f in range(features)]
                    if (sum(s14) == 0): sets += [[i, j, k, l]]

    return sets


#exec(open('logic.py').read())
