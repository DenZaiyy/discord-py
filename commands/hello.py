from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context):
        try:
            if not ctx.message.content.startswith(ctx.prefix):
                return
            
            if ctx.author == self.bot.user:
                return
            
            await ctx.reply(f'Hello {ctx.author.mention} !')
        except Exception as e:
            print(f'An error occurred with hello command: {e}')

async def setup(bot):
    await bot.add_cog(Hello(bot))