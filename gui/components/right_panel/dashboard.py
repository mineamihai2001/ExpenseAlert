import customtkinter

from globals import session
from pprint import pprint
from ..component import Component
from ..form import Form
from .info import Info
from modules import manager


class Dashboard(Component):
    def __init__(self, parent) -> None:
        self.dashboard = customtkinter.CTkFrame(master=parent)

        # PATH form
        self.dashboard.path_form = Form(parent, self.get_options())

        # Details panel
        self.dashboard.details = Info(parent, {})

        # Refresh button
        self.dashboard.refresh_btn = customtkinter.CTkButton(
            master=parent, text="refresh", command=self.action_refresh)

        self.dashboard.refresh_btn.pack(pady=12, padx=10)
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

    def action_refresh(self):
        manager.refresh(True)
        self.dashboard.details.refresh(manager.get_data())

    def change_path(self, inputs):
        data = dict([(i["name"], i["entry"].get()) for i in inputs])
        manager.change_path(data["path"])

    def reload(self):
        self.dashboard.details.add_data(manager.get_data())
