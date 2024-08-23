import discord
from discord.ext import commands

class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            total_members = member.guild.member_count
            await channel.send(f"""Welcome to Genesis, {member.mention}! If you are interested in joining the guild, fill out the application: https://forms.gle/9PVuV6p9PvZYwtUMA \nChannels and role selection are above in PLACEHOLDER. If you are not interested in joining the guild for now, select the Friend of the Guild role or the Guild Ambassador role if you are in another guild! We are now at {total_members} members!""")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            total_members = member.guild.member_count
            await channel.send(f'{member.mention} {member.name} has left Genesis! We are now at {total_members} members! ')

async def setup(bot):
    await bot.add_cog(EventHandler(bot))
