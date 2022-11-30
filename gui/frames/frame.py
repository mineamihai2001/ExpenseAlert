import customtkinter


class Frame:
    def __init__(self, app, router) -> None:
        self.root = app.get_root()
        self.router = router
        self.current = customtkinter.CTkFrame(master=self.root)

    def show(self):
        self.current.pack(fill="both", expand=True)

    def hide(self):
        self.current.pack_forget()
