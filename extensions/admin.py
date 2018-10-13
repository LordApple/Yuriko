import discord
from discord.ext import commands


class Admin:
    def __init__(self, bot,):
        self.bot = bot

    @commands.command(no_pm=True, pass_context=True)
    @commands.is_owner()
    async def kick(self, ctx, user: discord.Member, *, reason: str = None):
        await ctx.guild.kick(user)


def setup(bot):
    bot.add_cog(Admin(bot))