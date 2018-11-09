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
    async def spank(self, ctx, user : discord.Member = None):
        """ Give someone a spank  """
        if user is None:
            await ctx.send("Bruh, who are you giving a beating")
            return
        elif user is ctx.author:
            await ctx.send("woah, that's kinda weird not gonna lie.")
            return
        author = user.display_name
        user = ctx.author.display_name
        if ctx.channel.is_nsfw() != True:
            await ctx.send(italics("{}".format(author) + " got spanked by " + "{}".format(user)))
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/spank', 'url')    

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
    async def blowjob(self, ctx, bombamount=0):
        """ Posts a random blowjob gif 
        you can use *blowjob amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/bj', 'url')
        else:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/bj', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def kitsune(self, ctx, bombamount=0):
        """ Posts a random kitsune pictures 
        you can use *kitsune amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/lewdkemo', 'url')
        else:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/lewdkemo', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def pussy(self, ctx, bombamount=0):
        """ Posts a random anime pussy gif 
        you can use *pussy amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/pussy', 'url')
        else:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/pussy', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def kuni(self, ctx, bombamount=0):
        """ Posts a random kuni gif 
        you can use *kuni amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/kuni', 'url')
        else:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/kuni', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def trap(self, ctx, bombamount=0):
        """ Posts a random trap picture
        you can use *trap amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/trap', 'url')
        else:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/trap', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def futa(self, ctx, bombamount=0):
        """ Posts a random futa picture 
        you can use *futa amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/futanari', 'url')
        else:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/futanari', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def cumgif(self, ctx, bombamount=0):
        """ Posts a random gif of a hentai girl covered in cum
        you can use *cumgif amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum', 'url')
        else:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def cum(self, ctx, bombamount=0):
        """ Posts a random hentai gif covered in cum
        you can use *cum amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum_jpg', 'url')
        else:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum_jpg', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def yuri(self, ctx, bombamount=0):
        """ Posts a random yuri picture
        you can use *yuri amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/yuri', 'url')
        else:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/yuri', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def hentai(self, ctx, bombamount=0):
        """ Posts a random hentai gif
        you can use *hentai amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/Random_hentai_gif', 'url')
        else:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/Random_hentai_gif', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    async def nekogif(self, ctx, bombamount=0):
        """ Posts a random neko gif
        you can use *nekogif amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/nsfw_neko_gif', 'url')
        else:
            messages = 0
            while messages < int(bombamount):
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