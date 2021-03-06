import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog loaded')

    # Commands
    @commands.command()
    async def class_ping(self, ctx):
        await ctx.send('Pong!')

def setup(client):
    client.add_cog(Example(client))