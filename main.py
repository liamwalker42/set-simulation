from logic import play_game
from strategy import random, leave_most, leave_least, late_leave_most, \
                     random_ultra

import time

MAIN = True


if MAIN and __name__ == "__main__":

    iter = int(input("Number of games: "))

    game_sets = [0]*7 #game_sets[0] is 21 sets, game_sets[6] is 27 sets
    #game_sets = [0]*3 #game_sets[0] is 18 sets, game_sets[2] is 20 sets

    print("Starting games")

    elapsed = time.time()
    for i in range(iter):
        #if (i % 100 == 0): print("Starting game", i)

        num_sets = play_game(random)[0]
        #print(num_sets)

        #game_sets[num_sets-18] += 1
        game_sets[num_sets-21] += 1

    elapsed = time.time() - elapsed
    print("Finished", iter, "games")
    print(game_sets)
    print("Time elapsed: {}".format(elapsed))



if not MAIN and __name__ == "__main__":
    i = 0
    while True:
        i += 1
        if i % 1000 == 0: print("Starting game", i)

        [num_sets, sets, board] = play_game(random)
        if num_sets == 21:
            print("Sets:")
            for set in sets:
                print(set)
            print("\nBoard:")
            print(board)

            game = open("game.txt", 'w')
            game.write("Sets:\n")
            for set in sets:
                for card in set:
                    game.write(str(card))
                    game.write("  ")
                game.write("\n")

            game.write("\nBoard:\n")
            for i in range(len(board)):
                game.write(str(board[i]))
                game.write("\n") if i % 3 == 2 else game.write("  ")

            game.close()

            break
