from discord.ext import commands
from utils.db import DB
from utils.locale import Locale

class LocaleCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.db = DB()

    @commands.command(name='locale', aliases=['lang', 'language'])
    @commands.has_permissions(administrator=True)
    @commands.bot_has_permissions(administrator=True)
    async def locale(self, ctx: commands.Context, locale: str = commands.parameter(description=f'Available locales: ENG, FRA, GER, SPA')):
        try:
            if not ctx.message.content.startswith(ctx.prefix):
                return
            
            if ctx.author == self.bot.user:
                return
            
            guild = ctx.guild
            if guild is None:
                await ctx.reply('This command is only available in a server')
                return
            
            locales = Locale.get_available_locales(self)
            
            if locale not in locales:
                await ctx.reply(f'Invalid locale.\nPlease use available locale: {locales}')
                return
            
            # Save the locale in the database
            Locale.set_locale(self, guild.id, guild.name, locale)
            
            # Get current lang if i don't pass args
            if ctx.message.content == f'{ctx.prefix}{ctx.command.name}':
                current_locale = Locale.get_locale(self, ctx.guild.id)
                if current_locale == 'ENG':
                    await ctx.reply(f'Current language: {current_locale}')
                elif current_locale == 'FRA':
                    await ctx.reply(f'Langue actuelle : {current_locale}')
                elif current_locale == 'GER':
                    await ctx.reply(f'Aktuelle Sprache: {current_locale}')
                elif current_locale == 'SPA':
                    await ctx.reply(f'Idioma actual: {current_locale}')
                return

            if locale == 'ENG':
                await ctx.reply(f'Language set to {locale} !')
            elif locale == 'FRA':
                await ctx.reply(f'Langue défini sur {locale} !')
            elif locale == 'GER':
                await ctx.reply(f'Sprache auf {locale} gesetzt !')
            elif locale == 'SPA':
                await ctx.reply(f'Idioma establecido en {locale} !')
            
        except Exception as e:
            print(f'An error occurred with locale command: {e}')

    @locale.error
    async def locale_error(self, ctx: commands.Context, error):
        print(f'Locale command error: {error}')
        if isinstance(error, commands.MissingRequiredArgument):
            locales = Locale.get_available_locales(self)
            await ctx.reply(f'Please pass in the locale to set.\nAvailable locales: {locales}')
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply('I do not have the required permissions to set the locale', ephemeral=True)
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply('You do not have the required permissions to set the locale', ephemeral=True)

async def setup(bot):
    await bot.add_cog(LocaleCommand(bot))