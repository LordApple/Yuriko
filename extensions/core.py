import discord
from discord.ext import commands


class Core:
    def __init__(self, bot):
        self.bot = bot       

    @commands.command()
    async def invite(self, ctx):
        e = discord.Embed(title="Click to invite.", url="https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8".format(self.bot.user.id))
        await ctx.send(embed=e)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, name: str):
        """ Reloads an extension in the bot """
        m = await ctx.send(f'Loading {name}')
        try:
            self.bot.unload_extension(f'extensions.{name}')
            self.bot.load_extension(f'extensions.{name}')
            await m.edit(content='Extension reloaded.')
        except (ImportError, SyntaxError, discord.ClientException) as e:
            stack_line = str(e).split('\n')[-1]
            await m.edit(content=f'Error while loading {name}\n`{stack_line}`')

    @commands.command()
    async def unload(self, ctx, name: str):
        """Unloads an extension in the bot"""
        m = await ctx.send(f'unloading {name}')
        try:
            self.bot.unload_extension(f'extensions.{name}')
            await m.edit(content='Extension unloaded.')
        except:
            return

    @commands.command()
    async def load(self, ctx, name: str):
        """Loads an extension in the bot"""
        m = await ctx.send(f"loading {name}")
        try:
            self.bot.load_extension(f'extensions.{name}')
            await m.edit(content="Extension loaded.")
        except:
            return

def setup(bot):
    bot.add_cog(Core(bot))
