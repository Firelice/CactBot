from discord.ext.commands import Bot
from tokens import fetchtokens
from src.fetchlists import fetchlists
from src.pyinterface import datainterface


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


@bot.command(name = 'add',
             description="Adds the Final Fantasy character name to the database",
             aliases=['Add'],
             pass_context=True)
async def add(context, *, message):
    print("Adding " + message + " to static.")
    datainterface.insert_chara(message, str(context.message.author.id))
    await bot.add_reaction(context.message, '\U0001F44D')



bot.run(TOKEN)
