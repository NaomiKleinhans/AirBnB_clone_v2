#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
from console import AirBnbCommand


class TestConsole(unittest.TestCase):
    """Test Suite for the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = AirBnbCommand()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.consol

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        if (os.getenv('AirBnb_TYPE_STORAGE') != 'db'):
            try:
                os.remove("file.json")
            except Exception:
                pass

    def test_docstrings_in_console(self):
        """checking for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(AirBnbCommand.emptyline.__doc__)
        self.assertIsNotNone(AirBnbCommand.do_quit.__doc__)
        self.assertIsNotNone(AirBnbCommand.do_EOF.__doc__)
        self.assertIsNotNone(AirBnbCommand.do_create.__doc__)
        self.assertIsNotNone(AirBnbCommand.do_show.__doc__)
        self.assertIsNotNone(AirBnbCommand.do_destroy.__doc__)
        self.assertIsNotNone(AirBnbCommand.do_all.__doc__)
        self.assertIsNotNone(AirBnbCommand.do_update.__doc__)
        self.assertIsNotNone(AirBnbCommand.do_count.__doc__)

    def test_emptyline(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())


if __name__ == "__main__":
    unittest.main()
