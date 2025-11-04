import discord 
from discord.ext import commands
import asyncio

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        print("Cargado cog de purgar correctamente")

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, cantidad: int):
        if cantidad > 100:
            await ctx.send(f"{ctx.author.mention} La cantidad no puede ser superior a 100 mensajes.") 
            return
        elif cantidad < 1:
            await ctx.send(f"{ctx.author.mention} Debes eliminar al menos un mensaje.")
            return
        elif not isinstance(cantidad, int):
            await ctx.send(f"{ctx.author.mention} Debes de poner un número del 1 al 100.")
            return
        
        await ctx.channel.purge(limit=cantidad + 1)
        confirmacion = await ctx.send(f"{ctx.author.mention} Se han borrado {cantidad} mensajes.")
        await asyncio.sleep(5)
        
        await confirmacion.delete()
        return
        
async def setup(bot):
    await bot.add_cog(Purge(bot))