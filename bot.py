import discord
# from .sheets import finalData
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print('bot is ready')

@client.event
async def on_message(message):
    print('got message!')
    print(message)
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



# async def dm(ctx):

        # await client.send_message(questions, message.content)
    # print(message.channel.name)
    # channelType = message.channel.split(" ")
    # if(channelType[0] +" "+ channelType[1] == "Direct Message"):
    #     print("DM!")


# guild = ctx.message.guild
# await guild.create_text_channel('cool-channel')


client.run('NjkyNTQwMTE3MTMwMjgwOTkz.XnwB1w.KPjxivkUV6AtcH8xMU8Kx8Xis1Y')
