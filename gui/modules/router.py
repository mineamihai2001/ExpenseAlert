from ..frames import *


class Router:
    def __init__(self, routes, app) -> None:
        self.routes = routes
        self.frames = {route: routes[route]["frame"](app, self) for route in routes}

    def start(self):
        self.frames["home"].show()

    def redirect(self, source, destination):
        self.frames[source].hide()
        self.frames[destination].show()