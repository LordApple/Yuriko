import traceback
import discord
import aiohttp
import re
import traceback
import os
import random
import datetime
import sys
import json
import platform

from random import choice, randint
from datetime import timedelta
from discord.ext.commands import errors

games = ["How to commit die 101.", "🤔🤔🤔🤔🤔🤔", "nhentai.net", "☭ The Communist Manifesto ☭"]

class Events:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self,message):
        with open("config.json") as f:
            config = json.load(f)
        if not len(config.get("cleverbot")) == 0:
            msg = message.content.split()
            if msg[0] == (f"<@!{self.bot.user.id}>"):
                msg[0] = ""
                msg = "".join(msg)
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://www.cleverbot.com/getreply?key={}&input={}".format(config.get("cleverbot"),msg)) as r:
                        if r.status == 200:
                            js = await r.json()
                            await message.channel.send(js["output"])

    async def on_ready(self):
        print('Logged in as ' + self.bot.user.name + "  ID: " + (str(self.bot.user.id)))
        print('--------')
        print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
        print('--------')
        print('Use this link to invite {}:'.format(self.bot.user.name))
        print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(self.bot.user.id))
        print('--------')
        print('Created by Apple#1337')

        self.bot.invite_url = discord.utils.oauth_url(self.bot.user.id)
        game = discord.Activity(type=1,name=random.choice(games),url="https://www.twitch.tv/twitchbot_discord/")
        await self.bot.change_presence(status=discord.Status.dnd, activity=game)
    

    async def on_command_error(self, ctx, exception):
        if isinstance(exception, errors.MissingRequiredArgument):
            command = ctx.invoked_subcommand or ctx.command
            _help = await ctx.bot.formatter.format_help_for(ctx, command)

            for page in _help:
                await ctx.send(page)

        elif isinstance(exception, errors.CommandInvokeError):
            exception = exception.original
            _traceback = traceback.format_tb(exception.__traceback__)
            _traceback = ''.join(_traceback)

            error = ('`{0}` in command `{1}`: ```py\nTraceback (most recent call last):\n{2}{0}: {3}\n```')\
                .format(type(exception).__name__, ctx.command.qualified_name, _traceback, exception)

            await ctx.send(error)

        elif isinstance(exception, errors.CommandOnCooldown):
            await ctx.send('You can use this command in {0:.0f} seconds.'.format(exception.retry_after))

        else:
            print(exception)

def setup(bot):
    bot.add_cog(Events(bot))
