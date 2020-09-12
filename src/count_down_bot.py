"""
count_down_bot.py

Uses Discord's Text-to-Speech to count down from 3 to 0
"""
import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(str(client.user) + " has connected to Discord.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    countdown_messages = [
        "!countdown",
        "!cd",
        "!count"
    ]
    if message.content.lower() in countdown_messages:
        await message.channel.send("3\n2\n1\nGo", tts=True)
    elif message.content.lower() == "!helicopter":
        tts_msg = "Can you guys hear that helicopter?\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        await message.channel.send(tts_msg, tts=True)

client.run(TOKEN)