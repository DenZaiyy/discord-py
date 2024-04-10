from discord.ext import commands
from typing import Union

class ClearCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description='Clear messages from the channel', usage='!clear <amount>', aliases=['purge', 'c'])
    @commands.has_permissions(manage_messages=True, administrator=True)
    @commands.bot_has_permissions(manage_messages=True, administrator=True)
    async def clear(self, ctx: commands.Context, amount: Union[int, str]):
        if isinstance(amount, int):
            if amount > 100:
                await ctx.reply('You can only delete up to 100 messages at a time', ephemeral=True)
                return
            
            print(f'Clearing {amount} messages from {ctx.channel.name} ({ctx.guild.name}) by {ctx.author}')

            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f'{amount} messages cleared by {ctx.author.mention}')
        elif isinstance(amount, str):
            if amount.lower() == 'all' or amount.lower() == 'a':
                await ctx.channel.purge()
                await ctx.send(f'All messages cleared by {ctx.author.mention}')
            else:
                await ctx.reply('Please pass in "all" or "a" or an integer amount to clear messages', ephemeral=True)

    @clear.error
    async def clear_error(self, ctx: commands.Context, error):
        print(f'Clear command error: {error}')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Please pass in the amount of messages to delete')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply('I do not have the required permissions to delete messages')
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply('You do not have the required permissions to delete messages')

async def setup(bot):
    await bot.add_cog(ClearCommand(bot))