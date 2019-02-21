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
        "\U0000267FCactuar  Crew  coming through!\U0000267F"
    ]
    await bot.say(random.choice(jokes) + ", " + context.message.author.mention)

bot.run(TOKEN)
