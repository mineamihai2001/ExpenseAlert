import customtkinter
from .component import Component


class Form(Component):
    def __init__(self, parent, options: dict) -> None:
        self.options = options

        self.form = customtkinter.CTkFrame(master=parent)
        self.form.pack(pady=10, padx=10, fill="both")

        super().__init__(parent, self.form)

        self.inputs = list()
        self.buttons = list()

        self.build()

    def build(self):
        if self.options["title"] != None:
            self.build_title(self.options["title"])
        self.build_inputs(self.options["inputs"])
        self.build_buttons(self.options["buttons"])

    def build_title(self, text):
        title = customtkinter.CTkLabel(
            master=self.form, text=text, text_font=("Roboto", 24))
        title.pack(pady=12, padx=10)
        self.title = title

    def build_inputs(self, inputs: list):
        for input in inputs:
            entry = customtkinter.CTkEntry(
                master=self.form, placeholder_text=input["name"], **input["args"])
            if "grid" in input:
                entry.grid(**input["grid"])
            else:
                entry.pack(pady=12, padx=10)
            self.inputs.append({
                "name": input["name"],
                "entry": entry
            })

    def build_buttons(self, buttons: list):
        for button in buttons:
            btn = customtkinter.CTkButton(
                master=self.form, text=button["name"], command=lambda button=button: button["action"](self.inputs), **button["args"])
            if "grid" in button:
                btn.grid(**button["grid"])
            else:
                btn.pack(pady=12, padx=10)
            # self.buttons.append(btn)
