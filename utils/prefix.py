from utils.db import DB
import os

class Prefix:
    def __init__(self, prefix: str = os.getenv('DEFAULT_PREFIX')) -> None:
        self.prefix = prefix
        self.db = DB()

    def set_prefix(self, guild_id: int, name: str, prefix: str) -> None:
        try:
            # Check if guild exists in the database
            guild_row = self.db.query(q='SELECT * FROM guilds WHERE guild_id = %s', params=(guild_id,), fetchone=True)

            if guild_row is None:
                # Insert guild into the database
                self.db.query(q='INSERT INTO guilds (guild_id, name, prefix) VALUES (%s, %s, %s)', params=(guild_id, name, prefix))
            else:
                # Update guild prefix
                self.db.query(q='UPDATE guilds SET prefix = %s WHERE guild_id = %s', params=(prefix, guild_id))
            
            self.db.commit()

        except Exception as e:
            print(f"An error occurred while tried to set prefix: {e}")
            raise e
        
    def get_prefix(self, guild_id: int) -> str:
        try:
            # Check if guild exists in the database
            guild_row = self.db.query(q='SELECT prefix FROM guilds WHERE guild_id = %s', params=(guild_id,), fetchone=True)

            if guild_row is None:
                return self.prefix
            else:
                return guild_row[0]

        except Exception as e:
            print(f"An error occurred while tried to get prefix: {e}")
            raise e