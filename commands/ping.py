from discord.ext import commands
from utils.db import DB
from utils.locale import Locale

class PingCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = DB()

    @commands.command(name='ping', description='Check the bot latency', aliases=['latency'])
    async def ping(self, ctx: commands.Context):
        if not ctx.message.content.startswith(ctx.prefix) or ctx.author == self.bot.user:
            return
        
        # Get locale from the database
        locale = Locale.get_locale(self, ctx.guild.id)
        
        # Check if the command was triggered without args 
        if ctx.message.content != f'{ctx.prefix}{ctx.command.name}' and ctx.message.content != f'{ctx.prefix}{ctx.command.aliases[0]}':
            await ctx.reply('This command does not take any arguments', ephemeral=True)
            return
        
        latence = round(self.bot.latency * 1000)
        if locale == 'ENG':
            await ctx.reply(f'Current latency: {latence}ms')
        elif locale == 'FRA':
            await ctx.reply(f'Latence actuelle : {latence}ms')
        elif locale == 'GER':
            await ctx.reply(f'Aktuelle Latenz: {latence}ms')
        elif locale == 'SPA':
            await ctx.reply(f'Latencia actual: {latence}ms')
        else:
            await ctx.reply(f'Current latency: {latence}ms')

    @ping.error
    async def ping_error(self, ctx: commands.Context, error):
        print(f'Ping command error: {error}')
        await ctx.reply('An error occurred while trying to check the latency', ephemeral=True)

async def setup(bot):
    await bot.add_cog(PingCommand(bot))