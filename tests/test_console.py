#!/usr/bin/python3
"""
Unittests for console.py

Classes Unittested:
    HBNBCommand_prompting
"""

import unittest
from console import HBNBCommand
from models.base_model import BaseModel


class Test_HBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


if __name__ == "__main__":
    unittest.main()
