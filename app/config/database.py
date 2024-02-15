from pymongo import MongoClient
# from motor.motor_asyncio import AsyncIOMotorClient


def db():
    return MongoClient("mongodb://localhost:27017/")


def collection(client, db, table):
    return client[db][table]
