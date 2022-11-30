from ..components.form import Form
from .frame import Frame


class Register(Frame):
    def __init__(self, app, router) -> None:
        super().__init__(app, router)
        form = Form(self.current, self.get_options())

    def action_register(self, inputs):
        print("here123")

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
