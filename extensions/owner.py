import discord
import aiohttp
import time

from discord.ext import commands
from extensions.tools.chat_formatting import italics, bold, strikethrough, pagify, escape
from extensions.tools import config_forwarder

class Owner:
    def __init__(self, bot,):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        async with aiohttp.ClientSession() as session:
            await ctx.send("Shutting down...\n\U0001f44b")
            await self.bot.logout()

    @commands.command()
    @commands.is_owner()
    async def setavatar(self, ctx, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                data = await r.read()
        await self.bot.user.edit(avatar=data)
        await ctx.send("Avatar changed")

    @commands.command(aliases=["msg"])
    async def message(self, ctx, user : discord.Member, *, message):
        author = ctx.message.author.display_name
        if ctx.author.id in config_forwarder.owners:
            await user.send(message)
            print("User " + author + " used the msg command")
        else:
            embed = discord.Embed(title="This command is for the bot owners only.", color=0xFF0000)
            await ctx.send(embed=embed)
            print("User " + author + " tried to use the msg command.")

    @commands.command(aliases=["smsg"])
    async def smessage(self, ctx, spamamt, user : discord.Member, *, message):
        author = ctx.message.author.display_name
        if ctx.author.id in config_forwarder.owners:
            spamamt = int(spamamt)
            for x in range(0, spamamt):
                time.sleep(1)
                await user.send(message)
                print("User " + author + " used the msg command")
        else:
            embed = discord.Embed(title="This command is for the bot owners only.", color=0xFF0000)
            await ctx.send(embed=embed)
            print("User " + author + " tried to use the msg command.")

    @commands.command()
    @commands.is_owner()
    async def mbomb(self, ctx):
            msg = 'wow, this is a dead chat... lets fix that.\n'
            for member in ctx.guild.members:
                msg += '\n<@' + str(member.id) + '>'
            await ctx.send(msg)
    
    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    """
    @commands.command()
    @commands.is_owner()
    async def setgame(self, ctx, *, game):
        game = game.strip()
        if game != "":
            try:
                game = discord.Game(name=game)
                await self.bot.change_presence(status=discord.Status.dnd, activity=game)
            except:
                await ctx.send("Failed to change game")
            else:
                await ctx.send("Successfuly changed game to {}".format(game))
                """
    
    @commands.command()
    @commands.is_owner()
    async def setgame(self, ctx, gtype, *, game):
            try:
                game = discord.Activity(type=gtype,name=game, url="https://www.twitch.tv/twitchbot_discord/")
                await self.bot.change_presence(status=discord.Status.dnd, activity=game)
            except:
                await ctx.send("Failed to change game")
            else:
                await ctx.send("Done")

    @commands.command()
    @commands.is_owner()
    async def setname(self, ctx, *, name):
        name = name.strip()
        if name != "":
            try:
                await self.bot.user.edit(username=name)
            except:
                await ctx.send("Failed to change name")
            else:
                await ctx.send("Successfuly changed name to {}".format(name))

    @commands.command()
    @commands.has_permissions(manage_nickname=True)
    async def rall(self,ctx,*,name):
        for member in ctx.guild.members:
            if member.top_role.position < ctx.guild.me.top_role.position:
                await member.edit(nick=name)
                print(f'Member {member} has been renamed to {name}')

    @commands.command()
    async def guilds(self, ctx):
        """Lists all bot servers"""
        if ctx.author.id in config_forwarder.owners:
            msg = ''
            for server in self.bot.guilds:
                msg = msg + '\n' + str(server)
            msg = msg + '\n'
            embed = discord.Embed(color=0x3ef301,title="Im in {}".format(len(self.bot.guilds)) + " guilds")
            embed.add_field(name="Server list", value=msg)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="This command is for the bot owners only.", color=0xFF0000)
            await ctx.send(embed=embed)
            print("User " + author + " tried to use the guilds command.")

    @commands.command()
    @commands.is_owner()
    async def invites(self,ctx):
        """Creates a invite for the current discord server"""
        for server in self.bot.guilds:
            invite = await ctx.guild.invites()
            print("Invites: {0}".format(", ".join(map(str, invite))))

def setup(bot):
    bot.add_cog(Owner(bot))