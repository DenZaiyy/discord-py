import discord
from discord.ext import commands

class Messages(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        try:
            if message.author == self.bot.user:
                return

            # Print message details
            username = str(message.author)
            user_message = message.content
            channel = str(message.channel)
            guild = str(message.guild)

            # Check command prefix
            # ctx = await self.bot.get_context(message)
            # prefix = ctx.prefix
            prefix = await self.bot.get_prefix(message)
            # print(f'prefix: {prefix}')

            if not user_message.startswith(prefix):
                print(f'[{guild} - {channel}] {username}: "{user_message}"')
                return
            else:
                # Split message content into command and arguments
                command_content = user_message[len(prefix):].strip() # Remove prefix and leading/trailing whitespaces
                parts = command_content.split(maxsplit=1) # Split into command name and arguments
                command_name = parts[0] # Command name is the first part
                args = parts[1].split() if len(parts) > 1 else [] # Arguments are the second part, split into a list

                # Check if command exists and is valid
                command: commands.Command = self.bot.get_command(command_name)

                if command is not None and not command.hidden:
                    # check if command need args and if args are passed
                    if command.clean_params and not args:
                        await message.reply(f'Command **"{command_name}"** requires arguments. Please provide them.')
                        return

                    print(f'{username} triggered command "{command_name}" in channel "{channel}" on server "{guild}"')
                else:
                    await message.reply(f'Command **"{command_name}"** not found or you do not have permission to use it.')
                    return
        except Exception as e:
            print(f'An error occurred with on_message event: {e}') 

async def setup(bot):
    await bot.add_cog(Messages(bot))
