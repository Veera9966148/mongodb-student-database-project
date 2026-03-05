from pymongo import MongoClient

uri = "mongodb+srv://veereshkumar7601_db_user:veera123@cluster0.f7g9vxl.mongodb.net/"

client = MongoClient(uri)

db = client["student_db"]
collection = db["students"]

for data in collection.find():
    print(data)