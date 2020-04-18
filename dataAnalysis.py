import gspread
from printy import printy
import server as sv
import time
# #SPREADSHEET CODE
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)


client = gspread.authorize(creds)

sheetsF = client.open("Webinar Form (Responses)").sheet1
sheetsG = client.open("Daily Progress Form (Responses)").sheet1
sheetsH = client.open("Helped Another Team Form (Responses)").sheet1
sheetsI = client.open("Submit Media Form (Responses)").sheet1
sheetsJ = client.open("Followed NuevaHacks (Responses)").sheet1
sheetsK = client.open("Submit a message  (Responses)").sheet1
sheetsL = client.open("Submit Getting Help Form (Responses)").sheet1
sheetsM = client.open("Helped Another Team Form (Responses)").sheet1
sheetsN = client.open("Submit UI Design Form (Responses)").sheet1
sheetsO = client.open("Submit Guide of the Day Form (Responses)").sheet1
sheetsQ = client.open("Submit Repository Form (Responses)").sheet1
sheetsR = client.open("Team Points Leaderboard Gap").sheet1

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
def checkIfHas(arr,key,val):
    found = False
    place = len(arr)
    for i in range(len(arr)):
        if arr[i][key] == val:
            found = True
            place = i
            break

    return found,place




# PROJECT FOR COMPARING TEAMS FORMS SUBMITTED VS CURRENT POINTS OF TEAMS


def countForms():
    totalVals = [] #example: {"team": "teamName","count":1}
    #sheetsF
    dataF = sheetsF.get_all_records()
    numF = len(dataF)
    teamsF = getData(dataF, "Your team name (capitalization and spacing matters)")
    # print(teamsF)
    for pos in range(len(teamsF)):
        checking = checkIfHas(totalVals, "team", teamsF[pos])
        time.sleep(.1)
        print(checking)
        # if checking[0]:
        #     #We have the team already
        #     totalVals[checking[1]]["count"] = totalVals[checking[1]]["count"] + 1
        #     message = "Updated team " + str(totalVals[checking[1]]["team"]) + " to " + str(totalVals[checking[1]]["count"])
        #     print(message)
        # else:
        #We don't have the team

        if checking[0] != True:
            totalVals.append({"team": str(teamsF[checking[1]]), "count": 1})
        message = "Created team " + str(totalVals[checking[1]]["team"]) + " at " + str(totalVals[checking[1]]["count"])
        print(message)

    print(totalVals)


# countForms()

async def updateVals():
    total = await countForms()
    points = await sv.getAllPoints()
    for i in range(len(total)):
        #Find correct team
        point_pos = 0
        for x in range(len(points)):
            if total[i]["team"] == points[x]:
                point_pos = x
                break
        sheetsR.update_cell(col=4,row=i,value=points[point_pos])
        sheetsR.update_cell(col=5,row=i,value=total[i]["count"])
        sheetsR.update_cell(col=6,row=i,value=total[i]["team"])



# updateVals()

