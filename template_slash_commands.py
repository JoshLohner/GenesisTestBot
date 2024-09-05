import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

GUILD_ID = os.getenv('GUILD_ID')

# Define a Cog for handling slash commands
class SlashCommandHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Sends a greeting message.")
    @app_commands.guilds(discord.Object(id=GUILD_ID))  # Use the defined guild ID
    async def hello(self, interaction: discord.Interaction):
        print("test")
        
        await interaction.response.send_message("Hello, world!", ephemeral=True)
        
  
    @app_commands.command(name="viewcurrenttemplates", description="View all current templates.")
    @app_commands.guilds(discord.Object(id=GUILD_ID))  # Use the defined guild ID
    async def viewCurrentTemplates(self, interaction: discord.Interaction):
        await interaction.response.send_message("Here are the current templates:", ephemeral=True)
        
        
    
    
async def setup(bot):
    await bot.add_cog(SlashCommandHandler(bot))  # Add this Cog to the bot
