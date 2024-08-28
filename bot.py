import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # Retrieve the bot token from the .env file

# Initialize the bot with intents
intents = discord.Intents.default()  
intents.message_content = True  
intents.guilds = True  
intents.members = True  

# Create a bot instance with the specified command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Load the command and event handlers
async def load_extensions():
    await bot.load_extension('commands')
    await bot.load_extension('events')
    await bot.load_extension('template_slash_commands')

@bot.event
async def on_ready():
    # This event triggers when the bot successfully connects to Discord
    print(f'Bot connected as {bot.user}')
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))  # Replace GUILD_ID with your guild's ID
        print(f'Synced {len(synced)} commands for guild {GUILD_ID}.')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

# Run the bot
async def main():
    async with bot:
        await load_extensions()  # Load all extensions before starting the bot
        await bot.start(TOKEN)  # Start the bot using the token

# Entry point of the program to start the bot
asyncio.run(main())  # Run the main async function to start the bot
