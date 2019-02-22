import random


def joke():
    jokes = [
        "Samurai is a \U0000267F",
        "\U0000267FCactuar Crew coming through!\U0000267F",
        "A dragoon walks into a bar...\nEveryone else dodges it!",
        "Summoners ruin everything!",
        "When does the Ninja arrive at a party...\nRaiton time!",
        "Esuna Matata! What a wonderful phrase!",
        "Why are Black Mages bad team players... \nBecause after thirty seconds they foul everything!",
        "What do you call a guy playing a female Dragoon... \nA DRG Queen!",
        "Why did the Dragoon get fired...\nBecause they kept asking for a raise!",
        "What happened when the waiter tripped in Eorzea Cafè...\nThe server went down!",
        "Roegadyn Ninja!",
        "Vyn's Subway Sandwiches!",
        "Pineapple on Pizza!",
        "Cactuar Crew on O10S! \U0001F409",
        "Why can't Lalafells be chefs...\nThe steaks are too high",
        "Pugging with our Strats",
        "What do you call a fish with no eyes...\nFSH",
        "Where do Dragoons go on vacation the most...\nFloorda"
    ]
    return random.choice(jokes)
