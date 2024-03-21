from pymongo import MongoClient


# client = MongoClient("mongodb+srv://prince:<password>@cluster0.xfinu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client = MongoClient("mongodb://localhost:27017/mydb")
# client = MongoClient(f"mongodb://{USERNAME}:{PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/")

db = client.todo_app

collection_name = db["todos_app"]

