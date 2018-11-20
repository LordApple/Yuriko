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
    async def smessage(self, ctx, spamamt, user : discord.Member, *, message):
        author = ctx.message.author.display_name
        if ctx.author.id in config_forwarder.owners:
            spamamt = int(spamamt)
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
    async def mbomb(self, ctx):
            msg = 'wow, this is a dead chat... lets fix that.\n'
            for member in ctx.guild.members:
                msg += '\n<@' + str(member.id) + '>'
            await ctx.send(msg)
    
    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    """
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
                """
    
    @commands.command()
    @commands.is_owner()
    async def setgame(self, ctx, gtype, *, game):
            try:
                game = discord.Activity(type=gtype,name=game, url="https://www.twitch.tv/twitchbot_discord/")
                await self.bot.change_presence(status=discord.Status.dnd, activity=game)
            except:
                await ctx.send("Failed to change game")
            else:
                await ctx.send("Done")

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

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def rall(self,ctx,*,name):
        for member in ctx.guild.members:
            if member.top_role.position < ctx.guild.me.top_role.position:
                try:
                    await member.edit(nick=name)
                    print(f'Member {member} has been renamed to {name}')
                    time.sleep(0.45)
                except:
                    continue

    @commands.command()
    async def test(self, ctx):
        await ctx.send(f"Epic, my top role is {ctx.guild.me.top_role.position}")

    @commands.command()
    async def guilds(self, ctx):
        """Lists all bot servers"""
        if ctx.author.id in config_forwarder.owners:
            msg = ''
            for server in self.bot.guilds:
                msg = msg + '\n' + str(server)
            msg = msg + '\n'
            embed = discord.Embed(color=0x3ef301,title="Im in {}".format(len(self.bot.guilds)) + " guilds")
            embed.add_field(name="Server list", value=msg)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="This command is for the bot owners only.", color=0xFF0000)
            await ctx.send(embed=embed)
            print("User " + author + " tried to use the guilds command.")

    @commands.command()
    @commands.is_owner()
    async def invites(self,ctx):
        """Creates a invite for the current discord channel"""
        invite = await ctx.guild.invites()
        print("Invites: {0}".format(", ".join(map(str, invite))))

    @commands.command(hidden=True)
    @commands.is_owner()
    async def cinv(self, ctx, channelname, *, guildname):
        """Creates a invite for the current discord channel"""
        a = self.bot.guilds
        for i in a:
            if i.name == guildname:
                for b in i.channels:
                    if b.name == channelname:
                        return print(await b.create_invite())

    @commands.command(hidden=True)
    @commands.is_owner()
    async def createguild(self,ctx,*,name):
        await self.bot.create_guild(name=name)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def createrole(self,ctx,permsid,*,rolename):
        perms = discord.Permissions(permissions=int(permsid))
        await ctx.guild.create_role(name=rolename, permissions=perms)
        print(f"The role '{rolename}' has been created in {ctx.guild.name}")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def giverole(self,ctx,*,rolename):
        member = ctx.author
        message = []
        for role in ctx.guild.roles:
            if role.name == str(rolename):
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except IndexError:
            return await ctx.send(f"Are you sure you've made a role called **{rolename}**?")

        try:
            await member.add_roles(therole)
        except Exception as e:
            await ctx.send(e)



    @commands.command(hidden=True)
    async def get_invite(self, ctx, *, server: str = None):
        print(str(ctx.message.author.id) + " " + ctx.message.author.name + ": " + ctx.message.content)
        if ctx.author.id not in config_forwarder.owners:
            return await ctx.send("An error occurred, or you are not permitted to use this command!")
        else:
            b = self.bot.guilds
            if server != "current":
                for i in b:
                    if i.name == server:
                        b = i
                        break
                if type(b) == str:
                    return await ctx.send("No server found")
            else:
                b = ctx.guild
            try:
                a = b.audit_logs()
                c = None
                async for i in a:
                    if i.action == discord.AuditLogAction.invite_create:
                        try:
                            c = await self.bot.get_invite(i.target)
                            return await ctx.send(i.target)
                        except Exception as e:
                            print(e)
            except discord.Forbidden as e:
                print(e)
                return await ctx.send("Invalid permissions!")
            await ctx.send("No valid invites found!")

def setup(bot):
    bot.add_cog(Owner(bot))