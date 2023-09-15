import discord
from discord.ext import commands

TOKEN = 'MTEyMTE3MDM1MDk4MjU4MjI3Mg.GYVbZx.ilARGIxseyVJUmhjqOWy0j5Huc94OtMOa9-O-k'
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
            await message.channel.send("@everyone Attention - Alert!")

    await bot.process_commands(message)

bot.run(TOKEN)


# https://discord.com/api/oauth2/authorize?client_id=1121170350982582272&permissions=8&scope=bot