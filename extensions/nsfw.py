import discord
import json
import time

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
    async def blowjob(self, ctx):
        """ Posts a random kitsune picture """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/bj', 'url')

    @commands.command()
    async def blowjobbomb(self, ctx, amount):
        """ Posts random kitsune pictures """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            messages = 0
            while messages < int(amount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/bj', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def kitsune(self, ctx):
        """ Posts a random kitsune picture """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/lewdkemo', 'url')

    @commands.command()
    async def kitsunebomb(self, ctx, amount):
        """ Posts random kitsune pictures """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            messages = 0
            while messages < int(amount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/lewdkemo', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def pussy(self, ctx):
        """ Posts a random anime pussy gif """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/pussy', 'url')

    @commands.command()
    async def pussybomb(self, ctx, amount):
        """ Posts random anime pussy gifs """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            messages = 0
            while messages < int(amount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/pussy', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def kuni(self, ctx):
        """ Posts a random kuni gif """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/kuni', 'url')

    @commands.command()
    async def kunibomb(self, ctx, amount):
        """ Posts random kuni gifs """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            messages = 0
            while messages < int(amount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/kuni', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def trap(self, ctx):
        """ Posts a random trap picture """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/trap', 'url')

    @commands.command()
    async def trapbomb(self, ctx, amount):
        """ Posts random trap picture """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            messages = 0
            while messages < int(amount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/trap', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def futa(self, ctx):
        """ Posts a random futa picture """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/futanari', 'url')

    @commands.command()
    async def futabomb(self, ctx, amount):
        """ Posts random futa picture """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            messages = 0
            while messages < int(amount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/futanari', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def cumgif(self, ctx):
        """ Posts a random hentai gif covered in cum """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum', 'url')

    @commands.command()
    async def cumgifbomb(self, ctx, amount):
        """ Posts random hentai gif covered in cum """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            messages = 0
            while messages < int(amount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def cum(self, ctx):
        """ Posts a random hentai pictures covered in cum """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum_jpg', 'url')

    @commands.command()
    async def cumbomb(self, ctx, amount):
        """ Posts random hentai pictures covered in cum """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            messages = 0
            while messages < int(amount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum_jpg', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def yuri(self, ctx):
        """ Posts a random yuri pictures """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/yuri', 'url')

    @commands.command()
    async def yuribomb(self, ctx, amount):
        """ Posts random yuri pictures """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            messages = 0
            while messages < int(amount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/yuri', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def hentai(self, ctx):
        """ Posts a random hentai gif """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/Random_hentai_gif', 'url')

    @commands.command()
    async def hentaibomb(self, ctx, amount):
        """ Posts random hentai gif """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            messages = 0
            while messages < int(amount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/Random_hentai_gif', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def nekogif(self, ctx):
        """ Posts a random neko gif """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/nsfw_neko_gif', 'url')

    @commands.command()
    async def nekobomb(self, ctx, amount):
        """ Posts random neko gif """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:
            messages = 0
            while messages < int(amount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/nsfw_neko_gif', 'url')
                messages = messages + 1
                time.sleep(1)

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