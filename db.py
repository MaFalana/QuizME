'''
Name: db.py
Description: Database connection manager for
'''
from pymongo import MongoClient

username = "mfalana"

password = "OEyC14Muo6DYJrIU"

class DatabaseManager:
    def __init__(self, db_name):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]

    def query(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find(query)

    def insert(self, collection_name, document):
        collection = self.db[collection_name]
        collection.insert_one(document)
        #result = collection.insert_one(document)
        #return result.inserted_id

    def __del__(self):
        self.client.close()