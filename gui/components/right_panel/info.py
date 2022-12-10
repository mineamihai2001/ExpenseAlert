import customtkinter

from ..component import Component

show = ["total", "date", "file_name"]

class Info(Component):
    def __init__(self, parent, details: list) -> None:
        self.details = details
        self.info = customtkinter.CTkFrame(master=parent)

        self.rows = list()
        self.build()
        super().__init__(parent, self.info)

    def set_details(self, details):
        self.details = details

    def build(self):
        self.info.grid_columnconfigure(2, weight=1)
        self.info.grid_rowconfigure(len(self.details), weight=1)

        self.info.pack(padx=10, pady=10)

    def add_data(self, details):
        self.details = details
        for index, item in enumerate(self.details):
            category = customtkinter.CTkLabel(
                master=self.info, text=item["category"], text_font=("Roboto", 12))
            category.grid(row=index, column=0)

            for key in list(item):
                if key not in show:
                    item.pop(key)

            data = customtkinter.CTkLabel(
                master=self.info, text=str(item), text_font=("Roboto", 9))
            data.grid(row=index, column=1)

            self.rows.append((category, data))

    def refresh(self, details):
        for row in self.rows:
            for item in row:
                item.destroy()

        self.add_data(details)
