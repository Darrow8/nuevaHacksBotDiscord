import pyrebase

config = {
  "apiKey": "AIzaSyCj0jqBmHOFIdOdH98s2LDDLXX3Zit6QJg",
  "authDomain": "nuevahacks-85464.firebaseapp.com",
  "databaseURL": "https://nuevahacks-85464.firebaseio.com",
  "storageBucket": "nuevahacks-85464.appspot.com",
  "serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


async def newTeam(name):
  data = {"name": "Mortimer 'Morty' Smith"}
  db.child("Teams").push(data)