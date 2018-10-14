import discord
import aiohttp

from extensions.tools import perms, default
from discord.ext import commands


class Admin:
    def __init__(self, bot,):
        self.bot = bot

    @commands.command(no_pm=True, pass_context=True)
    @perms.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason: str = None):
        await ctx.guild.kick(user)

    @commands.command(no_pm=True, pass_context=True)
    @perms.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason: str = None):
        await ctx.guild.ban(user)

def setup(bot):
    bot.add_cog(Admin(bot))