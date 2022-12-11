import os
from globals import session
from modules.expense import Expense

from utils.database.collection import Collection
from bson import ObjectId
from pprint import pprint
from modules import parser

users = Collection("users")
expenses = Collection("expenses")


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
    user_id = session["user_id"]

    user = users.get({"_id": ObjectId(user_id)})[0]
    e = Expense(user_id)
    data = e.get_all()

    # formatted = dict()
    # for expense in data:
    #     if expense["category"] not in formatted:
    #         formatted[expense["category"]] = [expense]
    #     else:
    #         formatted[expense["category"]].append(expense)
    pprint(data)
    return data


def refresh(onclick=False):
    """ Lists the source directory and adds in the DB the updates (if any) """
    user_id = session["user_id"]

    user = users.get({"_id": ObjectId(user_id)})[0]
    path = user["path"]

    e = Expense(user_id)

    local_data = parser.parse(path)
    e.insert_list(local_data, onclick)


if __name__ == "__main__":
    session["user_id"] = ObjectId("6394abfd7519224ef6975e05")
    refresh()
