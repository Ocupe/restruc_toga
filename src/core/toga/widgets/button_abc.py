import abc


class ButtonABC(metaclass=abc.ABCMeta):
    """ This class defines the interface of a toga button """
    # @abc.abstractmethod
    # def test(self):
    #     pass

    @abc.abstractmethod
    def __init__(self, label, id=None, style=None, on_press=None, enabled=None):
        pass

    @abc.abstractmethod
    def _configure(self, label, on_press, enabled):
        self.label = label
        self.on_press = on_press
        self.enabled = enabled

    @abc.abstractproperty
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

    @abc.abstractmethod
    def _set_label(self, value):
        raise NotImplementedError('Button widget must define _set_label()')

    @abc.abstractproperty
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

    @abc.abstractproperty
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

    @abc.abstractmethod
    def _set_enabled(self, value):
        raise NotImplementedError('Button widget must define _set_enabled()')
