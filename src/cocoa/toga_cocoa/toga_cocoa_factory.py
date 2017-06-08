from toga.factory import FactoryInterface
from .widgets.button import Button


class TogaCocoaFactory(FactoryInterface):
    @staticmethod
    def Button(creator):
        return Button(creator)
