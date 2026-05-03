class Button:
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        return "Windows Button"


class MacButton(Button):
    def render(self):
        return "Mac Button"