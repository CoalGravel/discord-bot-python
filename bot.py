import discord
import random
import bot_settings #local file .gitignore'd as it contains the bot token
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")

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
async def roll(ctx, dice):
    quantity = dice.split('d')[0]
    size = dice.split('d')[1]
    result = []
    for i in range(int(quantity)):
        result.append(random.randrange(int(size)) + 1)
    await ctx.send(f"Result: {quantity}d{size} {result}\nTotal: {sum(result)}")

@client.command()
async def clear(ctx, amount=-1):
    amount = round(amount) + 1
    if amount <= 0:
        await ctx.send("Please specify how many messages to clear.")
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Cleared {amount-1} messages.")

client.run(bot_settings.token)