import discord
import re
from discord.ext import commands

TOKEN = 'YOUR_BOT_TOKEN'
GUILD_ID = 713095073939587113  # Replace with your Guild (Server) ID
CHANNEL_ID = 713095287568203877  # Replace with your Channel ID
WORD_TO_CHECK = 'distroyed'  # Replace with the word you want to check for

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.guild.id == GUILD_ID and message.channel.id == CHANNEL_ID:
        if WORD_TO_CHECK in message.content:
            # Extract timestamp and mapname
            pattern = r"\[(?P<timestamp>[^\]]+)\]\[(?P<mapname>[^\]]+)\]"
            match = re.search(pattern, message.content)
            if match:
                timestamp = match.group('timestamp')
                mapname = match.group('mapname')
                await message.channel.send(f"@everyone !!!Alarm!!! {mapname} at {timestamp}!")
            else:
                await message.channel.send("@everyone Alarm!")

    await bot.process_commands(message)

bot.run(TOKEN)


# https://discord.com/api/oauth2/authorize?client_id=1121170350982582272&permissions=8&scope=bot
