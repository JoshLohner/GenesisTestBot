import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize the bot with intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True  # Required to track member join/leave events

bot = commands.Bot(command_prefix='!', intents=intents)

# Load the command and event handlers
async def load_extensions():
    await bot.load_extension('commands')
    await bot.load_extension('events')

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

# Run the bot
async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())
