import discord
import aiohttp

from extensions.tools import perms, default
from discord.ext import commands


class Admin:
    def __init__(self, bot,):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self, ctx, user: discord.Member, *, reason: str = None):
        if user == ctx.author:
            e=discord.Embed(title="Self harm is bad")
            await ctx.send(embed=e)
            return
        else:
            await ctx.guild.kick(user)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def ban(self, ctx, user: discord.Member, *, reason: str = None):
        if user == ctx.author:
            e=discord.Embed(title="Self harm is bad")
            await ctx.send(embed=e)
            return
        else:
            await ctx.guild.ban(user)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
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
            return await ctx.send("Are you sure you've made a role called **Muted**?")

        try:
            await member.add_roles(therole, reason=default.responsible(ctx.author, reason))
            await ctx.send(default.actionmessage("muted"))
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
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

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.guild_only()
    async def setnick(self, ctx, member : discord.Member, *, name):
            try:
                await member.edit(nick=name)
            except:
                await ctx.send("Failed to change nickname")
            else:
                await ctx.send("Successfuly changed nickname to {}".format(name))

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def setguildicon(self, ctx, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                data = await r.read()
        await ctx.guild.edit(icon=data)
        await ctx.send("Icon changed")


    @commands.command(aliases=["prune"])
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def purge(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"Deleted {len(deleted)} messages")

def setup(bot):
    bot.add_cog(Admin(bot))
