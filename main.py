from typing import Final
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import logging

# Load the environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
PREFIX: Final[str] = os.getenv('DISCORD_PREFIX')

# Setup the client
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot.activity = discord.Game(name='!help to more infos')

# Setup logs
handler = logging.FileHandler(filename='logs.log', encoding='utf-8', mode='w')

# Event to load all commands available in commands folder
@bot.event
async def on_ready() -> None:
    # Load all commands in the commands folder
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')
            print(f'Loaded command: {filename[:-3]}')

    # Load all events in the events folder
    for filename in os.listdir('./events'):
        if filename.endswith('.py'):
            await bot.load_extension(f'events.{filename[:-3]}')
            print(f'Loaded event: {filename[:-3]}')

    # Print bot name when connected
    print(f'🤖 {bot.user.name} has connected (with prefix: {PREFIX})! 🤖')

# main entry point
def main() -> None:
    bot.run(token=TOKEN, log_handler=handler, log_level=logging.DEBUG)

if __name__ == '__main__':
    main()