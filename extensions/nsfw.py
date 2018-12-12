import discord
import json
import time
import aiohttp

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
            return await ctx.send("Bruh, who are you giving a beating")
        elif user is ctx.author:
            return await ctx.send("woah, that's kinda weird not gonna lie.")
        if ctx.channel.is_nsfw() != True:
            embed=discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        user = user.display_name
        author = ctx.author.display_name
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/spank') as r:
                if r.status == 200:
                    js = await r.json()
                    embed=discord.Embed(title=italics(f"{user} got spanked by {author}"), color=choice(embedcolors))
                    embed.set_image(url=(js['url']))
                    await ctx.send(embed=embed)  

    @commands.command()
    async def nsfwavatar(self, ctx):
        """ Gives you a NSFW avatar """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        author = ctx.author.display_name
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/nsfw_avatar') as r:
                if r.status == 200:
                    js = await r.json()
                    embed=discord.Embed(title=italics(f"{author}, Here is your avatar"), color=choice(embedcolors))
                    embed.set_image(url=(js['url']))
                    await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def blowjob(self, ctx, bombamount=0, **kwargs):
        """ Posts a random blowjob gif 
        you can use *blowjob amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/bj', 'url')
                self.bot.get_command("blowjob").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/bj', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.guild)
    async def kitsune(self, ctx, bombamount=0):
        """ Posts a random kitsune pictures 
        you can use *kitsune amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/lewdkemo', 'url')
            self.bot.get_command("kitsune").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/lewdkemo', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def pussy(self, ctx, bombamount=0):
        """ Posts a random anime pussy gif 
        you can use *pussy amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/pussy', 'url')
            self.bot.get_command("pussy").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/pussy', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def kuni(self, ctx, bombamount=0):
        """ Posts a random kuni gif 
        you can use *kuni amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/kuni', 'url')
            self.bot.get_command("kuni").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/kuni', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def trap(self, ctx, bombamount=0):
        """ Posts a random trap picture
        you can use *trap amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/trap', 'url')
            self.bot.get_command("trap").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/trap', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def futa(self, ctx, bombamount=0):
        """ Posts a random futa picture 
        you can use *futa amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/futanari', 'url')
            self.bot.get_command("futa").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/futanari', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def anal(self, ctx, bombamount=0):
        """ Posts a random anal gif 
        you can use *futa amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/anal', 'url')
            self.bot.get_command("anal").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/anal', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def cumgif(self, ctx, bombamount=0):
        """ Posts a random gif of a hentai girl covered in cum
        you can use *cumgif amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum', 'url')
            self.bot.get_command("cumgif").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def cum(self, ctx, bombamount=0):
        """ Posts a random hentai gif covered in cum
        you can use *cum amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum_jpg', 'url')
            self.bot.get_command("cum").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cum_jpg', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def yuri(self, ctx, bombamount=0):
        """ Posts a random yuri picture
        you can use *yuri amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/yuri', 'url')
            self.bot.get_command("yuri").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/yuri', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def hentai(self, ctx, bombamount=0):
        """ Posts a random hentai gif
        you can use *hentai amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/Random_hentai_gif', 'url')
            self.bot.get_command("hentai").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/Random_hentai_gif', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    @commands.cooldown(1, 50, commands.BucketType.guild)
    async def nekogif(self, ctx, bombamount=0):
        """ Posts a random neko gif
        you can use *nekogif amount for more
        """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        elif bombamount == 0:
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/nsfw_neko_gif', 'url')
            self.bot.get_command("nekogif").reset_cooldown(ctx)
        elif bombamount > 50:
            embed=discord.Embed(color=0xff0022,title="Max bomblimit is 50")
            await ctx.send(embed=embed)
        elif bombamount <= 50:
            messages = 0
            while messages < int(bombamount):
                await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/nsfw_neko_gif', 'url')
                messages += 1
                time.sleep(1)

    @commands.command()
    async def blow(self, ctx, user : discord.Member):
        """ Give someone a blow ( ͡° ͜ʖ ͡°) """
        if ctx.channel.is_nsfw() != True:
            embed = discord.Embed(color=0xff0022, title="This command can only be used in NSFW flagged channels.")
            return await ctx.send(embed=embed)
        user = user.display_name
        author = ctx.author.display_name
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/blowjob') as r:
                if r.status == 200:
                    js = await r.json()
                    embed=discord.Embed(title=italics(f"{user} Got a blowjob from {author}"), color=choice(embedcolors))
                    embed.set_image(url=(js['url']))
                    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(nsfw(bot))
