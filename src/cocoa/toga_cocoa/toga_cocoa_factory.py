from toga.factory import FactoryInterface
from .widgets.button import Button


class TogaCocoaFactory(FactoryInterface):

    @staticmethod
    def create_button(label, id=None, style=None, on_press=None, enabled=None):
        return Button(label)
