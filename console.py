#!/usr/bin/python3
""" The console entry point of the command interpreter """
import cmd
import sys

from models import storage
from models.base_model import BaseModel
from models.user import User

from shlex import split


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class
    """
    # a custom prompt (hbnb) for interactive/non-interactive mode
    if sys.stdin.isatty():
        prompt = "(hbnb)"
    else:
        promt = ""

    all_classes = {"BaseModel", "User"}

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

    def do_show(self, line):
        """ Prints the string representation of an object
        base on the class name and id
        Exception:
            SyntaxError: when no args given
            NameError: when the class name is wrong
            IndexError: when the id is missing
            KeyError: when the id is wrong
        """
        try:
            if not line:
                raise SyntaxError()
            args = split(line)
            if args[0] not in self.all_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            obj = storage.all()
            key = args[0] + "." + args[1]
            obj_real = obj[key]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        else:
            print(obj_real)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            args = split(line)
            if args[0] not in self.all_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            obj = storage.all(eval(args[0]))
            key = args[0] + '.' + args[1]
            obj_real = obj[key]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        else:
            obj_real.delete()
            storage.save()

    def do_all(self, line):
        """ prints all string representation of all instances
        Exceptions:
            NameError: when there is no object that has the name
        """
        try:
            if not line:
                objs = storage.all()
            else:
                args = split(line)
                if args[0] not in self.all_classes:
                    raise NameError()
                objs = storage.all(eval(args[0]))
        except NameError:
            print("** class doesn't exist **")
        else:
            new_list = []
            for key in objs:
                new_list.append(objs[key])
            print(new_list)

    def do_update(self, line):
        """Updates an instanceby adding or updating attribute
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object that has the name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
            AttributeError: when there is no attribute given
            ValueError: when there is no value given
        """
        try:
            if not line:
                raise SyntaxError()
            args = split(line)
            if args[0] not in self.all_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            objs = storage.all()
            key = args[0] + "." + args[1]
            if key not in objs:
                raise KeyError()
            if len(args) < 3:
                raise AttributeError()
            if len(args) < 4:
                raise ValueError()
            obj = objs[key]
            try:
                setattr(obj, args[2], eval(args[3]))
            except Exception:
                setattr(obj, args[2], args[3])
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")
        else:
            obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
