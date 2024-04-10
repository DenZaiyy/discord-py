from discord.ext import commands
from utils.db import DB
from utils.prefix import Prefix
from utils.locale import Locale

class PrefixCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = DB()

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(administrator=True)
    async def prefix(self, ctx: commands.Context, _prefix: str):
        try:
            if not ctx.message.content.startswith(ctx.prefix):
                return

            if ctx.author == self.bot.user:
                return

            guild = ctx.guild

            locale = Locale.get_locale(self, guild.id)
            print(f'locale: {locale}')
            
            if guild is None:
                if locale:
                    if locale == 'ENG':
                        await ctx.reply('This command is only available in a server')
                    elif locale == 'FRA':
                        await ctx.reply('Cette commande n\'est disponible que dans un serveur')
                    elif locale == 'GER':
                        await ctx.reply('Dieser Befehl ist nur in einem Server verfügbar')
                    elif locale == 'SPA':
                        await ctx.reply('Este comando solo está disponible en un servidor')
                else:
                    await ctx.reply('Cette commande n\'est disponible que dans un serveur')
                return

            # valid prefix is a single character
            if len(_prefix) != 1:
                if locale == 'ENG':
                    await ctx.reply('Invalid prefix. Please use a single character')
                elif locale == 'FRA':
                    await ctx.reply('Préfixe invalide. Veuillez utiliser un seul caractère')
                elif locale == 'GER':
                    await ctx.reply('Ungültiges Präfix. Bitte verwenden Sie ein einzelnes Zeichen')
                elif locale == 'SPA':
                    await ctx.reply('Prefijo inválido. Utilice un solo carácter')
                return

            Prefix.set_prefix(self, guild.id, guild.name, _prefix)
            self.bot.command_prefix = _prefix
            
            if locale == 'ENG':
                await ctx.reply(f'Prefix set to `{_prefix}`')
            elif locale == 'FRA':
                await ctx.reply(f'Préfixe défini sur `{_prefix}`')
            elif locale == 'GER':
                await ctx.reply(f'Präfix auf `{_prefix}` gesetzt')
            elif locale == 'SPA':
                await ctx.reply(f'Prefijo establecido en `{_prefix}`')

        except Exception as e:
            print(f'An error occurred with prefix command: {e}')
            
    @prefix.error
    async def prefix_error(self, ctx: commands.Context, error):
        print(f'Prefix command error: {error}')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Please pass in the prefix to set.')

async def setup(bot: commands.Bot):
    await bot.add_cog(PrefixCommand(bot))