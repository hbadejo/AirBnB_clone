#!/usr/bin/python3
"""
Unittests for console.py

Classes Unittested:
    AirBnB_Console_Entry_prompting
"""

import unittest
from console import AirBnB_Console_Entry


class Test_AirBnB_Console_Entry_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", AirBnB_Console_Entry.prompt)


if __name__ == "__main__":
    unittest.main()
