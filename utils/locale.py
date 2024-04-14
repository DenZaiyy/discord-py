from utils.db import DB

class Locale:
    def __init__(self, bot, locale: str = "FRA"):
        self.bot = bot
        self.locale = locale
        self.db = DB()
        pass
    
    def get_available_locales(self) -> list:
        try:
            locales = self.db.query(q='SELECT label FROM locales', fetchall=True)
            return ', '.join([locale[0] for locale in locales])
        
        except Exception as e:
            print(f"An error occurred while tried to get available locales: {e}")
            raise e

    def set_locale(self, guild_id: int, name: str, locale: str) -> None:
        try:
            # Check if locale exists in the database from the label and get the locale_id
            locale_row = self.db.query(q='SELECT id FROM locales WHERE label = %s', params=(locale,), fetchone=True)
            locale_id = locale_row[0] if locale_row is not None else None
            
            if locale_row is None:
                self.db.query(q='INSERT INTO locales (label) VALUES (%s)', params=(locale,))
                self.db.commit()
                locale_id = self.db.lastrowid()
            
            # Check if guild exists in the database
            guild_row = self.db.query(q='SELECT * FROM guilds WHERE guild_id = %s', params=(guild_id,), fetchone=True)

            if guild_row is None:
                # Insert guild into the database
                self.db.query(q='INSERT INTO guilds (guild_id, name, locale) VALUES (%s, %s, %s)', params=(guild_id, name, locale_id))
            else:
                # Update guild locale
                self.db.query(q='UPDATE guilds SET locale = %s WHERE guild_id = %s', params=(locale_id, guild_id))
            
            self.db.commit()

        except Exception as e:
            print(f"An error occurred while tried to set locale: {e}")
            raise e
        
    def get_locale(self, guild_id: int) -> None:
        try:
            # Check if guild exists in the database
            guild_locale = self.db.query('SELECT locale FROM guilds WHERE guild_id = %s', (guild_id,), fetchone=True)
            
            # check if guild_locale found in the database
            if guild_locale[0] is None:
                # Set the default locale
                print(f'locale: {self.locale}')
                return self.locale
            else:
                # Get the locale label from the locale_id
                locale_row = self.db.query('SELECT label FROM locales WHERE id = %s', (guild_locale[0],), fetchone=True)
                return locale_row[0]

        except Exception as e:
            print(f"An error occurred while tried to get locale: {e}")