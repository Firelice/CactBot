from discord.ext.commands import Bot
from tokens import fetchtokens
from src.fetchlists import fetchlists


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
    joke = fetchlists.joke()
    # fetches a joke
    await bot.say(context.message.author.mention + "\n" + joke)


bot.run(TOKEN)
