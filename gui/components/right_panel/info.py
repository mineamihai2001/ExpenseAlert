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

        sb = Scrollbar(self.parent)
        sb.pack(side=RIGHT, fill=Y)

        self.mylist = Listbox(self.parent, yscrollcommand=sb.set,
                              width=400, height=600)

        for index, item in enumerate(self.details):
            for key in list(item):
                if key not in show:
                    item.pop(key)
            self.mylist.insert(
                END, f"{index + 1}. {item['category']} => {str(item)}")

        self.mylist.pack(side=LEFT)
        sb.config(command=self.mylist.yview)

    def refresh(self, details):
        self.mylist.destroy()
        self.add_data(details)
