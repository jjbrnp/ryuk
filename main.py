import discord  
from discord.ext import commands
from dotenv import load_dotenv
import os


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="r!", intents=intents)

@bot.event
async def on_ready():
    print(f'Iniciada sesión como {bot.user}')

async def setup_hook():
    await bot.load_extension("cogs.bienvenida")
    await bot.load_extension("cogs.moderacion.purge")
        
bot.setup_hook = setup_hook

load_dotenv()
token = os.getenv("disc_token")

bot.run(token)
