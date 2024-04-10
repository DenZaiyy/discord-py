from discord.ext import commands
from utils.db import DB
from utils.locale import Locale

class HelloCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = DB()

    @commands.command(description='Say hello to user calling the command')
    async def hello(self, ctx: commands.Context):
        try:
            if not ctx.message.content.startswith(ctx.prefix):
                return
            
            if ctx.author == self.bot.user:
                return
            
            locale = Locale.get_locale(self, ctx.guild.id)
            
            if locale == 'ENG':
                await ctx.reply(f'Hello {ctx.author.mention} :wave: !')
            elif locale == 'FRA':
                await ctx.reply(f'Bonjour {ctx.author.mention} :wave: !')
            elif locale == 'GER':
                await ctx.reply(f'Hallo {ctx.author.mention} :wave: !')
            elif locale == 'SPA':
                await ctx.reply(f'Hola {ctx.author.mention} :wave: !')
            else:
                await ctx.reply(f'Hello {ctx.author.mention} :wave: !')
        except Exception as e:
            print(f'An error occurred with hello command: {e}')

async def setup(bot):
    await bot.add_cog(HelloCommand(bot))