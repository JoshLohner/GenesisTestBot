import discord
from discord.ext import commands

class CommandHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command(name='testjoin')
    async def test_join(self, ctx):
        """Command to test member join event."""
        fake_member = ctx.guild.get_member(ctx.author.id)  # Use the command sender as the fake member
        event_handler = self.bot.get_cog('EventHandler')
        if event_handler:
            await event_handler.on_member_join(fake_member)
        else:
            await ctx.send("EventHandler not loaded.")
            
    @commands.command(name='testleave')
    async def test_leave(self, ctx):
        """Command to test member leave event."""
        fake_member = ctx.guild.get_member(ctx.author.id)  # Use the command sender as the fake member
        event_handler = self.bot.get_cog('EventHandler')
        if event_handler:
            await event_handler.on_member_remove(fake_member)
        else:
            await ctx.send("EventHandler not loaded.")

async def setup(bot):
    await bot.add_cog(CommandHandler(bot))
