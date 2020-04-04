import gspread


from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)
client2 = gspread.authorize(creds)


sheetsA = client.open("NuevaHacks Online Hackathon (Responses)").sheet1
sheetsB = client2.open("Create your Team! (Responses)").sheet1


data1 = sheetsA.get_all_records()
data2 = sheetsB.get_all_records()
num = sheetsA.row_count



class User:
    def __init__(self,name,email,interests,discord,discordTag):
        self.name = name
        self.email = email
        self.interests = interests
        self.discord = discord
        self.discordTag = discordTag
    def returnAll(self):
        print("---------------------------------------------------")
        print("NAME: " + str(self.name))
        print("EMAIL: " + str(self.email))
        print("INTERESTS: " + str(self.interests))
        print("DISCORD USERNAME: " + str(self.discord))
        print("DISCORD TAG: " + str(self.discordTag))
        print("---------------------------------------------------")


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
                discordTag = "#" + getSingleData(data1, "Discord Tag (Example #1234)", pos).split("#")[0]
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
        totalUsers.append(User(firstName,email,interests,discord,discordTag))

    return totalUsers
# usersWithoutDiscord = getUsers(80,93)
usersWithDiscord = getUsers(94,102)
# incorrectAll = getUsers(0,1)[0]
# correct = getUsers(95,96)[0]
# incorrectTag = getUsers(91,92)[0]




