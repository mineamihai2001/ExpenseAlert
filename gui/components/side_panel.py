import customtkinter
from .component import Component


class SidePanel(Component):
    def __init__(self, parent, options) -> None:
        super().__init__(parent, None)
        self.options = options
        self.build()

    def build(self):
        # empty row with minsize as spacing
        self.parent.grid_rowconfigure(0, minsize=10)
        self.parent.grid_rowconfigure(5, weight=1)  # empty row as spacing
        # empty row with minsize as spacing
        self.parent.grid_rowconfigure(8, minsize=20)
        # empty row with minsize as spacing
        self.parent.grid_rowconfigure(11, minsize=10)

        self.label = customtkinter.CTkLabel(master=self.parent,
                                            text=self.options["title"],
                                            text_font=("Roboto Medium", -16))  # font name and size in px
        self.label.grid(row=1, column=0, pady=10, padx=10)

        for index, button in enumerate(self.options["buttons"]):
            self.btn = customtkinter.CTkButton(master=self.parent,
                                               **button)
            self.btn.grid(row=index + 2, column=0, pady=10, padx=20)

        # THEME SELECTOR
        self.label_mode = customtkinter.CTkLabel(
            master=self.parent, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.parent,
                                                        values=[
                                                            "Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
