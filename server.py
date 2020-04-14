import firebase_admin
from firebase_admin import credentials,firestore
# import sheets2 as st
import message as mp
# import models as md
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCj0jqBmHOFIdOdH98s2LDDLXX3Zit6QJg",
    "authDomain": "nuevahacks-85464.firebaseapp.com",
    "databaseURL": "https://nuevahacks-85464.firebaseio.com",
    "projectId": "nuevahacks-85464",
    "storageBucket": "nuevahacks-85464.appspot.com",
    "messagingSenderId": "471411391657",
    "appId": "1:471411391657:web:96f6ebe66153eb60863db8",
    "measurementId": "G-Y4YHYXXJHB"
};

cred = credentials.Certificate('./serviceAccountCred.json')
default_app = firebase_admin.initialize_app(cred)
pyrebase_app = pyrebase.initialize_app(config=firebaseConfig)
db = firestore.client()
auth = pyrebase_app.auth()


def authSystem():
    try:
        email = "support@nuevahacks.com"
        password = "testuser123!"
        auth.sign_in_with_email_and_password(email=email,password=password)
        print('logged in!')
    except:
        print("error on auth")


# authSystem()
def setTeamDB(teamName, users):
    authSystem()
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

def updatePoints(teamName, pointIncrease,email,form):
    try:
        authSystem()
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
        mp.runFormError(email,form)

def setPoints(teamName, setPoint,email,form):
    try:
        authSystem()
        team_ref = db.collection('teams').document(teamName)
        doc = team_ref.get()
        print('Document data: {}'.format(doc.to_dict()))

        # points_num = int('{}'.format(doc.to_dict()['points']))

        # newPoints = int(pointIncrease + points_num)
        point_data = {
            'points': setPoint
        }

        team_ref.update(point_data)
        print("update completed succesfully for team: " + str(teamName))
    except:
        print("ERROR ON UPDATEPOINTS()")
        mp.runFormError(email,form)






# def tryIt():
#     teams = st.getAllTeams(9,67)
#     for team in teams:
#         print("killing " + team.name)
#         setPoints(team.name,10,"darhart@nuevaschool.org","TEST")
#
#
# tryIt()