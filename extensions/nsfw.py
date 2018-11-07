import discord
import json

from extensions.tools import http
from discord.ext import commands
from extensions.tools.chat_formatting import italics


class nsfw:
    def __init__(self, bot):
        self.bot = bot

    async def randomimageapi(self, ctx, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except json.JSONDecodeError:
            return await ctx.send("Couldn't find anything from the API")

        await ctx.send(r[endpoint])

    @commands.command()
    async def nsfwavatar(self, ctx):
        """ Gives you a NSFW avatar """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            user = ctx.author.display_name
            await ctx.send(italics("{}".format(user) + ", Here is your avatar"))
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/nsfw_avatar', 'url')

    @commands.command()
    async def blow(self, ctx, user : discord.Member):
        """ Give someone a blow ( ͡° ͜ʖ ͡°) """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            author = user.display_name
            user = ctx.author.display_name
            await ctx.send(italics("{}".format(author) + " Got a blowjob from " + "{}".format(user)))
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/blowjob', 'url')

def setup(bot):
    bot.add_cog(nsfw(bot))