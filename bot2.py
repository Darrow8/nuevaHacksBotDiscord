import discord
from discord.ext import commands
import time
import sheets
import server
import randomcolor

client = commands.Bot(command_prefix="!")
guild = client.get_guild(688568885968109756)

@client.event
async def on_ready():
    print('bot2 is ready')
    await sheets.teamCounter()



@client.event
async def makeTeam(name,users):
    print("Reached MakeTeam Func!")
    guild = client.get_guild(688568885968109756)

    teamcategory = "TEAM"
    category = discord.utils.get(guild.categories, name=teamcategory)
    await guild.create_role(name=name)

    role = discord.utils.get(guild.roles, name=name)
    member = guild.get_member(595137733920292891)
    await member.add_roles(role)
    admin_role = discord.utils.get(guild.roles,id=689915377928765455)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        role: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    await guild.create_text_channel(name + "-text", overwrites=overwrites, category=category, reason=None)
    await guild.create_voice_channel(name + "-voice", overwrites=overwrites, category=category, reason=None)

    await server.newTeam(name,users)

    for userName in users:
        await addUserToTeam(name,userName)


@client.event
async def addUserToTeam(teamName,userName):
    guild = client.get_guild(688568885968109756)

    role = discord.utils.get(guild.roles, name=teamName)
    user = discord.utils.get(client.get_all_members(), name=userName)
    await user.add_roles(role)


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return [int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3)]


# @client.event
# async def running():
#     while True:
#         time.sleep(.5)
#         print("online")
#         print(time.perf_counter())
#         if(sheets.teamCounter()):
#             print("new team!")
#             await makeTeam(sheets.newTeamName(),sheets.newTeamUsers())
#             await running()
#         else:
#             print("checked")
#             await running()



client.run('NjkyNTQwMTE3MTMwMjgwOTkz.XnwB1w.KPjxivkUV6AtcH8xMU8Kx8Xis1Y')


