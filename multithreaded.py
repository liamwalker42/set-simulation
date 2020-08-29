from logic import play_game
from strategy import random, leave_most, leave_least, late_leave_most, \
                     random_ultra

import time

from concurrent.futures import ProcessPoolExecutor


def record_game(id):
    num_sets = play_game(random)[0]
    #print(num_sets)

    #game_sets[num_sets-18] += 1
    #game_sets[num_sets-21] += 1
    return num_sets-21




if __name__ == "__main__":
    iter = int(input("Number of games: "))
    values = range(iter)
    game_sets = [0]*7 #game_sets[0] is 21 sets, game_sets[6] is 27 sets
    #game_sets = [0]*3 #game_sets[0] is 18 sets, game_sets[2] is 20 sets

    print("Starting games")

    elapsed = time.time()
    #Set max_workers to the number of threads on the CPU
    with ProcessPoolExecutor(max_workers = 2) as executor:
        results = executor.map(record_game, values)

    for num in results:
        game_sets[num] += 1

    elapsed = time.time() - elapsed
    print("Finished", iter, "games")
    print(game_sets)
    print("Time elapsed: {}".format(elapsed))
