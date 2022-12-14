import json
import os
from globals import session
from modules.expense import Expense

from utils.database.collection import Collection
from bson import ObjectId
from pprint import pprint
from modules import parser

users = Collection("users")


def get_current():
    user_id = session["user_id"]
    res = users.get({"_id": ObjectId(user_id)})
    return res[0]["path"]


def change_path(new_path: str):
    user_id = session["user_id"]
    if not os.path.exists(new_path):
        print("[ERROR] - invalid path")
        return

    params = {
        "filter": {"_id": ObjectId(user_id)},
        "data": {"$set": {"path": new_path}}
    }

    res = users.update(**params)
    print(res.matched_count)


def get_data():
    """ Get the data stored in the DB """
    user_id = session["user_id"]

    user = users.get({"_id": ObjectId(user_id)})[0]
    e = Expense(user_id)
    data = e.get_all()

    pprint(data)
    return data


def refresh(onclick=False):
    """ 
    Lists the source directory and adds in the DB the updates (if any)
    :param onclick: True | False Show the info modal to the user 
    """
    user_id = session["user_id"]

    user = users.get({"_id": ObjectId(user_id)})[0]
    path = user["path"]
    if not os.path.exists(path):
        return False

    print(f"paring from {path}...")

    e = Expense(user_id)

    local_data = parser.parse(path)
    e.insert_list(local_data, onclick)
    return True


def get_setup():
    user_id = session["user_id"]
    path = users.get({"_id": ObjectId(user_id)})[0]["path"]
    if not os.path.exists(os.path.join(path, "setup.json")):
        return {}
    
    with open(os.path.join(path, "setup.json"), "r+") as setup:
        return json.loads(setup.read())


if __name__ == "__main__":
    session["user_id"] = ObjectId("6394abfd7519224ef6975e05")
    refresh()
