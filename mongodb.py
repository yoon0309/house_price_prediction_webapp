from pymongo import MongoClient


def db_info():
    HOST = 'cluster0.hxzch.mongodb.net'
    USER = 'yoon'
    PASSWORD = 'yoon123'
    DATABASE_NAME = 'price'
    DATABASE_NAME = 'price' 
    return HOST, USER, PASSWORD, DATABASE_NAME


def db_connect(MONGO_URI, DATABASE_NAME, COLLECTION_NAME):
    client = MongoClient(MONGO_URI)
    database = client[DATABASE_NAME]
    collection = database[COLLECTION_NAME]
    return collection