import discord 
from discord.ext import commands
import asyncio

class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Unmute cog loaded successfully")

    @commands.hybrid_command(name="unmute", description="Unmute a member")
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, user: discord.Member = None):

        if not ctx.guild.me.guild_permissions.manage_roles:
            msg = await ctx.send(f"{ctx.author.mention} I don't have permission to manage roles.")
            await asyncio.sleep(5)
            await msg.delete()
            return


        if user is None:
            msg = await ctx.send(f"{ctx.author.mention} You must mention a user to unmute.")
            await asyncio.sleep(5)
            await msg.delete()
            return
        
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role not in user.roles:
            msg = await ctx.send(f"{ctx.author.mention} {user.mention} Is not muted.")
            await asyncio.sleep(5)
            await msg.delete()
            return
        
        await user.remove_roles(muted_role, reason="Unmuted by command")
        await ctx.send(f"{ctx.author.mention} {user.mention} has been unmuted.")

        
    @unmute.error
    async def unmute_error(self, ctx, error):
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
    await bot.add_cog(Unmute(bot))