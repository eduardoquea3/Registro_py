from pymongo import MongoClient

def db():
    return MongoClient("mongodb://localhost:27017/")

def collection(client,db,table):
    return client[db][table]
