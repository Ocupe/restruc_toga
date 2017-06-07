from rubicon.objc import objc_method, get_selector
from .base import Widget
from ..libs import *
from ..utils import process_callback


class TogaButton(NSButton):
    @objc_method
    def onPress_(self, obj) -> None:
        if self._interface.on_press:
            process_callback(self._interface.on_press(self._interface))


class Button(Widget):
    def __init__(self, creator):
        self.creator = creator
        pass

    def create(self):
        self._impl = TogaButton.alloc().init()
        self._impl._interface = self

        self._impl.setBezelStyle_(NSRoundedBezelStyle)
        self._impl.setButtonType_(NSMomentaryPushInButton)
        self._impl.setTarget_(self._impl)
        self._impl.setAction_(get_selector('onPress:'))

        # Add the layout constraints
        self._add_constraints()

    def set_label(self, label):
        self._impl.setTitle_(label)
        self.rehint()

    def rehint(self):
        fitting_size = self._impl.fittingSize()
        self.creator.style.hint(
            height=fitting_size.height,
            min_width=fitting_size.width,
        )



