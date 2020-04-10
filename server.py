import pyrebase
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate('./serviceAccountCred.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


def setTeamDB(teamName, users):
    try:
        team_data = {
            'name': teamName,
            'users': users,
            'points': 10
        }
        db.collection('teams').document(teamName).set(team_data)
        print("Team Setup & Updated to DB")
    except:
        print("ERROR ON SETTEAMDB()")

def updatePoints(teamName, pointIncrease):
    try:
        team_ref = db.collection('teams').document(teamName)
        doc = team_ref.get()
        print('Document data: {}'.format(doc.to_dict()))

        points_num = int('{}'.format(doc.to_dict()['points']))

        newPoints = int(pointIncrease + points_num)
        point_data = {
            'points': newPoints
        }

        team_ref.update(point_data)
        print("update completed succesfully for team: " + str(teamName))
    except:
        print("ERROR ON UPDATEPOINTS()")



# setTeamDB('example-team',["Darrow8"])
# updatePoints('example-team',20)