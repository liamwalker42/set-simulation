from logic import play_game
from strategy import random

if __name__ == "__main__":

    iter = int(input("Number of games: "))

    game_sets = [0]*7 #game_sets[0] is 21 sets, game_sets[6] is 27 sets

    print("starting games")
    for i in range(iter):
        if (i % 100 == 0): print("Starting game", i)

        [num_sets] = play_game(random)
        game_sets[num_sets-21] += 1
        
    print("finished")
    print(game_sets)
