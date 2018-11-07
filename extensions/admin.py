import discord
import aiohttp

from extensions.tools import perms, default
from discord.ext import commands


class Admin:
    def __init__(self, bot,):
        self.bot = bot

    @commands.command()
    @perms.has_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self, ctx, user: discord.Member, *, reason: str = None):
        await ctx.guild.kick(user)

    @commands.command()
    @perms.has_permissions(ban_members=True)
    @commands.guild_only()
    async def ban(self, ctx, user: discord.Member, *, reason: str = None):
        await ctx.guild.ban(user)

    @commands.command()
    @perms.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def mute(self, ctx, member: discord.Member, *, reason: str = None):
        """ Mutes a user from the current server. """
        message = []
        for role in ctx.guild.roles:
            if role.name == "Muted":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except IndexError:
            return await ctx.send("Are you sure you've made a role called **Muted**? Remember that it's case sensetive too...")

        try:
            await member.add_roles(therole, reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("muted"))
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @perms.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def unmute(self, ctx, member: discord.Member, *, reason: str = None):
        """ Unmutes a user from the current server. """
        message = []
        for role in ctx.guild.roles:
            if role.name == "Muted":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except IndexError:
            return await ctx.send("Are you sure you've made a role called **Muted**? Remember that it's case sensetive too...")

        try:
            await member.remove_roles(therole, reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("unmuted"))
        except Exception as e:
            await ctx.send(e)

    @commands.command(aliases=["prune"])
    @perms.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def purge(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"Deleted {len(deleted)} messages")

def setup(bot):
    bot.add_cog(Admin(bot))
