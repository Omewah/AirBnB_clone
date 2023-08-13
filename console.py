#!/usr/bin/python3

"""Make the shell interactive"""

import cmd
import re
import models
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

hbnb_class = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)  '

    def do_EOF(self, line):
        """Close console"""
        print("")
        return True

    def do_quit(self, line):
        """The command to exit the console"""
        print("Thanks and Good-Bye!")
        return True

    def help_quit(self):
        """helps to quit if 2 args are passed"""
        print('\n'.join(["The command to exit the console"]))

    def emptyline(self):
        """ emptyline - reruns the last command"""
        return False

    def do_create(self, line):
        """This will create the new class"""
        if line:
            try:
                new_clss = globals().get(line, None)
                obj = new_clss()
                obj.save()
                print(obj.id)
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """view instance details: print class name and id"""
        split_str = line.split()

        if len(split_str) < 1:
            print("** class name missing **")
        elif split_str[0] not in hbnb_class:
            print("** class doesn't exist **")
        elif len(split_str) < 2:
            print("** instance id missing **")
        else:
            str_uptd = f"{split_str[0]}.{split_str[1]}"
            if str_uptd not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[str_uptd])

    def do_destroy(self, line):
        """Delete instance details: use class name and id"""
        split_str = line.split()
        if len(split_str) < 1:
            print("** class name missing **")
        elif split_str[0] not in hbnb_class:
            print("** class doesn't exist **")
        elif len(split_str) < 2:
            print("** instance id missing **")
        else:
            str_uptd = f"{split_str[0]}.{split_str[1]}"
            if str_uptd not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.all().pop(str_uptd)
                storage.save()

    def do_all(self, line):
        """This will print all instances"""
        all_inst = []
        if line == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            line_str = line.split(" ")
            if line_str[0] not in hbnb_class:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    clas = key.split(".")
                    if clas[0] == line_str[0]:
                        all_inst.append(str(value))
                print(all_inst)

    def do_update(self, line):
        """Update a class: modify the instances"""
        split_str = line.split()
        if len(split_str) < 1:
            print("** class name missing **")
            return
        elif split_str[0] not in hbnb_class:
            print("** class doesn't exist **")
            return
        elif len(split_str) < 2:
            print("** instance id missing **")
            return
        else:
            str_uptd = f"{split_str[0]}.{split_str[1]}"
            if str_uptd not in storage.all().keys():
                print("** no instance found **")
            elif len(split_str) < 3:
                print("** attribute name missing **")
                return
            elif len(split_str) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[str_uptd], split_str[2], split_str[3])
                storage.save()

    def do_count(self, line):
        """This counts all class instances"""
        all_class = globals().get(line, None)
        if all_class is None:
            print("** class doesn't exist **")
            return
        inst_counter = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == line:
                inst_counter += 1
        print(inst_counter)

    def default(self, line):
        """Handles the default: unrecognized line command"""
        if line is None:
            return

        command_regex = r"^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        params_regex = r"""^"([^"]+)"(?:,\s*(?:"([^"]+)
        "|(\{[^}]+\}))(?:,\s*(?:"[^"]+"))?)?"""
        c_mat = re.match(command_regex, line)
        if not c_mat:
            super().default(line)
            return
        cmdIN, method, paramIN = c_mat.groups()
        p_mat = re.match(params_regex, paramIN)
        ext = [item for item in p_mat.groups() if item] if p_mat else []

        cmd = " ".join([cmdIN] + ext)

        if method == 'all':
            return self.do_all(cmd)

        if method == 'count':
            return self.do_count(cmd)

        if method == 'show':
            return self.do_show(cmd)

        if method == 'destroy':
            return self.do_destroy(cmd)

        if method == 'update':
            return self.do_update(cmd)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
