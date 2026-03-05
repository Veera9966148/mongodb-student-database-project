from pymongo import MongoClient

uri = "YOUR_MONGODB_CONNECTION_STRING"

client = MongoClient(uri)

db = client["student_db"]
collection = db["students"]

for data in collection.find():
    print(data)
