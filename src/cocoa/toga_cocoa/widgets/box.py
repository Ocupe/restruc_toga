from rubicon.objc import *

# from toga.interface import Box as BoxInterface

from ..libs import *
from .base import Widget


class Box(Widget):
    def __init__(self, creator):
        self.creator = creator
        self._create()
        self._native = None

    def _create(self):
        # # self._impl.setWantsLayer_(True)
        # # self._impl.setBackgroundColor_(NSColor.blueColor)
        self._constraints = None
