import discord
from discord.ext import commands

# Define a Cog for handling commands
class CommandHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # Store a reference to the bot instance

    @commands.command(name='testjoin')
    async def test_join(self, ctx):
        """Command to test the member join event."""
        # Use the command sender as the fake member for testing
        fake_member = ctx.guild.get_member(ctx.author.id)
        event_handler = self.bot.get_cog('EventHandler')
        if event_handler:
            # Trigger the on_member_join event manually
            await event_handler.on_member_join(fake_member)
        else:
            # Notify if the EventHandler Cog is not loaded
            await ctx.send("EventHandler not loaded.")
            
    @commands.command(name='testleave')
    async def test_leave(self, ctx):
        """Command to test the member leave event."""
        # Use the command sender as the fake member for testing
        fake_member = ctx.guild.get_member(ctx.author.id)
        # Get the EventHandler Cog
        event_handler = self.bot.get_cog('EventHandler')
        if event_handler:
            # Trigger the on_member_remove event manually
            await event_handler.on_member_remove(fake_member)
        else:
            # Notify if the EventHandler Cog is not loaded
            await ctx.send("EventHandler not loaded.")

# Function to set up the Cog
async def setup(bot):
    await bot.add_cog(CommandHandler(bot))  # Add this Cog to the bot
