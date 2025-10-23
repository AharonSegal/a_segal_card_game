from utils.deck import compare_cards,create_deck,shuffle

def init_game()->dict:
    player_1,player_2 = create_player("aharon"),create_player()
    deck = create_deck()
    deck = shuffle(deck)
    player_1["hand"] = deck[:26]
    player_2["hand"] = deck[26:]
    game_dict = {"deck" : deck,
                 "player_1" : player_1,
                 "player_2" : player_2}

    #TODO REMOVE===============================
    print("===================================")
    print("game initialized : ", game_dict )
    print("===================================")
    print("p1 hand", player_1["hand"])
    print("p1 hand len", len(player_1["hand"]))
    print("p2 hand", player_1["hand"])
    print("p2 hand len", len(player_1["hand"]))


    return game_dict

def play_round(p1:dict,p2:dict):
    while p1["hand"]:
        p1_card,p2_card = p1["hand"].pop(),p2["hand"].pop()
        current = compare_cards(p1_card,p2_card)
        if current == "p1":
            p1["won_pile"].append(p1_card)
            p1["won_pile"].append(p2_card)
        elif current == "p2":
            p2["won_pile"].append(p1_card)
            p2["won_pile"].append(p2_card)
        else:
            "WAR"
    return

def create_player(name:str = "") -> dict:
    if name == "":
        name = "AI"
    player = {"name":name,"hand":[],"won_pile":[]}

    #TODO REMOVE===============================
    print("===================================")
    print("Ccrteated : ", player )

    return player


#TODO REMOVE===============================
if __name__ == "__main__":
    # python -m game_logic.game
    game_dict = init_game()
    game_round = play_round(game_dict["player_1"],game_dict["player_2"])




