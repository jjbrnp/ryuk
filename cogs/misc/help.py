import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Help cog loaded successfully")

    @commands.command(name="help")
    async def help_command(self, ctx):
        embed = discord.Embed(
            title="Ryuk Help",
            description="Here are the available commands and bot information:",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else discord.Embed.Empty)
        embed.set_footer(text="Developed by Jaime Bernal")

        embed.add_field(name="🛠️ Moderation", value="`kick`, `ban`, `mute`, `unmute`, `purge`", inline=False)
        embed.add_field(name="❓ Help", value="`help`", inline=False)
        embed.add_field(name="📌 Info", value="More features coming soon!", inline=False)

        embed.add_field(
            name="ℹ️ About the Bot",
            value=(
                f"**Name:** {self.bot.user.name}\n"
                f"**ID:** {self.bot.user.id}\n"
                f"**Prefix:** `r!`\n"
                f"**Servers:** {len(self.bot.guilds)}"
            ),
            inline=False
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))