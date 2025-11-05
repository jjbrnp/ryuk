import discord
from discord.ext import commands
import asyncio

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Ban cog loaded successfully")

    @commands.command(name="Ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member = None, *, reason=None):

        if not ctx.guild.me.guild_permissions.ban_members:
            msg = await ctx.send(f"{ctx.author.mention} I don't have permission to ban members.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        if user is None:
            msg = await ctx.send(f"{ctx.author.mention} You must mention a user to ban.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        if user.top_role >= ctx.guild.me.top_role:
            msg = await ctx.send(f"{ctx.author.mention} I can't ban {user.mention} because their role is higher than mine.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        if reason is None:
            msg = await ctx.send(f"{ctx.author.mention} Please provide a reason for the ban.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        await user.ban(reason=reason)
        confirmation = await ctx.send(f"{ctx.author.mention} {user.mention} has been banned. Reason: {reason}")
        await asyncio.sleep(5)
        await confirmation.delete()

    @ban.error
    async def ban_error(self, ctx, error):
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
    await bot.add_cog(Ban(bot))