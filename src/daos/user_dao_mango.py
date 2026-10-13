import os
from dotenv import load_dotenv
from pymongo import MongoClient
from models.user import User

load_dotenv(dotenv_path=".env")


class UserDAOMongo:
    def __init__(self):
        host = os.getenv("MONGODB_HOST")
        port = 27017
        username = os.getenv("DB_USERNAME")
        password = os.getenv("DB_PASSWORD")
        auth_source = "admin"

        self.client = MongoClient(
            host=host,
            port=port,
            username=username,
            password=password,
            authSource=auth_source
        )
        self.db = self.client[os.getenv("MYSQL_DB_NAME")]
        self.users = self.db["users"]

    def select_all(self):
        """ Select all users from MongoDB """
        self.insert(User(None, "Alice Test", "alice.test@example.com"))
        self.insert(User(None, "Bob Test", "bob.test@example.com"))
        self.insert(User(None, "Charlie Test", "charlie.test@example.com"))
        user_docs = self.users.find()
        return [User(str(doc["_id"]), doc["name"], doc["email"]) for doc in user_docs]
    def insert(self, user):
        """ Insert given user into MongoDB """
        user_doc = {"name": user.name, "email": user.email}
        result = self.users.insert_one(user_doc)
        return str(result.inserted_id)
    def update(self, user):
        """ Update given user in MongoDB """
        from bson import ObjectId
        result = self.users.update_one(
            {"_id": ObjectId(user.id)},
            {"$set": {"name": user.name, "email": user.email}}
        )
        return result.modified_count
    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        from bson import ObjectId
        result = self.users.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count
    