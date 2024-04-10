from typing import Final
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import logging

# Load the environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
PREFIX: Final[str] = os.getenv('DEFAULT_PREFIX')

# Setup the client
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot.activity = discord.Game(name=f'{PREFIX}help')

# Setup logs
handler = logging.FileHandler(filename='logs.log', encoding='utf-8', mode='w')

async def load_commands():
    try:
        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                await bot.load_extension(f'commands.{filename[:-3]}')
                print(f'Loaded command: {filename[:-3]}')
    except Exception as e:
        print(f'An error occurred while loading commands: {e}')

async def load_events():
    try:
        for filename in os.listdir('./events'):
            if filename.endswith('.py'):
                await bot.load_extension(f'events.{filename[:-3]}')
                print(f'Loaded event: {filename[:-3]}')
    except Exception as e:
        print(f'An error occurred while loading events: {e}')

@bot.event
async def on_ready() -> None:
    try:
        await load_commands()
        await load_events()

        print(f'🤖 {bot.user.name} has connected! 🤖')
    except Exception as e:
        print(f'An error occurred with on_ready event: {e}')

# main entry point
def main() -> None:
    bot.run(token=TOKEN, log_handler=handler, log_level=logging.DEBUG)

if __name__ == '__main__':
    main()