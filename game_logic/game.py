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

    return player




