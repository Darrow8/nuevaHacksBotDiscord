#RUN SHEETS2
import discord
from discord.ext import commands
import sheets3 as sheets3
import time

client = commands.Bot(command_prefix="!")
guild = client.get_guild(688568885968109756)

@client.event
async def on_ready():
    print('bot3 is ready')
    await sheets3.totalCounter()
    # await getusers("Quiz You")

# @client.commands

@client.command(pass_context=True)
async def getusers(teamName):
    totalCount = []
    guild = client.get_guild(688568885968109756)
    role = discord.utils.get(guild.roles, name=teamName)
    # user = discord.utils.get(client.get_all_members(), name=name)
    time.sleep(3)

    for member in guild.members:
        if role in member.roles:
            print("YAY!")
            totalCount.append(member.name)
            print(member.name)
    time.sleep(1)
    return len(totalCount)



client.run('NjkyNTQwMTE3MTMwMjgwOTkz.XnwB1w.KPjxivkUV6AtcH8xMU8Kx8Xis1Y')


