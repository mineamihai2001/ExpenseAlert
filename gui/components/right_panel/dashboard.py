import customtkinter

from globals import session
from pprint import pprint

from gui import modal
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
            master=parent, text="Refresh", command=self.action_refresh)


        # Categories button
        self.dashboard.categories = customtkinter.CTkButton(
            master=parent, text="Show Categories", command=self.action_categories)
        # All button
        self.dashboard.all = customtkinter.CTkButton(
            master=parent, text="Show All", command=self.action_all)

        self.dashboard.refresh_btn.pack(pady=1, padx=10)
        self.dashboard.categories.pack(pady=1, padx=10)
        self.dashboard.all.pack(pady=1, padx=10)
        # self.dashboard.all.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="we")
        # self.dashboard.categories.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="we")

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
        status = manager.refresh(True)
        if status == False:
            return modal.show("[ERROR] - The current path doesn't exist")
        self.dashboard.details.refresh(manager.get_data())
    
    def action_all(self):
        """Refresh and change the details to ALL"""
        status = manager.refresh()
        self.dashboard.details.refresh(manager.get_data())

    def action_categories(self):
        """Refresh and change the details to CATEGORIES"""
        status = manager.refresh()
        setup = manager.get_setup()
        self.dashboard.details.refresh(manager.get_data(), True, setup)

    def change_path(self, inputs):
        data = dict([(i["name"], i["entry"].get()) for i in inputs])
        manager.change_path(data["path"])

    def reload(self):
        self.dashboard.details.add_data(manager.get_data())

    def set_default(self):
        current_path = manager.get_current().replace("\\", "/")

        inputs = self.dashboard.path_form.inputs
        entry = inputs[0]["entry"]

        entry.insert(0, current_path)
