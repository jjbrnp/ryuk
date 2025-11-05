import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

class Bienvenida(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Cargado cog de bienvenida del servidor de prueba correctamente")

    @commands.Cog.listener()
    async def on_member_join(self, member):

        guild_id = os.getenv("test_server_id")

        if member.guild.id != guild_id:
            return
        
        canal_bienvenida = discord.utils.get(member.guild.text_channels, name="bienvenida")
        if canal_bienvenida:
            await canal_bienvenida.send(
                f"Bienvenido al servidor de prueba de Jaime Bernal, {member.mention} pásatelo bien."
            )
        else:
            print("Canal 'bienvenida' no encontrado.")

async def setup(bot):
    await bot.add_cog(Bienvenida(bot))
