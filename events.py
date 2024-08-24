import discord
from discord.ext import commands
from PIL import Image, ImageOps, ImageDraw, ImageFont
import requests
from io import BytesIO

# Define a Cog for handling events
class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # Store a reference to the bot instance

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Find the general channel or use a specific channel by ID
        channel = discord.utils.get(member.guild.text_channels, name='general')  # Get the 'general' text channel
        specific_channel = member.guild.get_channel(762144356156964865)  # Get a specific channel by its ID

        if channel:
            # Send a welcome message in the general channel
            await channel.send(
                f"""Welcome to Genesis, {member.mention}! If you are interested in joining the guild, fill out the application: https://forms.gle/9PVuV6p9PvZYwtUMA \nChannels and role selection are above in {specific_channel.mention}. If you are not interested in joining the guild for now, select the Friend of the Guild role or the Guild Ambassador role if you are in another guild! We are now at {member.guild.member_count} members!"""
            )

            # Get the member's avatar URL
            avatar_url = member.avatar.url if member.avatar else member.default_avatar.url

            # Open the guild logo image
            logo = Image.open('assets/new_gen_logo.png')

            # Download the member's avatar
            response = requests.get(avatar_url)
            avatar = Image.open(BytesIO(response.content))

            # Resize the avatar to fit on the logo
            avatar_size = (200, 200)  # Adjust the size as needed
            avatar = avatar.resize(avatar_size)

            # Make the avatar circular
            mask = Image.new("L", avatar_size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + avatar_size, fill=255)
            avatar = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
            avatar.putalpha(mask)  # Apply the circular mask to the avatar

            # Calculate the position to center the avatar on the logo
            avatar_position = ((logo.width - avatar.width) // 2, (logo.height - avatar.height) // 2)

            # Paste the avatar onto the logo
            logo.paste(avatar, avatar_position, avatar)

            # Draw text on the image inside a try-except block
            try:
                draw = ImageDraw.Draw(logo)
                
                # Use a bold and larger Arial font
                font = ImageFont.truetype("assets/Arial.ttf", 50)  # Adjust the font size as needed
                
                # Prepare the text
                welcome_text = "Welcome to Genesis"
                username_text = f"{member.name}"

                # Calculate the bounding box of the text to center it
                welcome_text_bbox = draw.textbbox((0, 0), welcome_text, font=font)
                username_text_bbox = draw.textbbox((0, 0), username_text, font=font)

                # Calculate text width and height from the bounding box
                welcome_text_width = welcome_text_bbox[2] - welcome_text_bbox[0]
                welcome_text_height = welcome_text_bbox[3] - welcome_text_bbox[1]
                username_text_width = username_text_bbox[2] - username_text_bbox[0]
                username_text_height = username_text_bbox[3] - username_text_bbox[1]

                # Calculate positions to center the text below the avatar
                welcome_position = ((logo.width - welcome_text_width) // 2, avatar_position[1] + avatar_size[1] + 10)
                username_position = ((logo.width - username_text_width) // 2, welcome_position[1] + welcome_text_height + 10)

                # Draw the text onto the image
                draw.text(welcome_position, welcome_text, font=font, fill="white")
                draw.text(username_position, username_text, font=font, fill="white")

            except Exception as e:
                print(f"Error while adding text: {e}")  # Log any text rendering errors

            # Save the combined image to a BytesIO object
            combined_image = BytesIO()
            logo.save(combined_image, format='PNG')
            combined_image.seek(0)

            # Send the combined image in the channel
            await channel.send(file=discord.File(fp=combined_image, filename='welcome_image.png'))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # Find the general channel to send a departure message
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            total_members = member.guild.member_count  # Get the current member count
            await channel.send(f'{member.mention} {member.name} has left Genesis! We are now at {total_members} members!')

# Function to set up the Cog
async def setup(bot):
    await bot.add_cog(EventHandler(bot))  # Add this Cog to the bot
