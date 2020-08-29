import logic
from logic import play_game
from strategy import random, leave_most, leave_least, late_leave_most, \
                     random_ultra

import time

from concurrent.futures import ProcessPoolExecutor #ThreadPoolExecutor


MAIN = True


def record_game(id):
    #num_sets = play_game(random)[0]

    [num_sets, sets, board] = play_game(random)
    if num_sets == 21:
        #This should be rare
        write_game_to_file(sets, board)
    #print(num_sets)

    #game_sets[num_sets-18] += 1
    #game_sets[num_sets-21] += 1

    t = [0]*logic.features
    for set in sets:
        num_sim = 0
        for f in range(logic.features):
            if set[0][f] == set[1][f]: num_sim += 1
        t[num_sim] += 1

    return (num_sets-21, t)




################################################################################

'''
def play_until(id):
    [num_sets, sets, board] = play_game(random)
    if num_sets == 21:
        executor.shutdown()
        write_game_to_file(sets, board)

        elapsed = time.time() - elapsed
        print("Time elapsed: {}".format(elapsed))
    else:
        try:
            executor.submit(play_until, id)
        except:
            print("Process {} stopped.".format(id))


workers = 8
#Set max_workers to the number of threads (logical processors) on the CPU
executor = ProcessPoolExecutor(max_workers = workers)

elapsed = 0

if not MAIN and __name__ == "__main__":
    print("Starting games")

    elapsed = time.time()
    for i in range(workers):
        executor.submit(play_until, i)
'''

################################################################################


def write_dist_to_file(total, set_dist, type_dist, elapsed):
    dist = open("set_dist.txt", 'w')

    dist.write("\nTotal games: {}\n\n".format(total))
    dist.write("Set count distribution\n")
    for i in range(len(set_dist)):
        dist.write("{0} sets: {1}\n".format(21 + i, set_dist[i]))

    dist.write("\nSet type distribution\n")

    for i in range(len(type_dist)):
        dist.write("{0} similar features: {1}\n".format(i, type_dist[i]))

    dist.write("\nTime elapsed: {}\n".format(elapsed))

    dist.close()
    dist = open("set_dist.txt", 'r')
    print(dist.read())
    dist.close()


def write_game_to_file(sets, board):
    file_no = 0
    while file_no < 1000:
        try:
            open("games\\game{}.txt".format(file_no))
        except:
            game = open("games\\game{}.txt".format(file_no), 'w')
            break
        else:
            file_no += 1

    game.write("\nSets:\n")
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
    game = open("games\\game{}.txt".format(file_no), 'r')
    print(game.read())
    game.close()



if MAIN and __name__ == "__main__":
    iter = int(input("Number of games: "))
    values = range(iter)
    game_sets = [0]*7 #game_sets[0] is 21 sets, game_sets[6] is 27 sets
    #game_sets = [0]*3 #game_sets[0] is 18 sets, game_sets[2] is 20 sets
    set_types = [0]*logic.features #[0] all different ... [3] 3 similar features

    print("Starting games")

    elapsed = time.time()

    #Set max_workers to the number of threads (logical processors) on the CPU
    chunk = 10000 if iter > 10000 else iter
    for i in range(int(iter / chunk)):
        print("Starting game {}".format(i * chunk))
        values = range(chunk)
        with ProcessPoolExecutor(max_workers = 8) as executor:
            results = executor.map(record_game, values)

        for (n, t) in results:
            game_sets[n] += 1
            for i in range(len(t)):
                set_types[i] += t[i]

    elapsed = time.time() - elapsed
    write_dist_to_file(chunk * int(iter/chunk), game_sets, set_types, elapsed)
