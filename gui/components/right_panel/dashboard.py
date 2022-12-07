import customtkinter
from ..component import Component
from ..form import Form


class Dashboard(Component):
    def __init__(self, parent) -> None:
        self.dashboard = customtkinter.CTkFrame(master=parent)
        self.dashboard.path_form = Form(parent, self.get_options())
        super().__init__(parent, self.dashboard)

    def build(self):
        pass

    def get_options(self):
        return {
            "title": None,
            "inputs": [
                {
                    "name": "path",
                    "args": {
                        "width": 200,
                    },
                    "grid": {
                        "row": 0,
                        "column": 0,
                        "columnspan": 2,
                        "pady": 20,
                        "padx": 20,
                        "sticky": "we"
                    }
                },
            ],
            "buttons": [
                {
                    "name": "Submit",
                    "action": self.change_path,
                    "args": {},
                    "grid": {
                        "row": 0,
                        "column": 2,
                        "columnspan": 1,
                        "pady": 20,
                        "padx": 20,
                        "sticky": "we"
                    }
                },
            ]
        }

    def change_path(self, inputs):
        print("path changed to ", [
              {i["name"]: i["entry"].get()} for i in inputs])
