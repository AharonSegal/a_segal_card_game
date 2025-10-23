import random

def create_card(rank:str,suite:str) -> dict:
    value = rank
    if value == "J":
        value = 11
    elif value == "Q":
        value = 12
    elif value == "K":
        value = 13
    elif value == "A":
        value = 14
    else:
        value = int(rank)

    card =  {"rank": rank, "suite": suite, "value":value}
    #TODO REMOVE===============================
    print("created card: ", card)
    
    return card

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    p1 = p1_card["value"] 
    p2 = p2_card["value"] 

    #TODO REMOVE===============================
    print("===================================")
    print(f"comparing: p1{p1} : p2{p2}", )

    if p1 > p2:
        return "p1"
    elif p2 > p1:
        return "p2"
    else:
        return "WAR"


def create_deck() -> list[dict]:
    RANKS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    SUITES = ["h","c","d","s"]
    deck = []
    for suite in SUITES:
        for rank in RANKS:
            card = create_card(rank,suite)
            deck.append(card)

    #TODO REMOVE===============================
    print("===================================")
    print("deck created: ", deck )
    print("size", len(deck))

    return deck


#TODO: GO OVER THIS 
def shuffle(deck:list[dict]) -> list[dict]:
    for i in range(1000):
        index1, index2 = random.randint(0,51),random.randint(0,51)
        same = index1==index2
        while same == True:
            index1, index2 = random.randint(0,51),random.randint(0,51)
            same = index1==index2

        temp = deck[index1]
        deck[index1] = deck[index2]
        deck[index2] = temp 

    #TODO REMOVE===============================
    print("===================================")
    print("shuffeled deck : ", deck )
    print("size", len(deck))


    return deck
