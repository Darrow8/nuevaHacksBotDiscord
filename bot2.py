#RUN SHEETS2
import discord
from discord.ext import commands
import time
import sheets2 as sheets2
# import message as mp

client = commands.Bot(command_prefix="!")
guild = client.get_guild(688568885968109756)

@client.event
async def on_ready():
    print('bot2 is ready')
    # await sheets2.totalCounter()
    await sheets2.teamCounter()
@client.event
async def makeTeam(name,users):
    print("Reached MakeTeam Func!")
    try:
        name = name.lower()
        print("TEAM NAME IS: ", name)

        guild = client.get_guild(688568885968109756)

        # teamcategory = "TEAM 2"
        category = discord.utils.get(guild.categories, id=700393662651301959)
        print(category)
        name = name.replace(" ","-")
        name = name.replace("'","")
        time.sleep(2)

        await guild.create_role(name=name,color=discord.Color.orange())

        time.sleep(2)
        unique_role = discord.utils.get(guild.roles, name=name)
        print("ROLE IS: ", unique_role)
        admin_role = discord.utils.get(guild.roles,id=689915377928765455)


        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            unique_role: discord.PermissionOverwrite(read_messages=True),
            admin_role: discord.PermissionOverwrite(read_messages=True)
        }

        await guild.create_text_channel(name + "-text", overwrites=overwrites, category=category, reason=None)
        await guild.create_voice_channel(name + "-voice", overwrites=overwrites, category=category, reason=None)

        for userName in users:
            goodUserName = userName.split("#")[0]
            # print(goodUserName)
            await addUserToTeam(name,goodUserName)
    except:
        print("error on makeTeam")

@client.event
async def addUserToTeam(teamName,userName):
    try:
        guild = client.get_guild(688568885968109756)

        role = discord.utils.get(guild.roles, name=teamName)
        time.sleep(3)
        print("ROLE IS: ", role)

        user = discord.utils.get(client.get_all_members(), name=userName)
        time.sleep(2)

        print("USER IS: ", user)
        if(user != None):
            await user.add_roles(role)

    except:
        print("error on addUserToTeam()")

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return [int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3)]




client.run('NjkyNTQwMTE3MTMwMjgwOTkz.XnwB1w.KPjxivkUV6AtcH8xMU8Kx8Xis1Y')


