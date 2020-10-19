import discord
import bot_settings
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")

client.run(bot_settings.token)