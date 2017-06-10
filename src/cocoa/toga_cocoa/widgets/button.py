from rubicon.objc import objc_method, get_selector
from .base import Widget
from ..libs import *
from ..utils import process_callback


class TogaButton(NSButton):
    @objc_method
    def onPress_(self, obj) -> None:
        if self._interface.on_press:
            process_callback(self._interface._creator.on_press(self._interface._creator))


class Button(Widget):
    def __init__(self, creator):
        self._creator = creator
        pass

    def create(self):
        self._plat_impl = TogaButton.alloc().init()
        self._plat_impl._interface = self

        self._plat_impl.setBezelStyle_(NSRoundedBezelStyle)
        self._plat_impl.setButtonType_(NSMomentaryPushInButton)
        self._plat_impl.setTarget_(self._plat_impl)
        self._plat_impl.setAction_(get_selector('onPress:'))

        # Add the layout constraints
        self._add_constraints()

    def set_label(self, label):
        self._plat_impl.setTitle_(label)
        self.rehint()

    def rehint(self):
        fitting_size = self._plat_impl.fittingSize()
        self._creator.style.hint(
            height=fitting_size.height,
            min_width=fitting_size.width,
        )



