import unittest
from unittest.mock import patch, Mock, MagicMock
import toga


class TestCoreButton(unittest.TestCase):

    def setUp(self):
        # TODO mock factory to make these test platform independent.
        self.factory = MagicMock()
        self.label = 'Test Button'
        self.btn = toga.Button(self.label, factory=self.factory)

    def tearDown(self):
        print(self.factory)
        pass

    def test_button_label(self):
        self.assertTrue(self.btn.label, self.label)
