import customtkinter

from tkinter import *
from ..component import Component

show = ["total", "date", "file_name", "category"]


class Info(Component):
    def __init__(self, parent, details: list) -> None:
        self.details = details
        self.parent = parent

        self.rows = list()
        super().__init__(parent, None)

    def set_details(self, details):
        self.details = details

    def build(self):
        self.info.grid_columnconfigure(2, weight=1)
        self.info.grid_rowconfigure(len(self.details), weight=1)

        self.info.pack(padx=10, pady=10)

    def add_data(self, details):
        self.details = details

        self.sb = Scrollbar(self.parent)
        self.sb.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.parent, yscrollcommand=self.sb.set,
                              width=400, height=600)

        for index, item in enumerate(self.details):
            for key in list(item):
                if key not in show:
                    item.pop(key)
            self.mylist.insert(
                END, f"{index + 1}. {item['category']} => {str(item)}")

        self.mylist.pack(side=LEFT)
        self.sb.config(command=self.mylist.yview)

    def add_categories(self, details, setup):
        self.details = details

        self.sb = Scrollbar(self.parent)
        self.sb.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.parent, yscrollcommand=self.sb.set,
                              width=400, height=600)

        # show each category
        parsed = dict()
        for index, item in enumerate(self.details):
            if item["category"] not in parsed:
                parsed[item["category"]] = {
                    "index": index,
                    "total": item["total"],
                }
            else:
                parsed[item["category"]]["total"] += item["total"]

        alert = setup["alert"] if "alert" in setup else {}
        warning = setup["warning"] if "warning" in setup else {}
        for index, (category, values) in enumerate(parsed.items()):
            self.mylist.insert(
                END, f"{index + 1}. {category} => {values}")

            if category in warning and values["total"] > int(warning[category]):
                self.mylist.itemconfig(index, {'fg': '#D6B41C'})
            if category in alert and values["total"] > int(alert[category]):
                self.mylist.itemconfig(index, {'fg': 'red'})

        self.mylist.pack(side=LEFT)
        self.sb.config(command=self.mylist.yview)

    def refresh(self, details, categories=False, setup=None):
        self.mylist.destroy()
        self.sb.destroy()
        self.add_data(
            details) if not categories else self.add_categories(details, setup)
