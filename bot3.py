#RUN SHEETS2
import discord
from discord.ext import commands
import sheets3 as sheets3

client = commands.Bot(command_prefix="!")
guild = client.get_guild(688568885968109756)

@client.event
async def on_ready():
    print('bot2 is ready')
    await sheets3.totalCounter()




client.run('NjkyNTQwMTE3MTMwMjgwOTkz.XnwB1w.KPjxivkUV6AtcH8xMU8Kx8Xis1Y')


