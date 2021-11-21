#!/usr/bin/python3
""" The console entry point of the command interpreter """
import cmd
import sys

from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class
    """
    # a custom prompt (hbnb) for interactive/non-interactive mode
    if sys.stdin.isatty():
        prompt = "(hbnb)"
    else:
        promt = ""

    def do_quit(self, line):
        """ Quit the command and exits the program
        """
        return True

    def do_EOF(self, line):
        """ exits the program
        """
        print()
        return True

    def emptyline(self):
        """empty line that ignore space
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
