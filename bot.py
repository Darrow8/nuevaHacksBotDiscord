import discord
from discord.ext import commands
import randomcolor

client = commands.Bot(command_prefix="!")
guild = client.get_guild(688568885968109756)


@client.event
async def on_ready():
    print('bot is ready')

    # await makeTeam("team-role")


@client.event
async def on_member_join(member):
    guild = client.get_guild(688568885968109756)
    role = discord.utils.get(member.guild.roles, id=689916456871133311)
    await member.add_roles(role)
    print("new participant" + str(member.display_name))


@client.event
async def on_message(message):
    # print('got message!')
    # print(message)
    try:
        print(message.channel.name)
        print(message.content)
    except:
        #the user is sending a DM
        print(message.channel.recipient.name)
        print(message.content)
        id = 697529501370024097
        channel = client.get_channel(id)
        await message.author.send("Thank you for asking a question, an admin will DM you shortly with an answer.")
        await channel.send("""
        Incoming Question! 
        User: """ + message.author.name + " #" + message.author.discriminator + """
        Question: """ + message.content)



@client.event
async def makeTeam(name):
    print("am here!")

    # team_category = {id: 697575868410626148}
    teamcategory = "TEAM"
    category = discord.utils.get(guild.categories, name=teamcategory)
    await guild.create_role(name=name)

    role = discord.utils.get(guild.roles, name=name)
    member = guild.get_member(595137733920292891)
    await member.add_roles(role)
    admin_role = discord.utils.get(guild.roles,id=689915377928765455)
    print(admin_role)
    print(member.id)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        role: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    await guild.create_text_channel(name + "-text", overwrites=overwrites, category=category, reason=None)
    await guild.create_voice_channel(name + "-voice", overwrites=overwrites, category=category, reason=None)




def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return [int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3)]

# print(hex_to_rgb("#4287f5"))

client.run('NjkyNTQwMTE3MTMwMjgwOTkz.XnwB1w.KPjxivkUV6AtcH8xMU8Kx8Xis1Y')
