from .db import db
from bson import ObjectId


class Collection:
    def __init__(self, collection_name) -> None:
        self.collection = db[collection_name]

    def get(self, data={}):
        cursor = self.collection.find(data)
        return [doc for doc in cursor]

    def put(self, data: dict | list):
        return self.collection.insert_one(data) if type(
            data) == dict else self.collection.insert_many(data)

    def delete(self, data: dict | list):
        return self.collection.delete_one(data) if type(
            data) == dict else self.collection.delete_many(data)

    def update(self, filter: dict, data: dict):
        return self.collection.update_one(filter, data)
