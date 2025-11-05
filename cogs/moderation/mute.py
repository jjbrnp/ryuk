import discord
from discord.ext import commands
import asyncio

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Mute cog loaded successfully")

    @commands.command(name="mute")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, user: discord.Member = None, *, reason=None):
        
        if not ctx.guild.me.guild_permissions.manage_roles:
            msg = await ctx.send(f"{ctx.author.mention} I don't have permission to manage roles.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        if user is None:
            msg = await ctx.send(f"{ctx.author.mention} You must mention a user to mute.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        if user.top_role >= ctx.guild.me.top_role:
            msg = await ctx.send(f"{ctx.author.mention} I can't mute {user.mention} because their role is higher than mine.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        if reason is None:
            reason = "No reason provided"
        
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            msg = await ctx.send(f"{ctx.author.mention} The 'Muted' role does not exist.")
            await asyncio.sleep(5)
            await msg.delete()
            return
        
        if muted_role in user.roles:
            msg = await ctx.send(f"{ctx.author.mention} {user.mention} is already muted.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        await user.add_roles(muted_role, reason=reason)
        await ctx.send(f"{ctx.author.mention} {user.mention} has been muted. Reason: {reason}")


    @mute.error
    async def mute_error(self, ctx, error):
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
    await bot.add_cog(Mute(bot))