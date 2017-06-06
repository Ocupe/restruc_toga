from rubicon.objc import objc_method, get_selector

from toga.widgets.button_abc import ButtonABC

from .base import WidgetMixin
from ..libs import *
from ..utils import process_callback

from toga.widgets.base import Widget

class TogaButton(NSButton):
    @objc_method
    def onPress_(self, obj) -> None:
        if self._interface.on_press:
            process_callback(self._interface.on_press(self._interface))


class Button(Widget, WidgetMixin, ButtonABC):
    def __init__(self, label, id=None, style=None, on_press=None, enabled=None):
        super().__init__(label=label, id=id, style=style, on_press=on_press, enabled=enabled)
        self._create()

    def create(self):
        self._impl = TogaButton.alloc().init()
        self._impl._interface = self

        self._impl.setBezelStyle_(NSRoundedBezelStyle)
        self._impl.setButtonType_(NSMomentaryPushInButton)
        self._impl.setTarget_(self._impl)
        self._impl.setAction_(get_selector('onPress:'))

        # Add the layout constraints
        self._add_constraints()

    def _set_label(self, label):
        self._impl.setTitle_(self.label)
        self.rehint()

    def _set_enabled(self, value):
        self._impl.setEnabled_(self.enabled)

    def rehint(self):
        fitting_size = self._impl.fittingSize()
        self.style.hint(
            height=fitting_size.height,
            min_width=fitting_size.width,
        )


    # stuff from button_impl

    def _configure(self, label, on_press, enabled):
        self.label = label
        self.on_press = on_press
        self.enabled = enabled

    @property
    def label(self):
        """
        :returns: The label value
        :rtype: ``str``
        """
        return self._label

    @label.setter
    def label(self, value):
        """
        Set the label value

        :param value: The new label value
        :type  value: ``str``
        """
        if value is None:
            self._label = ''
        else:
            self._label = str(value)
        self._set_label(str(value))
        self.rehint()

    @property
    def on_press(self):
        """
        The callable function for when the button is pressed

        :rtype: ``callable``
        """
        return self._on_press

    @on_press.setter
    def on_press(self, handler):
        """
        Set the function to be executed on button press.

        :param handler:     callback function
        :type handler:      ``callable``
        """
        self._on_press = handler
        self._set_on_press(handler)

    def _set_on_press(self, value):
        pass

    @property
    def enabled(self):
        """
        Indicates whether the button can be pressed by the user.

        :returns:   Button status. Default is True.
        :rtype:     ``Bool`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """
        Set if the button can be pressed by the user.

        :param value:   Enabled state for button
        :type value:    ``Bool``
        """
        if value is None:
            self._enabled = True
        else:
            self._enabled = value
        self._set_enabled(value)

