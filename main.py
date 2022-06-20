import discord, os
import functions.functions as fn
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
client = discord.Client()
BOT_TOKEN = "OTc2NTM1Mjk3NDA1ODk4Nzky.GEACzH.dshzBXpNf5dwIQIydxIceC6nOzWIwSbS6qFGKw"
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix="s!")
fn.commands(bot,discord,client)
bot.run(BOT_TOKEN)
