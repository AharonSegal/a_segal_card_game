from game_logic.game import init_game,play_round



if __name__ == "__main__":
    # python -m game_logic.game
    game_dict = init_game()
    #TODO REMOVE===============================
    print("===================================")
    print("============BUG===============")
    print("player_1: " , game_dict["player_1"])
    print("===================================")
    print("player_1 hand: " , game_dict["player_1"]["hand"])
    print("===========================")
    while len(game_dict["player_1"]["hand"]) > 0:
        
        game_round = play_round(game_dict["player_1"],game_dict["player_2"])

    if len(game_dict["player_1"]["won_pile"]) > len(game_dict["player_2"]["won_pile"]):
        print(f"{game_dict["player_1"]["name"]} WINS!")
    elif len(game_dict["player_1"]["won_pile"]) < len(game_dict["player_2"]["won_pile"]):
        print(f"{game_dict["player_2"]["name"]} WINS!")
    else:
        print("TIE <:>")

    
    #TODO REMOVE===============================
    print("===================================")
    print("============FINAL===============")
    print("===================================")
    print("----player 1 ----","\n",game_dict["player_1"],"\n","\n")
    print("pool",len(game_dict["player_1"]["won_pile"]))
    print("----player 2 ----","\n",game_dict["player_2"],"\n","\n")
    print("pool: ",len(game_dict["player_2"]["won_pile"]))
    #TODO REMOVE===============================

