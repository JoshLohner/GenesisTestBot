import discord
from discord.ext import commands

class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Find the general channel or use a specific channel by ID
        channel = discord.utils.get(member.guild.text_channels, name='general')
        specific_channel = member.guild.get_channel(762144356156964865)
        
        if channel:
            # Send a welcome message with an image
            
            await channel.send(
                f"""Welcome to Genesis, {member.mention}! If you are interested in joining the guild, fill out the application: https://forms.gle/9PVuV6p9PvZYwtUMA \nChannels and role selection are above in {specific_channel.mention}. If you are not interested in joining the guild for now, select the Friend of the Guild role or the Guild Ambassador role if you are in another guild! We are now at {member.guild.member_count} members!"""
            )

            #Send Logo
            await channel.send(file=discord.File('assets/new_gen_logo.png'))
            # Get the member's profile picture
            avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
            # Send the member's profile picture
            await channel.send(avatar_url)


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            total_members = member.guild.member_count
            await channel.send(f'{member.mention} {member.name} has left Genesis! We are now at {total_members} members! ')

async def setup(bot):
    await bot.add_cog(EventHandler(bot))
