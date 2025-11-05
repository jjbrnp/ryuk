import discord
from discord.ext import commands
import asyncio

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Purge cog loaded successfully")

    @commands.hybrid_command(name="purge", description="Purge a number of messages")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        if amount > 100:
            await ctx.send(f"{ctx.author.mention} You can't delete more than 100 messages at once.")
            return
        elif amount < 1:
            await ctx.send(f"{ctx.author.mention} You must delete at least one message.")
            return
        elif not isinstance(amount, int):
            await ctx.send(f"{ctx.author.mention} Please enter a number between 1 and 100.")
            return

        await ctx.channel.purge(limit=amount + 1)
        confirmation = await ctx.send(f"{ctx.author.mention} {amount} messages have been deleted.")
        await asyncio.sleep(5)
        await confirmation.delete()

async def setup(bot):
    await bot.add_cog(Purge(bot))