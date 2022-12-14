import customtkinter

from globals import session
from gui import modal
from .frame import Frame
from ..components.side_panel import SidePanel
from ..components.right_panel.dashboard import Dashboard
from modules import manager


class Home(Frame):
    def __init__(self, app, router) -> None:
        super().__init__(app, router)
        self.create()

    def create(self):
        # GRID configuration
        self.current.grid_columnconfigure(1, weight=1)
        self.current.grid_rowconfigure(0, weight=1)

        # LEFT panel
        self.current.frame_left = customtkinter.CTkFrame(master=self.current,
                                                         width=180,
                                                         corner_radius=0)
        self.current.frame_left.grid(row=0, column=0, sticky="nswe")
        self.side_panel = SidePanel(
            self.current.frame_left, self.get_options())
        self.side_panel.build()

        # RIGHT panel
        self.current.frame_right = customtkinter.CTkFrame(master=self.current)
        self.current.frame_right.grid(
            row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.dashboard = Dashboard(self.current.frame_right)
        # self.side_panel.build()

    def get_options(self):
        return {
            "title": "Expense Alert",
            "buttons": [
                {
                    "text": "Dashboard",
                    "command": self.show_home
                },
                {
                    "text": "Upload Receipts",
                    "command": self.show_upload
                },
                {
                    "text": "Logout",
                    "command": self.action_logout
                },
            ]
        }

    def action_logout(self):
        self.router.redirect("home", "login")

    def show_upload(self):
        print("go to upload")
        self.dashboard.hide()

    def show_home(self):
        print("go to dashboard")
        self.dashboard.show()

    def show(self):  # overrides
        self.current.pack(fill="both", expand=True)
        status = manager.refresh()
        # if not status:
        #     modal.show("[WARNING] - The current path doesn't exist")
        self.dashboard.reload()  # get the dashboard data only when this frame is shown

        self.dashboard.set_default()
