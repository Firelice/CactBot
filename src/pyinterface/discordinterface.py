from discord.ext.commands import Bot
from tokens import fetchtokens

TOKEN = fetchtokens.fetchdiscordtoken()
BOT_PREFIX = ("!")


bot = Bot(command_prefix=BOT_PREFIX)

