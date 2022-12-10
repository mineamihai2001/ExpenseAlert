import bcrypt

from utils.database.collection import Collection


users = Collection("users")
register_data = {
    "username": "",
    "password": "",
    "path": ""
}


def action_register(username: str, password: str):
    hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    if len(users.get({"username": username})):
        print("[ERROR] - username already exists")
        return None
    try:
        register_data["username"] = username
        register_data["password"] = hash
        res = users.put({**register_data})
        return res
    except Exception as e:
        print("[ERROR] - an error occurred when creating the user. Try again", e)
        return None


if __name__ == "__main__":
    username = "admin2"
    password = "admin2"
    status = action_register(username, password)
