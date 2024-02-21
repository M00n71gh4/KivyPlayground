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
    "Test1": "Val1RR",
    "Test2": "Val2RR",
    "Test3": "Val3RR",
}

#db.push(data) #Unique ID
db.child("MyBBList").child("TestCholdNode").set(data)
