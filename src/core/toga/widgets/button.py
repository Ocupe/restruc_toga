from ..platform import Platform


class Button:
    def __init__(self, label, id=None, style=None, on_press=None, enabled=None):
        self.factory = Platform().factory
        print(self.factory)
        self.imp = self.factory.create_button(label, id=None, style=None, on_press=None, enabled=None)

    @property
    def label(self):
        return self.imp.label

    @label.setter
    def label(self, label_str):
        self.imp.label = label_str
