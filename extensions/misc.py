import discord
import time
import os
import psutil
import random
import json

from datetime import datetime
from discord.ext import commands
from random import randint
from random import choice
from extensions.tools import default, config_forwarder, http, perms
from extensions.tools.chat_formatting import italics, bold, strikethrough, pagify, escape

embedcolors = [0x12a8a8, 0x2807ff, 0x12a873]
insultlist = ["Your mom is big gay"]

class Misc:
    def __init__(self, bot,):
        self.bot = bot
        self.ball = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                    "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                    "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                    "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    async def randomimageapi(self, ctx, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except json.JSONDecodeError:
            return await ctx.send("Couldn't find anything from the API")

        await ctx.send(r[endpoint])

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def avatar(self, ctx, member: discord.Member = None):
        """User Avatar"""
        if member is None:
            member = ctx.author
        author = member.display_name
        embed = discord.Embed()
        embed=discord.Embed(color=0x3ef301, title="{}'s avatar".format(author))
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def roll(self, ctx, number : int = 100):
        """Rolls random number (between 1 and user choice)
        Defaults to 100.
        """
        author = ctx.message.author
        if number > 1:
            n = randint(1, number)
            await ctx.send("{} :game_die: {} :game_die:".format(author.mention, n))
        else:
            await ctx.send("{} Maybe higher than 1? ;P".format(author.mention))

    @commands.command(name="8", aliases=["8ball"])
    async def _8ball(self, ctx, *, question : str):
        """Ask 8 ball a question
        Question must end with a question mark.
        """
        if question.endswith("?") and question != "?":
            embed = discord.Embed(color=0x3ef301)
            embed.add_field(name="8ball response.", value=choice(self.ball))
            await ctx.send(embed=embed)
        else:
            embederror = discord.Embed(color=0xff0022)
            embederror.add_field(name="That doesn't look like a question.", value="Question must end with a question mark.")
            await ctx.send(embed=embederror)
    
    @commands.command()
    @commands.guild_only()
    async def guildicon(self, ctx):
        """Guild Icon"""
        server = ctx.message.guild.name
        embed=discord.Embed(color=choice(embedcolors), title="{}'s icon".format(server))
        embed.set_image(url=ctx.message.guild.icon_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def insult(self, ctx, *, user: discord.Member):
        """Insults a user for you"""
        await ctx.send("{},".format(user.display_name) + " {}".format(choice(insultlist)))

    @commands.command()
    async def ping(self,ctx):
        """ping time"""
        t1 = time.perf_counter()
        await ctx.send("Pong :ping_pong:")
        t2 = time.perf_counter()
        await ctx.send("ping: {}ms".format(round((t2-t1)*1000)))

    @commands.command()
    async def pickle(self, ctx, *users: discord.Member):
        """Detects user's pickle length
        This is 100% accurate.
        Enter multiple users for an accurate comparison!"""

        if not users:
            await ctx.send("Please mention a user.")
            return        

        dongs = {}
        msg = ""
        state = random.getstate()

        for user in users:
            random.seed(user.id)
            if user.id == 381506124509347840: #because i can ok? also, this is not my id. its the bots
                dongs[user] = "8{}D".format("=" * 50)
            else:
                dongs[user] = "8{}D".format("=" * random.randint(0, 30))

        random.setstate(state)
        dongs = sorted(dongs.items(), key=lambda x: x[1])

        for user, dong in dongs:
            msg += "**{}'s size:**\n{}\n".format(user.display_name, dong)

        for page in pagify(msg):
            await ctx.send(page)

    @commands.command()
    async def reverse(self, ctx, *, text: str):
        """ Reverses everything you type.
        Everything you type after reverse will of course, be reversed
        """
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")
        
    @commands.group()
    @commands.guild_only()
    async def server(self, ctx):
        """ Check info about current server """
        if ctx.invoked_subcommand is None:
            findbots = sum(1 for member in ctx.guild.members if member.bot)

            embed = discord.Embed(title="ℹ information about **{}**".format(ctx.guild.name), color=0x3ef301)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
            embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
            embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
            embed.add_field(name="Bots", value=findbots, inline=True)
            embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
            embed.add_field(name="Region", value=ctx.guild.region, inline=True)
            embed.add_field(name="Created", value=default.date(ctx.guild.created_at), inline=True)
            await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    async def user(self, ctx, *, user: discord.Member = None):
        """ Get user information """
        if user is None:
            user = ctx.author

        embed = discord.Embed(colour=user.top_role.colour.value, title="ℹ About **{}**".format(user.id))
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Full name", value=user, inline=True)
        embed.add_field(name="Nickname", value=user.nick if hasattr(user, "nick") else "None", inline=True)
        embed.add_field(name="Account created", value=default.date(user.created_at), inline=True)
        embed.add_field(name="Joined this server", value=default.date(user.joined_at), inline=True)

        embed.add_field(
            name="Roles",
            value=', '.join([f"<@&{x.id}>" for x in user.roles if x is not ctx.guild.default_role]) if len(user.roles) > 1 else 'None',
            inline=False
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, user : discord.Member = None):
        """ Give someone a kiss OwO """
        if user is None:
            user = ctx.author.display_name
            await ctx.send("Bruh, who are you trying to kiss?")
            return
        elif user is ctx.author:
            await ctx.send("Sorry to see you alone ;-;")
            return
        else:
            author = user.display_name
            user = ctx.author.display_name
            await ctx.send(italics("{}".format(author) + " got a kiss from " + "{}".format(user)))
            await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/kiss', 'url')
    
    @commands.command()
    async def hug(self, ctx, user : discord.Member = None):
        """ Give someone a hug UwU """
        if user is None:
            await ctx.send("Bruh, who are you trying to hug?")
            return
        elif user is ctx.author:
            embed = discord.Embed(color=0xFF0000,title="Sorry to see you alone...")
            embed.set_image(url="https://readifgay.com/images/selfhug.gif")
            await ctx.send(embed=embed)
            return
        author = user.display_name
        user = ctx.author.display_name
        await ctx.send(italics("{}".format(author) + " got a hug from " + "{}".format(user)))
        await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/hug', 'url')
    
    @commands.command()
    async def tickle(self, ctx, user : discord.Member = None):
        """ Tickles someone :3"""
        if user is None:
            await ctx.send("Bruh, who are you trying to tickle")
            return
        elif user is ctx.author:
            await ctx.send("So you can manage to tickle yourself huh")
            return
        author = user.display_name
        user = ctx.author.display_name
        await ctx.send(italics("{}".format(author) + " tickled " + "{}".format(user)))
        await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/tickle', 'url')

    @commands.command()
    async def pat(self, ctx, user : discord.Member = None):
        """ Pat someone UwU """
        if user is None:
            await ctx.send("Bruh, who are you trying to pat")
            return
        elif user is ctx.author:
            await ctx.send("***Pats self***")
            return
        author = user.display_name
        user = ctx.author.display_name
        await ctx.send(italics("{}".format(author) + " got a pat from " + "{}".format(user)))
        await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/pat', 'url')

    @commands.command()
    async def giveavatar(self, ctx):
        """ Gives you a avatar to use """
        user = ctx.author.display_name
        await ctx.send(italics("{}".format(user) + ", Here is your avatar"))
        await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/avatar', 'url')

    @commands.command()
    async def cuddle(self, ctx, user : discord.Member = None):
        """ Cuddle with someone OwO """
        if user is None:
            await ctx.send("Bruh, who are you trying to cuddle with")
            return
        elif user is ctx.author:
            embed = discord.Embed(color=0xFF0000 ,title="***Cuddles pillow***")
            embed.set_image(url="https://readifgay.com/images/cuddelingpillow.png")
            await ctx.send(embed=embed)
            return
        author = user.display_name
        user = ctx.author.display_name
        await ctx.send(italics("{}".format(author) + " is cuddling with " + "{}".format(user)))
        await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/cuddle', 'url')

    @commands.command()
    async def neko(self, ctx):
        """ Posts a picture of a neko """
        await self.randomimageapi(ctx,'https://nekos.life/api/v2/img/neko', 'url')

    async def catapi(self, ctx, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except json.JSONDecodeError:
            return await ctx.send("Couldn't find anything from the API")

        url = (r[endpoint])
        embed = discord.Embed(title="cat")
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        """ Posts a random cat """
        await self.catapi(ctx, 'https://nekos.life/api/v2/img/meow', 'url')

    @commands.command()
    async def dog(self, ctx):
        """ Posts a random dog """
        await self.randomimageapi(ctx, 'https://random.dog/woof.json', 'url')
    
def setup(bot):
    bot.add_cog(Misc(bot))