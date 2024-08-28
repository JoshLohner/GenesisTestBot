import discord
from discord import app_commands
from discord.ext import commands

# Define your guild ID here
GUILD_ID = 123456789012345678  # Replace with your actual guild ID

# Define a Cog for handling slash commands
class SlashCommandHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Sends a greeting message.")
    @app_commands.guilds(discord.Object(id=GUILD_ID))  # Use the defined guild ID
    async def hello(self, interaction: discord.Interaction):
        # Reply with "Hello, world!" when the command is invoked
        await interaction.response.send_message("Hello, world!")

# Function to set up the Cog
async def setup(bot):
    await bot.add_cog(SlashCommandHandler(bot))  # Add this Cog to the bot
