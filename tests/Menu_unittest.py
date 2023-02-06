import io
import sys
import unittest
from unittest.mock import patch
from model.Menu import Menu
from console.MenuConsole import MenuConsole
from model.Constants import HELP_TEXT

breakLine = "\n"
enable = True
disabledMessage = "this test is disabled"
test_message_1, test_message_2 = "Mensaje 1", "Mensaje 2"

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput
    
    @classmethod
    def setUpClass(cls):
        print("Starting Menu testing.")

    @unittest.skipUnless(enable, disabledMessage)
    def test_show_header(self):
        menu = Menu()
        header = menu.getHeader()
        menuView = MenuConsole(menu)
        menuView.showHeader()
        self.assertEqual(self.capturedOutput.getvalue(), header + breakLine)
    
    @unittest.skipUnless(enable, disabledMessage)
    def test_show_help(self):
        menu = Menu()
        menuView = MenuConsole(menu)
        menuView.showHelp()
        self.assertEqual(self.capturedOutput.getvalue(), HELP_TEXT + breakLine)
    
    @unittest.skipUnless(enable, disabledMessage)
    def test_show_messages(self):
        menu = Menu()
        menuView = MenuConsole(menu)
        menuView.showMessages(test_message_1, test_message_2)
        self.assertEqual(self.capturedOutput.getvalue(), test_message_1 + breakLine + test_message_2 + breakLine)
    
    @patch('builtins.input', create = True)
    @unittest.skipUnless(enable, disabledMessage)
    def test_show_press_enter_to_continue(self, mock_input):
        menu = Menu()
        menuView = MenuConsole(menu)
        menuView.showPressEnterMessage()
        self.assertIsInstance(self.capturedOutput.getvalue(), str)

    def tearDown(self):
        sys.stdout = sys.__stdout__
    
    @classmethod
    def tearDownClass(cls):
        print("Ending Menu testing.")