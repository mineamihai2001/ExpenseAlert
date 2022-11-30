from .db import db
from bson import ObjectId

class Collection:
    def __init__(self, collection_name) -> None:
        self.collection = db[collection_name]

    def get(self, data={}):
        cursor = self.collection.find(data)
        return [doc for doc in cursor]


    
