import sys
import configs.setup
from utils.database.collection import Collection
from modules.ocr.textract import Textract
from gui.app import App
from gui.frames import *
from gui.modules.router import Router

routes = {
    "login": {
        "frame": login.Login
    },
    "register": {
        "frame": register.Register
    },
    "home": {
        "frame": home.Home
    }
}

if __name__ == "__main__":
    app = App()
    router = Router(routes, app)
    router.start()

    app.run()
