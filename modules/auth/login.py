import bcrypt

from utils.database.collection import Collection
from bson import ObjectId

users = Collection("users")


def action_login(username: str, password: str):
    try:
        user = users.get({"username": username})[0]
        return user["_id"] if bcrypt.checkpw(password.encode("utf-8"), user["password"]) else None
    except Exception as e:
        return None


if __name__ == "__main__":
    user_id = action_login("admin", "admin")
    print(user_id)
