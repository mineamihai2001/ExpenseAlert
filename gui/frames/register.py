from globals import session

from bson import ObjectId
from ..components.form import Form
from .frame import Frame
from modules.auth import register


class Register(Frame):
    def __init__(self, app, router) -> None:
        super().__init__(app, router)
        form = Form(self.current, self.get_options())

    def action_register(self, inputs: list):
        data = dict([(i["name"], i["entry"].get()) for i in inputs])

        if data["password"] != data["confirm password"]:
            print("[ERROR] - passwords don't match")
            return

        kwargs = dict((k, data[k]) for k in ("username", "password"))
        user = register.action_register(**kwargs)

        if user == None:
            return

        session["user_id"] = str(user.inserted_id)
        self.router.redirect("register", "home")

    def login(self, inputs):
        print("login redirect")
        self.router.redirect("register", "login")

    def get_options(self):
        return {
            "title": "Register",
            "inputs": [
                {
                    "name": "username",
                    "args": {
                        "width": 200,
                    }
                },
                {
                    "name": "password",
                    "args": {
                        "width": 200,
                        "show": "*"
                    }
                },
                {
                    "name": "confirm password",
                    "args": {
                        "width": 200,
                        "show": "*"
                    }
                },

            ],
            "buttons": [
                {
                    "name": "Register",
                    "action": self.action_register,
                    "args": {}
                },
                {
                    "name": "back to Login",
                    "action": self.login,
                    "args": {
                        "fg_color": ("white", "gray38")
                    }
                },
            ]
        }
