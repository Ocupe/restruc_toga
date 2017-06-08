import unittest
from unittest.mock import patch, Mock, MagicMock
import toga
import toga_cocoa


class TestCoreButton(unittest.TestCase):
    def setUp(self):
        # mock factory to return a mock button
        self.factory = MagicMock()
        self.factory.Button = MagicMock(return_value=MagicMock(spec=toga_cocoa.widgets.button.Button))
        # init button with test factory
        self.label = 'Test Button'
        self.on_press = None
        self.enabled = True
        self.btn = toga.Button(self.label, factory=self.factory)

    def tearDown(self):
        pass

    def test_button_creation(self):
        self.factory.Button.assert_called()

    def test_button_label(self):
        self.assertEqual(self.btn._label, self.label)
        self.btn.label = 'New Label'
        self.assertEqual(self.btn.label, 'New Label')
        # test if backend gets called with the right label
        self.btn._impl.set_label.assert_called_with('New Label')

    def test_button_enabled(self):
        self.assertEqual(self.btn._enabled, self.enabled)
        self.btn.enabled = False
        self.assertEqual(self.btn.enabled, False)
        # test if backend gets called with the right argument
        self.btn._impl.set_enabled.assert_called_with(False)

    def test_button_on_press(self):
        self.assertEqual(self.btn._on_press, self.on_press)
        # set new callback
        def callback(obj):
            return 'called'
        self.btn.on_press = callback
        self.assertEqual(self.btn.on_press, callback)
        # test if backend gets called with the right function

    def test_button_impl_created(self):
        self.btn._impl.create.assert_called()
