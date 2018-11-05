import discord
import aiohttp
from discord.ext import commands


class Owner:
    def __init__(self, bot,):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        async with aiohttp.ClientSession() as session:
            await ctx.send("Shutting down...\n\U0001f44b")
            await self.bot.logout()

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def setavatar(self, ctx, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                data = await r.read()
        await self.bot.user.edit(avatar=data)
        await ctx.send("Avatar changed")

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def setgame(self, ctx, *, game):
        game = game.strip()
        if game != "":
            try:
                await self.bot.change_presence(activity=discord.Game(type=0, name=game), status=discord.Status.dnd)
            except:
                await ctx.send("Failed to change game")
            else:
                await ctx.send("Successfuly changed game to {}".format(game))

    @commands.command(pass_context=True)
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
    @commands.is_owner()
    async def file(self, ctx):
        await ctx.send(file=discord.File('test.png'))

def setup(bot):
    bot.add_cog(Owner(bot))