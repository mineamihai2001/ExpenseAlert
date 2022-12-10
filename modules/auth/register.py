import bcrypt

from utils.database.collection import Collection


users = Collection("users")


def action_register(username: str, password: str):
    hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    if len(users.get({"username": username})):
        print("[ERROR] - username already exists")
        return None
    try:
        res = users.put({"username": username, "password": hash})
        return res
    except:
        print("[ERROR] - an error occurred when creating the user. Try again")
        return None


if __name__ == "__main__":
    username = "admin2"
    password = "admin2"
    status = action_register(username, password)
