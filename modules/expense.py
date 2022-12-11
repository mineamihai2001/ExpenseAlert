import time

from bson import ObjectId
from pprint import pprint
from utils.database.collection import Collection
from gui import modal


class Expense:
    def __init__(self, user_id) -> None:
        self.expenses = Collection("expenses")
        self.user_id = user_id

    def get_all(self):
        return self.expenses.get({"userId": self.user_id})

    def get_category(self, category: str):
        return self.expenses.get({
            "userId": self.user_id,
            "category": category
        })

    def get_period(self, start=0, end=int(time.time())):
        return self.expenses.get({
            "userId": self.user_id,
            "date": {"$gt": start, "$lt": end}
        })

    def get_dynamic(self, args: dict):
        return self.expenses.get({
            "userId": self.user_id,
            **args
        })

    def insert(self, data: dict):
        data["userId"] = self.user_id
        return self.expenses.put(data)

    def insert_list(self, data: list, onclick=False):
        current_data = self.get_all()
        new_data = list()
        for item in data:
            if not any(x["file_name"] == item["file_name"] for x in current_data):
                item["userId"] = self.user_id
                new_data.append(item)
                print(f"[DEBUG] - inserting item {item['file_name']}")

        if not len(new_data):
            print("[INFO] - nothing new")
            if onclick:
                return modal.show(message="[INFO] - nothing new")
            return
        return self.expenses.put(new_data)


if __name__ == "__main__":
    user_id = ObjectId("6394705d2de5e090ad36d766")
    e = Expense(user_id)

    res = e.insert_list([
        {
            "file_name": "example_1.json",
            "date": int(time.time()),
            "category": "food",
            "total": 10
        },
        {
            "file_name": "example.json",
            "date": int(time.time()),
            "category": "other",
            "total": 800
        },
    ])
