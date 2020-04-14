import discord
from discord.ext import commands
import time
# import sheets
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
    await member.send("""
    Hello!

        Welcome to the NuevaHacks Discord server! This will be your place for all things NuevaHacks over the next week. Our tech team has worked hard to make this server complete with a ton of amazing features that will make it super easy to communicate, collaborate, and ask for help. 
        
        To start, you’ll notice that the channels on the left side of your screen are split into five sections: information, general, resources, interests, and developers. All the channels within these sections have specific descriptions—we encourage you to take some time to explore the channels and get a sense of what all of them do. Below are explanations of the most important channels by section: 

        __**Information**__
        **Announcements: All major communication and resources from the NuevaHacks team. **
        This includes:
        - Daily morning/evening messages
        - Links to all speaker presentations, Q&A sessions, and other live Zoom sessions
        - Major updates about the leaderboard
        - All other announcements during the day
        **Resources:** All relevant resources will be kept in a “Master Resources” document, which is pinned in the channel. This document will be updated daily and contains technical resources, Discord support, and most importantly, our daily guides (one guide for each theme, sent out each day). 
            """"")
    await member.send("""
        __**General**__
        **General Chat:** A place for general questions about event logistics, as well as chatting with other participants.

        **Ideas:** Brainstorm/share ideas with other participants.

        __**Resources:**__
        **Leaderboard:** The hub of the ‘leaderboard’ competition. By completing the challenges listed in this channel throughout the week, you will gain points for you or your team. The top 5 point-getters by Friday night will receive an extra boost in their scores from the judges!
        
        **Interests:** You have been placed in a channel with participants who expressed similar interests as you when signing up. This is a great place to meet new people, seek technical help, brainstorm ideas, and find a team. 
        
        **Developers:** If you need technical support and would like to request help from one of our support developers, use this channel.
        
        If you need help at any point (or have questions or concerns about the event), please use the [Helper Bot] and the NuevaHacks team will communicate directly with you.
        
    Enjoy!
    
    The NuevaHacks Team
    """)



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
        exclamation = client.get_emoji(id=)
        print(exclamation)
        # await message.add_reaction(emoji=exclamation)






client.run('NjkyNTQwMTE3MTMwMjgwOTkz.XnwB1w.KPjxivkUV6AtcH8xMU8Kx8Xis1Y')
