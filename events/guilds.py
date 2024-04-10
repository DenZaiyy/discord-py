import discord
from discord.ext import commands
from utils.db import DB

class Guilds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DB()

    def save_guild(self, guild_id: int, name: str) -> None:
        try:
            # Check if guild exists in the database
            guild_row = self.db.query('SELECT * FROM guilds WHERE guild_id = %s', (guild_id,), fetchone=True)

            if guild_row is None:
                # Insert guild into the database
                self.db.query('INSERT INTO guilds (guild_id, name) VALUES (%s, %s)', (guild_id, name))
            else:
                # Update guild name
                self.db.query('UPDATE guilds SET name = %s WHERE guild_id = %s', (name, guild_id))
            
            self.db.commit()

        except Exception as e:
            print(f"An error occurred while tried to save guild: {e}")
            raise e
        
    def remove_guild(self, guild_id: int) -> None:
        try:
            # Check if guild exists in the database
            guild_row = self.db.query('SELECT * FROM guilds WHERE guild_id = %s', (guild_id,), fetchone=True)

            if guild_row is not None:
                # Remove guild from the database
                self.db.query('DELETE FROM guilds WHERE guild_id = %s', (guild_id,))
            
            self.db.commit()

        except Exception as e:
            print(f"An error occurred while tried to remove guild: {e}")
            raise e

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        try:
            self.save_guild(guild.id, guild.name)
            print(f'Joined guild "{guild}"!')
        except Exception as e:
            print(f'An error occurred with guild join: {e}')

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        try:
            self.remove_guild(guild.id)
            print(f'Removed from guild "{guild}"!')
        except Exception as e:
            print(f'An error occurred with guild remove: {e}')

async def setup(bot):
    await bot.add_cog(Guilds(bot))