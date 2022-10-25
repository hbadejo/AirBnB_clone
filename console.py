#!/usr/bin/python3
"""A file that define the AirBnB project console"""

import cmd
from datetime import datetime
import json


class AirBnB_Console_Entry(cmd.Cmd):
    """Defines the command line interpreter for the ALX AirBnB project.


    Attributes:
        prompt (str): Command input
    """
    prompt = "(hbnb)"

    def do_create(self, arg):
        """Create data in a CRUD design"""
        pass

    def do_retrieve(sefl, arg):
        """Retrieve data in a CRUD design"""
        pass

    def do_quit(self, arg):
        """Exit the terminal instance for the program"""
        pass

    def do_destroy(self, arg):
        """Delete data in a CRUD design"""
        pass

    def do_update(self, arg):
        """Update data in a CRUD design"""
        pass

    def emptyline(self):
        """Handling empty command input"""
        pass

    def do_EOF(self):
        """EOF signal to terminal instance for the program"""
        pass


if __name__ == "__main__":
    AirBnB_Console_Entry().cmdloop()
