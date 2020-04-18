import gspread
import models as md
import bot3 as bt
import time
import server as sv
from printy import printy
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

# CODE FOR THE TEAM POINTS UPDATES

credAll = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)


clientAll = gspread.authorize(credAll)


# sheetsE = clientAll.open("Invited A Friend (After Kickoff) (Responses)").sheet1
sheetsF = clientAll.open("Webinar Form (Responses)").sheet1
sheetsG = clientAll.open("Daily Progress Form (Responses)").sheet1
sheetsH = clientAll.open("Helped Another Team Form (Responses)").sheet1
# sheetsI = clientAll.open("Submit Media Form (Responses)").sheet1
# sheetsJ = clientAll.open("Followed NuevaHacks (Responses)").sheet1
sheetsK = clientAll.open("Submit a message  (Responses)").sheet1
sheetsL = clientAll.open("Submit Getting Help Form (Responses)").sheet1
sheetsM = clientAll.open("Helped Another Team Form (Responses)").sheet1
sheetsN = clientAll.open("Submit UI Design Form (Responses)").sheet1
sheetsO = clientAll.open("Submit Guide of the Day Form (Responses)").sheet1
sheetsP = clientAll.open("team roundup leaderboard").worksheet('aaref hilaly')
sheetsQ = clientAll.open("Submit Repository Form (Responses)").sheet1
# sheetsR = clientAll.open("Team Points Leaderboard Gap").sheet1


valE = "Invited A Friend (After Kickoff) (Responses)"
valF = "Webinar Form (Responses)"
valG = "Daily Progress Form (Responses)"
valH = "Helped Another Team Form (Responses)"
valI = "Submit Media Form (Responses)"
valJ = "Followed NuevaHacks (Responses)"
valK = "Submit a message  (Responses)"
valL = "Submit Getting Help Form (Responses)"
valM = "Helped Another Team Form (Responses)"
valN = "Submit UI Design Form (Responses)"
valO = "Submit Guide of the Day Form (Responses)"
valQ = "Submit Repository Form (Responses)"



def formSubmittedDetector(sheet):
    data = sheet.get_all_records()
    priorNumCounter = int(getSingleData(data, "Current Number Of Submissions", 0))

    currentNumCounter = len(data)

    if(currentNumCounter != priorNumCounter):
        # print("same num!")
        priorNumCounter += 1
        return True
    else:
        return False

async def formSubmittedCounter():
    final = "ALL GOOD"

    # #SHEET E
    # if (formSubmittedDetector(sheetsE)):
    #     final = "NEW SUBMISSION"
    #     data = sheetsE.get_all_records()
    #     currentCount = int(getSingleData(data, "Current Number Of Submissions", 0))
    #     print(currentCount)
    #     pointInc = int(getSingleData(data, "pointIncrease", 0))
    #     teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", currentCount))
    #     print(teamName)
    #     em = str(getSingleData(data, "Email Address", len(data) - 1))
    #     sv.updatePoints(teamName, pointInc,em,valE)
    #     print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
    #     currentCount += 1
    #     sheetsE.update_cell(col=8, row=2, value=int(currentCount))

    #SHEET F
    if (formSubmittedDetector(sheetsF)):
        final = "NEW SUBMISSION"
        data = sheetsF.get_all_records()
        currentCount = int(getSingleData(data, "Current Number Of Submissions", 0))
        print(currentCount)
        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)",currentCount))
        print(teamName)
        em = str(getSingleData(data, "Email Address", len(data) - 1))
        sv.updatePoints(teamName, pointInc,em,valF)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        currentCount += 1
        sheetsF.update_cell(col=8, row=2, value=int(currentCount))

    #SHEET G
    if (formSubmittedDetector(sheetsG)):
        final = "NEW SUBMISSION"
        data = sheetsG.get_all_records()
        currentCount = int(getSingleData(data, "Current Number Of Submissions", 0))
        pointInc = int(getSingleData(data, "pointIncrease", 0))
        em = str(getSingleData(data, "Email Address", len(data) - 1))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", currentCount))
        print(teamName)
        sv.updatePoints(teamName, pointInc,em,valG)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        currentCount += 1
        sheetsG.update_cell(col=8, row=2, value=int(currentCount))

    #SHEET H
    if (formSubmittedDetector(sheetsH)):
        final = "NEW SUBMISSION"
        data = sheetsH.get_all_records()
        currentCount = int(getSingleData(data, "Current Number Of Submissions", 0))
        print(currentCount)
        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)",currentCount))
        print(teamName)
        em = str(getSingleData(data, "Email Address", len(data) - 1))
        sv.updatePoints(teamName, pointInc,em,valH)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        currentCount += 1
        sheetsH.update_cell(col=8, row=2, value=int(currentCount))

    #SHEET K
    if (formSubmittedDetector(sheetsK)):
        final = "NEW SUBMISSION"
        data = sheetsK.get_all_records()
        currentCount = int(getSingleData(data, "Current Number Of Submissions", 0))
        print(currentCount)
        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", currentCount))
        print(teamName)
        em = str(getSingleData(data, "Email Address", currentCount))
        sv.updatePoints(teamName, pointInc,em,valK)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        currentCount += 1
        sheetsK.update_cell(col=8, row=2, value=int(currentCount))

    #SHEET L
    if (formSubmittedDetector(sheetsL)):
        final = "NEW SUBMISSION"
        data = sheetsL.get_all_records()
        currentCount = int(getSingleData(data, "Current Number Of Submissions", 0))
        print(currentCount)
        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "The name of the team that helped you (capitalization and spacing matters)", currentCount))
        print(teamName)
        em = str(getSingleData(data, "Email Address", currentCount))
        sv.updatePoints(teamName, pointInc,em,valL)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        currentCount += 1
        sheetsL.update_cell(col=8, row=2, value=int(currentCount))


    #SHEET M
    if (formSubmittedDetector(sheetsM)):
        final = "NEW SUBMISSION"
        data = sheetsM.get_all_records()
        currentCount = int(getSingleData(data, "Current Number Of Submissions", 0))
        print(currentCount)
        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", currentCount))
        print(teamName)
        em = str(getSingleData(data, "Email Address", currentCount))
        sv.updatePoints(teamName, pointInc,em,valM)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        currentCount += 1
        sheetsM.update_cell(col=8, row=2, value=int(currentCount))

    # ADD AGAIN LATER!
    #SHEET N
    if (formSubmittedDetector(sheetsN)):
        final = "NEW SUBMISSION"
        data = sheetsN.get_all_records()
        currentCount = int(getSingleData(data, "Current Number Of Submissions", 0))
        print(currentCount)
        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", currentCount))
        print(teamName)
        em = str(getSingleData(data, "Email Address", currentCount))
        sv.updatePoints(teamName, pointInc,em,valN)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        currentCount += 1
        sheetsN.update_cell(col=12, row=2, value=int(currentCount))

    print("SHEET O")
    #SHEET O
    if (formSubmittedDetector(sheetsO)):
        final = "NEW SUBMISSION"
        data = sheetsO.get_all_records()
        currentCount = int(getSingleData(data, "Current Number Of Submissions", 0))
        print(currentCount)
        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", currentCount))
        print(teamName)
        em = str(getSingleData(data, "Email Address", currentCount))
        sv.updatePoints(teamName, pointInc,em,valO)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        currentCount += 1
        sheetsO.update_cell(col=8, row=2, value=int(currentCount))

    print("formSubmittedCounter() running correctly, final for FORMS: " + final)


    #SHEET Q
    if (formSubmittedDetector(sheetsQ)):
        final = "NEW SUBMISSION"
        data = sheetsQ.get_all_records()
        currentCount = int(getSingleData(data, "Current Number Of Submissions", 0))
        print(currentCount)
        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", currentCount))
        print(teamName)
        em = str(getSingleData(data, "Email Address", currentCount))
        sv.updatePoints(teamName, pointInc,em,valQ)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        currentCount += 1
        sheetsQ.update_cell(col=8, row=2, value=int(currentCount))

    print("formSubmittedCounter() running correctly, final for FORMS: " + final)


async def getUserRoles():
    data = sheetsP.get_all_records()
    teams = (getData(data,"Teams in Form"))
    for i in range(len(teams)):
        sheetsP.update_cell(col=2, row=(i + 2), value=int(await bt.getusers(teams[i])))
        print(teams[i] +" "+ str(await bt.getusers(teams[i])))
#
# async def addAllTeamPoints():
#     arr = await sv.getAllPoints()
#     print(arr)
#     for pts in range(len(arr)):
#         sheetsR.update_cell(col=2,row=pts + 2,value=arr[pts])



async def totalCounter():
    interval = 30 #change!
    while True:
        time.sleep(.5)
        if round(time.perf_counter()) > interval:
            interval += 40 # add time
            # await addAllTeamPoints()
            # await getUserRoles()
            await formSubmittedCounter()
        print("SUBMITTER",round(time.perf_counter()))

