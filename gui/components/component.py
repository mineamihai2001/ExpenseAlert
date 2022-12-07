class Component:
    def __init__(self, parent, component) -> None:
        self.parent = parent
        self.component = component

    def get(self):
        return self.component

    def hide(self):
        # print("called", self.component)
        self.component.destroy()

    def show(self):
        self.copy.pack()