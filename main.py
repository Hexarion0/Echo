import os
import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[%(levelname)s] %(name)s: %(message)s'))
logging.getLogger('discord').addHandler(handler)
logging.getLogger('discord').setLevel(logging.INFO)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def load_commands():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"commands.{filename[:-3]}")

async def main():
    async with bot:
        await load_commands()
        await bot.start(token)

asyncio.run(main())