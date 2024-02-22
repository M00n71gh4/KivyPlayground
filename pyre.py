import pyrebase

config = {
    "apiKey": "AIzaSyCf2XWjJtKUXy2a4XdyGlEXySxFqc6tB_U",
    "authDomain": "neuralbasket-e13bc.firebaseapp.com",
    "databaseURL": "https://neuralbasket-e13bc-default-rtdb.europe-west1.firebasedatabase.app/",
    "storageBucket": "neuralbasket-e13bc.appspot.com"
}

PB = pyrebase.initialize_app(config)
db = PB.database()

data = {
    "Test4": "Val4RR",
    "Test5": "Val5RR",
    "Test6": "Val6RR",
}

#db.push(data) #Unique ID
db.child("MyBBList").push(data)
