# Bot created follwing tutorial by Lucas on YouTube https://www.youtube.com/channel/UCR-zOCvDCayyYy1flR5qaAg

import discord
import os
import random
import bot_settings #local file .gitignore'd as it contains the bot token
from discord.ext import commands

client = commands.Bot(command_prefix='!')

# Events
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with the API"))
    print(f"We have logged in as {client.user}")

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")

# Commands
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency*1000)}ms")

@client.command(aliases=['8ball','eightball'])
async def eight_ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(random.choice(responses))

@client.command()
async def clear(ctx, amount=-1):
    amount = round(amount) + 1
    if amount <= 0:
        await ctx.send("Please specify how many messages to clear.")
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Cleared {amount-1} messages.")

@client.command()
async def kick(ctx, user : discord.Member, reason=None):
    await user.kick(reason=reason)
    await ctx.send(f"Kicked {user.mention}")

@client.command()
async def ban(ctx, user : discord.Member, reason=None):
    await user.ban(reason=reason)
    await ctx.send(f"Banned {user.mention}")

@client.command()
async def unban(ctx, *, user):
    banned_users = await ctx.guild.bans()
    user_name, user_discriminator = user.split('#')
    for ban_entry in banned_users:
        if (ban_entry.user.name, ban_entry.user.discriminator) == (user_name, user_discriminator):
            await ctx.guild.unban(ban_entry.user)
            await ctx.send(f"Unbanned {ban_entry.user.mention}")
            return

# Cog stuff
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(bot_settings.token)