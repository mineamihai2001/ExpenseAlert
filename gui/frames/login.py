from ..components.form import Form
from .frame import Frame


class Login(Frame):
    def __init__(self, app, router) -> None:
        super().__init__(app, router)
        form = Form(self.current, self.get_options())

    def action_login(self, inputs: list):
        print("action called", [(i["name"], i["entry"].get()) for i in inputs])
        self.router.redirect("login", "home")

    def register(self, inputs):
        print("register redirect")
        self.router.redirect("login", "register")

    def get_options(self):
        return {
            "title": "Login",
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
                }
            ],
            "buttons": [
                {
                    "name": "Login",
                    "action": self.action_login,
                    "args": {}
                },
                {
                    "name": "or Register now",
                    "action": self.register,
                    "args": {
                        "fg_color": ("white", "gray38")
                    }
                },

            ]
        }
