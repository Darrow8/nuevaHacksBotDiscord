class Team:
    def __init__(self,users,name,desc,sht_desc):
        self.users = users
        self.name = name
        self.desc = desc
        self.sht_desc = sht_desc
    def returnAll(self):
        print("---------------------------------------------------")
        print("NAME: " + str(self.name))
        print("USERS: " + str(self.users))
        print("DESCRIPTION: " + str(self.desc))
        print("DISCORD USERNAME: " + str(self.discord))
        print("SHORT DESCRIPTION: " + str(self.sht_desc))
        print("---------------------------------------------------")


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

    def update(self,key,value):
        setattr(self,key,value)
        # print(self.key)
        print(self.returnAll())
