#RUN SHEETS2
import discord
from discord.ext import commands
import time
import sheets3 as sheets3
import server
import asyncio
import randomcolor

client = commands.Bot(command_prefix="!")
guild = client.get_guild(688568885968109756)

@client.event
async def on_ready():
    print('bot2 is ready')
    await sheets3.totalCounter()

@client.event
async def makeTeam(name,users):
    print("Reached MakeTeam Func!")
    # try:
    name = name.lower()
    print("TEAM NAME IS: ", name)

    guild = client.get_guild(688568885968109756)

    teamcategory = "TEAM 2"
    category = discord.utils.get(guild.categories, name=teamcategory)

    time.sleep(2)

    await guild.create_role(name=name,color=discord.Color.orange())

    time.sleep(2)
    role = discord.utils.get(guild.roles, name=name)
    print("ROLE IS: ", role)
    admin_role = discord.utils.get(guild.roles,id=689915377928765455)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        role: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }

    await guild.create_text_channel(name + "-text", overwrites=overwrites, category=category, reason=None)
    await guild.create_voice_channel(name + "-voice", overwrites=overwrites, category=category, reason=None)

    for userName in users:
        goodUserName = userName.split("#")[0]
        print(goodUserName)
        await addUserToTeam(name,goodUserName)
    # except:
    #     print("DARROW! LOOK INTO ", name)


@client.event
async def addUserToTeam(teamName,userName):
    guild = client.get_guild(688568885968109756)

    role = discord.utils.get(guild.roles, name=teamName)
    time.sleep(3)
    print("ROLE IS: ", role)
    user = discord.utils.get(client.get_all_members(), name=userName)
    print("USER IS: ", user)
    if(user != None):
        await user.add_roles(role)
    else:
        channelName = str(teamName + "-text")
        channel = discord.utils.get(guild.channels, name=channelName)
        print(channel)
        channel.send(content="User " + userName + " was not added because the user who filled out the form added his/her name incorrectly. Please DM the NuevaHacks Helper to change this.")



def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return [int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3)]




client.run('NjkyNTQwMTE3MTMwMjgwOTkz.XnwB1w.KPjxivkUV6AtcH8xMU8Kx8Xis1Y')


