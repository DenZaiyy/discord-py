import discord
from discord.ext import commands

class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        print(f'{member} has joined the server "{member.guild}"!')

        # Manage roles for new members joining the server
        roles = member.guild.roles
        for role in roles:
            if role.name == 'Membre' or role.name == 'Member':
                await member.add_roles(role)
                break

        # Manage channels for new members joining the server
        channels = member.guild.channels
        for channel in channels:
            if channel.name == 'bienvenue':
                try:
                    embed = discord.Embed(
                        title=f'Bienvenue {member.name}',
                        description=f'🎉 Bienvenue sur le serveur! On espère que tu te plairas parmi nous 🎉',
                        color=0x00ff00
                    )
                    embed.add_field(name='Règles', value='Merci de lire les règles dans le channel règles', inline=False)
                    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
                    if member.avatar:
                        embed.set_thumbnail(url=member.avatar.url)
                    else:
                        embed.set_thumbnail(url=member.default_avatar.url)

                    if member.guild.icon:
                        embed.set_footer(text=f'Vous êtes le {member.guild.member_count}ème membre', icon_url=member.guild.icon.url)
                    else:
                        embed.set_footer(text=f'Vous êtes le {member.guild.member_count}ème membre')
                    await channel.send(embed=embed)
                except Exception as e:
                    print(f"An error occurred: {e}")
                break
            elif channel.name == 'welcome':
                try:
                    embed = discord.Embed(
                        title=f'Welcome {member.name}',
                        description=f'🎉 Welcome to the server! We hope you will enjoy your time with us 🎉',
                        color=0x00ff00
                    )
                    embed.add_field(name='Rules', value='Please read the rules in the rules channel', inline=False)
                    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
                    if member.avatar:
                        embed.set_thumbnail(url=member.avatar.url)
                    else:
                        embed.set_thumbnail(url=member.default_avatar.url)

                    if member.guild.icon:
                        embed.set_footer(text=f'You are the {member.guild.member_count}th member', icon_url=member.guild.icon.url)
                    else:
                        embed.set_footer(text=f'You are the {member.guild.member_count}th member')
                    await channel.send(embed=embed)
                except Exception as e:
                    print(f"An error occurred: {e}")
                break
        pass

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        print(f'{member} has left the server "{member.guild}"!')
        channels = member.guild.channels
        for channel in channels:
            if channel.name == 'welcome':
                await channel.send(f'**{member}** has left us ! We are more than **{member.guild.member_count} members**')
                break
            elif channel.name == 'bienvenue':
                await channel.send(f'**{member}** nous a quitté ! Nous sommes plus que **{member.guild.member_count} membres**')
                break
        pass

async def setup(bot):
    await bot.add_cog(Members(bot))