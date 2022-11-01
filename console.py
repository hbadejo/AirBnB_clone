#!/usr/bin/python3
"""A file that define the AirBnB project console"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
from shlex import split
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


objectData = storage.all()


def commandList(arg):
    return [i.strip(",") for i in split(arg)]


class HBNBCommand(cmd.Cmd):
    """Defines the command line interpreter for the ALX AirBnB project.

    Attributes:
        prompt (str): Command input

        Private attribute:
            __mod -> Hold allowable classes instance that can be created
    """

    __mod = ["BaseModel", "User", "State",
             "City", "Amenity", "Place", "Review"]

    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id.
        Ex: $ create BaseModel.
        If the class name is missing,
            print ** class name missing ** (ex: $ create)
        If the class name doesn’t exist,
            print ** class doesn't exist ** (ex: $ create MyModel)
        """
        command = commandList(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in HBNBCommand.__mod:
            print("** class doesn't exist **")
        else:
            print(eval(command[0])().id)
            storage.save()

    def do_show(sefl, arg):
        """
        Prints the string representation of an
            instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        If the class name is missing,
            print ** class name missing ** (ex: $ show)
        If the class name doesn’t exist,
            print ** class doesn't exist ** (ex: $ show MyModel)
        If the id is missing,
            print ** instance id missing ** (ex: $ show BaseModel)
        If the instance of the class name doesn’t exist for the id,
            print ** no instance found ** (ex: $ show BaseModel 121212)
        """

        command = commandList(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in HBNBCommand.__mod:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif f'{command[0]}.{command[1]}' not in objectData.keys():
            print("** no instance found **")
        else:
            print(objectData[f'{command[0]}.{command[1]}'])

    def do_quit(self, arg):
        """Exit the terminal instance for the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to terminal instance for the program"""
        # print("")
        return True

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class
            name and id (save the change into the JSON file).
            Ex: $ destroy BaseModel 1234-1234-1234.
        If the class name is missing,
            print ** class name missing ** (ex: $ destroy)
        If the class name doesn’t exist,
            print ** class doesn't exist ** (ex: $ destroy MyModel)
        If the id is missing,
            print ** instance id missing ** (ex: $ destroy BaseModel)
        If the instance of the class name doesn’t exist for the id,
            print ** no instance found ** (ex: $ destroy BaseModel 121212)
        """
        command = commandList(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in HBNBCommand.__mod:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif f'{command[0]}.{command[1]}' not in objectData.keys():
            print("** no instance found **")
        else:
            del objectData[f'{command[0]}.{command[1]}']
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
            based or not on the class name.
            Ex: $ all BaseModel or $ all.
        The printed result must be a list of
            strings(like the example below)
        If the class name doesn’t exist,
            print ** class doesn't exist ** (ex: $ all MyModel)
        """
        command = commandList(arg)
        dataList = []
        if len(command) > 0 and command[0] not in HBNBCommand.__mod:
            print("** class doesn't exist **")
        else:
            for data in objectData.values():
                if len(command) > 0 and command[0] == data.__class__.__name__:
                    dataList.append(str(data))
                elif len(command) == 0:
                    dataList.append(str(data))
            print(dataList)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
            id by adding or updating attribute
            (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
            Usage: update <class name> <id> <attribute name>
                "<attribute value>"
            Only one attribute can be updated at the time
            #   You can assume the attribute name is valid
            #   (exists for this model)
            #   The attribute value must be casted
            #   to the attribute type
        If the class name is missing,
            print ** class name missing ** (ex: $ update)
        If the class name doesn’t exist,
            print ** class doesn't exist ** (ex: $ update MyModel)
        If the id is missing,
            print ** instance id missing ** (ex: $ update BaseModel)
        If the instance of the class name doesn’t exist for the id,
            print ** no instance found ** (ex: $ update BaseModel 121212)
        If the attribute name is missing,
            print ** attribute name missing **
            (ex: $ update BaseModel existing-id)
        If the value for the attribute name doesn’t exist,
            print ** value missing **
            (ex: $ update BaseModel existing-id first_name)
        All other arguments should not be used
        id, created_at and updated_at cant’ be updated.
        You can assume they won’t be passed in the update command
        Only “simple” arguments can be updated: string, integer and float.
        You can assume nobody will try to update list of ids or datetime
        """

        command = commandList(arg)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in HBNBCommand.__mod:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif f'{command[0]}.{command[1]}' not in objectData.keys():
            print("** no instance found **")
        elif len(command) == 2:
            print("** attribute name missing **")
        elif len(command) == 3:
            print("** value missing **")
        elif len(command) >= 4:
            if command[2] in ["id", "created_at", "updated_at"]:
                return False
            else:
                dictKeys = objectData[f'{command[0]}.{command[1]}']
                dictKeys.__dict__[command[2]] = command[3]
            storage.save()

    def emptyline(self):
        """Handling empty command input"""
        pass

    def do_count(self, arg):
        """
        Retrieve the number of instances of a given class.
        """
        comamand = commandList(arg)
        count = 0
        for data in storage.all().values():
            if comamand[0] == data.__class__.__name__:
                count += 1
        print(count)

    def default(self, line: str) -> None:
        """
        Overiding default input type for cmd module
        to accomodate for dot notation when input is invalid
        """
        validCommand = {
            "create": self.do_create,
            "all": self.do_all,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "show": self.do_show,
            "count": self.do_count
        }

        # Regex for "."
        # Captures "dot notation" and split commands base into a list
        pattern = re.search(r"\.", line)
        if pattern is not None:
            inp_funct = [line[:pattern.span()[0]], line[pattern.span()[1]:]]
            # Regex for "()"
            # Captures the command with "parenthesis"
            pattern = re.search(r"\((.*?)\)", inp_funct[1])
            if pattern is not None:
                command = [inp_funct[1][:pattern.span()[0]],
                           pattern.group()[1:-1]]
                if command[0] in validCommand.keys():
                    # value of command[1] will be values within parenthesis
                    # passed as a string. Or it will
                    # be an empty string
                    arg = f"{inp_funct[0]} {command[1]}"
                    return validCommand[command[0]](arg)
        print(f"*** Unknown syntax: {line}")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
