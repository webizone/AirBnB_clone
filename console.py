#!/usr/bin/python3
"""
contains the console class
"""
import cmd
from datetime import datetime
from operator import indexOf
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """
    defines all commands
    """

    prompt: str = "(hbnb)  "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "Review",
        "Place",
        "City",
        "Amenity"
    }

    __cmd = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel
        Args:
            arg(line):  BaseModel command
        """
        args_split = args.split()

        if (len(args_split) == 0):
            print("** class name missing **")
        elif (args_split[0] not in self.__classes):
            print("** class doesn't exist **")
        else:
            model = eval(f"{args_split[0]}()")
            model.save()
            print(model.id)

    def do_show(self, args):
        """
        prints string representation of identified
        object
        """
        args_split = args.split()

        if (len(args_split) == 0):
            print("** class name missing **")
        elif (len(args_split) < 2):
            print("** instance id missing **")
        elif (args_split[0] not in self.__classes):
            print("** class doesn't exist **")
        else:
            key = f"{args_split[0]}.{args_split[1]}"
            out = storage.all()
            for keys in out:
                if keys == key:
                    out = out[keys].__dict__.copy()
                    str_rep = f"[{args_split[0]}] ({args_split[1]}) {out}"
                    break
            try:
                print(str_rep)
            except:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        deletes indentified object from storage
        """
        args_split = args.split()

        if (len(args_split) == 0):
            print("** class name missing **")
        elif (len(args_split) < 2):
            print("** instance id missing **")
        elif (args_split[0] not in self.__classes):
            print("** class doesn't exist **")
        else:
            key = f"{args_split[0]}.{args_split[1]}"
            out = storage.all()
            try:
                out.pop(key)
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, args):
        """
        prints a list containing string representations
        of all objects in storage
        """
        args_split = args.split()
        if (args_split and args_split[0] not in self.__classes):
            print("** class doesn't exist **")
        elif not args_split:
            obj = storage.all()
            out = dict()
            out_list = []
            for value in obj.values():
                out = value.__dict__.copy()
                str_rep = f"[{value.__class__.__name__}] ({value.id}) {out}"
                out_list.append(str_rep)
            print(out_list)
        else:
            obj = storage.all()
            out = dict()
            out_list = []
            for value in obj.values():
                if value.__class__.__name__ == args_split[0]:
                    out = value.__dict__.copy()
                    class_name = value.__class__.__name__
                    str_rep = f"[{class_name}] ({value.id}) {out}"
                    out_list.append(str_rep)
            print(out_list)

    def do_update(self, args):
        """
        updates object properties in storage
        """
        value_range = []
        index = 0
        for char in args:
            if char == '"':
                value_range.append(index)
            index += 1

        start = value_range[0] + 1
        stop = value_range[1]
        valuestr = args[start:stop]

        args_split = args.split()

        if (len(args_split) == 0):
            print("** class name missing **")
        elif (args_split[0] not in self.__classes):
            print("** class doesn't exist **")
        elif (len(args_split) < 2):
            print("** instance id missing **")
        elif (len(args_split) < 3):
            print("** attribute name missing **")
        elif (len(args_split) < 4):
            print("** value missing **")
        else:
            propt = args_split[2]
            propt_value = valuestr
            id_num = args_split[1]
            cls_name = args_split[0]
            obj = storage.all()
            if f"{cls_name}.{id_num}" not in obj:
                print("** no instance found **")
            else:
                for key, value in obj.items():
                    if key == f"{cls_name}.{id_num}":
                        setattr(value, propt, propt_value)
                        value.save()
                        break

    def do_count(self, args):
        """
        prints number of input class objects in
        storage
        """
        args_split = args.split()

        if (len(args_split) == 0):
            print("** class name missing **")
        elif (args_split[0] not in self.__classes):
            print("** class doesn't exist **")
        else:
            out = storage.all().copy()
            num = 0
            for value in out.values():
                if value.__class__.__name__ == args_split[0]:
                    num += 1
            print(num)

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in self.__classes and cnd[0] in self.__cmd:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()

