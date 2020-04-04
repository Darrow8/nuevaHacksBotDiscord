import discord
# from .sheets import finalData
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print('bot is ready')

@client.event
async def on_message():
    print('got message!')


client.run('NjkyNTQwMTE3MTMwMjgwOTkz.XnwB1w.KPjxivkUV6AtcH8xMU8Kx8Xis1Y')
