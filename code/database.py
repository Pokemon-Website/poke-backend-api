import asyncio
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase
    )
from settings import URL

def connect_mongo() -> AsyncIOMotorClient:
    # Conectando no banco de dados
    client_mongo = AsyncIOMotorClient(URL)
    client_mongo.get_io_loop = asyncio.get_event_loop
    return client_mongo


client_mongo = connect_mongo()


def get_database() -> AsyncIOMotorDatabase:

    return client_mongo.get_default_database()


def get_collection(collection: str) -> AsyncIOMotorCollection:
    bd = get_database()
    collection_get = bd[collection]
    return collection_get