import random


def joke():
    jokes = [
        "Samurai is a \U0000267F",
        "\U0000267FCactuar  Crew  coming through!\U0000267F",
        "A dragoon walks into a bar...\n Everyone else dodges it!",
        "Summoners ruin everything!",
        "When does the Ninja arrive at a party...\n Raiton time!",
        "Esuna Matata! What a wonderful phrase!",
        "Why are black mages bad team players... \n Because after thirty seconds they foul everything!",
        "What do you call a guy playing a female dragoon... \n A DRG Queen!"
    ]
    return random.choice(jokes)
