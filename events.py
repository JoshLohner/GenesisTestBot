import discord
from discord.ext import commands

class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            await channel.send(f'Welcome to the server, {member.mention}!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            await channel.send(f'{member.name} has left the server.')

    @commands.command(name='testjoin')
    async def test_join(self, ctx):
        """Command to test member join event."""
        fake_member = ctx.guild.get_member(ctx.author.id)  # Use the command sender as the fake member
        await self.on_member_join(fake_member)

async def setup(bot):
    await bot.add_cog(EventHandler(bot))
