from toga.interface import Font as FontInterface
from .libs import NSFont

class Font(FontInterface):

    def create(self):
        self._native = NSFont.fontWithName_size_(self.family, self.size)
