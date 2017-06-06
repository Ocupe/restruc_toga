from ..platform import Platform


class Button:
    """ This class is a wrapper for a platform specific implementation of a button. """
    def __init__(self, label, id=None, style=None, on_press=None, enabled=None):
        self.factory = Platform().factory
        print(self.factory)
        self.impl = self.factory.create_button(label, id=None, style=None, on_press=None, enabled=None)

    def __getattr__(self, item):
        return getattr(self.impl, item)
