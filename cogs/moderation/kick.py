import discord
from discord.ext import commands
import asyncio

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Kick cog loaded successfully")

    @commands.hybrid_command(name="kick", description="Kick a member with a reason.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member = None, *, reason=None):

        if not ctx.guild.me.guild_permissions.kick_members:
            msg = await ctx.send(f"{ctx.author.mention} I don't have permission to kick members.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        if user is None:
            msg = await ctx.send(f"{ctx.author.mention} You must mention a user to kick.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        if user.top_role >= ctx.guild.me.top_role:
            msg = await ctx.send(f"{ctx.author.mention} I can't kick {user.mention} because their role is higher than mine.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        if reason is None:
            msg = await ctx.send(f"{ctx.author.mention} Please provide a reason for the kick.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        await user.kick(reason=reason)
        confirmation = await ctx.send(f"{ctx.author.mention} {user.mention} has been kicked. Reason: {reason}")
        await asyncio.sleep(5)
        await confirmation.delete()

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            msg = await ctx.send(f"{ctx.author.mention} You don't have permission to use this command.")
            await asyncio.sleep(5)
            await msg.delete()
        elif isinstance(error, commands.BadArgument):
            msg = await ctx.send(f"{ctx.author.mention} Couldn't find that user. Please mention a valid member.")
            await asyncio.sleep(5)
            await msg.delete()
        else:
            raise error  

async def setup(bot):
    await bot.add_cog(Kick(bot))