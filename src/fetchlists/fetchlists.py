import random


def joke():
    jokes = [
        "Samurai is a \U0000267F",
        "\U0000267FCactuar Crew coming through!\U0000267F",
        "A dragoon walks into a bar...\nEveryone else dodges it!",
        "Summoners ruin everything!",
        "When does the Ninja arrive at a party...\nRaiton time!",
        "Esuna Matata! What a wonderful phrase!",
        "Why are black mages bad team players... \nBecause after thirty seconds they foul everything!",
        "What do you call a guy playing a female dragoon... \nA DRG Queen!",
        "Why did the Dragoon get fired...\nBecause they kept asking for a raise!",
        "What happened when the waiter tripped in Eorzea Cafè...\nThe server went down!",
        "Roegadyn Ninja!",
        "Vyn's Subway Sandwiches!",
        "Pineapple on Pizza!"
    ]
    return random.choice(jokes)
