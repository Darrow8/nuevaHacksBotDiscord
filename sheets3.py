import gspread
import models as md
import time
import bot3 as bt
import server as sv
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

#
# sheetsA = client.open("NuevaHacks Online Hackathon (Responses)").sheet1
# sheetsB = client2.open("NuevaHacks III Sign Up(Responses)").sheet1
# sheetsC = client3.open("Submitting Discord Information for Nuevahacks (Responses)").sheet1
# sheetsD = client3.open("Create your Team! (Responses)").sheet1




# data1 = sheetsA.get_all_records()
# data2 = sheetsB.get_all_records()
# data3 = sheetsC.get_all_records()
# data4 = sheetsD.get_all_records()
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

# CODE FOR THE TEAM POINTS UPDATES

credAll = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)


clientAll = gspread.authorize(credAll)


sheetsE = clientAll.open("Invited A Friend (After Kickoff) (Responses)").sheet1
sheetsF = clientAll.open("Webinar Form (Responses)").sheet1
sheetsG = clientAll.open("Daily Progress Form (Responses)").sheet1
sheetsH = clientAll.open("Helped Another Team Form (Responses)").sheet1
sheetsI = clientAll.open("Submit Media Form (Responses)").sheet1
sheetsJ = clientAll.open("Followed NuevaHacks (Responses)").sheet1
sheetsK = clientAll.open("Submit a message  (Responses)").sheet1


valE = "Invited A Friend (After Kickoff) (Responses)"
valF = "Webinar Form (Responses)"
valG = "Daily Progress Form (Responses)"
valH = "Helped Another Team Form (Responses)"
valI = "Submit Media Form (Responses)"
valJ = "Followed NuevaHacks (Responses)"
valK = "Submit a message  (Responses)"



def formSubmittedDetector(sheet):
    data = sheet.get_all_records()
    currentNumCounter = int(getSingleData(data, "Current Number Of Submissions", 0))

    priorNumCounter = len(data)

    if(currentNumCounter != priorNumCounter):
        # print("same num!")
        currentNumCounter += 1
        return True
    else:
        return False

async def formSubmittedCounter():
    final = "ALL GOOD"

    #SHEET E
    if (formSubmittedDetector(sheetsE)):
        final = "NEW SUBMISSION"
        data = sheetsE.get_all_records()

        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", len(data) - 1))
        em = str(getSingleData(data, "Email Address", len(data) - 1))
        sv.updatePoints(teamName, pointInc,em,valE)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        sheetsE.update_cell(col=8, row=2, value=int(len(data)))

    #SHEET F
    if (formSubmittedDetector(sheetsF)):
        final = "NEW SUBMISSION"
        data = sheetsF.get_all_records()

        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", len(data) - 1))
        em = str(getSingleData(data, "Email Address", len(data) - 1))
        sv.updatePoints(teamName, pointInc,em,valF)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        sheetsF.update_cell(col=8, row=2, value=int(len(data)))

    #SHEET G
    if (formSubmittedDetector(sheetsG)):
        final = "NEW SUBMISSION"
        data = sheetsG.get_all_records()

        pointInc = int(getSingleData(data, "pointIncrease", 0))
        em = str(getSingleData(data, "Email Address", len(data) - 1))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", len(data) - 1))
        sv.updatePoints(teamName, pointInc,em,valG)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        sheetsG.update_cell(col=8, row=2, value=int(len(data)))

    #SHEET H
    if (formSubmittedDetector(sheetsH)):
        final = "NEW SUBMISSION"
        data = sheetsH.get_all_records()

        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", len(data) - 1))
        em = str(getSingleData(data, "Email Address", len(data) - 1))
        sv.updatePoints(teamName, pointInc,em,valH)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        sheetsH.update_cell(col=8, row=2, value=int(len(data)))


    #SHEET I
    if (formSubmittedDetector(sheetsI)):
        final = "NEW SUBMISSION"
        data = sheetsI.get_all_records()

        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", len(data) - 1))
        em = str(getSingleData(data, "Email Address", len(data) - 1))
        sv.updatePoints(teamName, pointInc,em,valI)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        sheetsI.update_cell(col=8, row=2, value=int(len(data)))


    #SHEET J
    if (formSubmittedDetector(sheetsJ)):
        final = "NEW SUBMISSION"
        data = sheetsJ.get_all_records()

        pointInc = int(getSingleData(data, "pointIncrease", 0))
        teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", len(data) - 1))
        em = str(getSingleData(data, "Email Address", len(data) - 1))
        sv.updatePoints(teamName, pointInc,em,valJ)
        print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
        sheetsJ.update_cell(col=8, row=2, value=int(len(data)))

    # #SHEET K
    # if (formSubmittedDetector(sheetsK)):
    #     final = "NEW SUBMISSION"
    #     data = sheetsK.get_all_records()
    #
    #     pointInc = int(getSingleData(data, "pointIncrease", 0))
    #     teamName = str(getSingleData(data, "Your team name (capitalization and spacing matters)", len(data) - 1))
    #     em = str(getSingleData(data, "Email Address", len(data) - 1))
    #     sv.updatePoints(teamName, pointInc,em,valK)
    #     print("updated points score for " + teamName + " added " + str(pointInc) + " points.")
    #     sheetsK.update_cell(col=8, row=2, value=int(len(data)))

    print("formSubmittedCounter() running correctly, final for FORMS: " + final)


async def totalCounter():
    interval = 60 #change!
    while True:
        time.sleep(.5)
        if round(time.perf_counter()) > interval:
            interval += 60 # add time

            # await teamCounter()
            await formSubmittedCounter()

        print("FORM SUBMITTER",round(time.perf_counter()))


