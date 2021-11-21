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

    all_classes = {"BaseModel"}

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

    def do_create(self, line):
        """ creates a new object of BaseModel, saves it
        Exceptions:
            SyntaxError: when there is no args
            NameError: when there is no object that has the name
        """
        try:
            if not line:
                raise SyntaxError()
            args = split(line)
            if args[0] not in self.all_classes:
                raise NameError()
            obj = eval(args[0] + "()")
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        else:
            pairs = [s.split("=", maxsplit=1) for s in args[1:] if "=" in s]
            for key, value in pairs:
                try:
                    setattr(obj, key, int(value))
                except ValueError:
                    try:
                        setattr(obj, key, float(value))
                    except ValueError:
                        try:
                            setattr(obj, key, str(value).replace("_", " "))
                        except ValueError:
                            pass
            obj.save()
            print(obj.id)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
