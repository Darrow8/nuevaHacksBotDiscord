import gspread
import models as md
import time
import bot2 as bt
#SPREADSHEET CODE
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
creds2 = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
creds3 = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
creds4 = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)


client = gspread.authorize(creds)
client2 = gspread.authorize(creds2)
client3 = gspread.authorize(creds3)
client4 = gspread.authorize(creds3)


sheetsA = client.open("NuevaHacks Online Hackathon (Responses)").sheet1
sheetsB = client2.open("NuevaHacks III Sign Up(Responses)").sheet1
sheetsC = client3.open("Submitting Discord Information for Nuevahacks (Responses)").sheet1
sheetsD = client3.open("Create your Team! (Responses)").sheet1



data1 = sheetsA.get_all_records()
data2 = sheetsB.get_all_records()
data3 = sheetsC.get_all_records()
data4 = sheetsD.get_all_records()




#get data for all
def getData(data,tag):
    Tag = tag
    Arr = []
    for i in data:
        Arr = Arr + i[Tag].split(", ")

    return Arr

#get data per user
def getSingleData(data,tag,position):
    Tag = tag
    Arr = ""
    Arr = data[position][Tag]

    return Arr

def getUsers(min,max):
    totalUsers = []
    for pos in range(min,max):
        email = getSingleData(data1,"Email Address",pos)
        firstName = getSingleData(data1,"Full Name",pos).split(" ")[0]
        interests = getSingleData(data1,"Interests",pos).split(", ")
        discord = ""
        discordTag = ""
        if pos > 93:
            discord = getSingleData(data1,"Discord Username (Username Only)",pos).split("#")[0]
            if getSingleData(data1,"Discord Username (Username Only)",pos).find('#') !=-1:
                discordTag = "#" + getSingleData(data1, "Discord Username (Username Only)", pos).split("#")[1]
            else:
                #you fucking idiot...
                discordTag = "#" + str(getSingleData(data1, "Discord Tag (Example #1234)", pos)).split("#")[0]
        else:
            #if you've fucked up in some way you're here
            if len(getSingleData(data1,"Discord Username (Username Only)",pos)) == 0:
                discord = "EMPTY!"
                discordTag = "EMPTY!"
            else:
                # print("HELLO")
                discord = getSingleData(data1, "Discord Username (Username Only)", pos).split("#")[0]
                if getSingleData(data1, "Discord Username (Username Only)", pos).find('#') != -1:
                    # print("HELLO 2")
                    discordTag = "#" + getSingleData(data1, "Discord Username (Username Only)", pos).split("#")[1]
                else:
                    # print("HELLO 3")
                    #you've fucked up!
                    discordTag = "EMPTY!"
        totalUsers.append(md.User(firstName,email,interests,discord,discordTag))

    return totalUsers

def compareUsers(userSetA,userSetB):
    #userSetA is signed up for original
    #userSetB is signed up for online
    oldEmailList = getData(userSetB,"Email Address")
    currentEmailList = getData(userSetA,"Email Address")
    emailList = []
    for pos in range(0, len(oldEmailList)):
        try:
            currentEmailList.index(oldEmailList[pos])
        except:
            print(oldEmailList[pos])
            emailList.append(oldEmailList[pos])

    return emailList

def updateUsers(currentUsers,data,sheet1):
    #all the email addresses of
    allNewData = getData(data,"Email Address")
    # print(allNewData)
    for i in range(len(currentUsers)):
        try:
            num = allNewData.index(currentUsers[i].email)
            currentUsers[i].update("discord",getSingleData(data,"Please Enter your Discord Username only",num))
            currentUsers[i].update("discordTag",getSingleData(data,"Please Enter your Discord Tag (example: #1234)",num))
            # user.returnAll()
            sheet1.update_cell(row=10,col=(1+i),value=currentUsers[i].discord)
            sheet1.update_cell(row=11,col=(1+i),value=currentUsers[i].discordTag)
        except:
            print("HAVE NOT FILLED OUT")


# DEPRECATED
def detectTeams():
    currentTeamsNum = int(getSingleData(data4,"Current Number Of Teams",0))
    print(currentTeamsNum)
    print(len(data4))
    if(currentTeamsNum == len(data4)):
        print("same ammount")

        return False
    else:
        print("not same")
        currentTeamsNum += 1
        sheetsD.update_cell(col=6,row=2,value=int(currentTeamsNum))
        return True

def newTeamUsers():
    numOfTeams = len(data4)
    indexAbleTeams = len(data4) - 1
    # print(data4[indexAbleTeams])
    users = getSingleData(data4,"List members of your team (separate users between one comma and one space) Example: Darrow8, Povellesto",indexAbleTeams).split(", ")
    return users

def newTeamName():
    numOfTeams = len(data4)
    indexAbleTeams = len(data4) - 1
    # print(data4[indexAbleTeams])
    name = getSingleData(data4,"Write Your Project Title",indexAbleTeams)
    return name


async def teamCounter():
    interval = 10
    while True:
        time.sleep(.5)
        if round(time.perf_counter()) > interval:
            interval += 10 # Adds 5 mins
            data4 = sheetsD.get_all_records()
            print(len(data4))
            currentTeamsNum = int(getSingleData(data4, "Current Number Of Teams", 0))
            print(currentTeamsNum)

            if(len(data4) != currentTeamsNum):
                print("NOT SAME!")
                await bt.makeTeam(newTeamName(), newTeamUsers())
                currentTeamsNum += 1
                sheetsD.update_cell(col=6, row=2, value=int(currentTeamsNum))

            else:
                print("Same")
        print("time",round(time.perf_counter()))

# CODE FOR THE TEA




