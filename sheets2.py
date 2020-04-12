import gspread
import models as md
import time
import bot2 as bt
import server as sv
# import sender as sd
import message as md
# #SPREADSHEET CODE
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
#
#
#
#
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

def newTeamUsers(num_back):
    numOfTeams = len(data4)
    indexAbleTeams = len(data4) - num_back
    print(indexAbleTeams)
    print(data4[indexAbleTeams]["List ALL members of your team. Please ONLY put your team members discord username. DO NOT include their tag. DO NOT include their current nickname. (separate users between one comma and one space) Example: Darrow8, Povellesto"])
    users = getSingleData(data4,"List ALL members of your team. Please ONLY put your team members discord username. DO NOT include their tag. DO NOT include their current nickname. (separate users between one comma and one space) Example: Darrow8, Povellesto",indexAbleTeams).split(", ")
    return users

def newTeamName(num_back):
    numOfTeams = len(data4)
    indexAbleTeams = len(data4) - num_back
    # print(data4[indexAbleTeams])
    name = getSingleData(data4,"Add Your Team Name",indexAbleTeams)
    return name


async def teamCounter():
        data4 = sheetsD.get_all_records()
        currentTeamsNum = int(getSingleData(data4, "Current Number Of Teams", 0))
        final = "SAME"
        if(len(data4) != currentTeamsNum):
            final = "NOT SAME"
            try:
                num_back = len(data4) - currentTeamsNum
                team_name = newTeamName(num_back)
                team_users = newTeamUsers(num_back)
                currentTeamsNum += 1
                sheetsD.update_cell(col=7, row=2, value=int(currentTeamsNum))
                await bt.makeTeam(team_name, team_users)
                sv.setTeamDB(team_name,team_users)
            except:
                em = getSingleData(data4, "Email Address", len(data4) -1)
                print(em)
                # md.runTeamError(em)
        else:
            final = "SAME"
        print("teamCounter() running correctly, final for DB: " + final)


async def totalCounter():
    interval = 30 #change!
    while True:
        time.sleep(.5)
        if round(time.perf_counter()) > interval:
            interval += 60 # add time
            await teamCounter()
            # await formSubmittedCounter()

        print("TEAM COUNTER: ",round(time.perf_counter()))




def getAllTeams(min,max):
    totalTeams = []
    for pos in range(min, max):
        name = getSingleData(data4,"Add Your Team Name",pos)
        users = getSingleData(data4,"List ALL members of your team. Please ONLY put your team members discord username. DO NOT include their tag. DO NOT include their current nickname. (separate users between one comma and one space) Example: Darrow8, Povellesto",pos)
        newTeam = md.Team(users=users,name=name,desc=None,sht_desc=None)
        totalTeams.append(newTeam)

    return totalTeams

