from logic import play_game
from strategy import random, random_ultra

if __name__ == "__main__":

    iter = int(input("Number of games: "))
    print("Starting games")

    #game_sets = [0]*7 #game_sets[0] is 21 sets, game_sets[6] is 27 sets
    game_sets = [0]*3 #game_sets[0] is 18 sets, game_sets[2] is 20 sets

    for i in range(iter):
        if (i % 100 == 0): print("Starting game", i)

        [num_sets] = play_game(random_ultra)
        #game_sets[num_sets-21] += 1
        #print(num_sets)
        game_sets[num_sets-18] += 1

    print("finished")
    print(game_sets)
