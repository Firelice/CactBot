from discord.ext.commands import Bot
from tokens import fetchtokens
import random

TOKEN = fetchtokens.fetchdiscordtoken()
BOT_PREFIX = "!"


bot = Bot(command_prefix=BOT_PREFIX)


@bot.command(name = 'joke',
             description="Tells a funny joke",
             aliases=['Joke'],
             pass_context=True)
async def joke(context):
    """
    on command !joke will return a message from a list of jokes
    :param context: context in order to get an author
    :return: none
    """
    jokes = [
        "Samurai is a \U0000267F",
        "\U0000267FCactuar  Crew  coming through!\U0000267F",
        "A dragoon walks into a bar...\n Everyone else dodges it.",
        "Summoners ruin everything!",
        "When does the Ninja arrive at a party...\n Raiton time!",
        "Esuna Matata! What a wonderful phrase!",
        "Why are black mages bad team players... \n Because after thirty seconds they foul everything.",
        "What do you call a guy playing a female dragoon... \n A DRG Queen"
    ]
    # The list of jokes
    await bot.say(context.message.author.mention + "\n" + random.choice(jokes))


bot.run(TOKEN)
