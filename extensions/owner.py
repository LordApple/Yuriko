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
    async def smessage(self, ctx, user : discord.Member, *, message):
        author = ctx.message.author.display_name
        if ctx.author.id in config_forwarder.owners:
            spamamt = int(input("Enter the amt of spam u want:"))
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
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

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
    
    @commands.command()
    @commands.is_owner()
    async def setstream(self, ctx, *, game):
        game = game.strip()
        if game != "":
            try:
                game = discord.Streaming(name=game, url="https://www.twitch.tv/twitchbot_discord/")
                await self.bot.change_presence(status=discord.Status.dnd, activity=game)
            except:
                await ctx.send("Failed to change game")
            else:
                await ctx.send("Successfuly changed game to {}".format(game))

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

def setup(bot):
    bot.add_cog(Owner(bot))