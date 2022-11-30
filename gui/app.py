import customtkinter
from .components.component import Component

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self) -> None:
        super().__init__()
        self.title("Expense Alert")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add(self):
        pass

    def get_root(self):
        return self

    def on_closing(self, event=0):
        self.destroy()

    def run(self):
        self.mainloop()
