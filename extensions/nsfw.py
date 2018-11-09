import discord
import json
import time

from random import choice
from extensions.tools import http
from discord.ext import commands
from extensions.tools.chat_formatting import italics

embedcolors = [0x12a8a8, 0x2807ff, 0x12a873, 0x00FF54, 0x7EFF00, 0xFF6000, 0xCC00FF, 0xFF007E]

class nsfw:
    def __init__(self, bot):
        self.bot = bot

    async def randomimageapi(self, ctx, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except json.JSONDecodeError:
            return await ctx.send("Couldn't find anything from the API")

        url = (r[endpoint])
        e = discord.Embed(color=choice(embedcolors))
        e.set_image(url=url)
        await ctx.send(embed=e)

    @commands.command()
    async def spank(self, ctx, user : discord.Member = None):
        """ Give someone a spank  """
        if user is None:
            await ctx.send("Bruh, who are you giving a beating")
            return
        elif user is ctx.author:
            await ctx.send("woah, that's kinda weird not gonna lie.")
            return
        if ctx.channel.is_nsfw() != True:
            embed=discord.Embed(color=random.choice(embedcolors), title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        else:   
            author = user.display_name
            user = ctx.author.display_name
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
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def blowjob(self, ctx, bombamount=0, **kwargs):
        """ Posts a random blowjob gif 
        you can use *blowjob amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/bj', 'url')
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/bj', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
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
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/lewdkemo', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
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
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/pussy', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
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
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/kuni', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
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
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/trap', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
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
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/futanari', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def anal(self, ctx, bombamount=0):
        """ Posts a random anal gif 
        you can use *futa amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            await ctx.send(embed=embed)
            return
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/anal', 'url')
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/anal', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
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
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
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
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum_jpg', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
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
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/yuri', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
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
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/Random_hentai_gif', 'url')
                messages = messages + 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
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
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
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
