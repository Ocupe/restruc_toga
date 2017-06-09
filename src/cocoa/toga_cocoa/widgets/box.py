from rubicon.objc import *

# from toga.interface import Box as BoxInterface

from ..libs import *
from .base import Widget


class Box(Widget):
    def __init__(self, creator, id=id, style=None, children=None):
        # super().__init__(id=id, style=style, children=children)
        self.creator = creator

    def create(self):
        # # self._impl.setWantsLayer_(True)
        # # self._impl.setBackgroundColor_(NSColor.blueColor)

        self._constraints = None
