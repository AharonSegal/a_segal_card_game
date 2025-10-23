from game_logic.game import init_game,play_round



if __name__ == "__main__":
    game_dict = init_game()
    while len(game_dict["player_1"]["hand"]) > 0:
        
        game_round = play_round(game_dict["player_1"],game_dict["player_2"])

    if len(game_dict["player_1"]["won_pile"]) > len(game_dict["player_2"]["won_pile"]):
        print(f"{game_dict["player_1"]["name"]} WINS!")
    elif len(game_dict["player_1"]["won_pile"]) < len(game_dict["player_2"]["won_pile"]):
        print(f"{game_dict["player_2"]["name"]} WINS!")
    else:
        print("TIE <:>")

    