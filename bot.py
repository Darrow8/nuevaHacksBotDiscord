import discord
from discord.ext import commands
import time
import sheets
import randomcolor

client = commands.Bot(command_prefix="!")
guild = client.get_guild(688568885968109756)

@client.event
async def on_ready():
    print('bot1 is online')


@client.event
async def on_member_join(member):
    guild = client.get_guild(688568885968109756)
    role = discord.utils.get(member.guild.roles, id=689916456871133311)
    await member.add_roles(role)
    print("new participant" + str(member.display_name))


@client.event
async def on_message(message):

    try:
        print(message.channel.name)
        print(message.content)
    except:
        #the user is sending a DM
        print(message.content)
        id = 697529501370024097
        channel = client.get_channel(id)
        await message.author.send("Thank you for asking a question, an admin will DM you shortly with an answer.")
        await channel.send("""
        Incoming Question!
        User: """ + message.author.name + " #" + message.author.discriminator + """
        Question: """ + message.content)



client.run('NjkyNTQwMTE3MTMwMjgwOTkz.XnwB1w.KPjxivkUV6AtcH8xMU8Kx8Xis1Y')
