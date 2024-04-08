from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='ping', description='Check the bot latency', usage='!ping')
    async def ping(self, ctx: commands.Context):
        if not ctx.message.content.startswith(ctx.prefix) or ctx.author == self.bot.user:
            return
        
        # Check if the command was triggered without args
        if ctx.message.content != f'{ctx.prefix}ping':
            await ctx.reply('This command does not take any arguments', ephemeral=True)
            return
        
        latence = round(self.bot.latency * 1000)
        await ctx.reply(f'Current latency: {latence}ms')

    @ping.error
    async def ping_error(self, ctx: commands.Context, error):
        print(f'Ping command error: {error}')
        await ctx.reply('An error occurred while trying to check the latency', ephemeral=True)

async def setup(bot):
    await bot.add_cog(Ping(bot))