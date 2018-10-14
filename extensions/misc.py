import discord
import time
import random

from discord.ext import commands
from random import randint
from random import choice
from extensions.tools.chat_formatting import italics, bold, strikethrough, pagify

class Misc:
    def __init__(self, bot,):
        self.bot = bot

        self.ball = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                    "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                    "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                    "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    @commands.command(pass_context=True, no_pm=True)
    async def avatar(self, ctx, member: discord.Member):
        """User Avatar"""
        await ctx.send(" {}".format(member.avatar_url))

    @commands.command(pass_context=True)
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
            await ctx.send("`" + choice(self.ball) + "`")
        else:
            await ctx.send("That doesn't look like a question.")
    
    @commands.command()
    async def guildcount(self, ctx):
        """Bot Guild Count"""
        servers = bold (len((self.bot.guilds)))
        await ctx.send("I'm in " + servers + " Guilds!")
        #await ctx.send(" ** I'm in {} Guilds!**".format(len(self.bot.guilds)))
    
    @commands.command(pass_context=True, no_pm=True)
    async def guildicon(self, ctx):
        """Guild Icon"""
        await ctx.send(" {}".format(ctx.message.guild.icon_url))

    @commands.command(no_pm=True)
    async def hug(self, ctx, user : discord.Member, intensity : int=1):
        """Because everyone likes hugs

        Up to 10 intensity levels."""
        name = italics(user.display_name)
        if intensity <= 0:
            msg = "(っ˘̩╭╮˘̩)っ" + name
        elif intensity <= 3:
            msg = "(っ´▽｀)っ" + name
        elif intensity <= 6:
            msg = "╰(*´︶`*)╯" + name
        elif intensity <= 9:
            msg = "(つ≧▽≦)つ" + name
        elif intensity >= 10:
            msg = "(づ￣ ³￣)づ{} ⊂(´・ω・｀⊂)".format(name)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def ping(self,ctx):
        """ping time"""
        t1 = time.perf_counter()
        await ctx.send("Pong :ping_pong:")
        t2 = time.perf_counter()
        await ctx.send("ping: {}ms".format(round((t2-t1)*1000)))

    @commands.command(pass_context=True)
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
            dongs[user] = "8{}D".format("=" * random.randint(0, 30))

        random.setstate(state)
        dongs = sorted(dongs.items(), key=lambda x: x[1])

        for user, dong in dongs:
            msg += "**{}'s size:**\n{}\n".format(user.display_name, dong)

        for page in pagify(msg):
            await ctx.send(page)

    @commands.command()
    async def cat(self, ctx):
        """ Posts a random cat """
        await ctx.randomimageapi(ctx, 'https://nekos.life/api/v2/img/meow', 'url')



def setup(bot):
    bot.add_cog(Misc(bot))